## Menu open screen ################################################################

screen menu_open():
    tag menu
    use game_menu(_("Menu")):
        style_prefix "open"

#################################################################################
## Quick Menu screen ############################################################
#################################################################################

screen quick_menu():

    zorder 100

    if quick_menu:

        fixed:
            style_prefix "quick"

            imagebutton:
                    xpos 500
                    yalign 1.0
                    idle "gui/menu_quick/1_save_1.png"
                    hover "gui/menu_quick/1_save.png"
                    #insensitive "gui/menu_quick/1_save_2.png"
                    action ShowMenu('save')
            imagebutton:
                    xpos 580
                    yalign 1.0
                    idle "gui/menu_quick/2_load_1.png"
                    hover "gui/menu_quick/2_load.png"
                    #insensitive "gui/menu_quick/2_load_2.png"
                    action ShowMenu('load')
            imagebutton:
                    xpos 660
                    yalign 1.0
                    idle "gui/menu_quick/3_skip_1.png"
                    hover "gui/menu_quick/3_skip.png"
                    insensitive "gui/menu_quick/3_skip_2.png"
                    action Skip() alternate Skip(fast=True, confirm=False)
            imagebutton:
                    if renpy.variant("mobile"):
                        xpos 160
                    else:
                        xpos 738
                    yalign 1.0
                    idle "gui/menu_quick/5_hide_1.png"
                    hover "gui/menu_quick/5_hide.png"
                    #insensitive "gui/menu_quick/5_hide_2.png"
                    action HideInterface()

            if renpy.variant("mobile"):
                imagebutton:
                    xpos 738
                    yalign 1.0
                    idle "gui/menu_quick/4_menu_1.png"
                    hover "gui/menu_quick/4_menu.png"
                    action ShowMenu("menu_open")

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

#################################################################################
## Game Menu screen #############################################################
#################################################################################

screen game_menu(title):
    style_prefix "game_menu"

    add "gui/menu_game/bg_game_menu.png"
    add "gui/menu_game/menu_flower.png" at anim_game_menu
    add "gui/menu_game/doily.png" at anim_doily

    frame:

        imagebutton:
            xpos 100
            ypos 432
            idle "gui/menu_game/0save.png"
            at menu_hover_float
            action ShowMenu("save")

        imagebutton:
            xpos 220
            ypos 432
            idle "gui/menu_game/1load.png"
            at menu_hover_float
            action ShowMenu("load")

        imagebutton:
            xpos 340
            ypos 432
            idle "gui/menu_game/2backlog.png"
            at menu_hover_float
            action ShowMenu("history")

        imagebutton:
            xpos 460
            ypos 432
            idle "gui/menu_game/3auto.png"
            at menu_hover_float
            action [Preference("auto-forward", "enable"), Return()]
            
        imagebutton:
            xpos 700
            ypos 432
            idle "gui/menu_game/5mainmenu.png"
            at menu_hover_float
            action MainMenu(confirm=False, save=False)

        imagebutton:
            xalign 0.0
            yalign 1.0
            idle "gui/menu_game/6help.png"
            at menu_hover_float
            action ShowMenu("menu_open2")
            


        imagebutton:
            xpos 50
            ypos 160
            idle "gui/menu_game/menu_01.png"
            at menu_jump
            action ShowMenu("text_speed")

        imagebutton:
            xpos 50
            ypos 216
            idle "gui/menu_game/menu_02.png"
            at menu_jump
            action ShowMenu("autotext_speed")

        imagebutton:
            xpos 50
            ypos 272
            idle "gui/menu_game/menu_03.png"
            at menu_jump
            action ShowMenu("font") 

        imagebutton:
            xpos 50
            ypos 328
            idle "gui/menu_game/menu_04.png"
            at menu_jump
            action Show("volume")

        if renpy.variant("mobile"):
            imagebutton:
                xalign 1.0
                yalign 0
                idle "gui/menu_game/return.png"
                action Return()


style game_menu_vscrollbar:
    unscrollable "hide"



## Menu animations ###########################################################


transform anim_game_menu:
    yoffset 27
    linear .83:
        yoffset 0


transform anim_doily:
    xycenter(151,408)
    rotate -40
    linear .83:
        xycenter(151,408)
        rotate 0
    

transform menu_jump:
    on hover:
        linear .61 yoffset -6
        yoffset 0
        repeat
    on idle:
        yoffset 0

transform menu_hover_float:
    on hover:
        linear 0.7 yoffset -15
        linear 0.7 yoffset 0
        repeat
    on idle:
        yoffset 0










