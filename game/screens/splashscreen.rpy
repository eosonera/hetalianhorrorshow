## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown.
## https://www.renpy.org/doc/html/splashscreen_presplash.html
##
##

default persistent.seen_splash = False
image kitayume0 = "gui/splash/kitayume0.png"
image kitayume = "gui/splash/kitayume.png"
image cloud1 = "gui/splash/cloud1.png"
image cloud2 = "gui/splash/cloud2.png"
image cloud3 = "gui/splash/cloud3.png"
image cloud31 = "gui/splash/cloud3.png"
image cloud4 = "gui/splash/cloud4.png"
image cloud41 = "gui/splash/cloud4.png"
image cloud42 = "gui/splash/cloud4.png"
image cloud43 = "gui/splash/cloud4.png"
image cloud7 = "gui/splash/cloud7.png"
image cloud8 = "gui/splash/cloud8.png"

transform splash_sky:
    linear 4.0:
        xoffset -100

transform kita_t:
    xalign 0.5
    ycenter 334
    zoom 2.0
    linear 0.76:
        zoom 1.0

transform kita_0t:
    xcenter 465
    ycenter 251
    alpha 0.0
    linear 0.9:
        ycenter 284
        alpha 1.0

transform cloud_1t:
    xycenter(488,500)
    zoom 0.8
    linear 4.0:
        xycenter(488,480)
        zoom 1.3

transform cloud_2t:
    xycenter(650,545)
    zoom 0.8
    linear 4.0:
        xycenter(850,545)
        zoom 2.0

transform cloud_3t:
    xycenter(488,519)
    zoom 0.8
    alpha 1.0
    linear 3.25:
        xycenter(490,500)
        zoom 7.0
        alpha 0.0

transform cloud_3t1:
    xalign 0.45
    ycenter 456
    zoom 0.8
    alpha 1.0
    linear 4.0:
        xalign 0.45
        ycenter 490
        zoom 3.0
        alpha 0.0

transform cloud_4t:
    xcenter 239
    yalign 1.0
    zoom 0.9
    linear 4.0:
        xcenter 31
        yoffset -6
        zoom 1.0

transform cloud_4t1:
    xycenter(250,423)
    xzoom 0.22
    yzoom 0.31
    linear 4.0:
        xycenter(107,458)
        xzoom 0.4
        yzoom 0.4
        
transform cloud_4t2:
    xalign 0.2
    ycenter 456
    zoom 0.8
    alpha 1.0
    linear 4.0:
        xalign 0.2
        ycenter 519
        alpha 0.0
        zoom 3.0

transform cloud_4t3:
    xalign 0.25
    ycenter 456
    zoom 0.8
    alpha 1.0
    linear 4.0:
        xalign 0.28
        ycenter 519
        zoom 4.0
        alpha 0.0

transform cloud_7t:
    xycenter(490,519)
    zoom 0.8
    alpha 1.0
    linear 2.76:
        xycenter(490,285)
        zoom 5.0
        alpha 0.0

transform cloud_8t:
    xycenter(400,519)
    zoom 0.8
    alpha 1.0
    linear 1.48:
        xycenter(400,300)
        zoom 5.0
        alpha 0.0

transform splash_fadeout:
    alpha 0.0
    time 3.12
    linear 1 alpha 1.0

label splashscreen1:

    scene bg base_sky at splash_sky
    show cloud4 at cloud_4t
    show cloud41 at cloud_4t1
    show cloud42 at cloud_4t2
    show cloud2 at cloud_2t
    show cloud1 at cloud_1t
    show cloud7 at cloud_7t
    show cloud8 at cloud_8t
    show cloud43 at cloud_4t3
    show cloud31 at cloud_3t1
    show cloud3 at cloud_3t
    show birds
    show birds1
    show white screen at splash_fadeout
    show kitayume0 at kita_0t
    show kitayume at kita_t


    if not persistent.seen_splash:
        
        $ renpy.pause(4.2, hard=True)
 
        $ persistent.seen_splash = True
    
    else:
        if renpy.pause(4.2):
            jump skip_splash
 
    label skip_splash: 
        pass
    
    return


# Splashscreen bird animation
init python:
    bird_frames = []
    bird_frames.append(("gui/splash/birds/0.png", 0.3))
    for i in range(46):
        frame = "gui/splash/birds/birds_{:02}.png".format(i)
        bird_frames.append((frame, 0.065))

    bird_frames1 = []
    bird_frames1.append(("gui/splash/birds/0.png", 1.16))
    for i in range(46):
        frame = "gui/splash/birds/birds_{:02}.png".format(i)
        bird_frames1.append((frame, 0.065))

image birds = Animation(*sum(bird_frames, ()))
image birds1 = Animation(*sum(bird_frames1, ()))


screen staffroll():
    zorder 99
    add "gui/staffroll.png" at credit_scroll


transform credit_scroll:
    ypos 600
    linear 20.25 yoffset -3000
    easein 5 yoffset -3600