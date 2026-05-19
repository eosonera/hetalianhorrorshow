################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for a controller-friendly on-screen keyboard in
## Ren'Py. It subclasses Input to add a method which can be called to add
## a letter to the input.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## If you'd like to see how to use this tool, check the Tools section on my
## website: https://feniksdev.com/tool/virtual-keyboard/
## This is just the backend; you don't need to understand everything in
## this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**01_controller_input.rpy", None)
    build.classify("**01_controller_input.rpyc", "archive")
################################################################################
python early:

    import re

    class ControllerInput(Input):
        """
        A class which allows for arbitrary buttons to control input for
        an input value. Subclasses Input from the engine.
        """

        def add_letter(self, raw_text=None):
            """
            Add a letter to the input at the current position. Borrowed from
            the event method of the Input class. Used to allow button presses
            to add letters to the input for controller support.
            """
            if raw_text is None:
                return

            l = len(self.content)
            text = ""

            for c in raw_text:

                # Allow is given
                if self.allow:

                    # Allow is regex
                    if isinstance(self.allow, re.Pattern):

                        # Character doesn't match
                        if self.allow.search(c) is None:
                            continue

                    # Allow is string
                    elif c not in self.allow:
                        continue

                # Exclude is given
                if self.exclude:

                    # Exclude is regex
                    if isinstance(self.exclude, re.Pattern):

                        # Character matches
                        if self.exclude.search(c) is not None:
                            continue

                    # Exclude is string
                    elif c in self.exclude:
                        continue

                text += c

            if self.length:
                remaining = self.length - len(self.content)
                text = text[:remaining]

            if text:

                content = self.content[0:self.caret_pos] + text + self.content[self.caret_pos:l]
                self.caret_pos += len(text)

                self.update_text(content, self.editable, check_size=True)


    renpy.register_sl_displayable("controller_input", ControllerInput, "input", 0, replaces=True
        ).add_property_group("ui"
        ).add_property_group("text"
        ).add_property("value"
        ).add_property("default"
        ).add_property("length"
        ).add_property("pixel_width"
        ).add_property("allow"
        ).add_property("exclude"
        ).add_property("copypaste"
        ).add_property("prefix"
        ).add_property("suffix"
        ).add_property("changed"
        ).add_property("mask"
        ).add_property("caret_blink"
        ).add_property("caret"
        ).add_property("multiline"
        )

init python:

    class InputLetter(Action):
        """
        A class which provides a screen action to add a letter to an input.
        May only be used with ControllerInput.

        Attributes:
        -----------
        id : str
            The id of the ControllerInput to add the letter to.
        letter : str
            The letter to add to the input.
        layer : int
            The layer the ControllerInput screen is on. Can usually be omitted.
        """
        def __init__(self, id, letter, layer=None):
            self.id = id
            self.letter = letter
            self.layer = layer
        def __call__(self):
            if self.letter == '\u00A0':
                return
            screen = renpy.current_screen()
            if not isinstance(screen, renpy.display.screen.ScreenDisplayable):
                return None
            if screen.child is None:
                screen.update()
            the_input = screen.widgets.get(self.id, self.layer)
            if the_input is not None:
                the_input.add_letter(self.letter)


    class UniversalInputToggle(Action):
        """
        A class which will either toggle on the provided input value or
        show an on-screen keyboard input screen for the player to use,
        depending on what control scheme they're using.
        """
        valid_input_kwargs = [
            'default', 'mask', 'length', 'allow', 'exclude', 'value', 'prefix',
            'suffix', 'copypaste', 'changed', 'pixel_width', 'action',
            'multiline', 'caret', 'caret_blink',
        ]
        def __init__(self, id, **kwargs):
            self.id = id
            self.kwargs = kwargs
        def get_selected(self):
            """Return selected if this input is currently editable."""
            current, editable = renpy.get_editable_input_value()
            dp = renpy.get_displayable(None, self.id)
            if dp is None:
                return False
            else:
                return (current == dp.value) and editable
        def __call__(self):
            ## Decide whether to use the controller input or the regular input
            dp = renpy.get_displayable(None, self.id)
            if pad_config.is_using_controller():
                if dp is not None:
                    dp_kwargs = {k: v for k, v in dp.__dict__.items() if k in UniversalInputToggle.valid_input_kwargs}
                    dp_kwargs.update(self.kwargs)
                    self.kwargs = dp_kwargs
                renpy.run(ShowOnscreenInput(**self.kwargs))
            else:
                if dp is not None:
                    renpy.run(dp.value.Toggle())


    class ShowOnscreenInput(Show):
        """
        An action which shows an onscreen keyboard for controller input.
        """
        def __init__(self, screen=None, transition=None, *args, **kwargs):
            self.transition = transition
            self.args = args
            self.kwargs = kwargs
            allow = kwargs.get("allow", None)
            exclude = kwargs.get("exclude", None)
            adjust_input_kwargs(None, allow, exclude, self.kwargs)
            ## Use the numpad, if suggested.
            suggested_screen = kwargs.pop('suggested_screen', None)
            if screen is None and suggested_screen is not None:
                self.screen = suggested_screen
            else:
                self.screen = "onscreen_keyboard"
            if 'done_action' in self.kwargs:
                ## Add `Hide()` to it if relevant
                if isinstance(self.kwargs['done_action'], list):
                    self.kwargs['done_action'].append(Hide())
                elif self.kwargs['done_action'] is None:
                    self.kwargs['done_action'] = Hide()
                else:
                    self.kwargs['done_action'] = [self.kwargs['done_action'], Hide()]


    def input_check(s, to_capitalize=False, properties=None, pad=10):
        """
        Capitalize the letters in the provided string, if to_capitalize is
        True. Otherwise, return the lowercase version of the string. If
        properties is provided, it should be a dictionary with properties
        from an input field (typically 'allow' or 'deny'). These will be used
        to filter out the final letters. It will also pad out the string to be
        10 characters long with non-breaking spaces.
        """
        ## For special characters like ' and ?, when shift is held down
        ## they are replaced with " and / respectively.
        lowercase_version = s.lower()
        capital_version = s.upper()
        for key in pad_config.SHIFT_DICT:
            capital_version = capital_version.replace(key, pad_config.SHIFT_DICT[key])

        if to_capitalize:
            s = capital_version
        else:
            s = lowercase_version

        if not properties:
            ## Pad out the string
            if pad:
                while len(s) < pad:
                    s += '\u00A0'
                    if len(s) < pad:
                        s = '\u00A0' + s
            return s

        if 'allow' in properties and properties['allow']:
            new_s = ''
            for indx, char in enumerate(s):
                if char in properties['allow']:
                    new_s += char
                elif not to_capitalize and capital_version[indx] in properties['allow']:
                    new_s += capital_version[indx]
                elif to_capitalize and lowercase_version[indx] in properties['allow']:
                    new_s += lowercase_version[indx]
                elif pad > 0:
                    new_s += '\u00A0'
            s = new_s
        elif 'exclude' in properties and properties['exclude']:
            for char in properties['exclude']:
                if pad > 0:
                    s = s.replace(char, '\u00A0')
                else:
                    s = s.replace(char, '')

        ## Pad out the string
        if pad:
            while len(s) < pad:
                s += '\u00A0'
                if len(s) < pad:
                    s = '\u00A0' + s
        return s

    renpy_input = renpy.input
    def universal_input(prompt, default='', allow=None, exclude='{}',
            length=None, with_none=None, pixel_width=None, screen=None,
            mask=None, copypaste=True, multiline=False, **kwargs): # @ReservedAssignment
        """
        An input function which will automatically use controller_input or
        regular renpy.input based on whether the player is using a controller
        or not.
        """
        if pad_config.is_using_controller():
            return controller_input(prompt, screen, default=default,
                allow=allow, exclude=exclude, length=length, with_none=with_none,
                pixel_width=pixel_width, mask=mask, copypaste=copypaste,
                multiline=multiline, **kwargs)
        return renpy_input(prompt, default, allow, exclude, length, with_none,
            pixel_width, screen or "input", mask, copypaste, multiline, **kwargs)
    ## End up replacing renpy.input anyway so that stuff like the
    ## automatic save sync input screen show the virtual keyboard too.
    renpy.input = universal_input

    def controller_input(prompt=None, screen=None, default='', allow=None,
            exclude='{}', length=None, with_none=None, pixel_width=None,
            mask=None, copypaste=True, multiline=False, **kwargs): # @ReservedAssignment
        """
        Keywords prefixed with ``show_`` have the prefix stripped and
        are passed to the screen.
        Works the same as https://www.renpy.org/doc/html/input.html#renpy.input
        but shows a virtual keyboard-friendly screen.
        """
        if renpy.config.disable_input:
            return default

        fixed = renpy.in_fixed_rollback()
        config.skipping = False

        if (not renpy.compat.PY2) and renpy.emscripten and renpy.config.web_input and not fixed:
            prompt = prompt or ''
            return web_input(prompt, default, allow, exclude, length, bool(mask))

        renpy.exports.mode('input')

        roll_forward = renpy.exports.roll_forward_info()
        if not isinstance(roll_forward, basestring):
            roll_forward = None

        # use previous data in rollback
        if roll_forward is not None:
            default = roll_forward

        show_properties, kwargs = renpy.easy.split_properties(kwargs, "show_", "")

        adjust_input_kwargs(prompt, allow, exclude, kwargs)
        show_properties["done_action"] = kwargs.pop("done_action", None)
        show_properties["has_numbers"] = kwargs.pop("has_numbers", None)
        show_properties["has_symbols"] = kwargs.pop("has_symbols", None)
        show_properties["allow"] = allow
        show_properties["exclude"] = exclude
        ## Use the numpad, if suggested.
        suggested_screen = kwargs.pop('suggested_screen', None)
        original_screen = screen
        if suggested_screen is not None:
            screen = suggested_screen
        else:
            screen = "onscreen_keyboard"
        show_properties["original_screen"] = original_screen
        if original_screen:
            show_properties['dim'] = True
            if original_screen == "sync_prompt":
                show_properties["has_symbols"] = False

        widget_properties = { }
        widget_properties["tinput"] = dict(default=default, length=length,
            allow=allow, exclude=exclude, editable=not fixed, pixel_width=pixel_width,
            mask=mask, copypaste=copypaste, multiline=multiline)
        renpy.show_screen(screen, _transient=True, _widget_properties=widget_properties,
            prompt=prompt, **show_properties)

        renpy.exports.shown_window()

        if renpy.config.autosave_on_input and not renpy.game.after_rollback:
            renpy.loadsave.force_autosave(True)

        # use normal "say" click behavior if input can't be changed
        if fixed:
            renpy.ui.saybehavior()

        rv = renpy.ui.interact(mouse='prompt', type="input", roll_forward=roll_forward)
        renpy.exports.checkpoint(rv)

        if with_none is None:
            with_none = renpy.config.implicit_with_none

        if with_none:
            renpy.game.interface.do_with(None, None)
        config.skipping = False

        return rv

    def adjust_input_kwargs(prompt, allow, exclude, kwargs):
        """
        Adjust the kwargs provided to input functions for use with the
        onscreen keyboard.
        """
        has_numbers = kwargs.pop('has_numbers', None)
        has_symbols = kwargs.pop('has_symbols', None)
        ## To know whether to show a number row
        if has_numbers is None:
            if allow is not None:
                has_numbers = False
                if any(x in '0123456789' for x in allow):
                    has_numbers = True
            elif exclude is not None:
                has_numbers = True
                if all(x in exclude for x in '0123456789'):
                    has_numbers = False
        ## To know whether to have the symbols page
        if has_symbols is None:
            if allow is not None:
                has_symbols = False
                if not all(c.isalnum() or c.isspace() for c in allow):
                    has_symbols = True
            elif exclude is not None:
                has_symbols = True
                if all(c.isalnum() or c.isspace() for c in exclude):
                    has_symbols = False
        ## A check to see if we should use the numpad
        only_numpad = False
        if allow is not None:
            only_numpad = all(x in '0123456789' for x in allow)
        ## It would be pretty silly to try to instead exclude everything but
        ## numbers, so we don't check for that.
        kwargs['suggested_screen'] = "onscreen_numpad" if only_numpad else None

        done_action = kwargs.pop('done_action', QueueEvent("input_enter"))
        kwargs['done_action'] = done_action
        kwargs['has_numbers'] = has_numbers
        kwargs['has_symbols'] = has_symbols
        return