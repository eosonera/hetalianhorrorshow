
################################################################################
## Confirm screen ##############################################################
################################################################################
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action=None):

    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/menu_game/confirm.png":
        xpos 206
        ypos 192

    vbox:
        xpos 305
        ypos 260
        spacing 10
        frame:
            
            label _(message) style "confirm_prompt"

        hbox:
            spacing 11
            
            textbutton _("OK") action yes_action
            if no_action is not None:
                textbutton _("キャンセル") action no_action
                    
    if no_action is not None:
        key "game_menu" action no_action
    else:
        key "game_menu" action yes_action


style confirm_prompt_text:
    color "#000"
    size 13
    layout "subtitle"

style confirm_button:
    background "gui/button/confirm_button_0.png"
    hover_background "gui/button/confirm_button_1.png"
    xsize 138
    ysize 49


style confirm_button_text:
    xalign 0.5
    color "#000"


#################################################################################
## Notify screen ###############################################################
#################################################################################
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    add "gui/menu_game/confirm.png":
        xpos 206
        ypos 192

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame:
    xpos 305
    ypos 260
    xsize 366
    ysize 90


style notify_text:
    size 14


#################################################################################
## Skip indicator screen #######################################################
#################################################################################
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text ("")


init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)


#################################################################################
## Choice screen ###############################################################
#################################################################################
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    add "gui/menu_game/choice.png":
        xpos 216
        ypos 156

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox:
    xpos 286
    ypos 260
    spacing 0
    

style choice_button:
    is default
    xysize (326, 40)
    hover_background Solid("#fff")

style choice_button_text:
    is default
    xalign 0.5
    yalign 0.5
    size 20
    color "#74BEC4"
    hover_color "#1D8EA4"


#################################################################################
## Input screen ################################################################
#################################################################################
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xanchor 0.0 ypos 20 spacing 10
            text prompt style "input_prompt"
            input id "input"

style input_prompt:
    xalign 0.0



style input:
    xalign 0.0
    xmaximum 1116
    color "#000"