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
image cloud4 = "gui/splash/cloud4.png"
image cloud7 = "gui/splash/cloud7.png"
image cloud8 = "gui/splash/cloud8.png"


label splashscreen:

    scene bg base_sky
    show kitayume0:
        xalign 0.5
        ypos 244
    show kitayume:
        xalign 0.5
        ypos 334
    show cloud1:
        xalign 0.5
        yalign 0.0
    show cloud2:
        xalign 0.5
        yalign 0.0
    show cloud3:
        xalign 0.5
        yalign 0.0
    show cloud4:
        xalign 0.5
        yalign 0.0
    show cloud7:
        xalign 0.5
        yalign 0.0
    show cloud8:
        xalign 0.5
        yalign 0.0

    show birds

    show text "{color=#000}{size=+10}eos hetascans\n[config.name!t] remake\nversion [config.version!t]{/color}{/size}":
        xalign 0.5
        yalign 0.3

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
    for i in range(46):  # from 0 to 45
        frame = "gui/splash/birds/birds_{:02}.png".format(i)
        bird_frames.append((frame, 0.08))

image birds = Animation(*sum(bird_frames, ()))
