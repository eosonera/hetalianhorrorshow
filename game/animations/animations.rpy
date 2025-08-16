
## Animated images ######################################################################

init python:
    ctc_frames = []
    for i in range(4):
        frame = f"gui/ctc/ctc_{i}.png"
        ctc_frames.append((frame, 0.2))

image ctc_button = Animation(*sum(ctc_frames, ()))

image thumb_hover_anim:
    "gui/slider/thumb_0.png"
    pause 1
    "gui/slider/thumb_2.png"
    pause 1
    "gui/slider/thumb_1.png"

image slider_hover_anim:
    "gui/slider/slider_0.png"
    pause 1
    "gui/slider/slider_2.png"
    pause 1
    "gui/slider/slider_1.png"

transform check_hover:
    on idle:
        "gui/button/check_0.png"
    on hover:
        "gui/button/check_1.png"

image nvl_textbox = At("images/textbox/nvl.png",nvl_alpha)
transform nvl_alpha:
    alpha 0.85

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define pause_dissolve = MultipleTransition([
    False, Pause(1.5),
    False, Dissolve(0.25),
    True])

## Cutscenes ######################################################################

## Meeting #######################################################

## England blackboard 

transform blackboard:
    linear 12.86 xoffset -400 yoffset -70

transform blue_upper_half_transform:
    alpha 1.0 additive_blend
    linear 3.25 alpha 0.0

transform eng_blackboard:
    "england large fufufu-n"
    alpha 0.0 zoom 0.9 xcenter 888 ycenter 585
    time 9.48
    linear 2.0 alpha 1.0 zoom 1.0 xoffset -280
    "england large eh2"
    linear 0.13 yoffset -28
    linear 0.2 yoffset 0
    linear 1.35
    "england large blush shout2"
    linear 0.24 yoffset -28
    linear 0.28 yoffset -3

transform upplerleft_yellow_transform:
    alpha 0.0 xzoom 1.3 yzoom 1.2 additive_blend
    time 7.0
    linear 3.36 alpha 0.35
    linear 3.67 alpha 0.0 xzoom 1.0 yzoom 1.0

#19.32

transform lightblue_transform:
    alpha 0.0 additive_blend
    time 10.3
    linear 2.55 alpha 0.35 xzoom 1.3 yzoom 1.2
    linear 2.21 alpha 0.0 xzoom 1.0 yzoom 1.0










## Celebs
transform aphro_intro:
    alpha 0 xoffset -20 
    linear 1.16 alpha 1.0 xoffset 0

transform jeremy_intro:
    alpha 0.0 xoffset 377 yoffset 6
    time .75 
    linear 1.16 alpha 1.0 xoffset 355 

transform bear_intro:
    alpha 0.0 xoffset 616 yoffset -16
    time 1.875 
    linear 1.16 alpha 1.0 xoffset 599 

transform aphro1:
    alpha 0 pos(0,-30)
    linear 0.5 alpha 1.0

transform jeremy1:
    alpha 0.0 pos(240,-40)
    time 0.5
    linear 0.5 alpha 1.0

transform bear1:
    alpha 0 pos(560,-40)
    time 1
    linear 0.5 alpha 1.0

define celebdissolve = MultipleTransition([
    False, Pause(3.0),
    False, Dissolve(1.0),
    True])


## Chapter 1 ############################################
## Sweden





image swe1_0 = "images/bg/story1/swe1.png"
transform swe1_transform:
    zoom 1.3 xycenter(450,180)
    linear 4.25:
        zoom 1.0 xycenter(450,300)
    linear 18.05:
        yalign 1.0

image swe2_0 = "images/bg/story1/swe2.png"
transform swe2_transform:
    zoom 1.3 xcenter 450 yalign 1.0
    linear 4.25:
        zoom 1.0 xcenter 450
    time 18.05
        

image swe3_0 = "images/bg/story1/swe3.png"
transform swe3_transform:
    zoom 1.3 alpha 0 xcenter 450 yalign 1.0
    linear 4.25:
        zoom 1.0 alpha 0.5 xcenter 450
    linear 4.25:
        alpha 0.1
    linear 5.25:
        alpha 0.8
    linear 5:
        alpha 0.03
    linear 3.55:
        alpha 1.0

## Chapter 2 ############################################
## Glass smash



transform jpn_glass:
    xpos 200 yalign 0 alpha 0.0
    time 1.0
    linear 0.2 alpha 1.0

transform fin_glass:
    xpos 320 ypos 30 alpha 0.0
    time 2.0
    linear 0.2 alpha 1.0

transform eng_glass:
    xpos 450 yalign 0 alpha 0.0
    time 3.0
    linear 0.2 alpha 1.0

transform ger_glass:
    xpos 630 yalign 0 alpha 0.0
    time 4.0
    linear 0.2 alpha 1.0



init python:
    glass_frames = []
    for i in range(90):
        frame = "images/vfx/glass_smash/glass{:03}.png".format(i)
        glass_frames.append((frame, 0.065, None))

image glass_smash = NonLoopAnimation(*sum(glass_frames, ()))




## Alien
transform tech3_pos:
    alpha 0.0
    pause 0.3 alpha 1.0
    align(0.5, 1.0) zoom 2.0
    linear 9.45 align(1.0, 0) zoom 1.0

transform mata_pos:
    alpha 0.0
    pause 0.3 alpha 1.0
    xycenter(660, 165) zoom 3.0
    linear 9.45 xycenter(620, 195) zoom 2.0

transform tony_pos:
    xpos 400 ypos 280
    pause 0.3

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')


## UFO

transform ufo1_pos:
    xpos 0 ypos -200
    linear 19.8 xpos -100 ypos 0

transform ufo2_pos:
    xycenter(100,306) rotate -12 xzoom 0.8 yzoom 0.87
    linear 19.8 xoffset 424 yoffset -24 rotate 18 xzoom 1.0 yzoom 1.0

transform ufo3_pos:
    xycenter(530,298) alpha 0.4 additive_blend
    linear 19.8 xpos -20 ypos 90 alpha 0.2

transform ufo4_pos:
    xpos 0 ypos -100
    linear 19.8 xpos -150 ypos 0





## Chapter 3 ############################################


init python:
    rain_frames = []
    for i in range(418):
        frame = "images/vfx/window_rain/glass{:03}.png".format(i)
        rain_frames.append((frame, 0.065))

image window_rain = Animation(*sum(rain_frames, ()))