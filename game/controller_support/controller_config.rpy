
################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for several configuration values relating to the
## controller support pack.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## For examples and detailed information, check out the Tools section on my
## website: https://feniksdev.com/tool/configuration-variables/
## This is just the backend; you don't need to understand everything in
## this file.
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
## Code to archive these files for a distributed game. Do not remove.
init python:
    build.classify("**controller_config.rpy", None)
    build.classify("**controller_config.rpyc", "archive")
################################################################################
init -500 python in pad_config:
    _constant = True

    ############################################################################
    ## ICONS
    ############################################################################
    ## The folder where the icons can be found. Change this if needed.
    ICON_FOLDER = "controller_support/controller_ui/"
    ## The file extension
    ICON_EXTENSION = "svg"
    ## If you're using SVG, you can also set the DPI. If you are not, set
    ## this to None.
    ## The icons included with this pack use 150 so the icons are around 75px.
    DEFAULT_DPI = 150
    ## How big the icons are (max dimension) at the provided DPI
    DEFAULT_ICON_SIZE = 75
    ## In this icon set, the PS and Xbox buttons can be coloured in different
    ## ways. 1 is no colour, 2 is full colour, and 3 is text colour only.
    ## You can also set this to '' if you don't have numbering for colours
    ## in your icons.
    ICON_COLOR_TYPE = 2

    ## Colours used for the text version of Xbox and PlayStation buttons.
    ## Updating these colours does not change the colour of the svg files!
    ## You'll need to edit them directly for that. This just updates the
    ## text-only colours.
    XBOX_A_COLOR = "#BAE236"
    XBOX_B_COLOR = "#FC551D"
    XBOX_X_COLOR = "#23C3F6"
    XBOX_Y_COLOR = "#FEB21B"

    PS_X_COLOR = "#5FD3F8"
    PS_O_COLOR = "#FD6248"
    PS_SQUARE_COLOR = "#F450A5"
    PS_TRIANGLE_COLOR = "#36E2A7"

    ## These are lists to identify keywords in the controller name and match
    ## it to an icon set.
    XBOX_CONTROLLER_NAMES = ["xbox", "microsoft"]
    PLAYSTATION_CONTROLLER_NAMES = ["ps3", "dualshock", "ps4", "playstation",
        "ps5", "dualsense", "ps2", "ps1", "sony", "ds4", "ds5"]
    NINTENDO_CONTROLLER_NAMES = ["nintendo", "joycon", "pro controller",
        "switch", "gamecube", "wii"]
    STEAM_CONTROLLER_NAMES = ["steam", "valve"]

    ############################################################################
    ## INPUT
    ############################################################################
    ## The letters used on the on-screen keyboard. Put up for translation,
    ## in case you want a non-standard layout
    KEYBOARD_ROW1 = _("qwertyuiop")
    KEYBOARD_ROW2 = _("asdfghjkl'")
    KEYBOARD_ROW3 = _("zxcvbnm,.?")

    ## A dictionary of the characters to change a given special character to
    ## while shift is held down
    SHIFT_DICT = {
        "," : "-",
        "." : "_",
        "'" : '"',
        "?" : "/",
        ## Add more to suit any translation needs etc.
    }

    ## How wide the keyboard keys are
    KEYBOARD_BUTTON_WIDTH = 120
    ## How tall the keyboard keys are
    KEYBOARD_BUTTON_HEIGHT = 90
    ## How much space is between the keyboard keys
    KEYBOARD_BUTTON_SPACING = 5

    ############################################################################
    ## VIRTUAL CURSOR
    ############################################################################
    ## A dictionary of event : (displayable, xoffset, yoffset) pairs equivalent
    ## to https://www.renpy.org/doc/html/mouse.html#hardware-mouse-cursor
    ## You can turn on debug for a virtual_cursor container to see where
    ## that mouse cursor hotspot is to set the offsets.
    DEFAULT_VIRTUAL_CURSORS = { }

    ############################################################################
    ## FOCUS MANAGEMENT
    ############################################################################
    ## Screens that have their focus saved and restored when entering and
    ## leaving them.
    RESTORE_FOCUS_SCREENS = [ "main_menu", "game_menu", "controller_remap" ]

    ## Optional. A list of callbacks that will be run if the focus type
    ## changes between keyboard, controller, and mouse. It will be passed
    ## a string with the old focus type and the new one.
    INPUT_TYPE_CALLBACKS = [ refresh_controller_ui, refresh_redrawables ]
    INPUT_CHANGE_REDRAWABLES = [ ]

    ############################################################################
    ## CALLBACKS
    ############################################################################
    CONTROLLER_DISCONNECT_CALLBACKS = [ ]
    CONTROLLER_CONNECT_CALLBACKS = [ choose_icon_set ]

    ############################################################################
    ## CONTROLLER STICKS
    ############################################################################
    STICK_MAX = 32767
    STICK_MIN = -32768
    ## These can be changed; the numbers are what I feel like works
    MINIMUM_DEADZONE = 1024
    DEFAULT_DEADZONE = 4096
    MAXIMUM_DEADZONE = 16384

    MINIMUM_SENSITIVITY = 0.2
    DEFAULT_SENSITIVITY = 1.0
    MAXIMUM_SENSITIVITY = 3.0

    ############################################################################
    ## INTERNAL USE
    ############################################################################
    ## A dictionary of pad events to their associated icon image name.
    EVENT_TO_ICON = {
        ## SHOULDER BUTTONS
        ## LEFT SHOULDER
        "pad_leftshoulder_press" : "l1",
        "pad_leftshoulder_release" : "l1",
        "repeat_pad_leftshoulder_press" : "l1",

        ## RIGHT SHOULDER
        "pad_rightshoulder_press" : "r1",
        "pad_rightshoulder_release" : "r1",
        "repeat_pad_rightshoulder_press" : "r1",

        ## TRIGGERS
        ## LEFT TRIGGER
        "pad_lefttrigger_pos" : "l2",
        "pad_lefttrigger_zero" : "l2",
        "repeat_pad_lefttrigger_pos" : "l2",

        ## RIGHT TRIGGER
        "pad_righttrigger_pos" : "r2",
        "pad_righttrigger_zero" : "r2",
        "repeat_pad_righttrigger_pos" : "r2",

        ## BUTTONS
        ## A BUTTON
        "pad_a_press" : "a",
        "pad_a_release" : "a",
        "repeat_pad_a_press" : "a",

        ## B BUTTON
        "pad_b_press" : "b",
        "pad_b_release" : "b",
        "repeat_pad_b_press" : "b",

        ## X BUTTON
        "pad_x_press" : "x",
        "pad_x_release" : "x",
        "repeat_pad_x_press" : "x",

        ## Y BUTTON
        "pad_y_press" : "y",
        "pad_y_release" : "y",
        "repeat_pad_y_press" : "y",

        ## D-PAD
        ## LEFT
        "pad_dpleft_press" : "left",
        "pad_dpleft_release" : "left",
        "repeat_pad_dpleft_press" : "left",

        ## RIGHT
        "pad_dpright_press" : "right",
        "pad_dpright_release" : "right",
        "repeat_pad_dpright_press" : "right",

        ## UP
        "pad_dpup_press" : "up",
        "pad_dpup_release" : "up",
        "repeat_pad_dpup_press" : "up",

        ## DOWN
        "pad_dpdown_press" : "down",
        "pad_dpdown_release" : "down",
        "repeat_pad_dpdown_press" : "down",

        ## STICKS
        ## LEFT STICK
        "pad_leftstick_press" : "l3",
        "pad_leftstick_release" : "l3",
        "repeat_pad_leftstick_press" : "l3",

        "pad_leftx_pos" : "left_stick",
        "repeat_pad_leftx_pos" : "left_stick",
        "pad_leftx_neg" : "left_stick",
        "repeat_pad_leftx_neg" : "left_stick",
        "pad_lefty_pos" : "left_stick",
        "repeat_pad_lefty_pos" : "left_stick",
        "pad_lefty_neg" : "left_stick",
        "repeat_pad_lefty_neg" : "left_stick",

        ## RIGHT STICK
        "pad_rightstick_press" : "r3",
        "pad_rightstick_release" : "r3",
        "repeat_pad_rightstick_press" : "r3",

        "pad_rightx_pos" : "right_stick",
        "repeat_pad_rightx_pos" : "right_stick",
        "pad_rightx_neg" : "right_stick",
        "repeat_pad_rightx_neg" : "right_stick",
        "pad_righty_pos" : "right_stick",
        "repeat_pad_righty_pos" : "right_stick",
        "pad_righty_neg" : "right_stick",
        "repeat_pad_righty_neg" : "right_stick",

        ## SELECT/BACK
        "pad_back_press" : "select",
        "pad_back_release" : "select",
        "repeat_pad_back_press" : "select",

        ## HOME
        "pad_guide_press" : "home",
        "pad_guide_release" : "home",
        "repeat_pad_guide_press" : "home",

        ## START
        "pad_start_press" : "start",
        "pad_start_release" : "start",
        "repeat_pad_start_press" : "start",
    }

    ICON_TO_ALT_TEXT = {
        "l3" : _("Press Left stick"),
        "r3" : _("Press Right stick"),
        "left" : _("Left"),
        "right" : _("Right"),
        "up" : _("Up"),
        "down" : _("Down"),
        "left_stick" : _("Left stick"),
        "right_stick" : _("Right stick"),

        ## These next ones go in the order xbox, playstation, nintendo,
        ## steam, generic
        "a" : [_("A Button"), _("Cross Button"), _("A Button"), _("A Button"),
            _("A Button")],
        "b" : [_("B Button"), _("Circle Button"), _("B Button"), _("B Button"),
            _("B Button")],
        "x" : [_("X Button"), _("Square Button"), _("X Button"), _("X Button"),
            _("X Button")],
        "y" : [_("Y Button"), _("Triangle Button"), _("Y Button"), _("Y Button"),
            _("Y Button")],
        "l1" : [_("Left Bumper"), _("L1 Button"), _("L Button"), _("L1 Button"),
            _("Left Shoulder")],
        "r1" : [_("Right Bumper"), _("R1 Button"), _("R Button"), _("R1 Button"),
            _("Right Shoulder")],
        "l2" : [_("Left Trigger"), _("L2 Button"), _("ZL Button"), _("L2 Trigger"),
            _("Left Trigger")],
        "r2" : [_("Right Trigger"), _("R2 Button"), _("ZR Button"), _("R2 Trigger"),
            _("Right Trigger")],
        "select" : [_("Back Button"), _("Share Button"), _("Minus Button"), _("View Button"),
            _("Select Button")],
        "start" : [_("Start Button"), _("Options Button"), _("Plus Button"), _("Menu Button"),
            _("Start Button")],
        "home" : [_("Home Button"), _("PS Button"), _("Home Button"), _("Steam Button"),
            _("Home Button")],
    }

    EVENT_LISTENER = EventListener(callbacks=INPUT_TYPE_CALLBACKS, on_changed=True)
    PRESS_ANYTHING = EventListener(callbacks=[wait_for_event], on_changed=False)

################################################################################
## PERSISTENT
################################################################################
default persistent.ALWAYS_SHOWN_FOCUS_DISPLAYABLE = None
## The point past which the stick is considered to start moving.
default persistent.left_stick_dead_zone = dict()
default persistent.right_stick_dead_zone = dict()
## Maximum amount the stick can move
default persistent.left_stick_max = dict()
default persistent.right_stick_max = dict()
## Inverted stick axes
default persistent.left_stick_invert_x = False
default persistent.left_stick_invert_y = False
default persistent.right_stick_invert_x = False
default persistent.right_stick_invert_y = False
## Sensitivity multiplier for stick speed
default persistent.left_stick_sensitivity = 1.0
default persistent.right_stick_sensitivity = 1.0

################################################################################
## INTERNAL USE
################################################################################
init 999 python in pad_config:
    EVENT_LISTENER = EventListener(callbacks=INPUT_TYPE_CALLBACKS, on_changed=True)
    ## Declare all the FocusManagers
    FOCUS_MANAGERS = [FocusManager(x) for x in RESTORE_FOCUS_SCREENS]

## An always-on overlay screen which helps manage focus and controller events.
screen event_listener():
    layer 'overlay'
    zorder 999
    ## This listens for all events, to know if the player is using a controller,
    ## mouse, or keyboard.
    add pad_config.EVENT_LISTENER
    ## These listen for focus changes and restore focus when the screen
    ## is re-shown.
    for manager in pad_config.FOCUS_MANAGERS:
        add manager
    ## Optionally add the always-shown focus displayable to help guide focus
    if persistent.ALWAYS_SHOWN_FOCUS_DISPLAYABLE:
        add persistent.ALWAYS_SHOWN_FOCUS_DISPLAYABLE

init python:
    ## Ensures we can always listen for controller events
    config.always_shown_screens.append("event_listener")
    _game_menu_screen = "game_menu"