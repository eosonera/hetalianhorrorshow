## Menu open screen ################################################################

screen menu_open():
    tag menu
    use game_menu(_("Menu")):
        style_prefix "open"

screen menu_open2():
    tag menu
    use game_menu2(_("Menu")):
        style_prefix "open"


## Quick Menu screen ###########################################################

screen quick_menu():

    zorder 100

    if quick_menu:

        fixed:
            style_prefix "quick"

            imagebutton:
                    xpos 500
                    yalign 1.0
                    idle "gui/button/qm_button_01_1.png"
                    hover "gui/button/qm_button_01.png"
                    #insensitive "gui/button/qm_button_01_2.png"
                    action ShowMenu('save')
            imagebutton:
                    xpos 580
                    yalign 1.0
                    idle "gui/button/qm_button_02_1.png"
                    hover "gui/button/qm_button_02.png"
                    #insensitive "gui/button/qm_button_02_2.png"
                    action ShowMenu('load')
            imagebutton:
                    xpos 660
                    yalign 1.0
                    idle "gui/button/qm_button_03_1.png"
                    hover "gui/button/qm_button_03.png"
                    insensitive "gui/button/qm_button_03_2.png"
                    action Skip() alternate Skip(fast=True, confirm=False)
            imagebutton:
                    xpos 740
                    yalign 1.0
                    idle "gui/button/qm_button_05_1.png"
                    hover "gui/button/qm_button_05.png"
                    #insensitive "gui/button/qm_button_05_2.png"
                    action HideInterface()

            if renpy.variant("mobile"):
                imagebutton:
                    xpos 820
                    yalign 1.0
                    idle "gui/button/qm_button_04_1.png"
                    action ShowMenu("menu_open")

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.


screen game_menu(title):
    style_prefix "game_menu"

    add gui.game_menu_background
    add "gui/bg menu.png"

    frame:

        imagebutton:
            xpos 100
            ypos 432
            idle "gui/button/0save.png"
            at menu_hover_float
            action ShowMenu("save")

        imagebutton:
            xpos 220
            ypos 432
            idle "gui/button/1load.png"
            at menu_hover_float
            action ShowMenu("load")

        imagebutton:
            xpos 340
            ypos 432
            idle "gui/button/2backlog.png"
            at menu_hover_float
            action ShowMenu("history")

        imagebutton:
            xpos 460
            ypos 432
            idle "gui/button/3auto.png"
            at menu_hover_float
            action [Preference("auto-forward", "enable"), Return()]
            
        imagebutton:
            xpos 700
            ypos 432
            idle "gui/button/5mainmenu.png"
            at menu_hover_float
            action MainMenu(confirm=False, save=False)

        imagebutton:
            xpos 50
            ypos 160
            idle "gui/button/menu_01.png"
            at menu_jump
            action ShowMenu("text_speed_popup")

        imagebutton:
            xpos 50
            ypos 216
            idle "gui/button/menu_02.png"
            at menu_jump
            action ShowMenu("autotext_speed_popup")

        imagebutton:
            xpos 50
            ypos 272
            idle "gui/button/menu_03.png"
            at menu_jump
            action ShowMenu("font") 

        imagebutton:
            xpos 50
            ypos 328
            idle "gui/button/menu_04.png"
            at menu_jump
            action Show("volume_popup")

        if renpy.variant("mobile"):
            imagebutton:
                xalign 1.0
                yalign 0
                idle "gui/button/return.png"
                action Return()


style game_menu_vscrollbar:
    unscrollable gui.unscrollable




## Menu 2 ###################


screen game_menu2(title):
    style_prefix "game_menu2"

    add "gui/game_menu2.png"
    add "gui/bg menu.png"

    frame:

        imagebutton:
            xpos 50
            ypos 160
            idle "gui/button/menu_05.png"
            at menu_jump
            action ShowMenu("about")

        imagebutton:
            xpos 50
            ypos 216
            idle "gui/button/menu_06.png"
            at menu_jump
            action ShowMenu("language")

        imagebutton:
            xpos 50
            ypos 272
            idle "gui/button/menu_07.png"
            at menu_jump
            action Show("preferences")


        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            imagebutton:
                xpos 50
                ypos 328
                idle "gui/button/menu_08.png"
                at menu_jump
                action ShowMenu("help")

        imagebutton:
            xpos 700
            ypos 432
            idle "gui/button/5mainmenu.png"
            at menu_hover_float
            action Return()
        




style game_menu2_vscrollbar:
    unscrollable gui.unscrollable










