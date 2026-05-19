################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for callbacks when the controller is connected
## or disconnected. See the tools section on my website for more details:
## https://feniksdev.com/tool/configuration-variables/#Callbacks
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################

init python:

    def pause_on_controller_disconnect(index):
        """
        Pauses the game when a controller is disconnected by showing a menu.
        """
        global pad_connection_action
        if _menu:
            pad_connection_action = Hide("controller_disconnected_prompt")
        else:
            pad_connection_action = Return()

        renpy.show_screen("controller_disconnected_prompt")

    def reconnect_controller(index):
        global pad_connection_action
        if renpy.get_screen("controller_disconnected_prompt"):
            renpy.show_screen("controller_reconnected_prompt")


screen controller_disconnected_prompt():
    zorder 300
    tag controller_connection
    modal True

    add "#0008"

    frame:
        style_prefix 'confirm'
        has vbox
        label _("The controller was disconnected.") style "confirm_prompt"
        textbutton _("OK") action Hide("controller_disconnected_prompt")

    key pad_config.get_event("button_select") action Hide("controller_disconnected_prompt")

screen controller_reconnected_prompt():
    zorder 300
    tag controller_connection
    modal True

    add "#0008"

    frame:
        style_prefix 'confirm'
        has vbox
        label _("Controller reconnected.") style "confirm_prompt"

    timer 1.0 action Hide("controller_reconnected_prompt")
    key pad_config.get_event("button_select") action Hide("controller_reconnected_prompt")

## Add the function to the list of callbacks
define pad_config.CONTROLLER_DISCONNECT_CALLBACKS += [ pause_on_controller_disconnect ]
define pad_config.CONTROLLER_CONNECT_CALLBACKS += [ reconnect_controller ]