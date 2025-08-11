
## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action=None):

    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/menu_game/confirm.png":
        xpos 206
        ypos 192

    frame:
        xpos 305
        ypos 260
        label _(message) style "confirm_prompt"
            
        null height 10

    hbox:
        xpos 306
        ypos 290   
        spacing 11
        
        textbutton _("OK") action yes_action
        if no_action is not None:
            textbutton _("キャンセル") action no_action
                    

    ## Right-click and escape answer "no".
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



## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
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



