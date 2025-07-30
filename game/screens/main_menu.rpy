
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background
    add "gui/P1030291.png" at fade_in_title
    add "gui/title_e.png" at title_main_menu
    add "gui/lower_part.png" at fade_in_title

    fixed:
        imagebutton:
            xpos 102
            ypos 456
            activate_sound "sfx/bell01.ogg"
            idle "gui/button/title_03.png"
            hover "gui/button/title2_03.png"
            action Start("start")
            at fade_in_title

        imagebutton:
            xpos 266
            ypos 456
            activate_sound "sfx/bell01.ogg"
            idle "gui/button/title_04.png"
            hover "gui/button/title2_04.png"
            action ShowMenu("load")
            at fade_in_title

        imagebutton:
            xpos 441
            ypos 456
            activate_sound "sfx/bell01.ogg"
            idle "gui/button/title_05.png"
            hover "gui/button/title2_05.png"
            action Start("gallery")
            at fade_in_title

        imagebutton:
            xpos 617
            ypos 456
            idle "gui/button/title_06.png"
            hover "gui/button/title2_06.png"
            
            if renpy.variant("pc"):
                activate_sound "sfx/bell01.ogg"
                action Quit(confirm=not main_menu)
            else:
                activate_sound "sfx/bell01.ogg"
            at fade_in_title

