## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.


screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):
    style_prefix "game_menu"

    add gui.game_menu_background
    add "gui/menu.png"

    if renpy.variant("mobile"):
        textbutton _("Return"):
            style "return_button"
            action Return()

    frame:

        fixed:

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
                action Preference("auto-forward", "toggle")

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
                action ShowMenu("about") 

            imagebutton:
                xpos 50
                ypos 328
                idle "gui/button/menu_04.png"
                at menu_jump
                action Show("volume_popup")

        frame:
            xpos 300
            ypos 50
            left_margin 29
            right_margin 15
            top_margin 800

            if scroll == "viewport":
                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    vbox:
                        spacing spacing
                        transclude

            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    spacing spacing

                    transclude

            else:
                transclude

style game_menu_outer_frame:
    bottom_padding 22
    top_padding 85

style game_menu_navigation_frame:
    xsize 197
    yfill True

style game_menu_content_frame:
    left_margin 29
    right_margin 15
    top_margin 8

style game_menu_viewport:
    xsize 400
    ysize 400
    xalign 0.6
    yalign 0.3

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 8


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        fixed:
            style_prefix "quick"

            imagebutton:
                    xpos 500
                    yalign 1.0
                    idle "gui/button/qm_button_1_01.png"
                    hover "gui/button/qm_button_01.png"
                    action ShowMenu('save')
            imagebutton:
                    xpos 580
                    yalign 1.0
                    idle "gui/button/qm_button_1_02.png"
                    hover "gui/button/qm_button_02.png"
                    action ShowMenu('load')
            imagebutton:
                    xpos 660
                    yalign 1.0
                    idle "gui/button/qm_button_1_03.png"
                    hover "gui/button/qm_button_03.png"
                    action Skip() alternate Skip(fast=True, confirm=False)
            imagebutton:
                    xpos 740
                    yalign 1.0
                    idle "gui/button/qm_button_1_05.png"
                    hover "gui/button/qm_button_05.png"
                    action HideInterface()

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True