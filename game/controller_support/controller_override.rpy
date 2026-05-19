################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## A file which basically overrides some functions in controller.py to add
## additional controller support. In future Ren'Py versions, this might be
## in the engine itself and thus unnecessary.
################################################################################

################################################################################
## BACKEND
################################################################################
## You generally shouldn't need to modify anything below this line, but you're
## welcome to look through it or adjust it if you know what you're doing.
################################################################################
## Code to identify which controller is used, and to fix an issue with multiple
## controller events passed to renpy.map_event
################################################################################

init python:
    from renpy.display.controller import controllers as renpy_controllers

    def my_controller_start(index):
        """
        Starts the controller at index. Borrowed from the engine in
        renpy.display.controller.py
        """

        renpy.display.controller.quit(index)
        c = renpy.display.controller.Controller(index)

        if not c.is_controller():
            return

        renpy.exports.write_log("controller: %r %r %r" % (c.get_guid_string(),
            c.get_name(), c.is_controller()))

        if renpy.game.preferences.pad_enabled != "all":
            for prefix in renpy.config.controller_blocklist:
                if c.get_guid_string().startswith(prefix):
                    renpy.exports.write_log("Controller found in blocklist, not using.")
                    return

        success = False
        try:
            c.init()
            renpy.display.controller.controllers[index] = c
            success = True
        except Exception:
            success = False
            renpy.display.log.exception()

        ## Some custom callback code
        try:
            is_calibrating = store.pad_is_calibrating
        except:
            is_calibrating = False

        if not is_calibrating and success:
            for cb in store.pad_config.CONTROLLER_CONNECT_CALLBACKS:
                renpy.run(cb, index)
        ## End of custom code

        renpy.restart_interaction()

    ## Redirect the start function to the custom one.
    renpy.display.controller.start = my_controller_start

    def my_controller_quit(index):
        """
        Quits the controller at index. Overwritten so that there's a callback
        when a controller is removed.
        """

        if index in renpy_controllers:
            renpy_controllers[index].quit()
            del renpy_controllers[index]
            ## Some custom callback code
            try:
                is_calibrating = store.pad_is_calibrating
            except:
                is_calibrating = False

            if not is_calibrating:
                for cb in store.pad_config.CONTROLLER_DISCONNECT_CALLBACKS:
                    renpy.run(cb, index)

                renpy.restart_interaction()

    ## Redirect the quit function to the custom one.
    renpy.display.controller.quit = my_controller_quit

    ############################################################################
    ## BUG FIX CODE - the engine has an error on 8.2.3 and below. If you are on
    ## 8.3 or higher, you can remove this code (it only replaces the default
    ## if you're on a lower version).
    def map_event(ev, keysym):
        """
        Borrowed and fixed from renpy.display.behavior.py
        The fix should be on the nightly 8.2.3 and 8.3.0 versions of Ren'Py,
        and thus this code can be removed if you are on or above those versions.

        Returns true if the pygame event `ev` matches `keysym`

        `keysym`
            One of:

            * The name of a keybinding in :var:`config.keymap`.
            * A keysym, as documented in the :ref:`keymap` section.
            * A list containing one or more keysyms.
        """

        if ev.type == renpy.display.core.EVENTNAME:
            if isinstance(keysym, list):
                for k in keysym:
                    if k in ev.eventnames and not ev.up:
                        return True
                return False
            if (keysym in ev.eventnames) and not ev.up:
                return True
            return False

        if isinstance(keysym, list):
            keysym = tuple(keysym)

        check_code = renpy.display.behavior.event_cache.get(keysym, None)
        if check_code is None:
            check_code = eval("lambda ev : " + renpy.display.behavior.compile_event(keysym, True), globals())
            renpy.display.behavior.event_cache[keysym] = check_code

        return check_code(ev)

    ## Only need to replace this if it hasn't been fixed in the engine.
    if ((renpy.version(tuple=True)[0] == 7
                and renpy.version(tuple=True) < (7, 8, 0))
            or (renpy.version(tuple=True) < (8, 3, 0))):
        renpy.display.behavior.map_event = map_event
    ## END OF BUG FIX CODE
    ############################################################################

    old_gamepad_calibrate = GamepadCalibrate
    class CustomGamepadCalibrate(Action):
        """
        A custom action which does the same thing as GameCalibrate, but also
        sets a variable to prevent the start/quit callbacks from going off
        while selecting a stick to calibrate.
        """
        def is_sensitive(self):
            return GamepadExists()

        def __call__(self):
            store.pad_is_calibrating = True
            renpy.run(old_gamepad_calibrate())
            store.pad_is_calibrating = False
    GamepadCalibrate = CustomGamepadCalibrate

    def hide_windows_without_focus_drop():
        """
        Avoid calling the _hide_windows label at all while in the menu context.
        """
        if not renpy.context()._menu and not _windows_hidden:
            renpy.run(HideInterface())

    config.underlay.append(renpy.Keymap(hide_windows=hide_windows_without_focus_drop))


init 100 python in controller_event_replacement:

    import pygame_sdl2
    from pygame_sdl2 import CONTROLLERDEVICEADDED, CONTROLLERDEVICEREMOVED
    from pygame_sdl2 import CONTROLLERAXISMOTION, CONTROLLERBUTTONDOWN, CONTROLLERBUTTONUP
    from pygame_sdl2.controller import Controller, get_string_for_axis, get_string_for_button
    from store.pad_config import get_stick_dead_zone
    pygame = pygame_sdl2

    stick_values = dict()

    def my_controller_event(ev):
        """
        Processes an event and returns the same event, a new event, or None if
        the event has been processed and should be ignored.

        Borrowed from renpy.display.controller.py and adapted to pass axis
        values and information as part of gamepad events.
        """
        THRESHOLD = renpy.display.controller.THRESHOLD
        ZERO_THRESHOLD = renpy.display.controller.ZERO_THRESHOLD

        if renpy.config.pass_controller_events:
            rv = ev
        else:
            rv = None

        if ev.type == CONTROLLERDEVICEADDED:
            renpy.display.controller.start(ev.which)
            return rv

        elif ev.type == CONTROLLERDEVICEREMOVED:
            for k, v in renpy.display.controller.controllers.items():
                if v.instance_id == ev.which:
                    renpy.display.controller.quit(k)
                    break

            return rv

        elif ev.type == CONTROLLERAXISMOTION:

            pygame_sdl2.event.pump()
            events = [ ev ] + pygame.event.get(CONTROLLERAXISMOTION)

            for ev in events:

                old_pos = renpy.display.controller.axis_positions.get((ev.which, ev.axis), None)
                old_value = stick_values.get((ev.which, ev.axis), 0)

                if ev.value > THRESHOLD:
                    pos = "pos"
                elif ev.value < -THRESHOLD:
                    pos = "neg"
                elif abs(ev.value) < ZERO_THRESHOLD:
                    pos = "zero"
                else:
                    pos = old_pos

                ## Don't post a zero event if we've had no stick events.
                if pos != old_pos and (old_pos is not None or pos != "zero"):
                    renpy.display.controller.axis_positions[(ev.which, ev.axis)] = pos

                    renpy.display.controller.controller_event(get_string_for_axis(ev.axis), pos)

                ## If it's in the dead zone, count the value as 0.
                dead_zone = get_stick_dead_zone(ev.which, get_string_for_axis(ev.axis)[:-1])
                new_value = 0 if abs(ev.value) < dead_zone else 1
                ## Otherwise, if the value has changed, post an event.
                if old_value != new_value and (new_value == 0 or old_value == 0):
                    stick_values[(ev.which, ev.axis)] = new_value
                    ## Allow this event to be passed directly
                    ev.value = new_value
                    rv = ev

            return rv

        elif ev.type in (CONTROLLERBUTTONDOWN, CONTROLLERBUTTONUP):

            if ev.type == CONTROLLERBUTTONDOWN:
                pr = "press"
            else:
                pr = "release"

            renpy.display.controller.controller_event(get_string_for_button(ev.button), pr)
            return rv

        elif ev.type in (
                pygame.JOYAXISMOTION,
                pygame.JOYHATMOTION,
                pygame.JOYBALLMOTION,
                pygame.JOYBUTTONDOWN,
                pygame.JOYBUTTONUP,
                pygame.JOYDEVICEADDED,
                pygame.JOYDEVICEREMOVED,
                ):

            if not renpy.config.pass_joystick_events:
                return None

        return ev

    renpy.display.controller.event = my_controller_event

    ############################################################################
    ## BUG FIX CODE - the engine has an error on 8.3.5 and below. If you are on
    ## 8.3.6 or higher, you can remove this code (it only replaces the default
    ## if you're on a lower version).
    ############################################################################
    ## Required import statements for the function to work as written
    from renpy.display.focus import override, grab, modal_generation
    from renpy.display.focus import old_max_default, screen_of_focused, argument
    from renpy.display.focus import replaced_by, focus_list, screen_of_focused_names
    from renpy.display.focus import global_focus, focus_type, pending_focus_type
    from renpy.display.focus import tooltip, last_tooltip, get_focused, set_focused
    from renpy.display.focus import old_max_default_focus_name, set_grab, operator
    ############################################################################

    def my_before_interact(roots):
        """
        Called before each interaction to choose the focused and grabbed
        displayables.
        """
        ########################################################################
        ## NEW! This overrides the original (only needed due to relocating code):
        # global override
        # global grab
        # global modal_generation
        # global old_max_default
        ## Replacement:
        override = renpy.display.focus.override
        grab = renpy.display.focus.grab
        modal_generation = renpy.display.focus.modal_generation
        old_max_default = renpy.display.focus.old_max_default
        ########################################################################

        ########################################################################
        ## NEW! This overrides the original (only needed due to relocating code):
        # modal_generation = 0
        ## Replacement:
        renpy.display.focus.modal_generation = modal_generation = 0
        ########################################################################

        # a list of focusable, name, screen tuples.
        fwn = [ ]

        def callback(f, n):
            fwn.append((f, n, renpy.display.screen._current_screen, modal_generation))

        for root in roots:
            try:
                root.find_focusable(callback, None)
            except renpy.display.layout.IgnoreLayers:
                pass

        # Assign a full name to each focusable.

        namecount = { }

        fwn2 = [ ]

        for fwn_tuple in fwn:

            f, n, screen, gen = fwn_tuple

            serial = namecount.get(n, 0)
            namecount[n] = serial + 1

            if f is None:
                continue

            f.full_focus_name = n, serial

            replaced_by[id(f)] = f

            fwn2.append(fwn_tuple)

        fwn = fwn2

        # Determine the default, as determined by the current screen.
        defaults = [ ]

        for f, n, screen, gen in fwn:
            if gen != modal_generation:
                continue

            if f.default:
                defaults.append((f.default, f, screen))

        if defaults:
            if len(defaults) > 1:
                defaults.sort(key=operator.itemgetter(0))

            max_default, max_default_focus, max_default_screen = defaults[-1]
            max_default_focus_name = max_default_focus.full_focus_name

        else:
            max_default = 0
            max_default_focus = None
            max_default_screen = None
            max_default_focus_name = None

        # Should we do the max_default logic?
        try:
            should_max_default = renpy.display.interface.input_event_time > renpy.display.interface.mouse_event_time + .1
        except:
            try: # This might fail during init
                should_max_default = pad_config.EVENT_LISTENER.last_event_type != pad_config.EventListener.MOUSE
            except NameError:
                should_max_default = ((renpy.display.interface.last_event is None)
                    or (renpy.display.interface.last_event.type not in [
                    pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION ]))

        # Is this an explicit change, using the override operation?
        explicit = False

        # We assume id(None) is not in replaced_by.
        replaced_by.pop(None, None)

        # If there's something with the same full name as the current widget,
        # it becomes the new current widget.

        current = get_focused()
        current = replaced_by.get(id(current), current)
        old_current = current

        # Update the grab.
        ########################################################################
        ## NEW! This overrides the original (only needed due to relocating code):
        # grab = replaced_by.get(id(grab), None)
        ## Replacement:
        renpy.display.focus.grab = grab = replaced_by.get(id(grab), None)
        ########################################################################

        if override is not None:
            d = renpy.exports.get_displayable(*override, base=True) # type: ignore

            if (d is not None) and (current is not d) and not grab:
                current = d
                explicit = True

        ########################################################################
        ## NEW! This overrides the original (only needed due to relocating code):
        # override = None
        ## Replacement:
        renpy.display.focus.override = None
        ########################################################################

        # When increasing the default focus, and the user is not using the mouse,
        # switch to the default.
        ########################################################################
        ## NEW! This fixes a bug in 8.3.5 and lower. It should be fixed in
        ## later Ren'Py versions. Original:
        # if should_max_default and (max_default > old_max_default):
        ## Replacement:
        if not explicit and should_max_default and (max_default > old_max_default):
        ########################################################################
            current = max_default_focus
            set_grab(None)
            set_focused(max_default_focus, None, max_default_screen)
            explicit = True

        ########################################################################
        ## NEW! This overrides the original (only needed due to relocating code):
        # old_max_default = max_default
        ## Replacement:
        renpy.display.focus.old_max_default = old_max_default = max_default
        ########################################################################

        # Try to find the current focus.
        if current is not None:
            current_name = current.full_focus_name

            for f, n, screen, gen in fwn:

                if gen != modal_generation:
                    continue

                if f.full_focus_name == current_name:
                    current = f
                    set_focused(f, argument, screen)
                    break
            else:
                current = None

        if grab is not None:
            current = grab

        # If nothing has focus, focus the default if the highest priority has changed,
        # or if the default is None.
        if (should_max_default and (max_default > 0) and (current is None) and
            (renpy.display.interface.start_interact or (max_default_focus_name != old_max_default_focus_name))):

            explicit = True
            current = max_default_focus
            set_focused(max_default_focus, None, max_default_screen)

        if current is None:
            set_focused(None, None, None)

        # Finally, mark the current widget as the focused widget, and
        # all other widgets as unfocused.
        for f, n, screen, _modal in fwn:
            if f is not current:
                renpy.display.screen.push_current_screen(screen)
                try:
                    if (f is old_current) and renpy.config.always_unfocus:
                        f.unfocus(default=False)
                    else:
                        f.unfocus(default=not explicit)

                finally:
                    renpy.display.screen.pop_current_screen()

        if current:
            renpy.display.screen.push_current_screen(screen_of_focused)
            try:
                current.focus(default=not explicit)
            finally:
                renpy.display.screen.pop_current_screen()

        # Clear replaced_by.
        replaced_by.clear()


    ## Only need to replace this if it hasn't been fixed in the engine.
    if ((renpy.version(tuple=True)[0] == 7
                and renpy.version(tuple=True) < (7, 8, 6))
            or (renpy.version(tuple=True) < (8, 3, 6))):
        renpy.display.focus.before_interact = my_before_interact
    ## END OF BUG FIX CODE
    ############################################################################

