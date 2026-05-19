################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for several creator-defined classes and their screen
## language equivalents.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## For examples and detailed information, check out the Tools section on my
## website: https://feniksdev.com/docs-category/controller-support-expansion/
## This is just the backend; you don't need to understand everything in
## this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**01_controller_cdsl.rpy", None)
    build.classify("**01_controller_cdsl.rpyc", "archive")
################################################################################

python early:

    ############################################################################
    ## CONTROLLER BAR
    ############################################################################
    class ControllerBar(Bar):
        """
        A bar which does not need to be grabbed to be adjusted. Horizontal bars
        can be controlled immediately with left/right input, and vertical bars
        with up/down input.

        Attributes:
        -----------
        The attributes are identical to the Bar class; see the doc page on Bar
        for more: https://www.renpy.org/doc/html/screens.html#bar
        """
        def __init__(self, *args, **kwargs):
            super(ControllerBar, self).__init__(*args, **kwargs)
            self.last_input_was_mouse = pad_config.is_using_mouse()

        def deactivate_bar(self):
            grabbed = (renpy.display.focus.get_grab() is self)
            value = self.adjustment.value
            if grabbed:
                renpy.display.tts.speak(renpy.minstore.__("deactivate"))
                self.set_style_prefix("hover_", True)
                renpy.display.focus.set_grab(None)

            # Invoke rounding adjustment on bar release
            value = self.adjustment.round_value(value, release=True)

            if not grabbed:
                return
            rv = renpy.run(self.released)
            if rv is not None:
                return rv

        def focus(self, default=False):
            if default:
                if (self.last_input_was_mouse or pad_config.is_using_mouse()):
                    return super(ControllerBar, self).focus(default)
                ## Ensure that if this bar is focused by default, that it
                ## is activated.
                alt_txt = __(self.value.alt) + " " + renpy.minstore.__("activate")
                renpy.display.tts.speak(alt_txt)
                renpy.display.focus.set_grab(self)
                self.set_style_prefix("selected_hover_", True)
                renpy.play(self.style.activate_sound)
            return super(ControllerBar, self).focus(default)

        def event(self, ev, x, y, st):
            """
            Handle events for this bar.
            """
            if ev.type == pygame.MOUSEMOTION:
                ## Deactivate the bar
                if not self.last_input_was_mouse:
                    ## Transition from keyboard to mouse; deactivate bar
                    rv = self.deactivate_bar()
                self.last_input_was_mouse = True
            elif not pad_config.is_using_mouse():
                self.last_input_was_mouse = False
                grabbed = (renpy.display.focus.get_grab() is self)
                bar_vertical = self.style.bar_vertical
                if self is renpy.display.focus.get_focused() and not grabbed:
                    ## Set this as a grab
                    renpy.queue_event("bar_activate")
                elif grabbed:
                    ## Up/down changes focus for horizontal bars
                    if bar_vertical:
                        if (renpy.map_event(ev, "focus_left")
                                or renpy.map_event(ev, "focus_right")):
                            rv = self.deactivate_bar()
                            if rv is not None:
                                return rv
                    else:
                        if (renpy.map_event(ev, "focus_up")
                                or renpy.map_event(ev, "focus_down")):
                            rv = self.deactivate_bar()
                            if rv is not None:
                                return rv

            grabbed = (renpy.display.focus.get_grab() is self)
            ignore = False
            try:
                ret = super(ControllerBar, self).event(ev, x, y, st)
            except renpy.IgnoreEvent:
                ignore = True
                ret = None
            if not self.focusable or not self.is_focused() or self.hidden:
                if ignore:
                    raise renpy.IgnoreEvent()
                return ret
            if (not grabbed and map_event(ev, "bar_activate")):
                ## Override the "activate" self-voicing with something
                ## clearer
                alt_txt = __(self.value.alt)
                renpy.display.tts.speak(alt_txt)
            if ignore:
                raise renpy.IgnoreEvent()
            return ret


    renpy.register_sl_displayable("controller_bar", ControllerBar, "bar", 0, replaces=True,
        pass_context=True
        ).add_property("hovered"
        ).add_property("unhovered"
        ).add_property("update_interval"
        ).add_property("adjustment"
        ).add_property("range"
        ).add_property("value"
        ).add_property("changed"
        ).add_property("released"
        ).add_property("activate_sound"
        ).add_property("hover_sound"
        ).add_property_group("bar")

    def controller_sl2vbar(context=None, **properties):
        """A convenience function to turn bar properties into vbar."""
        range = 1 # @ReservedAssignment
        value = 0
        width = None
        height = None

        if "width" in properties:
            width = properties.pop("width")
        if "height" in properties:
            height = properties.pop("height")
        if "range" in properties:
            range = properties.pop("range") # @ReservedAssignment
        if "value" in properties:
            value = properties.pop("value")

        if "style" not in properties:
            if isinstance(value, renpy.ui.BarValue):
                style = renpy.ui.combine_style(context.style_prefix, value.get_style()[1])
                properties["style"] = style

        return ControllerBar(range, value, width, height, vertical=True, **properties)

    renpy.register_sl_displayable("controller_vbar", controller_sl2vbar, "vbar", 0, replaces=True,
        pass_context=True,
        ).add_property("hovered"
        ).add_property("unhovered"
        ).add_property("update_interval"
        ).add_property("adjustment"
        ).add_property("range"
        ).add_property("value"
        ).add_property("changed"
        ).add_property("released"
        ).add_property("activate_sound"
        ).add_property("hover_sound"
        ).add_property_group("bar")

    ############################################################################
    ## KEY CONTROLLER / FOCUSED_ON
    ############################################################################
    class KeyController(Null):
        """
        A class which controls what should happen when a button is pressed
        on the screen. Primarily intended to indicate where focus should
        travel to when using the arrow keys/dpad, but can be used for other
        controller button shortcuts.

        Attributes:
        -----------
        keymap : dict
            A dictionary of id : dict() pairs, where the id is the id of the
            focused displayable, and dict is a dictionary of event_name + action
            pairs to execute when the event is triggered.
            e.g.
            {
                "button_id": {
                    "focus_up": SetFocus("screen_name", "disp_id"),
                    "focus_down": [SetVariable("something", False),
                        SetFocus("screen_name", "disp_id")],
                }
            }
            These are passed in as kwargs so you can write:
            KeyController(button_id=dict(focus_up=SetFocus("screen", "disp_id")))
        capture : bool
            If True, the KeyController will ignore the event after executing
            the action. If False, the event will be passed to the rest of the
            screen after executing the action.
        activate_sound : string
            The sound to play when a button is pressed. None by default.
        """
        def __init__(self, **kwargs):
            self.capture = kwargs.pop("capture", True)
            activate_sound = kwargs.pop("activate_sound", None)
            self.keymap = kwargs
            if activate_sound is not None:
                super(KeyController, self).__init__(style="default", activate_sound=activate_sound)
            else:
                super(KeyController, self).__init__(style='default')

        def event(self, ev, x, y, st):
            """
            Handle events for this keymapping.
            """
            focused = renpy.display.focus.get_focused()
            if focused is None:
                return

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
                screen = renpy.current_screen()
                if not isinstance(screen, renpy.display.screen.ScreenDisplayable):
                    return None
                if screen.child is None:
                    screen.update()

                ## Reverse lookup to get the ID
                disp_to_id = {id(v): k for k, v in screen.widgets.items()}
                focused_id = disp_to_id.get(id(focused), None)
                if focused_id is None:
                    try:
                        focused_id = disp_to_id.get(id(focused.child), None)
                    except:
                        pass

            if focused_id in self.keymap:
                mapping = self.keymap[focused_id]
                for event_name, action in mapping.items():
                    if renpy.map_event(ev, event_name):
                        renpy.play(self.style.activate_sound)
                        rv = renpy.run(action)
                        if rv is not None:
                            return rv
                        if self.capture:
                            raise renpy.IgnoreEvent()


    def make_key_controller(displayable_id, key, action, activate_sound=None,
            capture=True, **kwargs):
        """
        Make a key controller displayable for a specific key and action.
        """
        ## Split up `key` into its parts, if it's a list
        if isinstance(key, list):
            key_dict = {k : action for k in key}
        else:
            key_dict = {key : action}
        return KeyController(activate_sound=activate_sound, capture=capture,
            **{displayable_id : key_dict})

    renpy.register_sl_displayable("focused_on", make_key_controller, "default", 0,
        unique=True
        ).add_positional("displayable_id",
        ).add_property("key"
        ).add_property("action"
        ).add_property("activate_sound"
        ).add_property("capture"
        )


    ############################################################################
    ## FOCUS DISPLAYABLE
    ############################################################################
    class FocusDisplayable(renpy.Displayable):
        """
        A class which will add a displayable near the focused displayable,
        such as a pointer or a highlight frame. Used to draw attention to
        where the currently selected displayable is.

        Attributes:
        -----------
        d : Displayable
            What will be shown when a displayable is focused on-screen.
        xwarper : str
            The warper to use when animating movement on the x-axis. e.g. "ease"
            May also be a function, which will be passed a number between 0.0
            and 1.0 and is expected to return a float.
        ywarper : str
            The warper to use when animating movement on the y-axis. e.g. "ease"
            May also be a function, which will be passed a number between 0.0
            and 1.0 and is expected to return a float.
        xtime : float
            The time it takes to animate the x-axis movement between focused
            displayables. 0, the default, means no animation.
        ytime : float
            The time it takes to animate the y-axis movement between focused
            displayables. 0, the default, means no animation.
        padding : tuple
            An (xpadding, ypadding) or (left, top, right, bottom) padding tuple
            to add around the focused displayable (as though the focused
            displayable were padded). Most useful for frame-style
            FocusDisplayables.
        hide_on_mouse : bool
            If True, the displayable will not show when the mouse is used.
            This is False by default.
        linger_on_focused : bool
            If True, the FocusDisplayable will remain over the last-focused
            displayable, even if focus has been lost. This is False by default.
            This is largely only relevant for mouse-based focus, where
            unhovering a displayable will remove focus.
        active_area : tuple
            An (x, y, width, height) tuple which defines the active area for
            the FocusDisplayable. In most cases, this is relative to the
            screen. If the focused displayable is outside of this area, the
            FocusDisplayable will not appear. This is None by default.
        recheck_period : float
            The number of seconds to re-check the focus coordinates for after
            focus has changed. Useful to ensure displayables with a changing
            focus size have the proper coordinates.
        displayables : dict
            A dictionary of displayable names and their corresponding
            displayables. The default displayable is "default". The names are
            the names of mouse states - you can provide different displayables
            to be used if certain buttons are hovered via the `mouse` property,
            or if the button is pressed via the `pressed` key.

        start_x : float
            The x-coordinate of the last-focused displayable.
        start_y : float
            The y-coordinate of the last-focused displayable.
        start_w : float
            The width of the last-focused displayable.
        start_h : float
            The height of the last-focused displayable.
        target_x : float
            The x-coordinate of the currently-focused displayable.
        target_y : float
            The y-coordinate of the currently-focused displayable.
        target_w : float
            The width of the currently-focused displayable.
        target_h : float
            The height of the currently-focused displayable.
        x : float
            The current x-coordinate of the FocusDisplayable.
        y : float
            The current y-coordinate of the FocusDisplayable.
        w : float
            The current width of the FocusDisplayable.
        h : float
            The current height of the FocusDisplayable.
        anim_st : float
            The start time of the animation, when animating between displayables.
        last_focus_st : float
            The time the last focus change occurred.
        st : float
            The current time.
        has_focus : bool
            Whether the FocusDisplayable is currently focused on a displayable.
        """
        def __init__(self, d=None, **kwargs):
            self.xwarper = kwargs.pop("xwarper", "linear")
            self.ywarper = kwargs.pop("ywarper", "linear")
            self.xtime = kwargs.pop("xtime", 0.0)
            self.ytime = kwargs.pop("ytime", 0.0)
            self.padding = kwargs.pop("padding", (0, 0))
            self.recheck_period = kwargs.pop("recheck_period", 0.25)
            self.last_focus_st = None
            if len(self.padding) == 2:
                self.padding = (self.padding[0], self.padding[1],
                                self.padding[0], self.padding[1])
            self.hide_on_mouse = kwargs.pop("hide_on_mouse", False)
            self.hidden = self.hide_on_mouse and pad_config.is_using_mouse()
            self.linger_on_focused = kwargs.pop("linger_on_focused", False)
            self.active_area = kwargs.pop("active_area", None)

            if isinstance(self.xwarper, str):
                try:
                    xw = renpy.atl.warpers[self.xwarper]
                except KeyError:
                    raise Exception("X warper {} not found.".format(self.xwarper))
                self.xwarper = xw
            if isinstance(self.ywarper, str):
                try:
                    yw = renpy.atl.warpers[self.ywarper]
                except KeyError:
                    raise Exception("Y warper {} not found.".format(self.ywarper))
                self.ywarper = yw
            if self.xtime < 0 or self.ytime < 0:
                raise Exception("Time for the FocusDisplayable must be a positive value.")

            self.start_x = None
            self.start_y = None
            self.start_w = None
            self.start_h = None
            self.target_x = None
            self.target_y = None
            self.target_w = None
            self.target_h = None
            self.x = None
            self.y = None
            self.w = None
            self.h = None
            self.anim_st = None
            self.st = 0
            self.has_focus = False

            displayables = kwargs.pop("displayables", {})
            if d is not None:
                displayables["default"] = d
            self.displayables = {k : renpy.displayable(c) for k, c in displayables.items()}
            if self.displayables.get("default", None) is None:
                renpy.error("FocusDisplayable must have a default displayable.")
            self.displayable = None
            self.d = None
            self.displayable_cache = dict(default='default')
            self.last_displayable = "_default_"
            self.last_displayable_st = 0

            super(FocusDisplayable, self).__init__()

        def visit(self):
            return self.displayables.values()

        def render(self, width, height, st, at):
            self.st = st
            rv = renpy.Render(width, height)
            if self.x is None:
                return rv

            if self.last_focus_st is not None and st-self.last_focus_st < self.recheck_period:
                self.update_focus(st)
                renpy.redraw(self, 0)

            if not self.linger_on_focused and self.start_x is None:
                ## Nothing to focus
                return rv
            elif self.hide_on_mouse and pad_config.is_using_mouse():
                ## Don't show when the mouse is focused
                return rv

            x = self.target_x
            y = self.target_y
            w = self.target_w
            h = self.target_h

            if (self.anim_st is not None and st-self.anim_st > self.xtime
                    and st-self.anim_st > self.ytime):
                ## Animation is done
                self.anim_st = None
            elif (self.xtime > 0 and self.ytime > 0 and self.anim_st is not None
                    and self.start_x is not None and self.start_y is not None
                    and st > 0):
                ## Calculate the location and size of the FocusDisplayable
                ## as it animates to the new position.
                xt = (st - self.anim_st) / self.xtime
                yt = (st - self.anim_st) / self.ytime
                xt = self.xwarper(xt)
                yt = self.ywarper(yt)

                x = self.start_x + (self.target_x - self.start_x) * xt
                y = self.start_y + (self.target_y - self.start_y) * yt
                w = self.start_w + (self.target_w - self.start_w) * xt
                h = self.start_h + (self.target_h - self.start_h) * yt

                if st-self.anim_st <= self.xtime or st-self.anim_st <= self.ytime:
                    renpy.redraw(self, 0)
            else:
                x = self.x
                y = self.y
                w = self.w
                h = self.h

            if self.x != x or self.y != y or self.w != w or self.h != h:
                renpy.redraw(self, 0)

            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.old_position = (self.x, self.y, self.w, self.h)

            rv.place(self.get_displayable_render(st), absolute(self.x-self.padding[0]),
                absolute(self.y-self.padding[1]),
                absolute(self.w+self.padding[0]+self.padding[2]),
                absolute(self.h+self.padding[1]+self.padding[3]), st, at)
            return rv

        def get_displayable_name(self):
            """
            Get the name of the displayable to use.
            """

            disp_kind = renpy.display.focus.get_mouse() # str|None

            if disp_kind is None:
                disp_kind = "default"

            if pygame.mouse.get_pressed()[0]:
                disp_kind = "pressed_" + disp_kind # type: ignore

            if disp_kind in self.displayable_cache:
                return self.displayable_cache[disp_kind]

            original_kind = disp_kind

            if original_kind in self.displayables:
                self.displayable_cache[original_kind] = original_kind
                return original_kind

            if disp_kind.startswith("pressed_") and ("pressed_default" in self.displayables): # type: ignore
                # if a generic pressed_default displayable is defined, use it
                disp_kind = "pressed_default"
            elif disp_kind.startswith("pressed_") and (disp_kind[8:] in self.displayables): # type: ignore
                # otherwise use the non-pressed displayable if we have it in cache
                disp_kind = disp_kind[8:]
            else:
                disp_kind = 'default'

            self.displayable_cache[original_kind] = disp_kind

            return disp_kind

        def get_displayable_render(self, st):
            """
            Determine the name of the displayable to use, and return the
            correct displayable.
            """
            name = self.get_displayable_name()

            if name not in self.displayables:
                name = "default"

            # Adjust st when the displayable changes.
            if (name != self.last_displayable) or (self.displayable is None):
                self.last_displayable = name
                self.last_displayable_st = st
                self.displayable = self.displayables[name]._duplicate(None)

            st = st - self.last_displayable_st

            return self.displayable

        def is_new_focus(self, x, y, w, h):
            """
            Return True if the new focus coordinates are different from the
            current focus coordinates.
            """
            if (self.target_x is None or self.target_y is None
                    or self.target_w is None or self.target_h is None):
                return True
            elif (self.x is None or self.y is None
                    or self.w is None or self.h is None):
                return True

            if (round(self.target_x) != round(x)
                    or round(self.target_y) != round(y)
                    or round(self.target_w) != round(w)
                    or round(self.target_h) != round(h)):
                return True
            return False

        def update_focus(self, st):
            """
            Update the focus coordinates for the FocusDisplayable so we can
            animate to a new position (or appear there).
            """
            if st is None:
                st = self.st

            x, y, w, h = renpy.focus_coordinates()

            if self.active_area is not None and x is not None:
                ## Make sure the new focus coordinates are within the active area
                ax, ay, aw, ah = self.active_area
                if (x < ax or x+w > ax+aw or y < ay or y+h > ay+ah):
                    x = None
                    y = None
                    w = None
                    h = None

            if x is None and not self.linger_on_focused:
                ## Stopped focusing anything
                self.start_x = None
                self.start_y = None
                self.start_w = None
                self.start_h = None
                self.has_focus = False
                self.last_focus_st = st
                renpy.redraw(self, 0)
                return
            elif x is None:
                ## Keep the previous focus coordinates
                self.has_focus = False
                return
            elif self.is_new_focus(x, y, w, h) or not self.has_focus:
                self.last_focus_st = st
                renpy.redraw(self, 0)

            self.has_focus = True

            if self.start_x is None:
                ## First time focus; simply appear, no animation
                self.start_x = x
                self.target_x = x
                self.x = x

                self.start_y = y
                self.target_y = y
                self.y = y

                self.start_w = w
                self.target_w = w
                self.w = w

                self.start_h = h
                self.target_h = h
                self.h = h
                return
            elif self.is_new_focus(x, y, w, h):
                self.anim_st = st
                ## Focus has changed; animate to new position
                self.start_x = self.x
                self.start_y = self.y
                self.start_w = self.w
                self.start_h = self.h
                self.target_x = x
                self.target_y = y
                self.target_w = w
                self.target_h = h

            return

        def event(self, ev, x, y, st):
            self.st = st
            if (self.hide_on_mouse and not self.hidden
                    and pad_config.is_using_mouse()):
                ## Haven't yet hidden it but the mouse is used
                self.hidden = True
                renpy.redraw(self, 0)
            elif self.hidden and not pad_config.is_using_mouse():
                ## Was hidden but the mouse is no longer used
                self.hidden = False
                renpy.redraw(self, 0)
            self.update_focus(st)
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                renpy.redraw(self, 0)


    ############################################################################
    ## ICONBUTTON
    ############################################################################
    class IconButton(Button):
        """
        A class which manages information on a button icon for controllers,
        mouse, and keyboard, in order to display it as a button prompt or in
        a footer.

        Attributes:
        -----------
        pad_event : str
            The event to use for the button on a controller. Should correspond
            to a custom or built-in event in the pad keymaps.
        key_event : str
            The event to use for the button on a keyboard or mouse. Should be
            an event or list of events as recognized by Ren'Py.
            https://www.renpy.org/doc/html/keymap.html
        caption : str
            The text to display alongside the button icon.
        mkb_icon : str or list
            The icon to use for the mouse or keyboard. Should be the name of
            an image or a list of them.
        action : Action
            The action to perform when the appropriate button(s) is clicked.
        activate_sound : str
            The sound to play when the button is activated.
        kind : IconButton
            A IconButton to inherit properties from.
        use_keysym : bool
            If True, then the generated displayable will also use the keysym
            property to receive key events. True by default.
        suffix : string
            Optional. A suffix to use for the images used for the icon
            e.g. "small".
        icon_only : bool
            If True, only the icon will be displayed, without the text. Default
            is False.
        keymap_only : bool
            If True, no image or text will be displayed; only events will be
            captured. Default is False.

        It also takes style properties prefixed with text_, and hbox_ to use
        for the text and hbox displayables, respectively. Other properties are
        passed to the wrapping Button.
        """
        def __init__(self, pad_event=None, key_event=None, caption=None,
                mkb_icon=None, action=None,  activate_sound=None, kind=None,
                use_keysym=True, suffix="", icon_only=False, keymap_only=False,
                hide_on_mouse=False, hide_on_keyboard=False,
                hide_on_controller=False, **kwargs):

            def get_property(name, value, default):
                if value:
                    return value
                if kind:
                    return getattr(kind, name)
                return default

            text_properties, hbox_properties, kwargs = renpy.easy.split_properties(kwargs, "text_", "hbox_", "")

            self.pad_event = get_property("pad_event", pad_event, None)
            self.key_event = get_property("key_event", key_event, None)
            self.caption = get_property("caption", caption, "")
            self.mkb_icon = get_property("mkb_icon", mkb_icon, None)
            if not isinstance(self.mkb_icon, list):
                self.mkb_icon = [self.mkb_icon]
            self.action = get_property("action", action, None)
            self.activate_sound = get_property("activate_sound", activate_sound, None)
            self.use_keysym = get_property("use_keysym", use_keysym, True)
            self.suffix = get_property("suffix", suffix, "")
            self.icon_only = get_property("icon_only", icon_only, False)
            self.keymap_only = get_property("keymap_only", keymap_only, False)
            self.hide_on_mouse = get_property("hide_on_mouse", hide_on_mouse, False)
            self.hide_on_keyboard = get_property("hide_on_keyboard", hide_on_keyboard, False)
            self.hide_on_controller = get_property("hide_on_controller", hide_on_controller, False)
            self.saved_icon = None
            self.last_interaction_type = None
            self.last_layout = persistent.controller_layout

            self.original_button_style = kwargs.get("style", None)
            self.original_text_style = text_properties.get("style", None)
            self.original_hbox_style = hbox_properties.get("style", None)

            if kind is not None:
                ## Inherit hbox properties from another IconButton
                self.hbox_properties = kind.hbox_properties.copy()
                self.hbox_properties.update(hbox_properties)
                self.text_properties = kind.text_properties.copy()
                self.text_properties.update(text_properties)
                self.button_properties = kind.button_properties.copy()
                self.button_properties.update(kwargs)

                ## All IconButtons have a style, so we have to figure out if
                ## it was specifically supplied (to inherit) or just automated.
                if self.original_button_style is None:
                    self.button_properties['style'] = kind.original_button_style or self.button_properties.get("default_style", "icon_button")
                if self.original_text_style is None:
                    self.text_properties['style'] = kind.original_text_style or self.text_properties.get("default_style", "icon_button_text")
                if self.original_hbox_style is None:
                    self.hbox_properties['style'] = kind.original_hbox_style or self.hbox_properties.get("default_style", "icon_button_hbox")
            else:
                self.hbox_properties = hbox_properties
                self.text_properties = text_properties
                self.button_properties = kwargs

                if self.original_button_style is None:
                    self.button_properties['style'] = self.button_properties.get("default_style", "icon_button")
                if self.original_text_style is None:
                    self.text_properties['style'] = self.text_properties.get("default_style", "icon_button_text")
                if self.original_hbox_style is None:
                    self.hbox_properties['style'] = self.hbox_properties.get("default_style", "icon_button_hbox")

            super(IconButton, self).__init__(activate_sound=self.activate_sound,
                action=self.action, alt=self.caption, keyboard_focus=False,
                **self.button_properties)

            ## Register this image to be redrawn when switching between mouse
            ## and keyboard and controller
            pad_config.register_redrawable(self)

        def reset_child(self):
            self.saved_icon = None
            self.set_saved_icon()

        def set_saved_icon(self):
            if not self.saved_icon:
                if self.keymap_only:
                    self.saved_icon = self.get_key()
                else:
                    self.saved_icon = self.get_icon(self.suffix, self.icon_only)
                self._clear()
                self.add(self.saved_icon)

        def render(self, width, height, st, at):
            old_event_type = self.last_interaction_type
            self.last_interaction_type = pad_config.EVENT_LISTENER.last_event_type
            if ((old_event_type != self.last_interaction_type)
                    or persistent.controller_layout != self.last_layout):
                self.last_layout = persistent.controller_layout
                self.reset_child()
            self.set_saved_icon()
            return super(IconButton, self).render(width, height, st, at)

        def visit(self):
            pad_icons = pad_config.get_icons(self.pad_event, self.suffix)
            keyboard_icons = self.mkb_icon
            return [renpy.displayable(x) for x in (pad_icons + keyboard_icons)]

        def get_icon(self, suffix="", icon_only=False):
            ## Return a button with the provided information
            if pad_config.is_using_controller():
                if self.hide_on_controller:
                    return Null()
                event = pad_config.get_event(self.pad_event)
                icon_pairs = pad_config.get_icons(self.pad_event, suffix, True)
                if not icon_pairs:
                    ## There is nothing mapped to this; return Null
                    return Null()
                icons = [ ]
                for i, a in icon_pairs:
                    icons.append(Transform(i, alt=a))
            elif pad_config.is_using_mouse() or pad_config.is_using_keyboard():
                if self.hide_on_mouse and pad_config.is_using_mouse():
                    return Null()
                if self.hide_on_keyboard and pad_config.is_using_keyboard():
                    return Null()
                ## These icons are actually clickable, but not keyboard-focusable
                event = self.key_event
                if not self.mkb_icon:
                    return Null()
                icons = [ ]
                icon = self.mkb_icon
                for i in icon:
                    if suffix:
                        icons.append(i + "_" + suffix)
                    else:
                        icons.append(i)

            if (pad_config.is_using_mouse() or pad_config.is_using_keyboard()
                    or pad_config.is_using_controller()):
                if self.use_keysym:
                    keysym = event
                else:
                    keysym = None
                if not icon_only:
                    icons.append(Text(self.caption, **self.text_properties))
                box = HBox(*icons, **self.hbox_properties)
                self.keysym = keysym
                return box
            return Null()

        def get_key(self):
            """Return a KeyMap with the key event."""
            if not self.action:
                return Null()
            if pad_config.is_using_controller():
                return ui.key(pad_config.get_event(self.pad_event),
                    action=self.action, activate_sound=self.activate_sound)
            else:
                return ui.key(self.key_event, action=self.action,
                    activate_sound=self.activate_sound)


    def icon_button_wrapper(**kwargs):
        """
        A wrapper to handle proper style_prefix assignment for the icon_button
        text and hbox.
        """
        if kwargs.get('style') is None:
            kwargs['default_style'] = ui.prefixed_style("icon_button")
            style = kwargs['default_style']
        else:
            style = kwargs['style']
        if kwargs.get('text_style') is None:
            kwargs['text_default_style'] = renpy.style.get_text_style(style, ui.prefixed_style('icon_button_text'))
        if kwargs.get('hbox_style') is None:
            kwargs['hbox_default_style'] = ui.prefixed_style('icon_button_hbox')
        return IconButton(**kwargs)

    renpy.register_sl_displayable("icon_button", icon_button_wrapper, "icon_button", 0,
        ).add_property("pad_event"
        ).add_property("key_event"
        ).add_property("caption"
        ).add_property("mkb_icon"
        ).add_property("action"
        ).add_property("activate_sound"
        ).add_property("kind"
        ).add_property("use_keysym"
        ).add_property("suffix"
        ).add_property("icon_only"
        ).add_property("keymap_only"
        ).add_property("hide_on_mouse"
        ).add_property("hide_on_keyboard"
        ).add_property("hide_on_controller"
        ).add_property_group("text", prefix='text_'
        ).add_property_group("ui", prefix='text_'
        ).add_property_group("box", prefix='hbox_'
        ).add_property_group("ui", prefix='hbox_'
        ).add_property_group("button", prefix=''
        ).add_property_group("window", prefix=''
        ).add_property_group("ui", prefix=''
        )

    ############################################################################
    ## STICK EVENT
    ############################################################################
    class StickEvent(Null):
        """
        A displayable which handles granular stick events.

        Attributes:
        -----------
        x : Adjustment
            Tracks the general x position of the stick.
        y : Adjustment
            Tracks the general y position of the stick.
        speed : float
            The maximum percentage the stick can cover when it's moved
            all the way to the edge. Only relevant when event_type is 'range'.
        event_type : str
            If 'range', events will use the speed attribute to adjust x and y
            within a provided range. So, positive y axis movement increases y
            (holding down) and negative y axis movement decreases y (holding
            up). Suitable for events such as scrolling, cursor movement,
            etc. If 'axis', the default, the x and y attributes record the
            relative position of the stick along that axis (compared to its full
            range of motion). Note that the 'axis' x and y will be multiplied
            by the stick sensitivity; for a non-multiplied number, see the
            raw_x and raw_y properties.
        which_stick : str
            Which stick to track. "left", "right", or "both".
        changed : callable
            A list of functions to call when the stick position changes. It
            should take three arguments, the x adjustment and the y adjustment
            and the StickEvent object.
        x_min : float
            -1.0 by default. The minimum x value possible.
        x_max : float
            1.0 by default. The maximum x value possible.
        y_min : float
            -1.0 by default. The minimum y value possible.
        y_max : float
            1.0 by default. The maximum y value possible.
        absorb_events : bool
            If True, the StickEvent will absorb stick events and prevent them
            from being passed to other displayables. If False, the default,
            other displayables will receive stick events as well. Which events
            are absorbed depends on which_stick. Note that this only absorbs
            events that are passed along in the event method - it will not
            prevent other StickEvents from updating based on the current
            position of the sticks.
        refresh_rate : float
            The number of seconds before polling the stick coordinates again,
            if it's outside of a dead zone. 0.0 by default, aka as often as
            possible. Setting this to higher numbers can help with performance,
            at the cost of less accurate/frequent stick information.

        possible_stick_events : list
            A list of possible stick events to listen for.
        in_deadzone : bool
            Whether the stick is in the deadzone.
        newly_in_deadzone : bool
            Whether the stick has just entered the deadzone.
        stick_directions : dict
            A dictionary of the current stick directions.
        raw_x : float
            The raw x position of the stick, as a percentage from -1.0 to 1.0
            based on how far it is from the deadzone.
        raw_y : float
            The raw y position of the stick, as a percentage from -1.0 to 1.0
            based on how far it is from the deadzone.
        last_used_stick : tuple
            A tuple of (ID, direction) where ID is the index of the controller
            whose stick was last used, and direction is which stick (i.e.
            "left" or "right") was last used.
        angle : int
            An angle from 0 to 359 where 12:00 is 0 degrees based on the
            current stick position.
        distance : float
            The distance the stick is from the deadzone, as a percentage from
            0.0 to 1.0.
        st : float
            The shown timebase of this StickEvent.
        """
        RANGE_TYPE = 1
        AXIS_TYPE = 2
        def __init__(self, **kwargs):
            """
            Initialize the StickEvent displayable.

            Parameters:
            -----------
            start_x : float
                The starting x position of the stick. Typically a percentage
                between 0.0 and 1.0.
            start_y : float
                The starting y position of the stick. Typically a percentage
                between 0.0 and 1.0.
            x : Adjustment
                The Adjustment object to track the x position of the stick.
                If not provided, this is an adjustment from 0 to 1.
            y : Adjustment
                The Adjustment object to track the y position of the stick.
                If not provided, this is an adjustment from 0 to 1.
            The remaining parameters are as seen in the class attributes.
            """
            event_type = kwargs.pop("event_type", 'axis')
            if event_type == 'axis':
                self.event_type = StickEvent.AXIS_TYPE
            else:
                self.event_type = StickEvent.RANGE_TYPE
            self.refresh_rate = kwargs.pop("refresh_rate", 0.0)
            self.x_min = kwargs.pop("x_min", -1.0)
            self.x_max = kwargs.pop("x_max", 1.0)
            self.y_min = kwargs.pop("y_min", -1.0)
            self.y_max = kwargs.pop("y_max", 1.0)
            start_x = kwargs.pop("start_x", (self.x_max-self.x_min)/2.0)
            start_y = kwargs.pop("start_y", (self.y_max-self.y_min)/2.0)
            self._x = kwargs.pop("x", renpy.display.behavior.Adjustment(range=self.x_max-self.x_min, value=start_x))
            self._y = kwargs.pop("y", renpy.display.behavior.Adjustment(range=self.y_max-self.y_min, value=start_y))
            self.speed = kwargs.pop("speed", min(self.x_max-self.x_min, self.y_max-self.y_min)*10.0)
            self.absorb_events = kwargs.pop("absorb_events", False)
            self.which_stick = kwargs.pop("which_stick", "right")
            self.changed = kwargs.pop("changed", [ ])
            if not isinstance(self.changed, list):
                self.changed = [self.changed]
            super(StickEvent, self).__init__(**kwargs)
            self.possible_stick_events = [ ]
            if self.which_stick in ("left", "both"):
                self.possible_stick_events.extend([
                    pygame.CONTROLLER_AXIS_LEFTX, pygame.CONTROLLER_AXIS_LEFTY])
            if self.which_stick in ("right", "both"):
                self.possible_stick_events.extend([
                    pygame.CONTROLLER_AXIS_RIGHTX, pygame.CONTROLLER_AXIS_RIGHTY])
            self.in_deadzone = True
            self.newly_in_deadzone = False
            self.stick_directions = dict()
            self.last_used_stick = None
            self.repeatable_stick_event = None
            self.last_stick_st = None
            self.angle = 0
            self.distance = 0
            self.raw_x = 0
            self.raw_y = 0
            self.st = 0

        @property
        def x(self):
            return absolute(self._x.value)
        @x.setter
        def x(self, value):
            self._x.change(value)
            self.run_changed()
        def run_changed(self):
            x = self.x + self.x_min
            y = self.y + self.y_min
            if self.event_type == StickEvent.AXIS_TYPE:
                if self.last_used_stick[1] == "left":
                    sensitivity = persistent.left_stick_sensitivity
                else:
                    sensitivity = persistent.right_stick_sensitivity
                x *= sensitivity
                y *= sensitivity
            rv = None
            for cb in self.changed:
                rv = renpy.run(cb, x, y, self)
            if rv is not None:
                renpy.end_interaction(rv)
            ## This is a workaround for Ren'Py's "100 restarts with no
            ## interaction" problem reported only during development which can
            ## occur with this displayable.
            renpy.game.interface.interaction_counter = 0
        @property
        def y(self):
            return absolute(self._y.value)
        @y.setter
        def y(self, value):
            self._y.change(value)
            self.run_changed()

        def check_pygame_sticks(self):
            """
            Check the pygame controller object to see if the stick is
            still being moved, for repeat events.
            """
            uses_left = self.which_stick in ("left", "both")
            uses_right = self.which_stick in ("right", "both")
            for key, ctrl in renpy_controllers.items():
                ## Check if the sticks are in use
                moving = False
                if uses_left:
                    left_deadzone = pad_config.get_stick_dead_zone(key, "left")
                    moving = (abs(ctrl.get_axis(pygame.CONTROLLER_AXIS_LEFTX)) > left_deadzone
                        or abs(ctrl.get_axis(pygame.CONTROLLER_AXIS_LEFTY)) > left_deadzone)
                if moving:
                    break
                if uses_right:
                    right_deadzone = pad_config.get_stick_dead_zone(key, "right")
                    moving = (abs(ctrl.get_axis(pygame.CONTROLLER_AXIS_RIGHTX)) > right_deadzone
                        or abs(ctrl.get_axis(pygame.CONTROLLER_AXIS_RIGHTY)) > right_deadzone)
                if moving:
                    break
            return moving

        def handle_stick_movement(self, reset_deadzone=True):
            """
            Handle stick movement events.
            """
            self.calculate_new_stick_position()
            if self.in_deadzone: # Stopped moving
                self.stick_directions = dict()
                self.angle = 0
                self.distance = 0
            renpy.redraw(self, self.refresh_rate)
            if self.newly_in_deadzone and self.event_type == StickEvent.AXIS_TYPE:
                self.x = 0
                self.y = 0
            if self.newly_in_deadzone and reset_deadzone:
                self.newly_in_deadzone = False

        def calculate_new_stick_position(self):
            """
            Calculate a new x, y position based on the position of the sticks.
            """
            self.refresh_stick_position()
            previous_st = self.last_stick_st
            self.last_stick_st = renpy.display.core.get_time()

            if not self.stick_directions or self.in_deadzone:
                ## Nothing to update
                return

            x = self.stick_directions.get("x", 0)
            y = self.stick_directions.get("y", 0)

            id, dir = self.last_used_stick
            dead_zone = pad_config.get_stick_dead_zone(id, dir)
            total = pad_config.get_stick_max(id, dir) - dead_zone
            if x in range(-dead_zone, dead_zone+1):
                left_right_pct = 0
            elif x > 0:
                left_right_pct = (x-dead_zone) / total
            else:
                left_right_pct = (x+dead_zone) / total

            if y in range(-dead_zone, dead_zone+1):
                up_down_pct = 0
            elif y > 0:
                up_down_pct = (y-dead_zone) / total
            else:
                up_down_pct = (y+dead_zone) / total

            self.angle = (math.degrees(math.atan2(up_down_pct, left_right_pct))+90) % 360 # 12:00 is 0
            self.distance = clamp(math.sqrt(left_right_pct**2 + up_down_pct**2), 0.0, 1.0)
            self.raw_x = left_right_pct
            self.raw_y = up_down_pct

            if self.event_type == StickEvent.RANGE_TYPE:
                xspeed = left_right_pct * self.speed
                yspeed = up_down_pct * self.speed

                if previous_st is None:
                    ## First time
                    the_boost = 1.0/60.0
                else:
                    the_boost = (self.last_stick_st - previous_st)

                if self.last_used_stick[1] == "left":
                    the_boost *= persistent.left_stick_sensitivity
                else:
                    the_boost *= persistent.right_stick_sensitivity

                self.x += xspeed * the_boost
                self.y += yspeed * the_boost
            else:
                self.x = left_right_pct + 1.0
                self.y = up_down_pct + 1.0

        def refresh_stick_position(self):
            """
            Update the position of the control sticks.
            """
            if not self.which_stick:
                return
            uses_left = self.which_stick in ("left", "both")
            uses_right = self.which_stick in ("right", "both")
            using_left = False
            using_right = False
            self.stick_directions = dict()
            self.last_used_id = None
            ## Basically, the last controller to not be in the deadzone wins
            ## if there are multiple.
            for key, ctrl in renpy_controllers.items():
                if uses_left:
                    leftx = ctrl.get_axis(pygame.CONTROLLER_AXIS_LEFTX)
                    lefty = ctrl.get_axis(pygame.CONTROLLER_AXIS_LEFTY)
                    left_deadzone = pad_config.get_stick_dead_zone(key, "left")
                    if abs(leftx) > left_deadzone:
                        self.stick_directions["x"] = leftx
                        using_left = True
                        if persistent.left_stick_invert_x:
                            self.stick_directions["x"] *= -1
                    if abs(lefty) > left_deadzone:
                        using_left = True
                        self.stick_directions["y"] = lefty
                        if persistent.left_stick_invert_y:
                            self.stick_directions["y"] *= -1
                    if using_left:
                        self.last_used_stick = (key, "left")
                if uses_right:
                    rightx = ctrl.get_axis(pygame.CONTROLLER_AXIS_RIGHTX)
                    righty = ctrl.get_axis(pygame.CONTROLLER_AXIS_RIGHTY)
                    right_deadzone = pad_config.get_stick_dead_zone(key, "right")
                    if abs(rightx) > right_deadzone:
                        using_right = True
                        self.stick_directions["x"] = rightx
                        if persistent.right_stick_invert_x:
                            self.stick_directions["x"] *= -1
                    if abs(righty) > right_deadzone:
                        using_right = True
                        self.stick_directions["y"] = righty
                        if persistent.right_stick_invert_y:
                            self.stick_directions["y"] *= -1
                    if using_right:
                        self.last_used_stick = (key, "right")
            if not self.stick_directions:
                self.newly_in_deadzone = not self.in_deadzone
                self.in_deadzone = True
            else:
                if self.in_deadzone:
                    ## Make sure to update the stick time, so it doesn't jump
                    self.last_stick_st = renpy.display.core.get_time()
                self.in_deadzone = False

        def event(self, ev, x, y, st):
            is_stick_event = self.check_stick_event(ev)
            self.do_absorb_events(ev, is_stick_event)

        def render(self, width, height, st, at):
            self.st = st
            if not self.in_deadzone:
                self.handle_stick_movement()
            return super(StickEvent, self).render(width, height, st, at)

        def check_stick_event(self, ev):
            """Handle granular stick movement. Returns whether the event
            was a stick event."""
            is_stick_event = False
            ## NOTES:
            ## up - False
            ## value - between -32768 and 32767
            ## axis - 1 (left) or 3 (right)
            ## which - The pad ID in the controllers dict
            try:
                is_stick_event = (ev.type == pygame.CONTROLLERAXISMOTION
                    and ev.axis in self.possible_stick_events)
            except:
                pass
            if is_stick_event:
                uses_left = self.which_stick in ("left", "both")
                uses_right = self.which_stick in ("right", "both")
                is_valid = False
                if uses_left and ev.axis in (pygame.CONTROLLER_AXIS_LEFTX,
                        pygame.CONTROLLER_AXIS_LEFTY):
                    if ev.axis == pygame.CONTROLLER_AXIS_LEFTX:
                        self.stick_directions["x"] = ev.value
                    else:
                        self.stick_directions["y"] = ev.value
                    is_valid = "left"
                elif uses_right and ev.axis in (pygame.CONTROLLER_AXIS_RIGHTX,
                        pygame.CONTROLLER_AXIS_RIGHTY):
                    if ev.axis == pygame.CONTROLLER_AXIS_RIGHTX:
                        self.stick_directions["x"] = ev.value
                    else:
                        self.stick_directions["y"] = ev.value
                    is_valid = "right"
                if is_valid:
                    self.last_used_stick = (ev.which, is_valid)
                    self.handle_stick_movement()
            return is_stick_event

        def do_absorb_events(self, ev, is_stick_event):
            ## Ignore the left/right stick events if we're absorbing them.
            if self.absorb_events:
                if (ev.type == pygame.CONTROLLERAXISMOTION
                        and ev.axis in self.possible_stick_events):
                    raise renpy.IgnoreEvent()
                try:
                    left_event = (any([(x in ev.controller) for x in ("pad_leftx", "pad_lefty")])
                        and self.which_stick in ("left", "both"))
                    right_event = (any([(x in ev.controller) for x in ("pad_rightx", "pad_righty")])
                        and self.which_stick in ("right", "both"))
                except:
                    return
                if left_event or right_event:
                    raise renpy.IgnoreEvent()

    renpy.register_sl_displayable("stick_event", StickEvent, "default", 0,
        ).add_property("start_x"
        ).add_property("start_y"
        ).add_property("x_min"
        ).add_property("y_min"
        ).add_property("x_max"
        ).add_property("y_max"
        ).add_property("x"
        ).add_property("y"
        ).add_property("speed"
        ).add_property("which_stick"
        ).add_property("changed"
        ).add_property("event_type"
        ).add_property("refresh_rate"
        ).add_property("absorb_events"
        )
