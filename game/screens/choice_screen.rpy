
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
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
    
## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
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