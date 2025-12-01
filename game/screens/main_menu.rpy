
## Main Menu screen ############################################################
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


init python:
    list_ch = []
    for i in range(1,8):
        ch = f"story{i}"
        list_ch.append(ch)


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "white screen"
    add "gui/menu_main/P1030291.png" at mm_fade_in_bg
    add "images/vfx/dust.png" at mm_dust
    add "images/vfx/dust.png" at mm_dust1
    add "gui/menu_main/imagebutton_bg.png" at mm_imagebutton_bg
    add "images/vfx/sunlight2.png" at sunlight2_mm
    add "images/vfx/sunlight2.png" at sunlight2_1_mm
    add "images/vfx/blue.png" at mm_blue
    add "images/vfx/orange.png" at mm_orange
    
    add "gui/menu_main/title.png" at mm_title

    vbox:
        style_prefix "mm"
        yalign 1.0
        text "hetascanlations\n[config.name!t] remake\nversion [config.version]"

    vbox:
        xalign 1.0
        yalign 0.0
        label("Debug menu")
        textbutton("Jump to Meeting"):
            action Start("meeting")
        for ch in list_ch:
            textbutton ("Jump to [ch]"):
                action Start(ch)
        textbutton("Splashscreen"):
            action Start("splashscreen")


    fixed:
        imagebutton:
            xpos 102
            ypos 456
            activate_sound "sfx/bell01.ogg"
            idle "gui/menu_main/title_03.png"
            hover "gui/menu_main/title2_03.png"
            action Start("start")
            at mm_fade_in

        imagebutton:
            xpos 266
            ypos 456
            activate_sound "sfx/bell01.ogg"
            idle "gui/menu_main/title_04.png"
            hover "gui/menu_main/title2_04.png"
            action ShowMenu("load")
            at mm_fade_in

        imagebutton:
            xpos 441
            ypos 456
            activate_sound "sfx/bell01.ogg"
            idle "gui/menu_main/title_05.png"
            hover "gui/menu_main/title2_05.png"
            action Start("gallery")
            at mm_fade_in

        imagebutton:
            xpos 617
            ypos 456
            idle "gui/menu_main/title_06.png"
            hover "gui/menu_main/title2_06.png"
            
            if renpy.variant("pc"):
                activate_sound "sfx/bell01.ogg"
                action Quit(confirm=not main_menu)
            else:
                activate_sound "sfx/bell01.ogg"
            at mm_fade_in

        imagebutton:
            xalign 1.0
            yalign 1.0
            activate_sound "sfx/bell01.ogg"
            idle "gui/menu_main/title_07.png"
            hover "gui/menu_main/title2_07.png"
            action ShowMenu("menu_open2")
            at mm_fade_in

style mm_text is gui_text
style mm_text:
    size 9

#################################################################################
## Main menu animations ###########################################################
#################################################################################

transform mm_title:
    zoom 2.0 rotate -190 xycenter(454,294)

    linear .6 zoom 1.0 rotate 0 xycenter(450,300)
    linear .2 rotate 10 

    block:
        parallel:
            linear .2 rotate -10
        parallel:
            linear .2 zoom 1.1
        
    block:
        parallel:
            linear .2 rotate 7
        parallel:
            linear .2 zoom 1.0

    linear .2 rotate -7
    linear .2 rotate 0
    
    time 1.75
    block:
        linear .9 yoffset -5
        linear .9 yoffset 0
        repeat

# transform title_float:
#     linear xpos 266 ypos 456
    
#     repeat

transform mm_fade_in:
    alpha 0.0
    linear 1.25 alpha 1.0

transform mm_fade_in_bg:
    alpha 0.0 yoffset -120
    linear 1.6 alpha 1.0 yoffset 0

transform mm_imagebutton_bg:
    alpha 0.0
    linear 1.25 alpha 0.78



transform mm_dust:
    pos(0, 200) alpha 0.3 additive_blend
    linear 1.6 xoffset 200 alpha 0.0

transform mm_dust1:
    pos(0, 200) alpha 0.3 additive_blend
    linear 1.6 xoffset 300 yoffset -100 alpha 0.0

transform mm_blue:
    align(0.5,0.5) alpha 0.0 additive_blend
    block:
        time 1.85
        linear 4.4 align(0.5,0.5) alpha 0.2 xzoom 1.3 yzoom 1.2 additive_blend
        linear 4.5 align(0.5,0.5) alpha 0.0 xzoom 1.0 yzoom 1.0
        time 12.55
        repeat

transform mm_orange:
    align(0.5,0.5) alpha 0.0 additive_blend
    block:
        time 13.35
        linear 4.4 align(0.5,0.5) alpha 0.2 xzoom 1.3 yzoom 1.2 additive_blend
        linear 4.5 align(0.5,0.5) alpha 0.0 xzoom 1.0 yzoom 1.0
        time 1.25
        repeat

transform sunlight2_mm:
    parallel:
        alpha 0.0 rotate 1 additive_blend
        block:
            time 1.88
            linear 6.72 alpha 0.2 rotate -35 additive_blend
            linear 5.83 alpha 0.0 rotate -58
            linear 8.87 alpha 0.0 rotate 1
            repeat
    parallel:
        xycenter(46,2) xzoom 0.15 yzoom 0.24
        block:
            time 1.88
            linear 6.72 xycenter(47,1) xzoom 1.0 yzoom 1.0
            linear 5.83 xycenter(48,3) xzoom 1.0 yzoom 1.0
            linear 8.87 xycenter(46,2) xzoom 0.15 yzoom 0.24
            repeat
        
transform sunlight2_1_mm:
    parallel:
        alpha 0.0 rotate 1 additive_blend
        block:
            time 8.92
            linear 6.71 alpha 0.2 rotate -35 additive_blend
            linear 5.87 alpha 0.0 rotate -28
            linear 1.8 alpha 0.0 rotate 1
            repeat
    parallel:
        xycenter(62,-7) xzoom 0.15 yzoom 0.24
        block:
            time 8.92
            linear 6.71 xycenter(78,-3) xzoom 0.80 yzoom 0.60
            linear 5.87 xycenter(83,-5) xzoom 1.0 yzoom 1.0
            linear 1.8 xycenter(62,-7) xzoom 0.15 yzoom 0.24
            repeat



#################################################################################