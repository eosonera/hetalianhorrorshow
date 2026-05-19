################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0.1
##
################################################################################
## This file contains code for several helper functions and classes relating to
## the controller support pack.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## For examples and detailed information, check out the Tools section on my
## website: https://feniksdev.com/tool/helper-functions-and-classes/
## This is just the backend; you don't need to understand everything in
## this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
init -550 python in pad_config:
    ############################################################################
    ## EVENT LISTENER
    ############################################################################
    import pygame
    from renpy.store import config, Null, persistent

    class EventListener(Null):
        """
        A simple class which listens for controller, keyboard, and mouse events
        to know which was last used. This is required for most controller
        support displayables to work with both mouse and with controller.

        Attributes:
        -----------
        last_event_type : int
            The last event type received. One of MOUSE, CONTROLLER, or KEYBOARD.
        callbacks : list
            A list of callbacks to run when the event type changes.
        on_changed : bool
            If True, runs the callbacks only when the event type changes.
            Otherwise, runs them every time an event is received.
        """
        last_event_type = None
        MOUSE = 1
        CONTROLLER = 2
        KEYBOARD = 3
        def __init__(self, callbacks=None, on_changed=True):
            super(EventListener, self).__init__()
            self.callbacks = callbacks or [ ]
            self.on_changed = on_changed
            self.last_event_type = None
        def event(self, ev, x, y, st):
            last_type = self.last_event_type
            if ev.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP,
                    pygame.MOUSEBUTTONDOWN):
                self.last_event_type = EventListener.MOUSE
            elif ev.type in (renpy.display.core.EVENTNAME,
                    pygame.CONTROLLERDEVICEADDED, pygame.CONTROLLERAXISMOTION,
                    pygame.CONTROLLERBUTTONDOWN, pygame.CONTROLLERBUTTONUP):
                if (ev.type == renpy.display.core.EVENTNAME
                        and any([x.startswith("pad_") for x in ev.eventnames])):
                    self.last_event_type = EventListener.CONTROLLER
                elif ev.type == renpy.display.core.EVENTNAME:
                    ## Some other kind of default event, like activating a bar
                    if self.on_changed:
                        return
                else:
                    self.last_event_type = EventListener.CONTROLLER
            else:
                try:
                    if ev.key:
                        self.last_event_type = EventListener.KEYBOARD
                except:
                    if self.on_changed:
                        return
            if not self.on_changed or (last_type != self.last_event_type):
                for callback in self.callbacks:
                    rv = renpy.run(callback, last_type, self.last_event_type, ev)
                    if rv is not None:
                        return rv


    def is_using_mouse():
        """
        A simple function intended to return whether the player has recently
        moved the mouse rather than using the keyboard or a gamepad.
        """
        return EVENT_LISTENER.last_event_type == EventListener.MOUSE

    def is_using_controller():
        """
        A simple function intended to return whether the player has recently
        used a controller rather than the keyboard or mouse.
        """
        return EVENT_LISTENER.last_event_type == EventListener.CONTROLLER

    def is_using_keyboard():
        """
        A simple function intended to return whether the player has recently
        used the keyboard rather than a controller or mouse.
        """
        return EVENT_LISTENER.last_event_type == EventListener.KEYBOARD

    def get_event(event, kind="all", error_on_missing=True, for_icons=False):
        """
        Returns the event name(s) for a given gamepad event. Returns a list.

        Parameters:
        -----------
        event : str
            The event name to get the internal events for.
        kind : str
            Optional. One of "all", "press", "release", "release_replace",
            "repeat", or "repeat_replace". Default is "all". Filters the events
            to only return those of the given kind. "release_replace" will
            return the events from "press", replaced to their release
            counterparts. "repeat_replace" does the same but for repeat events.
        """
        ## Designed so it throws an error if you didn't declare this event
        ## already.
        if config.developer and error_on_missing:
            events = persistent.pad_bindings[event]
        else:
            events = persistent.pad_bindings.get(event, [])

        ########################################################################
        ## Special case: if we're in input mode and this event is shared by
        ## events which start with "input_", return None (aka make sure the
        ## input events take precedence for things like the onscreen keyboard).
        try:
            mode = renpy.game.context().get_mode()
        except:
            mode = None
        if (not for_icons and mode == "input"
                and not event.startswith("input_") and events): # Check for conflicts
            shared_events = [ ]
            for e in events:
                shared_events.extend(renpy.store.pad_remap.find_events(e))
            if any(e.startswith("input_") for e in shared_events):
                return None
        ########################################################################

        if kind == "all":
            return events
        elif kind == "release":
            return [e for e in events if (e.endswith("release") or e.endswith("zero")) and not e.startswith("repeat")]
        elif kind in ("press", "release_replace", "repeat_replace"):
            lst = [e for e in events if (e.endswith("pos") or e.endswith("press")) and not e.startswith("repeat")]
            if kind == "release_replace":
                lst = [e.replace("press", "release") for e in lst]
                lst = [e.replace("pos", "zero") for e in lst]
            elif kind == "repeat_replace":
                lst = ["repeat_{}".format(e) for e in lst]
            return lst
        elif kind == "repeat":
            return [e for e in events if e.startswith("repeat")]

    def map_event(ev, event, kind="all"):
        """
        Like renpy.map_event, but for gamepad events. Uses the output of
        get_event to run renpy.map_event.
        """
        buttons = get_event(event, kind) or [ ]
        if not buttons:
            return False
        return renpy.map_event(ev, buttons)

    def get_icons(event, suffix="", zip_alt_text=False):
        """
        Returns the icon image(s) for a given gamepad event. Returns a list
        like ["pad_a", "pad_b"].

        Parameters:
        -----------
        event : str
            The event name to get the icon for.
        suffix : str
            Optional. A suffix to add to the end of the icon name, such as
            "small". Default is "".
        zip_alt_text : bool
            Optional. If True, returns a list of tuples with the icon name and
            the alt text for that icon. Default is False.
        """
        buttons = get_event(event, error_on_missing=False, for_icons=True)
        if buttons is None:
            return [ ]
        else:
            icons = list(set(["pad_{}{}{}".format(
                EVENT_TO_ICON[button],
                '_' if suffix else '',
                suffix) for button in buttons]))
            if not zip_alt_text:
                return icons
            return list(zip(icons, get_alt_text(event, as_list=True)))

    def get_alt_text(event, as_list=False, is_event=True, alt_tag=True):
        """
        Get human-readable alt text for the controller icons.

        Parameters:
        -----------
        event : str
            The event name to get the alt text for.
        as_list : bool
            Optional. If True, returns a list of alt text strings. Default is
            False (returns a single string joined with commas).
        is_event : bool
            If True, the event is an event name. If False, the event name has
            already been passed through get_event to get a list like
            ["pad_x_press"].
        alt_tag : bool
            If True, wraps the alt text in {alt} tags. Default is True.
        """
        ## Fetch the icons
        if is_event:
            icons = [x[4:] for x in get_icons(event)]
        else:
            icons = event
        ## If there are no icons, return an empty string
        if not icons:
            return ""
        ## Otherwise, return the appropriate text based on the icon set.
        ret = [ ]
        order = ["xbox", "playstation", "nintendo", "steam", "generic"]
        idx = order.index(persistent.controller_layout)
        for icon in icons:
            if icon in ("left", "right", "up", "down",
                    "l3", "r3", "left_stick", "right_stick"):
                ## Consistent for all controllers
                ret.append(ICON_TO_ALT_TEXT[icon])
            else:
                ## Different for each controller
                ret.append(ICON_TO_ALT_TEXT[icon][idx])
        if as_list:
            return ret
        txt = ", ".join(ret)
        if alt_tag:
            return "{alt}" + txt + "{/alt}"
        return txt

    def get_inline_icons(event, suffix="small", joiner=""):
        """
        Returns a string with {image=some_image} for the buttons which can be
        used to activate the provided event.

        Parameters:
        -----------
        event : str
            The event name to get the icon for.
        suffix : str
            Optional. A suffix to add to the end of the icon name, such as
            "small". Default is "small".
        joiner : str
            Optional. A string to join the icons with. Default is "".
        """
        icons = get_icons(event, suffix)
        alt_text = get_alt_text(event)
        ret = joiner.join(["{image=%s}" % icon for icon in get_icons(event, suffix)])
        return ret + alt_text

    def register_redrawable(disp):
        """
        A function which registers the given displayable to be redrawn
        when the focus type changes.
        """
        INPUT_CHANGE_REDRAWABLES.append(disp)

    def refresh_controller_ui(old_type, new_type, event):
        """
        A function which refreshes the screen if the player switches
        to controller from keyboard or mouse, or vice versa.
        """
        if new_type == EventListener.CONTROLLER:
            renpy.restart_interaction()
        elif old_type == EventListener.CONTROLLER:
            renpy.restart_interaction()
        elif old_type is None:
            ## No focus type yet; just restart the interaction
            ## since it's changed
            renpy.restart_interaction()

    def refresh_redrawables(old_type, new_type, event, force=False):
        """
        A function which refreshes some special displayables (to avoid having to
        refresh the whole screen).
        """
        if old_type != new_type:
            for disp in INPUT_CHANGE_REDRAWABLES:
                try:
                    if force and isinstance(disp, renpy.store.IconButton):
                        disp.reset_child()
                except:
                    pass
                renpy.redraw(disp, 0)

    def manage_focus():
        """
        A function which triggers all focus managers to check if they're
        showing and, if so, to restore focus.
        """
        for manager in FOCUS_MANAGERS:
            ret = manager.refresh_focus()
            if ret:
                return

    def clear_managed_focus(screen=None):
        """
        A function which clears either all focus manager focuses, or the one
        from a specific screen.
        """
        if screen is None:
            FocusManager.focuses = dict()
        else:
            FocusManager.focuses[screen] = None


    class FocusManager(Null):
        """
        A class which manages the focus of a screen, saving and restoring
        it when the screen is revisited.

        Attributes:
        -----------
        screen : str
            The name of the screen to manage.
        layer : str
            Optional. The layer to manage the focus on. Default is None, which
            will automatically choose the layer the screen is on.
        is_showing : ScreenDisplayable
            The result of calling renpy.get_screen on this screen.
        displayable_lookup : dict
            A lookup of Displayable ID : Displayable for the screen. Used only
            if the .id property is not available for displayables in order
            to look up the focused displayable.
        """
        focuses = dict()
        def __init__(self, screen, layer=None):
            self.screen = screen
            self.layer = layer
            self.is_showing = renpy.get_screen(self.screen)
            self.displayable_lookup = dict()
            self.refresh_triggered = False
            super(FocusManager, self).__init__()

        def refresh_focus(self):
            """
            Check if we are still showing; if so, this indicates we should
            restore focus and return True.
            """
            if self.is_showing:
                self.refresh_triggered = self.focuses.get(self.screen)
                ## This avoids Ren'Py using default_focus for things like
                ## when the confirm screen is hidden
                renpy.timeout(1.0/60.0)
                return True
            return False

        def per_interact(self):
            old_showing = self.is_showing
            self.is_showing = renpy.get_screen(self.screen)
            if old_showing is not self.is_showing:
                ## Update the displayable lookup
                self.displayable_lookup = dict()
                if not old_showing:
                    ## Wasn't showing and now is; restore focus
                    self.restore_focus()

        def restore_focus(self):
            """
            Restore focus to the last-focused displayable on this screen.
            """
            if is_using_mouse():
                ## Don't force focus when using the mouse
                return
            id = self.focuses.get(self.screen, None)
            if id is not None:
                renpy.set_focus(self.screen, id, self.layer)

        def event(self, x, y, ev, st):
            """
            Record the focus of the screen when it changes.
            """
            ## Avoid dealing with events if this screen isn't showing
            if not self.is_showing:
                self.refresh_triggered = False
                return

            if self.refresh_triggered:
                self.focuses[self.screen] = self.refresh_triggered
                self.refresh_triggered = False
                self.restore_focus()
                return

            if renpy.display.focus.screen_of_focused is self.is_showing:
                ## We are the screen with the currently focused displayable.
                ## Save the focused ID.

                focused = renpy.display.focus.get_focused()
                if focused is None:
                    self.focuses[self.screen] = None
                    return

                ## If this isn't keyboard-focusable, we don't want to save
                ## focus to it (which is specifically for keyboard/controller).
                try:
                    if not focused.style.keyboard_focus:
                        return
                except:
                    pass

                try:
                    ## In later Ren'Py versions, displayables store their IDs
                    focused_id = focused.id
                    if focused_id is None:
                        try:
                            focused_id = focused.child.id
                        except:
                            pass
                except:
                    ## Otherwise, we grab all the displayables on the screen and
                    ## try to find the focused one.
                    screen = self.is_showing
                    if not isinstance(screen, renpy.display.screen.ScreenDisplayable):
                        return None
                    if screen.child is None:
                        screen.update()

                    if not self.displayable_lookup:
                        ## Reverse lookup to get the ID
                        self.displayable_lookup = {
                            id(v): k for k, v in screen.widgets.items()}
                    focused_id = self.displayable_lookup.get(id(focused))
                    if focused_id is None:
                        ## Sometimes the thing that's focused is the child of
                        ## one of the displayables instead.
                        try:
                            focused_id = self.displayable_lookup.get(
                                id(focused.child), None)
                        except:
                            pass
                ## Now we have the ID of the focused item, so save that.
                self.focuses[self.screen] = focused_id


    def wait_for_event(old_type, new_type, event):
        """
        A callback for an event listener which returns on a button down
        or a key press event.
        """
        if event.type in (pygame.MOUSEBUTTONUP, pygame.KEYUP):
            ## Keyboard or mouse up event
            return True
        elif event.type in (renpy.display.core.EVENTNAME, pygame.CONTROLLERBUTTONUP):
            if (event.type == renpy.display.core.EVENTNAME
                    and any([x.startswith("pad_") for x in event.eventnames])):
                return True
            elif event.type == renpy.display.core.EVENTNAME:
                ## Some other kind of default event, like activating a bar
                return
            else:
                return True
        return None

    def get_stick_dead_zone(id=None, stick="left"):
        """
        Get the dead zone for the provided controller, or the default if it
        hasn't been calibrated.
        """
        if id is None:
            ## Try to get the first id in renpy_controllers
            id = next(iter(renpy_controllers))
        key = renpy_controllers.get(id)
        if key is None:
            return DEFAULT_DEADZONE
        key = key.get_guid_string()
        if stick == "left":
            return persistent.left_stick_dead_zone.get(key, DEFAULT_DEADZONE)
        return persistent.right_stick_dead_zone.get(key, DEFAULT_DEADZONE)

    def get_stick_max(id=None, stick="left"):
        """
        Get the maximum value for the provided controller, or the default if it
        hasn't been calibrated.
        """
        if id is None:
            ## Try to get the first id in renpy_controllers
            id = next(iter(renpy_controllers))
        key = renpy_controllers.get(id)
        if key is None:
            return STICK_MAX
        key = key.get_guid_string()
        if stick == "left":
            return persistent.left_stick_max.get(key, STICK_MAX)
        return persistent.right_stick_max.get(key, STICK_MAX)

    def choose_icon_set(index):
        """
        A callback called when a new controller is plugged in to change the
        icon set based on the controller name.
        """
        ## Do we have any existing controllers? If so, don't update the UI.
        ## This may happen if a second controller is added.
        if len(renpy_controllers) > 1:
            return

        ## See if we can pick out the right glyph set.
        name = renpy_controllers[index].get_name()
        guid = renpy_controllers[index].get_guid_string()

        ## First, do we have a mapping for this GUID?
        layout = persistent.controller_guid_to_type.get(guid)
        if layout is not None:
            ## We do. Use it.
            persistent.controller_layout = layout
            return

        ## Otherwise, try to determine the layout based on the name.
        name = name.lower()
        if any([x in name for x in XBOX_CONTROLLER_NAMES]):
            persistent.controller_layout = "xbox"
        elif any([x in name for x in PLAYSTATION_CONTROLLER_NAMES]):
            persistent.controller_layout = "playstation"
        elif any([x in name for x in NINTENDO_CONTROLLER_NAMES]):
            persistent.controller_layout = "nintendo"
        elif (any([x in name for x in STEAM_CONTROLLER_NAMES])
                or renpy.variant("steam_deck")):
            persistent.controller_layout = "steam"
        ## Not sure of the layout, so it can use the generic.
        else:
            persistent.controller_layout = "generic"

        ## Save the mapping for future use.
        persistent.controller_guid_to_type[guid] = persistent.controller_layout
        return

init 10 python in pad_config:
    from renpy.store import renpy_controllers
