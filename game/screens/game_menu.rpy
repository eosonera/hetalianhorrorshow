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
            xpos 50
            ypos 160
            idle "gui/menu_game/menu_01.png"
            at menu_jump
            action ShowMenu("text_speed_popup")

        imagebutton:
            xpos 50
            ypos 216
            idle "gui/menu_game/menu_02.png"
            at menu_jump
            action ShowMenu("autotext_speed_popup")

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
            action Show("volume_popup")

        if renpy.variant("mobile"):
            imagebutton:
                xalign 1.0
                yalign 0
                idle "gui/menu_game/return.png"
                action Return()


style game_menu_vscrollbar:
    unscrollable "hide"




## Menu 2 ###################


screen game_menu2(title):
    style_prefix "game_menu2"

    add "gui/menu_game/bg_game_menu2.png"
    add "gui/menu_game/menu_flower.png"

    frame:

        imagebutton:
            xpos 50
            ypos 160
            idle "gui/menu_game/menu_05.png"
            at menu_jump
            action ShowMenu("about")

        imagebutton:
            xpos 50
            ypos 216
            idle "gui/menu_game/menu_06.png"
            at menu_jump
            action ShowMenu("language")

        imagebutton:
            xpos 50
            ypos 272
            idle "gui/menu_game/menu_07.png"
            at menu_jump
            action Show("preferences")


        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            imagebutton:
                xpos 50
                ypos 328
                idle "gui/menu_game/menu_08.png"
                at menu_jump
                action ShowMenu("help")

        imagebutton:
            xpos 700
            ypos 432
            idle "gui/menu_game/5mainmenu.png"
            at menu_hover_float
            action Return()
        
        text _("Made with {a=https://ja.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"):
            xalign 0.0
            yalign 1.0
            xsize 350
            

style game_menu2_text:
    size 12
    color "#fff"
    outlines [(1.2, "#597a87", 0, 0)]


style game_menu2_vscrollbar:
    unscrollable "hide"










