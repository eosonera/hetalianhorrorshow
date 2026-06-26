## Menu open screen ################################################################

screen menu_open():
    tag menu
    use game_menu(("Menu")):
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
                        xpos 84
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

default gamemenu_open = False

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
            if not renpy.variant("mobile"):
                at menu_hover_float
            action switch_tab("save"), SetVariable("gamemenu_open", True)

        imagebutton:
            xpos 220
            ypos 432
            idle "gui/menu_game/1load.png"
            if not renpy.variant("mobile"):
                at menu_hover_float
            action switch_tab("load"), SetVariable("gamemenu_open", True)

        imagebutton:
            xpos 340
            ypos 432
            idle "gui/menu_game/2backlog.png"
            if not renpy.variant("mobile"):
                at menu_hover_float
            action switch_tab("history")

        imagebutton:
            xpos 460
            ypos 432
            idle "gui/menu_game/3auto.png"
            if not renpy.variant("mobile"):
                at menu_hover_float
            action [Preference("auto-forward", "enable"), Return()]
            
        imagebutton:
            xpos 700
            ypos 432
            idle "gui/menu_game/5mainmenu.png"
            action MainMenu(confirm=True, save=False)
            if not renpy.variant("mobile"):
                at menu_hover_float
            

        imagebutton:
            xalign 0.0
            yalign 1.0
            idle "gui/menu_game/6help.png"
            if not renpy.variant("mobile"):
                at menu_hover_float
            action [
                Hide(current_tab_screen) if current_tab_screen else NullAction(),
                SetVariable("current_tab_screen", None),
                ShowMenu("menu_open2")
            ]
            


        imagebutton:
            xpos 50
            ypos 160
            idle "gui/menu_game/menu_01.png"
            if not renpy.variant("mobile"):
                at menu_jump
            action switch_tab("text_speed")

        imagebutton:
            xpos 50
            ypos 216
            idle "gui/menu_game/menu_02.png"
            if not renpy.variant("mobile"):
                at menu_jump
            action switch_tab("autotext_speed")

        imagebutton:
            xpos 50
            ypos 272
            idle "gui/menu_game/menu_03.png"
            if not renpy.variant("mobile"):
                at menu_jump
            action switch_tab("font") 

        imagebutton:
            xpos 50
            ypos 328
            idle "gui/menu_game/menu_04.png"
            if not renpy.variant("mobile"):
                at menu_jump
            action switch_tab("volume")

        if renpy.variant("mobile"):
            imagebutton:
                xalign 1.0
                yalign 0
                idle "gui/button/return.png"
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


default current_tab_screen = None
init python:
    def switch_tab(screen_name):
        actions = []

        if current_tab_screen is not None:
            if renpy.get_screen(current_tab_screen):
                actions.append(Hide(current_tab_screen))

        if screen_name is not None:
            actions.append(Show(screen_name))
            actions.append(SetVariable("current_tab_screen", screen_name))
        else:
            actions.append(SetVariable("current_tab_screen", None))

        return actions









