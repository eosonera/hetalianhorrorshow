################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for a controller-friendly on-screen keyboard in
## Ren'Py. It includes a screen to display the keyboard to the player which
## supports several button shortcuts.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## The backend can be found in 01_controller_input.rpy.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################

## How wide the keyboard keys are
define pad_config.KEYBOARD_BUTTON_WIDTH = 120
## How tall the keyboard keys are
define pad_config.KEYBOARD_BUTTON_HEIGHT = 90
## How much space is between the keyboard keys
define pad_config.KEYBOARD_BUTTON_SPACING = 5


## A convenient screen to organize the footer with key prompts.
screen key_footer():
    ## Show controller prompts for controller users.
    hbox:
        anchor (1.0, 1.0) pos (0.97, 0.97)
        spacing 25 style_prefix None
        transclude

style pad_prompt_hbox:
    spacing 12
style pad_prompt_text:
    yalign 0.5

## This is the screen that's used when you need to get input from the
## player. Most of these will be automatically filled out; the main new one
## is dim (True by default; will dim the screen behind the keyboard).
## You can also provide a more specific done action if needed.
screen onscreen_keyboard(prompt=None, value=None, has_numbers=True, has_symbols=True,
    done_action=Return(), dim=True, **input_properties):

    modal True
    zorder 100

    default original_screen = input_properties.pop("original_screen", None)
    if original_screen:
        use expression original_screen pass (prompt=prompt)

    if dim:
        ## Feel free to change the background image. `modal True` should be
        ## retained to prevent clicking through to the screen underneath
        ## (if applicable).
        frame:
            background "#000b" modal True
            xysize (config.screen_width, config.screen_height)

    ## Whether shift is active or not
    default holding_shift = False
    ## Whether the symbol tab is active or not
    default which_tab = 0

    if value is not None:
        ## Make sure it's editable
        on 'show' action value.Enable()

    vbox:
        style_prefix 'ckeyboard'

        frame:
            has vbox
            if prompt is not None:
                text prompt
            ## This uses the special controller_input displayable rather than
            ## regular input. It has an ID so it can be referenced by the
            ## buttons.
            controller_input id 'tinput' properties input_properties:
                if value is not None:
                    value value

        if has_numbers:
            hbox:
                for let in "1234567890":
                    textbutton let action InputLetter("tinput", let)

        if which_tab == 0: ## Alphabet tab
            hbox:
                ## input_check will help pad out the keys and display them
                ## properly when the shift key is held down.
                for idx, let in enumerate(input_check(__(pad_config.KEYBOARD_ROW1), holding_shift, input_properties)):
                    textbutton let action InputLetter("tinput", let):
                        if idx == 0 and pad_config.is_using_controller():
                            default_focus True
            hbox:
                for let in input_check(__(pad_config.KEYBOARD_ROW2), holding_shift, input_properties):
                    textbutton let action InputLetter("tinput", let)
            hbox:
                for let in input_check(__(pad_config.KEYBOARD_ROW3), holding_shift, input_properties):
                    textbutton let action InputLetter("tinput", let)

        elif which_tab == 1: ## Symbols tab
            hbox:
                for let in input_check("!@#$%^&*()", False, input_properties):
                    textbutton let action InputLetter("tinput", let)
            hbox:
                for let in input_check("`~_-+=:;'\"", False, input_properties):
                    textbutton let action InputLetter("tinput", let)
            hbox:
                for let in input_check("<>,.?/\\|", False, input_properties):
                    textbutton let action InputLetter("tinput", let)

        # else:
            ## Optional! You can add a third tab with special characters,
            ## such as accents or other symbols. Just follow the format with
            ## the hboxes above.

        hbox:
            style_prefix 'ckeyboard2'
            button:
                action ToggleScreenVariable("holding_shift")
                ## This shows the L2 icon, which is used in this screen to
                ## toggle Shift. It uses pad_config.get_icons in case it is
                ## remapped.
                for icon in pad_config.get_icons("input_shift", "small"):
                    add icon
                text _("Shift")
            ## This button allows players to switch to the second tab,
            ## with symbol characters, if those characters are allowed.
            button:
                action ToggleScreenVariable("which_tab", 1, 0)
                sensitive has_symbols insensitive_child Null()
                for icon in pad_config.get_icons("input_page", "small"):
                    add icon
                if which_tab == 0:
                    text _("@#:{#keyboard_symbols}")
                ## If you have a third tab, use the action
                # action CycleScreenVariable("which_tab", [0, 1, 2])
                ## and add an elif which_tab == 1: here.
                else:
                    text _("abc{#keyboard_letters}")

            ## These buttons allow the player to move the caret left and right
            ## in the input field. They use L1 and R1.
            button:
                action QueueEvent('input_left')
                for icon in pad_config.get_icons("input_left", "small"):
                    add icon
                text "◀" prefer_emoji False font "DejaVuSans.ttf"
            button:
                action QueueEvent('input_right')
                for icon in pad_config.get_icons("input_right", "small"):
                    add icon
                text "▶" prefer_emoji False font "DejaVuSans.ttf"
            ## This button is a shortcut for adding a space to the input. It
            ## uses the Y button.
            button:
                xsize pad_config.KEYBOARD_BUTTON_WIDTH*3+pad_config.KEYBOARD_BUTTON_SPACING*2
                action InputLetter("tinput", " ")
                insensitive_child Null()
                sensitive '\u00A0' not in input_check(" ", False, input_properties, 1)
                for icon in pad_config.get_icons("input_space", "small"):
                    add icon
                text _("Space")
            ## This button is a shortcut to backspace the input. It uses the X
            ## button.
            button:
                action QueueEvent('input_backspace')
                xsize pad_config.KEYBOARD_BUTTON_WIDTH*2+pad_config.KEYBOARD_BUTTON_SPACING
                keysym pad_config.get_event("input_backspace")
                for icon in pad_config.get_icons("input_backspace", "small"):
                    add icon
                text _("Backspace")
            ## This button will close the input. It uses the R2 button.
            button:
                selected True action done_action
                keysym pad_config.get_event("input_enter")
                for icon in pad_config.get_icons("input_enter", "small"):
                    add icon
                text _("Done")

    ############################################################################
    ## For the controller; toggles shift.
    ############################################################################
    ## This version makes it so you can hit the button to toggle it on and off
    # key pad_config.get_event("input_shift", kind="press") action ToggleScreenVariable("holding_shift")
    # key pad_config.get_event("input_shift", kind="repeat_replace") action NullAction()
    ############################################################################
    ## This version makes it so you have to hold the button down to keep shift on
    key pad_config.get_event("input_shift", kind="press") action SetScreenVariable("holding_shift", True)
    key pad_config.get_event("input_shift", kind="release_replace") action SetScreenVariable("holding_shift", False)
    ############################################################################

    ## This makes pressing Y to input a space work.
    key pad_config.get_event("input_space") action InputLetter("tinput", " ")

    if has_symbols:
        ## If you have a third tab, you'll want to update this action to
        ## cycle to the right one with CycleScreenVariable("which_tab", [0, 1, 2])
        key pad_config.get_event("input_page") action ToggleScreenVariable("which_tab", 0, 1)

    ## Ensure that hitting Enter closes the input even if they switched over
    ## to mouse/keyboard input.
    key ["K_RETURN", "K_KP_ENTER"] action done_action

    use key_footer():
        if original_screen == "sync_prompt":
            ## Specific case where we want to show a cancel prompt
            icon_button kind icn.back:
                suffix "small" caption _("Cancel") action Return(False)
        icon_button kind icn.select suffix "small"

################################################################################
## STYLES
################################################################################
## The styles used by the onscreen keyboard. Feel free to adapt this any way
## you like so it matches your game theme!

## This style is used for the frame that holds the input
style ckeyboard_frame:
    background Transform("#FFF", ysize=5, yalign=1.0)
    xpadding 25 xminimum 300 bottom_margin 40
    align (0.5, 0.5)

## This style is used for the input text. It will be overwritten by any
## properties you provide to the screen.
style ckeyboard_input:
    color "#FFF"

style ckeyboard_vbox:
    spacing pad_config.KEYBOARD_BUTTON_SPACING
    xalign 0.5 ypos 0.92 yanchor 1.0
style ckeyboard_hbox:
    spacing pad_config.KEYBOARD_BUTTON_SPACING

## This style is used by the standard buttons/first 3-4 rows
style ckeyboard_button:
    background "#333"
    hover_background "#777"
    selected_background "#ff8335"
    selected_hover_background "#ca5f1c"
    xysize (pad_config.KEYBOARD_BUTTON_WIDTH, pad_config.KEYBOARD_BUTTON_HEIGHT)
style ckeyboard_button_text:
    color "#FFF"
    align (0.5, 0.5)
style ckeyboard_text:
    color "#FFF"
    align (0.5, 0.5)

style ckeyboard2_vbox is ckeyboard_vbox
style ckeyboard2_hbox is ckeyboard_hbox
## This styling is used for the bottom row, with the shift, space, and done keys
style ckeyboard2_button:
    is ckeyboard_button
    ysize int(pad_config.KEYBOARD_BUTTON_HEIGHT*1.4)
    background "#444"
    hover_background "#777"
    selected_background "#ff8335"
    selected_hover_background "#ca5f1c"
style ckeyboard2_button_text is ckeyboard_button_text
style ckeyboard2_text is ckeyboard_text

################################################################################
## NUMPAD SCREEN
################################################################################
## This is a variant on the keyboard screen which only has numbers.
## It works in much the same way as the QWERTY keyboard screen, so refer to the
## comments there for explanations.
screen onscreen_numpad(prompt=None, value=None, done_action=Return(), dim=True,
        **input_properties):

    modal True
    zorder 100

    default other_screen = input_properties.pop("other_screen", None)
    if other_screen:
        use expression other_screen pass (prompt=prompt, **input_properties)

    if dim:
        ## Feel free to change the background image. `modal True` should be
        ## retained to prevent clicking through to the screen underneath
        ## (if applicable).
        frame:
            background "#000b" modal True
            xysize (config.screen_width, config.screen_height)


    if value is not None:
        ## Make sure it's editable
        on 'show' action value.Enable()

    vbox:
        style_prefix 'ckeyboard'

        frame:
            has vbox
            if prompt is not None:
                text prompt
            controller_input id 'tinput' properties input_properties:
                if value is not None:
                    value value

        hbox:
            vbox:
                hbox:
                    for let in input_check("789", False, input_properties, 3):
                        textbutton let action InputLetter("tinput", let)
                hbox:
                    for let in input_check("456", False, input_properties, 3):
                        textbutton let action InputLetter("tinput", let):
                            if let == "5" and pad_config.is_using_controller():
                                default_focus True
                hbox:
                    for let in input_check("123", False, input_properties, 3):
                        textbutton let action InputLetter("tinput", let)
                hbox:
                    button:
                        action QueueEvent('input_left')
                        for icon in pad_config.get_icons("input_left", "small"):
                            add icon
                        text "◀" prefer_emoji False font "DejaVuSans.ttf"
                    textbutton "0" action InputLetter("tinput", "0")
                    button:
                        action QueueEvent('input_right')
                        for icon in pad_config.get_icons("input_right", "small"):
                            add icon
                        text "▶" prefer_emoji False font "DejaVuSans.ttf"

            null width pad_config.KEYBOARD_BUTTON_SPACING

            vbox:
                button:
                    action QueueEvent('input_backspace')
                    xsize pad_config.KEYBOARD_BUTTON_WIDTH*2+pad_config.KEYBOARD_BUTTON_SPACING
                    keysym pad_config.get_event("input_backspace")
                    for icon in pad_config.get_icons("input_backspace", "small"):
                        add icon
                    text _("Backspace")
                button:
                    selected True action done_action
                    xsize pad_config.KEYBOARD_BUTTON_WIDTH*2+pad_config.KEYBOARD_BUTTON_SPACING
                    keysym pad_config.get_event("input_enter")
                    for icon in pad_config.get_icons("input_enter", "small"):
                        add icon
                    text _("Done")

    key ["K_RETURN", "K_KP_ENTER"] action done_action
    use key_footer():
        icon_button kind icn.select suffix "small"

