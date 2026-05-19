################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for a controller-friendly viewport in Ren'Py. There
## is both a CDD to handle the rendering of the viewport, and a screen language
## keyword so it can be easily declared in-game.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## For examples and detailed information, check out the Tools section on my
## website: https://feniksdev.com/tool/controller-viewport/
## This is just the backend; you don't need to understand everything in
## this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**01_controller_vp.rpy", None)
    build.classify("**01_controller_vp.rpyc", "archive")
################################################################################

python early:

    class ControllerVP(Viewport, StickEvent):
        """
        A special viewport that can be scrolled with the analog sticks and will
        update the scroll position based on the currently focused child.
        Inherits from the built-in Viewport.

        Attributes:
        -----------
        vscroll_style : string or tuple
            The style of scrolling to use when adjusting the vertical scroll.
            One of "start", "page", "nudge", "center", None, or a tuple.
            Default is None.
            "start" ensures the currently focused child is always at the top
            of the viewport.
            "page" will not scroll unless the currently focused child is out
            of view, in which case it will adjust the viewport to put the child
            at the top/left of the viewport.
            "nudge" will not scroll unless the currently focused child is out
            of view, in which case it will only scroll as much as is required
            to put it within view.
            "center" will scroll the viewport to put the currently focused child
            in the center (where possible - if the child is at the edge it
            scrolls as far as it can).
            None does not adjust the vertical scrolling for a focused child.
            May also be provided a tuple, in which case the numbers are
            (yanchor, ypos). The yanchor is the anchor on the focused child,
            and the ypos is the position relative to the viewport window where
            that anchor is positioned. So, (0.5, 0.5) is equivalent to the
            "center" scroll style. (1.0, 0.5) would put the bottom of the child
            at the center of the viewport. Takes floats, integers, and position
            types and handles them accordingly.

        hscroll_style : string
            The style of scrolling to use when adjusting the horizontal scroll.
            As for vscroll_style, but with priority for putting the child
            to the left of the viewport rather than the top. If provided a
            tuple, it is (xanchor, xpos) instead.
        scroll_delay : tuple
            A tuple of two floats, the first being the time to scroll
            horizontally to the new position and the second being the time
            to scroll vertically to the new position. Set this to (0, 0) for
            no scrolling animation.
        scroll_warper : string
            The name of the warper to use for scrolling animations. Default
            is "ease". May also be a function, which will be passed a value
            between 0.0 and 1.0 and is expected to return a float.
        trap_focus : iterable
            If not None, a list with a subset of "left", "right", "up", "down".
            Focus will be trapped in the viewport in the directions specified
            (so if "right" is trapped, pressing right will not leave the
            viewport). A value of ("left", "right", "up", "down") will
            prevent any focus input from leaving the viewport. This can prevent
            unintentionally leaving the viewport when scrolling.
        which_stick : string
            One of "right", "left", "both", or None. Default is None. If
            not None, the provided stick on the controller will also scroll
            the viewport, like arrowkey input. Typically this should be used
            for viewports without selectable children (otherwise it's preferred
            to let the focus change the scroll position).
        absorb_events : bool
            If True, the default, this viewport will absorb stick input when
            which_stick is not None, to avoid focus issues. If you have more than
            one viewport, this should be False for all but one of the viewports.
            Only important if focus_scroll is False.
        focus_scroll : bool
            If True, the viewport will only scroll when it is focused. If
            False, the controller sticks can scroll the viewport even if it
            is not focused. False by default.
        shortcuts : bool
            If True, the shortcut R+Up will scroll to the top of the viewport
            and R+Down will scroll to the bottom of the viewport. Default is
            False. R+Left and R+Right do the same for horizontal scrolling.
        extra_scroll : dict
            If not None, this is a dictionary with direction : amount pairs.
            If the provided direction is pressed, the viewport will scroll
            in that direction plus the provided extra scroll amount. This can
            be used if you're trying to keep a title/subtitle in view when
            scrolling. e.g. {"up": 100, "down": 100} will scroll an extra 100
            pixels up or down when the up or down direction is pressed.
            May also be a dictionary with displayable IDs as keys, to scroll
            extra amounts for specific displayables. e.g. {"up": 100, "down": 100,
            "title" : {"up": 150, "down": 150}} will scroll an extra 150 pixels
            instead of 100 if the displayable with the ID "title" is focused.
        focus_displayables : FocusDisplayable[]
            If using FocusDisplayables on this screen, they should be provided
            to this list so they are updated when the viewport is scrolling.
        column_limit_wrap : string
            One of "next", "loop", or None (the default). If "loop", hitting
            up/down at the top/bottom of the viewport will focus the
            bottom/top item. If "next", it will focus the bottom/top item in
            the next column. If None, no wrap behavior is applied.
        row_limit_wrap : string
            One of "next", "loop", or None (the default). If "loop", hitting
            left/right at the left/right of the viewport will focus the
            right/left item. If "next", it will focus the right/left item in
            the next row. If None, no wrap behavior is applied.
        start_end_wrap : True, str
            If True, hitting up/left on the top/leftmost item will focus the
            bottom/rightmost item, and vice-versa. If False, no wrap behavior
            is applied. Can also be set to "row" to only wrap when going
            left/right, or "column" to only wrap when going up/down.
        penalty : int
            A penalty applied to distances outside of the preferred focus
            direction. Used to avoid selecting things too far in the wrong
            direction.
        cache_reverse : bool
            True by default. This means that "reverse" directions will also be
            cached in the focus_cache. e.g. if hitting "left" on button B
            selects button A, then it will also record that hitting "right" on
            button A should select button B. If False, only the "left"->B
            relationship will be cached. This can help speed up performance if
            button relationships are symmetrical.


        vp_children : list
            A list of the children of this viewport's child, for focusing.
        last_focused_in_vp : bool
            True if the last focused item was inside this viewport. Used to
            adjust the viewport when the focus changes from outside of it.
        children_sizes : list
            A list of the sizes of the children of this viewport's child.
        vp_size : tuple
            A (width, height) tuple of this viewport's area, for calculating
            scroll values.
        holding_shortcut : bool
            True if the player is holding the R button for shortcuts.
        new_focus_lock : bool
            True if the viewport is in the process of focusing a new child
            and hasn't yet rendered. After it's rendered, it's set to False.
            While True, new focus events won't be processed.
        focus_cache : dict
            A dictionary of focus relationships, to avoid recalculating them
            every time a new focus event is processed.
        restrict_arrowkeys : string
            If "keyboard", arrowkeys should only process input from keyboards,
            not controller sticks or the controller D-pad. If "not sticks",
            arrowkeys should only process input from keyboards and the D-pad,
            not the sticks. Default is False. Set by setting arrowkeys to
            "keyboard" or "not sticks".
        """
        reverse_dir = {"up": "down", "down": "up",
                    "left": "right", "right": "left"}
        def __init__(self, **kwargs):
            """
            Create a Controller Viewport.
            """
            self.vscroll_style = kwargs.pop("vscroll_style", None)
            if self.vscroll_style == "center":
                self.vscroll_style = (0.5, 0.5)
            elif self.vscroll_style == "start":
                self.vscroll_style = (0.0, 0.0)
            self.hscroll_style = kwargs.pop("hscroll_style", None)
            if self.hscroll_style == "center":
                self.hscroll_style = (0.5, 0.5)
            elif self.hscroll_style == "start":
                self.hscroll_style = (0.0, 0.0)
            self.scroll_delay = kwargs.pop("scroll_delay", (0.3, 0.3))
            self.scroll_warper = kwargs.pop("scroll_warper", "ease")
            self.trap_focus = kwargs.pop("trap_focus", None)
            self.absorb_events = kwargs.pop("absorb_events", True)
            self.shortcuts = kwargs.pop("shortcuts", False)
            self.extra_scroll = kwargs.pop("extra_scroll", None)
            self.column_limit_wrap = kwargs.pop("column_limit_wrap", None)
            self.row_limit_wrap = kwargs.pop("row_limit_wrap", None)
            self.start_end_wrap = kwargs.pop("start_end_wrap", False)
            self.focus_displayables = kwargs.pop("focus_displayables", None)
            self.penalty = kwargs.pop("penalty", None)
            arrowkeys = kwargs.pop("arrowkeys", False)
            if arrowkeys == "keyboard":
                self.restrict_arrowkeys = 'kb'
                kwargs['arrowkeys'] = True
            elif arrowkeys == "not sticks":
                self.restrict_arrowkeys = 'kbd'
                kwargs['arrowkeys'] = True
            else:
                self.restrict_arrowkeys = False
            if self.focus_displayables is None:
                self.focus_displayables = [ ]
            if not isinstance(self.focus_displayables, list):
                self.focus_displayables = [self.focus_displayables]
            if persistent.ALWAYS_SHOWN_FOCUS_DISPLAYABLE:
                self.focus_displayables.append(persistent.ALWAYS_SHOWN_FOCUS_DISPLAYABLE)
            ## Convert strings to displayables, if relevant
            new_displayables = [ ]
            for fd in self.focus_displayables:
                if isinstance(fd, str):
                    new_displayables.append(renpy.get_registered_image(fd))
                else:
                    new_displayables.append(fd)
            self.focus_displayables = new_displayables

            self.vp_children = None
            self.all_offsets = [ ]
            self.children_sizes = [ ]
            self.last_focused_in_vp = False
            self.vp_size = None
            self.holding_shortcut = False
            self.new_focus_lock = False
            self.focus_cache = dict()
            self.cache_reverse = True

            kwargs["event_type"] = "range"
            kwargs["speed"] = kwargs.get("speed", 1000.0)
            kwargs["which_stick"] = kwargs.get("which_stick", None)
            kwargs["absorb_events"] = self.absorb_events
            super(ControllerVP, self).__init__(**kwargs)
            kwargs["x"] = self.xadjustment
            kwargs["y"] = self.yadjustment
            kwargs["event_type"] = "range"
            kwargs["speed"] = kwargs.get("speed", 1000.0)
            kwargs["which_stick"] = kwargs.get("which_stick", None)
            kwargs["absorb_events"] = self.absorb_events
            StickEvent.__init__(self, **kwargs)
            self.focus_scroll = kwargs.pop("focus_scroll", False)

        def per_interact(self):
            self.children_sizes.clear()
            self.vp_size = None
            self.focus_cache.clear()
            super(ControllerVP, self).per_interact()

        def render(self, width, height, st, at):
            """
            Render the controller viewport to the screen, and save some
            information if needed.
            """
            ret = super(ControllerVP, self).render(width, height, st, at)

            if not self.children_sizes:
                self.vp_children, self.all_offsets, self.children_sizes = get_all_children(self.child, 0, 0, width, height)

            if self.vp_size is None:
                self.vp_size = (width, height)

            if (self.which_stick and not self.arrowkeys
                    and not self.draggable and self.focus_scroll):
                ret.add_focus(self, None, 0, 0, width, height)

            for fd in self.focus_displayables:
                fd.update_focus(None)

            if not self.in_deadzone:
                self.handle_stick_movement()

            ## Set the lock to False after it's been rendered
            self.new_focus_lock = False
            return ret

        def get_scroll_delay(self, amount, direction):
            """
            Return the scroll delay for the provided amount and direction.
            """
            if direction == "x":
                return self.scroll_delay[0]
            return self.scroll_delay[1]

        def handle_passing_focus(self, ev, is_stick_event):
            """
            Handle whether the event should be ignored or passed along.
            """
            if self.focus_scroll:
                ## This viewport can only be scrolled when it is focused,
                ## and should pass along events when it isn't focused.
                if renpy.display.focus.get_focused() is not self:
                    return None
            elif self.absorb_events and is_stick_event:
                raise renpy.IgnoreEvent()
            elif self.absorb_events: # For the pad_leftx_pos etc events
                uses_left = self.which_stick in ("left", "both")
                uses_right = self.which_stick in ("right", "both")
                eat_event = False
                try:
                    if uses_left and ('pad_leftx' in ev.controller
                            or 'pad_lefty' in ev.controller):
                        eat_event = True
                    elif uses_right and ('pad_rightx' in ev.controller
                            or 'pad_righty' in ev.controller):
                        eat_event = True
                except:
                    pass
                if eat_event:
                    raise renpy.IgnoreEvent()

            ## Otherwise, it *is* focused or doesn't need to be to handle
            ## events. Does it trap focus in any direction?
            if self.trap_focus:
                for direction in ["up", "down", "left", "right"]:
                    if (direction in self.trap_focus
                            and renpy.map_event(ev, "focus_{}".format(direction))):
                        raise renpy.IgnoreEvent()

            return None

        def handle_scrolling(self, ev=None):
            """
            Handle scrolling with the sticks for this viewport.
            """
            if self.which_stick is None:
                return
            if self.focus_scroll and renpy.display.focus.get_focused() is not self:
                return
            is_stick_event = self.check_stick_event(ev)
            if self.holding_shortcut:
                invert_x = False
                invert_y = False
                try:
                    stick_scroll = any([x in ev.controller for x in [
                        "pad_righty", "pad_rightx", "pad_lefty", "pad_leftx"]])
                except:
                    stick_scroll = False
                if stick_scroll:
                    if persistent.right_stick_invert_y and self.last_used_stick[1] == "right":
                        invert_y = True
                    if persistent.right_stick_invert_x and self.last_used_stick[1] == "right":
                        invert_x = True
                    if persistent.left_stick_invert_y and self.last_used_stick[1] == "left":
                        invert_y = True
                    if persistent.left_stick_invert_x and self.last_used_stick[1] == "left":
                        invert_x = True
                if renpy.map_event(ev, "focus_up"):
                    ## Jump to the top
                    if invert_y:
                        self.yadjustment.change(self.yadjustment.range)
                    else:
                        self.yadjustment.change(0)
                elif renpy.map_event(ev, "focus_down"):
                    ## Jump to the bottom
                    if invert_y:
                        self.yadjustment.change(0)
                    else:
                        self.yadjustment.change(self.yadjustment.range)
                elif renpy.map_event(ev, "focus_left"):
                    ## Jump to the left
                    if invert_x:
                        self.xadjustment.change(self.xadjustment.range)
                    else:
                        self.xadjustment.change(0)
                elif renpy.map_event(ev, "focus_right"):
                    ## Jump to the right
                    if invert_x:
                        self.xadjustment.change(0)
                    else:
                        self.xadjustment.change(self.xadjustment.range)
            self.handle_passing_focus(ev, is_stick_event)

        def get_warper(self):
            """
            Return the warper function for scrolling this viewport.
            """
            if callable(self.scroll_warper):
                return self.scroll_warper
            else:
                return renpy.atl.warpers[self.scroll_warper]

        def extra_scroll_amount(self, focus_dir, nf_index):
            """
            Return the extra scroll amount for the currently focused child
            based on the direction being scrolled.
            """

            ## First, check if the extra_scroll dictionary has items besides
            ## 'left', 'right', 'up', and 'down'.
            if not self.extra_scroll:
                return 0
            ml = [x for x in self.extra_scroll if x not in ("left", "right", "up", "down")]
            if not ml:
                return self.extra_scroll.get(focus_dir, 0)
            amount = self.extra_scroll.get(focus_dir, 0)

            focused = self.vp_children[nf_index]
            try:
                ## In later Ren'Py versions, displayables store their IDs
                focused_id = focused.id
                if focused_id is None:
                    ## For textbuttons, the child gets the ID and the button
                    ## does not.
                    try:
                        focused_id = focused.child.id
                    except:
                        pass
            except:
                ## Otherwise, check if the focused child ID has an entry
                screen = renpy.current_screen()
                if not isinstance(screen, renpy.display.screen.ScreenDisplayable):
                    return amount
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

            if focused_id is None:
                return amount

            return self.extra_scroll.get(focused_id,
                self.extra_scroll.get(focus_dir, amount))

        def is_child_visible(self, child_index, axis="both"):
            """
            Return True if the child at child_index is not visible at the
            current scroll position, False otherwise.
            """
            x, y = self.all_offsets[child_index]
            w, h = self.children_sizes[child_index]
            if axis in ("x", "both"):
                if x+w < self.xadjustment.value:
                    return False
                if x > self.xadjustment.value+self.vp_size[0]:
                    return False
            if axis in ("y", "both"):
                if y+h < self.yadjustment.value:
                    return False
                if y > self.yadjustment.value+self.vp_size[1]:
                    return False
            return True

        def keep_in_view(self, focus_dir, nf_index):
            """
            If the currently focused child is out of view, adjust the viewport
            to keep it in view.
            """
            if (focus_dir or (not self.last_focused_in_vp
                    and focus_dir is None)) and self.vscroll_style:
                amount = 0
                if isinstance(self.vscroll_style, tuple):
                    ## Unpack position types
                    yanchor = absolute.compute_raw(self.vscroll_style[0], int(self.children_sizes[nf_index][1]))
                    ypos = absolute.compute_raw(self.vscroll_style[1], int(self.vp_size[1]))
                    ## Put the yanchor at ypos
                    amount = (self.all_offsets[nf_index][1]
                        + yanchor - (self.yadjustment.value+ypos))
                elif self.vscroll_style in ("nudge", "page"):
                    ## Nudge the viewport only if the child isn't
                    ## fully visible
                    ## Check if it's fully visible.
                    if self.all_offsets[nf_index][1] < self.yadjustment.value:
                        ## The child is above the viewport
                        if self.vscroll_style == "nudge":
                            amount = self.all_offsets[nf_index][1]-self.yadjustment.value
                        else:
                            ## Put it at the bottom
                            amount = self.all_offsets[nf_index][1]+self.children_sizes[nf_index][1]-(self.yadjustment.value+self.vp_size[1])
                    elif self.all_offsets[nf_index][1]+self.children_sizes[nf_index][1] > self.yadjustment.value+self.vp_size[1]:
                        ## The child is below the viewport
                        if self.vscroll_style == "nudge":
                            amount = self.all_offsets[nf_index][1]+self.children_sizes[nf_index][1]-(self.yadjustment.value+self.vp_size[1])
                        else:
                            ## Put it at the top
                            amount = self.all_offsets[nf_index][1]-self.yadjustment.value
                if amount:
                    if self.extra_scroll:
                        ## Special case for re-focused displayables; extra
                        ## amount depends on which way we scrolled
                        if amount < 0:
                            ## Going up
                            amount += self.extra_scroll_amount("up", nf_index)
                        else:
                            ## Going down
                            amount += self.extra_scroll_amount("down", nf_index)
                    ## Special case: We try to make it so the child isn't
                    ## off-screen, even if the player is scrolling really
                    ## quickly. If needed, we'll zap the scroll to keep it
                    ## in view before animating.
                    if (self.yadjustment.animation_target is not None
                            and not self.is_child_visible(nf_index, "y")):
                        ## How far along is the animation?
                        adj_start = self.yadjustment.animation_target - self.yadjustment.animation_amplitude
                        pct_complete = (self.yadjustment.value - adj_start) / self.yadjustment.animation_amplitude
                        ## If it hasn't animated for a frame, instantly set it there
                        if pct_complete*self.yadjustment.animation_delay < 1.0/10.0:
                            if amount < 0: ## Child is above
                                start_y = self.all_offsets[nf_index][1]
                            else: ## Child is below
                                start_y = self.all_offsets[nf_index][1]+self.children_sizes[nf_index][1]-self.vp_size[1]
                            diff = self.yadjustment.value-start_y
                            self.yadjustment.change(start_y, end_animation=True)
                            amount += diff
                            renpy.redraw(self, 0)
                            self.new_focus_lock = True
                    self.yadjustment.animate(amount,
                        self.get_scroll_delay(amount, "y"), self.get_warper())

            if self.hscroll_style and (focus_dir
                    or (focus_dir is None and not self.last_focused_in_vp)):
                amount = 0
                if isinstance(self.hscroll_style, tuple):
                    ## Unpack position types
                    xanchor = absolute.compute_raw(self.hscroll_style[0], int(self.children_sizes[nf_index][0]))
                    xpos = absolute.compute_raw(self.hscroll_style[1], int(self.vp_size[0]))
                    ## Put the xanchor at xpos
                    amount = (self.all_offsets[nf_index][0]
                        + xanchor - (self.xadjustment.value+xpos))
                elif self.hscroll_style in ("nudge", "page"):
                    ## Nudge the viewport only if the child isn't
                    ## fully visible
                    ## Check if it's fully visible.
                    if ((self.all_offsets[nf_index][0]
                            + self.children_sizes[nf_index][0])
                            > self.xadjustment.value+self.vp_size[0]):
                        ## The child is right of the viewport
                        if self.hscroll_style == "nudge":
                            amount = (self.all_offsets[nf_index][0]
                                + self.children_sizes[nf_index][0]
                                - (self.xadjustment.value+self.vp_size[0]))
                        else:
                            ## Put it at the left
                            amount = (self.all_offsets[nf_index][0]
                                - self.xadjustment.value)
                    elif self.all_offsets[nf_index][0] < self.xadjustment.value:
                        ## The child is left of the viewport
                        if self.hscroll_style == "nudge":
                            amount = (self.all_offsets[nf_index][0]
                                - self.xadjustment.value)
                        else:
                            ## Put it at the right edge
                            amount = (self.all_offsets[nf_index][0]
                                + self.children_sizes[nf_index][0]
                                - (self.xadjustment.value+self.vp_size[0]))
                if amount:
                    if self.extra_scroll:
                        ## Special case for re-focused displayables; extra
                        ## amount depends on which way we scrolled
                        if amount < 0:
                            ## Going left
                            amount += self.extra_scroll_amount("left", nf_index)
                        else:
                            ## Going right
                            amount += self.extra_scroll_amount("right", nf_index)
                    ## Special case: We try to make it so the cursor isn't going
                    ## off-screen, even if the player is scrolling really
                    ## quickly. If needed, we'll zap the scroll to keep it
                    ## in view before animating.
                    if (self.xadjustment.animation_target is not None
                            and not self.is_child_visible(nf_index, "x")):
                        ## How far along is the animation?
                        adj_start = self.xadjustment.animation_target - self.xadjustment.animation_amplitude
                        pct_complete = (self.xadjustment.value - adj_start) / self.xadjustment.animation_amplitude
                        if pct_complete*self.xadjustment.animation_delay < 1.0/10.0:
                            if amount < 0: ## Child is left
                                start_x = self.all_offsets[nf_index][0]
                            else: ## Child is right
                                start_x = self.all_offsets[nf_index][0]+self.children_sizes[nf_index][0]-self.vp_size[0]
                            diff = self.xadjustment.value-start_x
                            self.xadjustment.change(start_x, end_animation=True)
                            amount += diff
                            renpy.redraw(self, 0)
                            self.new_focus_lock = True
                    self.xadjustment.animate(amount,
                        self.get_scroll_delay(amount, "x"), self.get_warper())

        def find_extreme_child(self, focused_child, focus_dir):
            """Return the extreme child in the provided direction from the
            currently focused child."""
            last_focus = focused_child
            while True:
                new_focus = self.get_nearest_child(last_focus, focus_dir)
                if new_focus is None:
                    break
                last_focus = new_focus
            return last_focus

        def get_nearest_child(self, start_child, direction):
            """
            Return the nearest child from the starting one in the provided
            direction.
            """
            start_child_index = self.vp_children.index(start_child)
            in_cache = (start_child_index, direction) in self.focus_cache
            ## Save to the focus cache dictionary for easier re-lookup
            ret = self.focus_cache.setdefault((start_child_index, direction),
                nearest_child(self.vp_children,
                    self.all_offsets, self.children_sizes,
                    start_child_index, direction,
                    penalty=self.penalty))
            if ret is not None and self.cache_reverse and not in_cache:
                ## Make sure the opposite version is recorded also
                self.focus_cache.setdefault((self.vp_children.index(ret),
                    ControllerVP.reverse_dir[direction]), start_child)
            return ret

        def event(self, ev, x, y, st):
            """
            Capture events for the controller viewport. Handles focusing and
            scrolling with the gamepad sticks, but otherwise passes off events
            to the viewport like normal.
            """
            grab = renpy.display.focus.get_grab()
            grabbed = False
            if (grab is not None) and getattr(grab, '_draggable', False) and (grab is not self):
                ## Yes grabbed; is it a bar? Which direction?
                if isinstance(grab, Bar):
                    ## Vertical bar, and we're adjusting up/down, so we
                    ## shouldn't focus anything
                    if grab.style.bar_vertical and any([
                            renpy.map_event(ev, "focus_up"),
                            renpy.map_event(ev, "focus_down")]):
                        grabbed = True
                    ## Horizontal bar, and we're adjusting left/right, so we
                    ## shouldn't focus anything
                    elif not grab.style.bar_vertical and any([
                            renpy.map_event(ev, "focus_left"),
                            renpy.map_event(ev, "focus_right")]):
                        grabbed = True

            if self.shortcuts:
                if pad_config.map_event(ev, "scroll_shortcut", "press"):
                    self.holding_shortcut = True
                    raise renpy.IgnoreEvent()
                elif pad_config.map_event(ev, "scroll_shortcut", "release_replace"):
                    self.holding_shortcut = False
                    raise renpy.IgnoreEvent()

            ignore_directions = False
            if self.restrict_arrowkeys and any([
                    renpy.map_event(ev, x) for x in ["focus_down", "focus_left",
                        "focus_right", "focus_up"]]):
                ## Check if it originated from a gamepad
                try:
                    ignore_directions = any(['pad_{}'.format(k) in ev.controller for k in (
                        "leftx", "lefty", "rightx", "righty")])
                    if not ignore_directions and self.restrict_arrowkeys == 'kb':
                        ## Also restrict the d-pad
                        ignore_directions = any(['pad_{}'.format(k) in ev.controller for k in (
                            "dpup", "dpdown", "dpleft", "dpright")])
                except:
                    ignore_directions = False


            focused_child = renpy.display.focus.get_focused()
            if (not grabbed and focused_child is self and not self.focus_scroll
                    and not pad_config.is_using_mouse()):
                ## We don't want to focus the viewport, but the stuff
                ## inside the viewport. Focus the first child.
                renpy.display.focus.clear_focus()
                focused_child = self.find_extreme_child(self.vp_children[0], "left") or self.vp_children[0]
                focused_child = self.find_extreme_child(focused_child, "up") or focused_child
            elif (focused_child not in self.vp_children or grabbed
                    or pad_config.is_using_mouse()):
                ## No point handling focus information. We also don't want
                ## to focus something else if something inside the viewport
                ## was grabbed.
                self.last_focused_in_vp = False
                self.handle_scrolling(ev)
                if ignore_directions and self.absorb_events:
                    raise renpy.IgnoreEvent()
                elif ignore_directions:
                    return
                return super(ControllerVP, self).event(ev, x, y, st)

            nf_index = None
            focus_dir = None
            new_focus_dir = None
            if not self.new_focus_lock and any([
                    renpy.map_event(ev, x) for x in ["focus_down", "focus_left",
                        "focus_right", "focus_up"]]):
                if renpy.map_event(ev, "focus_down"):
                    focus_dir = "down"
                    opposite_dir = "up"
                    next_dir = "right"
                elif renpy.map_event(ev, "focus_up"):
                    focus_dir = "up"
                    opposite_dir = "down"
                    next_dir = "left"
                elif renpy.map_event(ev, "focus_left"):
                    focus_dir = "left"
                    opposite_dir = "right"
                    next_dir = "up"
                else: #if renpy.map_event(ev, "focus_right"):
                    focus_dir = "right"
                    opposite_dir = "left"
                    next_dir = "down"
                new_focus_dir = focus_dir

                if self.holding_shortcut:
                    ## Focus the extreme child in this direction
                    new_focus = self.find_extreme_child(focused_child, focus_dir)
                else:
                    new_focus = self.get_nearest_child(focused_child, focus_dir)

                ## column_limit_wrap, row_limit_wrap, and start_end_wrap
                if new_focus is None and any([self.column_limit_wrap,
                        self.row_limit_wrap, self.start_end_wrap]):

                    ## Case 1: we have column wrapping, and the direction is
                    ## up/down. Focus extreme in the opposite direction.
                    wrap_type = None
                    if self.column_limit_wrap and focus_dir in ("up", "down"):
                        wrap_type = self.column_limit_wrap
                    elif self.row_limit_wrap and focus_dir in ("left", "right"):
                        wrap_type = self.row_limit_wrap

                    skip_wrap = False
                    if not wrap_type and not self.start_end_wrap:
                        ## Nothing to wrap here/focus is whatever it is
                        skip_wrap = True
                    ## If we got to this point, we tried focusing in this
                    ## direction, and there was nothing. Is there anything
                    ## in the start/end direction, with start_end_wrap?
                    elif self.start_end_wrap:
                        which_extreme = None
                        if focus_dir == "left" and self.start_end_wrap in (True, "row"):
                            ## Check if there's anything up
                            if self.get_nearest_child(focused_child, "up") is None:
                                ## Nothing up either. This is the leftmost
                                ## topmost child.
                                which_extreme = "start"
                        elif focus_dir == "right" and self.start_end_wrap in (True, "row"):
                            ## Check if there's anything down
                            if self.get_nearest_child(focused_child, "down") is None:
                                ## Nothing down either. This is the rightmost
                                ## bottommost child.
                                which_extreme = "end"
                        elif focus_dir == "up" and self.start_end_wrap in (True, "column"):
                            ## Check if there's anything left
                            if self.get_nearest_child(focused_child, "left") is None:
                                ## Nothing left either. This is the topmost
                                ## leftmost child.
                                which_extreme = "start"
                        elif focus_dir == "down" and self.start_end_wrap in (True, "column"):
                            ## Check if there's anything right
                            if self.get_nearest_child(focused_child, "right") is None:
                                ## Nothing right either. This is the bottommost
                                ## rightmost child.
                                which_extreme = "end"

                        if which_extreme == "start":
                            if self.start_end_wrap in (True, "row"):
                                directions = ("down", "right")
                            else:
                                directions = ("right", "down")
                            ## focus all the way down and then right
                            opposite_focus = self.find_extreme_child(focused_child, directions[0]) or focused_child
                            new_focus = self.find_extreme_child(opposite_focus, directions[1])
                            new_focus_dir = directions
                            skip_wrap = True
                        elif which_extreme == "end":
                            if self.start_end_wrap in (True, "row"):
                                directions = ("up", "left")
                            else:
                                directions = ("left", "up")
                            ## focus all the way up and then left
                            opposite_focus = self.find_extreme_child(focused_child, directions[0]) or focused_child
                            new_focus = self.find_extreme_child(opposite_focus, directions[1])
                            new_focus_dir = directions
                            skip_wrap = True

                    if not skip_wrap and wrap_type:
                        ## We're not at the start or end, and we can wrap to
                        ## the next item or loop.

                        ## Start by wrapping to the extreme opposite end.
                        new_focus = self.find_extreme_child(focused_child, opposite_dir) or focused_child
                        if wrap_type == "loop":
                            ## That's all we need to do
                            new_focus_dir = opposite_dir
                        else:
                            ## Need to go to the next item
                            new_focus = self.get_nearest_child(new_focus, next_dir)
                            new_focus_dir = (opposite_dir, next_dir)

                ## Ensure that the new child is visible in the viewport
                if new_focus is not None:
                    renpy.display.focus.force_focus(new_focus)
                    nf_index = self.vp_children.index(new_focus)
            elif not self.new_focus_lock:
                ## Make sure this child is visible (this can happen if focusing
                ## this viewport from something else on-screen)
                nf_index = self.vp_children.index(focused_child)

            if self.new_focus_lock and any([
                    renpy.map_event(ev, x) for x in ["focus_down", "focus_left",
                        "focus_right", "focus_up"]]):
                ## Ignore this event until the viewport has time to render
                raise renpy.IgnoreEvent()
            elif nf_index is not None:
                self.keep_in_view(new_focus_dir, nf_index)

                if focus_dir is not None:
                    self.last_focused_in_vp = True
                    raise renpy.IgnoreEvent()

            elif self.trap_focus and focus_dir in self.trap_focus:
                ## The focus is trapped in this direction, so don't let it
                ## leave the viewport
                self.last_focused_in_vp = True
                raise renpy.IgnoreEvent()

            self.last_focused_in_vp = True
            self.handle_scrolling(ev)
            if ignore_directions:
                return
            return super(ControllerVP, self).event(ev, x, y, st)

    def nearest_child(children, offsets, sizes, start_index, direction, penalty=None):
        """
        Calculate the nearest child from the provided start child in
        the provided direction, or None if no child is in that direction.

        children : Displayable[]
            A list of Displayables that it's possible to focus.
        offsets : tuple[]
            A list of (x, y) tuples of the offsets of the children in the
            viewport.
        sizes : tuple[]
            A list of (width, height) tuples of the sizes of the children.
        start_index : int
            The index of the child to start from.
        direction : string
            One of "down", "up", "left", "right". The direction to search in.
        """
        start = children[start_index]
        closest = None
        if penalty is None:
            penalty = config.focus_crossrange_penalty
        closest_dist = (65536.0 * config.focus_crossrange_penalty) ** 2

        if direction in ("down", "up"):
            line_dist = horiz_line_dist
        else:
            line_dist = verti_line_dist

        fx0, fy0 = offsets[start_index]
        fx1, fy1 = offsets[start_index][0]+sizes[start_index][0], offsets[start_index][1]+sizes[start_index][1]
        try:
            insets = children[start_index].style.keyboard_focus_insets or (0, 0, 0, 0)
        except AttributeError: ## keyboard insets were added to 8.3
            insets = (0, 0, 0, 0)
        fx0 += insets[0]
        fx1 -= insets[2]
        fy0 += insets[1]
        fy1 -= insets[3]

        for i in range(len(children)):
            if i == start_index:
                continue
            if not children[i].style.keyboard_focus:
                continue
            if not children[i].focusable:# and not preferences.self_voicing:
                continue
            # if not preferences.self_voicing:
            #     ## Check if it's sensitive (if it's a button)
            #     try:
            #         if not children[i].is_sensitive():
            #             continue
            #     except:
            #         pass

            tx0, ty0 = offsets[i]
            tx1, ty1 = offsets[i][0]+sizes[i][0], offsets[i][1]+sizes[i][1]
            try:
                insets = children[i].style.keyboard_focus_insets or (0, 0, 0, 0)
            except AttributeError: ## keyboard insets were added to 8.3
                insets = (0, 0, 0, 0)
            tx0 += insets[0]
            tx1 -= insets[2]
            ty0 += insets[1]
            ty1 -= insets[3]

            if direction == "down":
                ## Ignore children above the start child
                if offsets[i][1] <= offsets[start_index][1]:
                    continue
                ## Use the bottom edge of the "from" focus
                ax0 = fx0
                ay0 = fy1
                ax1 = fx1
                ay1 = fy1
                ## Use the top edge of the new focus
                bx0 = tx0
                by0 = ty0
                bx1 = tx1
                by1 = ty0
            elif direction == "up":
                ## Ignore children below the start child
                if offsets[i][1] >= offsets[start_index][1]:
                    continue
                ## Use the top edge of the "from" focus
                ax0 = fx0
                ay0 = fy0
                ax1 = fx1
                ay1 = fy0
                ## Use the bottom edge of the new focus
                bx0 = tx0
                by0 = ty1
                bx1 = tx1
                by1 = ty1
            elif direction == "right":
                ## Ignore children to the left of the start child
                if offsets[i][0] <= offsets[start_index][0]:
                    continue
                ## Use the right edge of the "from" focus
                ax0 = fx1
                ay0 = fy0
                ax1 = fx1
                ay1 = fy1
                ## Use the left edge of the new focus
                bx0 = tx0
                by0 = ty0
                bx1 = tx0
                by1 = ty1
            elif direction == "left":
                ## Ignore children to the right of the start child
                if offsets[i][0] >= offsets[start_index][0]:
                    continue
                ## Use the left edge of the "from" focus
                ax0 = fx0
                ay0 = fy0
                ax1 = fx0
                ay1 = fy1
                ## Use the right edge of the new focus
                bx0 = tx1
                by0 = ty0
                bx1 = tx1
                by1 = ty1
            ## Use the Ren'Py distance calculator
            dist = line_dist(ax0, ay0, ax1, ay1, bx0, by0, bx1, by1, penalty)

            if dist < closest_dist:
                closest = children[i]
                closest_dist = dist

        return closest

    def get_all_children(d, xoffset, yoffset, width, height):
        """Return all the children, grandchildren etc of d."""
        children = [ ]
        offsets = [ ]
        sizes = [ ]
        if not hasattr(d, "children"):
            return children, offsets, sizes
        for i, child in enumerate(d.children):
            children.append(child)
            offsets.append(d.offsets[i])
            ## Render it to get the size
            cr = child.render(width, height, 0, 0)
            sizes.append((cr.width, cr.height))
            if hasattr(child, "children"):
                ch, of, sz = get_all_children(child, d.offsets[i][0], d.offsets[i][1], cr.width, cr.height)
                children.extend(ch)
                offsets.extend(of)
                sizes.extend(sz)

        new_offsets = [ ]
        for of in offsets:
            new_offsets.append((of[0]+xoffset, of[1]+yoffset))

        return children, new_offsets, sizes

    def horiz_line_dist(ax0, ay0, ax1, ay1, bx0, by0, bx1, by1, penalty):
        """
        This computes the distance between two horizontal lines. (So the
        distance is either vertical, or has a vertical component to it.)
        The distance is left squared.
        Taken from Ren'Py's focus.py and adjusted to take a variable penalty.
        """

        # The lines overlap in x.
        if bx0 <= ax0 <= ax1 <= bx1 or \
        ax0 <= bx0 <= bx1 <= ax1 or \
        ax0 <= bx0 <= ax1 <= bx1 or \
        bx0 <= ax0 <= bx1 <= ax1:
            return (ay0 - by0) ** 2

        # The right end of a is to the left of the left end of b.
        if ax0 <= ax1 <= bx0 <= bx1:
            return renpy.display.focus.points_dist(ax1, ay1, bx0, by0, penalty, 1.0)
        else:
            return renpy.display.focus.points_dist(ax0, ay0, bx1, by1, penalty, 1.0)

    def verti_line_dist(ax0, ay0, ax1, ay1, bx0, by0, bx1, by1, penalty):
        """
        This computes the distance between two vertical lines. (So the
        distance is either horizontal, or has a horizontal component to it.)
        The distance is left squared.
        Taken from Ren'Py's focus.py and adjusted to take a variable penalty.
        """

        # The lines overlap in y.
        if by0 <= ay0 <= ay1 <= by1 or \
        ay0 <= by0 <= by1 <= ay1 or \
        ay0 <= by0 <= ay1 <= by1 or \
        by0 <= ay0 <= by1 <= ay1:
            return (ax0 - bx0) ** 2

        # The bottom end of a is above the top end of b.
        if ay0 <= ay1 <= by0 <= by1:
            return renpy.display.focus.points_dist(ax1, ay1, bx0, by0, 1.0, penalty)
        else:
            return renpy.display.focus.points_dist(ax0, ay0, bx1, by1, 1.0, penalty)

    renpy.register_sl_displayable("controller_viewport", ControllerVP, 'viewport', 1,
        replaces=True, pass_context=True,
    ).add_property("child_size"
    ).add_property("mousewheel"
    ).add_property("arrowkeys"
    ).add_property("pagekeys"
    ).add_property("draggable"
    ).add_property("edgescroll"
    ).add_property("xadjustment"
    ).add_property("yadjustment"
    ).add_property("xinitial"
    ).add_property("yinitial"
    ).add_property("scrollbars"
    ).add_property("spacing"
    ).add_property("transpose"
    ).add_property("xminimum"
    ).add_property("yminimum"
    ).add_property("penalty"
    ).add_property("cache_reverse"
    ).add_property("vscroll_style"
    ).add_property("hscroll_style"
    ).add_property("scroll_delay"
    ).add_property("scroll_warper"
    ).add_property("which_stick"
    ).add_property("absorb_events"
    ).add_property("speed"
    ).add_property("focus_scroll"
    ).add_property("shortcuts"
    ).add_property("trap_focus"
    ).add_property("extra_scroll"
    ).add_property("focus_displayables"
    ).add_property("column_limit_wrap"
    ).add_property("row_limit_wrap"
    ).add_property("start_end_wrap"
    ).add_property_group("position",
    ).add_property_group("ui",
    )