################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for a controller-friendly cursor in Ren'Py. There
## is both a CDD to handle the rendering of the cursor, and a screen language
## keyword so it can be easily declared in-game.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## For examples and detailed information, check out the Tools section on my
## website: https://feniksdev.com/tool/virtual-cursor/
## This is just the backend; you don't need to understand everything in
## this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**01_virtual_cursor.rpy", None)
    build.classify("**01_virtual_cursor.rpyc", "archive")
################################################################################
python early:
    import pygame, math

    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))

    class VirtualCursor(renpy.display.layout.MultiBox, StickEvent):
        """
        A virtual cursor that can be moved around the screen with the arrow keys
        or the controller sticks.

        Attributes:
        -----------
        cursor : (Displayable, xoffset, yoffset)
            The cursor to display on the screen, and the x and y offsets to use
            to position the hotspot (the pixel which actually triggers events).
            Can be omitted if the "default" key is provided to the cursors dict.
        start_pos : tuple
            The starting position of the cursor. If not provided, it will start
            at the center of the given area.
        keyboard_speed : float
            The speed at which the cursor moves when controlled by the keyboard
            keys, in approximate pixels per second.
        hide_on_mouse : bool
            If True, the virtual cursor will be hidden when the mouse is used.
            True by default.
        snap_to_center : bool
            If True, the cursor will snap to the center of the focus when it
            changes. False by default.
        snap_delay : float
            How long it takes from releasing the stick to snapping to the
            center of the focused displayable, in seconds. 0.5 by default.
        warper : function
            The name of the warper to use for the snapping movement. Default
            is "ease". May also be a function, which will be passed a value
            between 0.0 and 1.0 and is expected to return a float.
        which_stick : str
            One of "left", "right", or "both". Determines which stick(s) to use
            for controlling the cursor. "left" by default.
        debug : bool
            If True, a small red dot will be drawn where the "pointer" part of
            the cursor is. False by default.
        speed : int
            The speed at which the cursor moves when controlled by the
            controller. Approximately pixels-per-second.
        pin_to_coordinates : tuple
            A tuple of (x, y) coordinates where the cursor should be pinned to.
            Typically this is the center of the area (e.g. (0.5, 0.5)). If set,
            instead of the cursor moving, everything else moves around it.
        crop_outside_area : bool
            If True, anything inside the virtual cursor container will be
            cropped if it goes outside the container. False by default. Usually
            only set to True when pin_to_coordinates is set.
        cursor_area : tuple
            An (x, y, width, height) tuple of the area that the cursor moves
            around in. Also the crop area if crop_outside_area is True.
            If not provided, this is just the size of the full screen.
        cursors : dict
            If provided, this is a dictionary of event name : (Displayable,
            xoffset, yoffset) pairs which correspond to cursors that should be
            used for the provided event.
        viewport_id : str
            If provided, the cursor will scroll the viewport with the given id
            instead of moving itself. This is useful for dragging viewports.
        unpin_at_edge : bool
            If True, and pin_to_coordinates and viewport_id are set, the cursor will
            "unpin" from its pinned position when it reaches the edge of the
            viewport,so that elements on the edge can be interacted with (aka it
            moves the cursor and not the viewport at the edges). Otherwise,
            viewports should be padded to account for unreachable areas.

        container_size : tuple
            The size of the container that the cursor moves around in.
            Automatically calculated.
        _x : Adjustment
            The x position of the cursor.
        _y : Adjustment
            The y position of the cursor.
        possible_stick_events : list
            A list of event names that correspond to stick movements. Used to
            determine if a stick event is relevant to this cursor.
        dragging : bool
            True if a drag event was activated. Turns off automatic
            snap_to_center behavior.
        no_snap_displayables : list
            A list of displayables that the cursor should not snap to the
            center for, even if snapping is turned on. By default, this includes
            Drag and Bar.
        last_focus : Displayable
            The last focus that the cursor was over.
        updated_focus : bool
            True if the focus has changed since the last event.
        directions : dict
            A dictionary of directions and their speeds. Used for keyboard
            movement.
        stick_directions : dict
            A dictionary of stick directions and their values. Used for stick
            movement.
        in_deadzone : bool
            True if the stick is in a deadzone.
        hidden : bool
            True if the cursor is hidden due to mouse usage.
        last_used_stick : tuple
            A tuple of (id, "left" or "right") for the last stick used.
        last_keyboard_time : float
            The time the cursor was last updated, when being controlled
            by the keyboard keys.
        pressing : bool
            True if the button_select button is being pressed. For the mouse
            cursor states.
        cursor_cache : dict
            A dictionary of which cursor to use for the different mouse states.
        vp_xadj_ranged : callable
            The value of the viewport's xadjustment's ranged method.
        vp_yadj_ranged : callable
            The value of the viewport's yadjustment's ranged method.
        the_viewport : Viewport
            The saved reference to the viewport, if viewport_id is set.
        """
        def __init__(self, cursor=None, cursors=None, **kwargs):

            self.start_pos = kwargs.pop("start_pos", None)
            self.keyboard_speed = kwargs.pop("keyboard_speed", 1000.0)
            self.hide_on_mouse = kwargs.pop("hide_on_mouse", True)
            self.debug = kwargs.pop("debug", False) if config.developer else False
            self.no_snap_displayables = kwargs.get("no_snap_displayables", [Drag, Bar])
            self.snap_to_center = kwargs.pop("snap_to_center", False)
            self.warper = kwargs.pop("warper", 'ease')
            if not callable(self.warper):
                self.warper = renpy.atl.warpers[self.warper]
            self.snap_delay = kwargs.pop("snap_delay", 0.5)
            self.pin_to_coordinates = kwargs.pop("pin_to_coordinates", None)
            self.crop_outside_area = kwargs.pop("crop_outside_area", False)
            self.cursor_area = kwargs.pop("cursor_area", (0, 0, config.screen_width, config.screen_height))
            self.viewport_id = kwargs.pop("viewport_id", None)
            self.unpin_at_edge = kwargs.pop("unpin_at_edge", False)

            kwargs["x_min"] = 0.0
            kwargs["y_min"] = 0.0
            kwargs["speed"] = kwargs.pop("speed", 1000.0)
            kwargs["event_type"] = "range"
            kwargs["absorb_events"] = kwargs.pop("absorb_events", True)
            kwargs["which_stick"] = kwargs.pop("which_stick", "left")
            StickEvent.__init__(self, **kwargs)

            ## Included here because we fudge drag events via mouse events,
            ## and need to know how to identify dragging.
            self.dragging = False
            self.hidden = self.hide_on_mouse
            self.last_focus = None
            self.updated_focus = False
            self.container_size = None
            self.directions = dict()
            self.last_keyboard_time = None
            self.pressing = False
            self.cursor_cache = dict(default=getattr(renpy.store, 'default_mouse', 'default'))
            self.the_viewport = None
            self.vp_xadj_ranged = None
            self.vp_yadj_ranged = None

            if cursors is None:
                cursors = pad_config.DEFAULT_VIRTUAL_CURSORS
            if cursor is not None:
                cursors["default"] = cursor
            self.cursors = {k : (renpy.displayable(c[0]), c[1], c[2]) for k, c in cursors.items()}
            self.cursor = None
            self.last_cursor = "_default_"
            self.last_cursor_st = 0
            kwargs['layout'] = 'fixed'
            super(VirtualCursor, self).__init__(**kwargs)

        def per_interact(self):
            """
            A method called once per interaction. Used to register the
            x and y adjustments to the cursor.
            """
            self._x.register(self)
            self._y.register(self)
            super(VirtualCursor, self).per_interact()

        def redraw_adjustments(self, st):
            """Redraw the cursor if it's moved."""
            redraw = self._x.periodic(st)
            if redraw is not None:
                renpy.redraw(self, redraw)
            redraw = self._y.periodic(st)
            if redraw is not None:
                renpy.redraw(self, redraw)

        def get_cursor_render(self, st):
            """Determine the name of the mouse to use, and return the cursor."""
            name = self.get_mouse_name()

            # If it doesn't exist, use the default.
            if (name not in self.cursors) or (name == "default"):
                name = getattr(store, "default_mouse", "default")

            if name not in self.cursors:
                name = "default"

            # Adjust st when the cursor changes.
            if (name != self.last_cursor) or (self.cursor is None):
                self.last_cursor = name
                self.last_cursor_st = st
                self.cursor = self.cursors[name][0]._duplicate(None)

            st = st - self.last_cursor_st

            return self.cursor, self.cursors[name][1], self.cursors[name][2]

        def render(self, width, height, st, at):
            rv = super(VirtualCursor, self).render(width, height, st, at)

            if not self.container_size:
                ax, ay, aw, ah = self.cursor_area
                ax = absolute.compute_raw(ax, config.screen_width)
                ay = absolute.compute_raw(ay, config.screen_height)
                aw = absolute.compute_raw(aw, config.screen_width)
                ah = absolute.compute_raw(ah, config.screen_height)
                self.cursor_area = (ax, ay, aw, ah)
                self.container_size = (aw, ah)
                if self.start_pos:
                    x, y = self.start_pos
                    x = absolute.compute_raw(x, aw)
                    y = absolute.compute_raw(y, ah)
                else:
                    x = aw/2.0
                    y = ah/2.0

                if self.pin_to_coordinates:
                    ## Convert the coordinates
                    xc, yc = self.pin_to_coordinates
                    xc = absolute.compute_raw(xc, aw)
                    yc = absolute.compute_raw(yc, ah)
                    self.pin_to_coordinates = (xc+ax, yc+ay)

                if self.pin_to_coordinates and self.viewport_id:
                    self.the_viewport = renpy.get_widget(None, self.viewport_id)
                    vp = self.the_viewport
                    if self.the_viewport is None:
                        raise Exception("There is no viewport with the id {}.".format(self.viewport_id))
                    self.vp_xadj_ranged = vp.xadjustment.ranged
                    self.vp_yadj_ranged = vp.yadjustment.ranged
                    vp.xadjustment.ranged = self.vp_xadj_ranged_fn
                    vp.yadjustment.ranged = self.vp_yadj_ranged_fn

                    ## Our adjustments become the viewport adjustments, plus
                    ## the cursor area.
                    start_x = vp.xadjustment.value + x + xc
                    start_y = vp.yadjustment.value + y + yc
                    self._x.range = vp.xadjustment.range+aw
                    self._x.value = clamp(start_x - xc, 0, vp.xadjustment.range)
                    self._y.range = vp.yadjustment.range+ah
                    self._y.value = clamp(start_y - yc, 0, vp.yadjustment.range)
                else:
                    self._x.range = config.screen_width
                    self._x.value = x+ax
                    self._y.range = config.screen_height
                    self._y.value = y+ay

            if self.hidden:
                if self.crop_outside_area:
                    ret = rv.subsurface(self.cursor_area, focus=True)
                    rv = renpy.Render(width, height)
                    rv.blit(ret, (self.cursor_area[0], self.cursor_area[1]))
                return rv
            ## Refresh for animations
            self.redraw_adjustments(st)

            if not self.in_deadzone:
                self.handle_stick_movement()
            if self.directions:
                ## Keyboard movement
                self.calculate_new_position()
                self.check_for_focus()
            ## Make a fake mousemotion event for edgescrolling and dragging
            ev, x, y = self.make_mousemotion()
            try:
                super(VirtualCursor, self).event(ev, x, y, st)
            except Exception as e:
                pass

            ## Get the cursor
            cursor = self.get_cursor_render(st)
            if self.debug:
                ## Draw a debug dot where the "pointer" part is.
                dot = renpy.displayable(Transform("#f00", xysize=(5, 5))).render(width, height, st, at)
            cursor_x, cursor_y = self.get_cursor_coords()

            if self.pin_to_coordinates and not self.viewport_id:
                xc, yc = self.pin_to_coordinates
                ## Rather than moving the cursor around, everything moves
                ## around the cursor like dragging a viewport.
                offsets = (xc-self.x, yc-self.y)
                ret = renpy.Render(width, height)
                ret.blit(rv, offsets)
                if self.crop_outside_area:
                    rv = ret.subsurface(self.cursor_area, focus=True)
                    ret = renpy.Render(width, height)
                    ret.blit(rv, (self.cursor_area[0], self.cursor_area[1]))
            elif self.pin_to_coordinates and self.viewport_id:
                ## The adjustments should already be set up
                ret = rv
            else:
                if self.crop_outside_area:
                    ret = rv.subsurface(self.cursor_area, focus=True)
                    rv = renpy.Render(width, height)
                    rv.blit(ret, (self.cursor_area[0], self.cursor_area[1]))
                ret = rv

            cr = renpy.render(cursor[0], width, height, st, at)
            ret.subpixel_blit(cr, (cursor_x-cursor[1], cursor_y-cursor[2]))
            if self.debug:
                ## Draw a debug dot where the "pointer" part is.
                ret.blit(dot, (cursor_x, cursor_y))
            return ret

        def vp_xadj_ranged_fn(self, adj):
            """The ranged function for the viewport's x adjustment."""
            if self.vp_xadj_ranged:
                self.vp_xadj_ranged(adj)
            self.refresh_adjustments()

        def vp_yadj_ranged_fn(self, adj):
            """The ranged function for the viewport's y adjustment."""
            if self.vp_yadj_ranged:
                self.vp_yadj_ranged(adj)
            self.refresh_adjustments()

        def refresh_adjustments(self):
            """If we're tied to a viewport, refresh the adjustments."""
            if self.pin_to_coordinates and self.viewport_id:
                vp = self.the_viewport
                if vp is None:
                    raise Exception("There is no viewport with the id {}.".format(self.viewport_id))
                ## Update the adjustments
                self._x.range = vp.xadjustment.range+self.cursor_area[2]
                self._y.range = vp.yadjustment.range+self.cursor_area[3]
                ## Update the values
                xc, yc = self.pin_to_coordinates
                ax, ay, aw, ah = self.cursor_area
                xc -= ax
                yc -= ay
                self._x.value = (clamp(vp.xadjustment.value + xc, 0, vp.xadjustment.range+self.cursor_area[2]))
                self._y.value = (clamp(vp.yadjustment.value + yc, 0, vp.yadjustment.range+self.cursor_area[3]))
                renpy.redraw(self, 0)

        def get_cursor_coords(self, for_passing=False):
            """
            Get the coordinates where the cursor pointer should be rendered.
            This is in screen-space, unless for_passing is True, in which case
            it is adjusted to account for pinned offsets to be passed to its
            children.
            """
            if self.pin_to_coordinates and not self.viewport_id:
                if for_passing:
                    return (self.x, self.y)
                xc, yc = self.pin_to_coordinates
                return (xc, yc)
            elif self.pin_to_coordinates and self.viewport_id:
                xc, yc = self.pin_to_coordinates
                vp = self.the_viewport
                if vp is None:
                    raise Exception("There is no viewport with the id {}.".format(self.viewport_id))
                ax, ay, aw, ah = self.cursor_area
                xc -= ax
                yc -= ay
                if not self.unpin_at_edge or (
                        self.x >= xc and self.x <= xc+vp.xadjustment.range
                        and self.y >= yc and self.y <= yc+vp.yadjustment.range):
                    return (xc + ax, yc + ay)
                else:
                    ## Otherwise, the cursor itself needs to move.
                    ## Calculate the new x and y
                    ## From 0 to xc,
                    if self.x < xc:
                        x = ax + self.x
                    elif self.x > xc+vp.xadjustment.range:
                        x = ax + self.x - vp.xadjustment.range
                    else:
                        x = xc + ax
                    if self.y < yc:
                        y = ay + self.y
                    elif self.y > yc+vp.yadjustment.range:
                        y = ay + self.y - vp.yadjustment.range
                    else:
                        y = yc + ay
                    return (x, y)
            else:
                return (self.x, self.y)

        @property
        def x(self):
            return absolute(self._x.value)
        @x.setter
        def x(self, value):
            if self.pin_to_coordinates and self.viewport_id:
                ## Clamp is different
                vp = self.the_viewport
                if vp is None:
                    raise Exception("There is no viewport with the id {}.".format(self.viewport_id))
                xc, yc = self.pin_to_coordinates
                ax, ay, aw, ah = self.cursor_area
                xc -= ax
                yc -= ay
                if self.unpin_at_edge:
                    new_value = clamp(value, 0, vp.xadjustment.range+self.cursor_area[2])
                else:
                    new_value = clamp(value, xc, vp.xadjustment.range+self.cursor_area[2]-xc)
                self._x.change(new_value)
                vp.xadjustment.change(clamp(new_value - xc, 0, vp.xadjustment.range))
                renpy.redraw(self, 0)
                renpy.redraw(vp, 0)
            else:
                self._x.change(clamp(value, self.cursor_area[0], self.cursor_area[0]+self.cursor_area[2]))
        @property
        def y(self):
            return absolute(self._y.value)
        @y.setter
        def y(self, value):
            if self.pin_to_coordinates and self.viewport_id:
                ## Clamp is different
                vp = self.the_viewport
                if vp is None:
                    raise Exception("There is no viewport with the id {}.".format(self.viewport_id))
                xc, yc = self.pin_to_coordinates
                ax, ay, aw, ah = self.cursor_area
                xc -= ax
                yc -= ay
                if self.unpin_at_edge:
                    new_value = clamp(value, 0, vp.yadjustment.range+self.cursor_area[3])
                else:
                    new_value = clamp(value, yc, vp.yadjustment.range+self.cursor_area[3]-yc)
                self._y.change(new_value)
                vp.yadjustment.change(clamp(new_value - yc, 0, vp.yadjustment.range))
                renpy.redraw(self, 0)
                renpy.redraw(vp, 0)
            else:
                self._y.change(clamp(value, self.cursor_area[1], self.cursor_area[1]+self.cursor_area[3]))

        def animate_to(self, x, y, duration=0.5, warper=None):
            """Animate x and y to the provided coordinates."""
            if self.pin_to_coordinates and self.viewport_id:
                vp = self.the_viewport
                if vp is None:
                    raise Exception("There is no viewport with the id {}.".format(self.viewport_id))
                x = clamp(x, 0, vp.xadjustment.range+self.cursor_area[2])
                y = clamp(y, 0, vp.yadjustment.range+self.cursor_area[3])
            else:
                x = clamp(x, self.cursor_area[0], self.cursor_area[0]+self.cursor_area[2])
                y = clamp(y, self.cursor_area[1], self.cursor_area[1]+self.cursor_area[3])
            x_amplitude = x - self._x.value
            y_amplitude = y - self._y.value

            if warper is None:
                warper = self.warper

            self._x.animate(x_amplitude, duration, warper)
            self._y.animate(y_amplitude, duration, warper)

        def calculate_new_position(self):
            """
            Calculate a new x, y position based on the speed and direction.
            For the keyboard control method.
            """
            previous_st = self.last_keyboard_time
            self.last_keyboard_time = renpy.display.core.get_time()
            ## Figure out the xspeed and yspeed
            xspeed = self.directions.get("left", 0) + self.directions.get("right", 0)
            yspeed = self.directions.get("up", 0) + self.directions.get("down", 0)

            ## Calculate the angle
            if xspeed == 0 and yspeed == 0:
                return
            else:
                angle = math.atan2(yspeed, xspeed)

            ## Calculate the time delta
            if previous_st is not None:
                time_delta = self.last_keyboard_time - previous_st
            else:
                time_delta = 1.0/60.0

            ## Calculate the new x and y
            self.x += self.keyboard_speed * math.cos(angle) * time_delta
            self.y += self.keyboard_speed * math.sin(angle) * time_delta

            renpy.redraw(self, 0)

        def check_for_focus(self, default=False):
            """
            Check if the cursor is over a displayable to focus.
            """
            if renpy.display.focus.grab:
                return

            x, y = self.get_cursor_coords()

            try:
                if not self.hidden:
                    new_focus = renpy.display.render.focus_at_point(x, y)
                else:
                    new_focus = None
            except renpy.display.layout.IgnoreLayers:
                new_focus = None

            if new_focus is None:
                new_focus = renpy.display.focus.global_focus

            self.updated_focus = new_focus is not self.last_focus
            self.last_focus = new_focus

            return renpy.display.focus.change_focus(new_focus, default=default)

        def snap_to_focus(self):
            """
            Snap the cursor to the center of the current focus.
            """
            if not (self.last_focus and self.snap_to_center
                    and self.updated_focus):
                return
            if self.dragging:
                return
            if any(isinstance(self.last_focus.widget, x) for x in self.no_snap_displayables):
                ## Don't snap drags or bars, etc.
                return
            if self.hidden:
                return
            coordinates = None
            for i in renpy.display.focus.focus_list:
                if (i.widget == self.last_focus.widget
                        and i.arg == renpy.display.focus.argument):
                    coordinates = (i.x, i.y, i.w, i.h)
                    break
            if coordinates:
                target_x = coordinates[0] + coordinates[2] // 2
                target_y = coordinates[1] + coordinates[3] // 2
                current_x, current_y = self.get_cursor_coords()
                x_diff = target_x - current_x
                y_diff = target_y - current_y
                x = self.x + x_diff
                y = self.y + y_diff

                self.move_mouse(x, y,
                    duration=self.snap_delay, warper=self.warper)

        def move_mouse(self, x, y, duration=0, warper=None):
            """
            Animate the mouse to the provided point over duration seconds
            using warper.
            """
            self.animate_to(x, y, duration, warper)
            renpy.redraw(self, 0)

        def get_mouse_name(self):
            """
            Get the name of the mouse cursor to use.
            """

            mouse_kind = renpy.display.focus.get_mouse() # str|None

            if mouse_kind is None:
                mouse_kind = "default"

            if self.pressing:
                mouse_kind = "pressed_" + mouse_kind # type: ignore

            if mouse_kind in self.cursor_cache:
                return self.cursor_cache[mouse_kind]

            original_kind = mouse_kind

            if original_kind in self.cursors:
                self.cursor_cache[original_kind] = original_kind
                return original_kind

            if mouse_kind.startswith("pressed_") and ("pressed_default" in self.cursors): # type: ignore
                # if a generic pressed_default cursor is defined, use it
                mouse_kind = "pressed_default"
            elif mouse_kind.startswith("pressed_") and (mouse_kind[8:] in self.cursors): # type: ignore
                # otherwise use the non-pressed cursor if we have it in cache
                mouse_kind = mouse_kind[8:]
            else:
                mouse_kind = 'default'

            self.cursor_cache[original_kind] = mouse_kind

            return mouse_kind

        def handle_stick_movement(self):
            """Handle control stick movement and snapping."""
            super(VirtualCursor, self).handle_stick_movement(reset_deadzone=False)
            if not self.in_deadzone:
                self.check_for_focus()
            elif self.newly_in_deadzone: # Stopped moving
                self.snap_to_focus()
                self.newly_in_deadzone = False

        def event(self, ev, x, y, st):
            """
            Move the cursor around the screen via the arrow keys or the
            controller sticks.
            """
            if self.hide_on_mouse and pad_config.is_using_mouse() and not self.hidden:
                self.hidden = True
                self.pressing = False
                self.stick_directions = dict()
                self.directions = dict()
                renpy.redraw(self, 0)
                try:
                    return super(VirtualCursor, self).event(ev, x, y, st)
                except Exception as e:
                    raise e
            elif self.hide_on_mouse and pad_config.is_using_mouse():
                ## Track the mouse position so we can make the cursor appear
                ## there.
                if not self.pin_to_coordinates:
                    self.x = x
                    self.y = y
                self.pressing = False
                try:
                    return super(VirtualCursor, self).event(ev, x, y, st)
                except Exception as e:
                    raise e
            elif self.hide_on_mouse and not pad_config.is_using_mouse() and self.hidden:
                self.hidden = False
                self.pressing = False
                renpy.redraw(self, 0)

            ## Record the pressed state, for buttons
            old_pressing = self.pressing
            if renpy.map_event(ev, pad_config.get_event("button_select", "press")):
                self.pressing = True
            elif renpy.map_event(ev, pad_config.get_event("button_select", "release_replace")):
                self.pressing = False
            if self.pressing != old_pressing:
                renpy.redraw(self, 0)

            is_stick_event = self.check_stick_event(ev)

            if is_stick_event:
                pass
            elif ev.type == pygame.KEYDOWN:
                if not self.directions:
                    self.last_keyboard_time = renpy.display.core.get_time()

                if ev.key == pygame.K_LEFT:
                    self.directions['left'] = -self.keyboard_speed
                elif ev.key == pygame.K_RIGHT:
                    self.directions['right'] = self.keyboard_speed
                elif ev.key == pygame.K_UP:
                    self.directions['up'] = -self.keyboard_speed
                elif ev.key == pygame.K_DOWN:
                    self.directions['down'] = self.keyboard_speed

                if ev.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                    self.calculate_new_position()
                    renpy.redraw(self, 0)
                    self.check_for_focus()

            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_LEFT:
                    self.directions.pop('left', None)
                elif ev.key == pygame.K_RIGHT:
                    self.directions.pop('right', None)
                elif ev.key == pygame.K_UP:
                    self.directions.pop('up', None)
                elif ev.key == pygame.K_DOWN:
                    self.directions.pop('down', None)

                if ev.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                    if not self.directions:
                        self.last_keyboard_time = renpy.display.core.get_time()
                    self.calculate_new_position()
                    renpy.redraw(self, 0)

                    if not self.directions:
                        ## Snap it if needed
                        self.snap_to_focus()

            original_event = ev

            if (((self.stick_directions or is_stick_event)
                        and (not self.in_deadzone or self.newly_in_deadzone))
                    or self.directions):
                ev, x, y = self.make_mousemotion()

            elif (not pad_config.is_using_mouse()
                    and renpy.map_event(ev, "drag_activate")
                    and not self.dragging):
                ## Make a fake mousedown event for the drag
                x, y = self.get_cursor_coords(for_passing=True)
                x = int(x)
                y = int(y)
                ev = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {
                    "pos" : (x, y),
                    "button" : 1,
                    "mod" : 0,
                })
                self.dragging = True
            elif (not pad_config.is_using_mouse()
                    and renpy.map_event(ev, "drag_deactivate")
                    and self.dragging):
                ## Make a fake mouseup event for the drag
                x, y = self.get_cursor_coords(for_passing=True)
                x = int(x)
                y = int(y)
                ev = pygame.event.Event(pygame.MOUSEBUTTONUP, {
                    "pos" : (x, y),
                    "button" : 1,
                    "mod" : 0,
                })
                self.dragging = False

            ## Shouldn't be able to change focus any other way
            if any(renpy.map_event(ev, x) for x in ["focus_left",
                        "focus_right", "focus_up", "focus_down"]):
                raise renpy.IgnoreEvent()

            try:
                ret = super(VirtualCursor, self).event(ev, x, y, st)
            except Exception as e:
                raise e

            if any(renpy.map_event(original_event, x) for x in ["focus_left",
                        "focus_right", "focus_up", "focus_down"]):
                raise renpy.IgnoreEvent()
            return ret

        def make_mousemotion(self):
            ## Convert this event into a mousemotion one
            ## so stuff like edgescroll works
            x, y = self.get_cursor_coords(for_passing=True)
            x = int(x)
            y = int(y)
            ev = pygame.event.Event(pygame.MOUSEMOTION, {
                "pos" : (x, y),
                "touch" : False,
                "mod" : 0,
            })
            return ev, x, y


    class MoveVirtualCursor(Action):
        """
        An action that moves the virtual cursor to a specific location,
        relative to the size of the virtual cursor area.

        Attributes:
        -----------
        id : str
            The id of the virtual cursor.
        x : int
            The x position to move to.
        y : int
            The y position to move to.
        duration : float
            The duration of the movement. 0 by default.
        warper : function
            The warper function to use for the movement. A string name of a
            pre-existing warper such as "ease", or a custom function that takes
            a float between 0.0 and 1.0 and returns a float. Default is "ease".
        """
        def __init__(self, id, x, y, duration=0, warper="ease"):
            self.id = id
            self.x = x
            self.y = y
            self.duration = duration
            self.warper = warper
            if not callable(self.warper):
                self.warper = renpy.atl.warpers[self.warper]

        def get_sensitive(self):
            """
            Return True if it's possible to move the cursor to this position.
            """
            d = renpy.get_widget(None, self.id)
            if d is None:
                raise Exception("There is no displayable with the id {}.".format(self.id))
            ## Can't move it if it's already there
            return not (d.x == self.x and d.y == self.y)

        def __call__(self):
            if not _preferences.mouse_move:
                return
            d = renpy.get_widget(None, self.id)
            if d is None:
                raise Exception("There is no displayable with the id {}.".format(self.id))
            d.move_mouse(self.x, self.y, self.duration, self.warper)


    ## Register the virtual cursor container as a screen language keyword.
    renpy.register_sl_displayable("virtual_cursor", VirtualCursor, "cursor_box", "many",
        # default_keywords={ 'layout' : 'fixed' }
        ).add_property("cursor"
        ).add_property("cursors"
        ).add_property("start_pos"
        ).add_property("speed"
        ).add_property("changed"
        ).add_property("snap_to_center"
        ).add_property("snap_delay"
        ).add_property("warper"
        ).add_property("hide_on_mouse"
        ).add_property("no_snap_displayables"
        ).add_property("which_stick"
        ).add_property("debug"
        ).add_property("pin_to_coordinates"
        ).add_property("crop_outside_area"
        ).add_property("keyboard_speed"
        ).add_property("cursor_area"
        ).add_property("refresh_rate"
        ).add_property("viewport_id"
        ).add_property("unpin_at_edge"
        ).add_property("absorb_events"
        ).add_property_group("box"
        ).add_property_group("ui")


style cursor_box:
    is fixed