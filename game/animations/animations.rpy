
## Animated images ######################################################################

init python:
    ctc_frames = []
    for i in range(4):
        frame = f"gui/ctc/ctc_{i}.png"
        ctc_frames.append((frame, 0.2))

image ctc_button = Animation(*sum(ctc_frames, ()))

transform roll_arrow:
    yalign 0.5
    block:
        linear 0.3 yzoom 0.0 yoffset 32
        linear 0.3 yzoom 1.0 yoffset 0
        repeat

image ctc_arrow = At("gui/arrow0.png", roll_arrow)


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

transform tr_eng_blue:
    alpha 1.0 additive_blend
    linear 3.25 alpha 0.0

transform eng_blackboard:
    "england large heheheh"
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

transform tr_eng_yellow:
    alpha 0.0 xzoom 1.3 yzoom 1.2 additive_blend
    time 7.0
    linear 3.36 alpha 0.35
    linear 3.67 alpha 0.0 xzoom 1.0 yzoom 1.0


transform tr_eng_lightblue:
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


image wrapmist = WrapTiled("images/vfx/mist.png", speed_x=30, speed_y=20)
image wrapmist1 = WrapTiled("images/vfx/mist.png", speed_x=20, speed_y=50, init_x=0.0, init_y=200.0)


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

transform bul_glass:
    xpos 0 yalign 0 alpha 0.0
    time 0.5
    linear 0.2 alpha 1.0
    linear 0.05 xoffset -8 yoffset +8
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -4 yoffset -4
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +2 yoffset -2
    linear 0.05 xoffset 0 yoffset 0

transform jpn_glass:
    xpos 200 yalign 0 alpha 0.0
    time 1.5
    linear 0.2 alpha 1.0
    linear 0.05 xoffset -8 yoffset -8
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +4 yoffset +4
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset 0 yoffset 0

transform fin_glass:
    xpos 320 ypos 30 alpha 0.0
    time 2.5
    linear 0.2 alpha 1.0
    linear 0.05 xoffset +8 yoffset -8
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +4 yoffset -4
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset 0 yoffset 0

transform eng_glass:
    xpos 450 yalign 0 alpha 0.0
    time 3.5
    linear 0.2 alpha 1.0
    linear 0.05 xoffset +8 yoffset -8
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -4 yoffset -4
    linear 0.05 xoffset 0 yoffset 0

transform ger_glass:
    xpos 630 yalign 0 alpha 0.0
    time 4.5
    linear 0.2 alpha 1.0
    linear 0.05 xoffset +8 yoffset -8
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +4 yoffset +4
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +2 yoffset -2
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -2 yoffset -2
    linear 0.05 xoffset 0 yoffset 0



init python:
    glass_frames = []
    for i in range(90):
        frame = "images/vfx/glass_smash/glass{:03}.png".format(i)
        glass_frames.append((frame, 0.065, None))

image glass_smash = NonLoopAnimation(*sum(glass_frames, ()))




## Alien


transform mata_pos:
    alpha 0.0
    pause 0.3 alpha 1.0
    xycenter(660, 165) zoom 3.0
    linear 9.45 xycenter(620, 195) zoom 2.0


define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')


## UFO

transform ufo1_pos:
    xpos 0 ypos -200
    linear 19.85 xpos -100 ypos 0

transform ufo2_pos:
    pos(-490, -100) rotate -12 xzoom 0.8 yzoom 0.87
    linear 19.85 pos(-200, -360) rotate 18 xzoom 1.0 yzoom 1.13

transform ufo3_pos:
    pos(-81,-58) alpha 0.35 additive_blend
    linear 4.85 pos(-100,-31) alpha 0.25 additive_blend

transform ufo4_pos:
    xpos 0 ypos -100
    linear 19.85 xpos -150 ypos 0


transform tr_snow_a:
    xpos 379 ypos 47 alpha 0.2 additive_blend
    parallel:
        linear 8 xpos 110 ypos 212 alpha 0.9 additive_blend
        linear 8 xpos 379 ypos 47 alpha 0.2 additive_blend
        repeat
    parallel:
        rotate 0
        linear 15 rotate 360
        repeat

image snow_a = At("snow", tr_snow_a)
image snow_alien = Dust("snow_a", count=8, xradius=300, yradius=70, center=(300,20), speed=(5, 5), start=10, fast=True)




## Chapter 3 ############################################


init python:
    rain_frames = []
    for i in range(0, 150, 1):
        frame = "images/vfx/window_rain/glass{:03}.png".format(i)
        rain_frames.append((frame, 0.065))

image window_rain = Animation(*sum(rain_frames, ()))

transform tr_rainjpn1:
    xpos 100
    linear 8.3 xoffset -100


transform tr_rainjpn2:
    alpha 1.0 xpos 100
    linear 8.3 alpha 0.0 xoffset -100
    block:
        linear 3.9 alpha 1.0
        linear 11 alpha 0.0
        repeat


transform bow2:
    "images/japan/japan large normal.png"
    yoffset 0
    pause 0.5
    "images/japan/japan large contemplation.png"
    easein 0.45 yoffset +35
    easein 0.3 yoffset 0


## Rain ###########
transform tr_rain1:
    xpos 9 ypos -48 alpha 0.4 xzoom .5 yzoom .4 additive_blend
    linear 60 xpos 19 ypos 177 alpha 0.0 xzoom 1 yzoom 1
    repeat
image rain1 = At("rain", tr_rain1)

image rain1_0 = SnowBlossom("rain1", count=20, border=50, xspeed=0, yspeed=(100, 200), start=0, fast=True)

transform tr_rain2:
    xpos 1 ypos -114 alpha 0.4 xzoom .3 yzoom .4 additive_blend
    linear 60 xpos 3 ypos 157 alpha 0.0 xzoom .58 yzoom 1
    repeat
image rain2_1 = At("rain", tr_rain2)

image rain2_0 = SnowBlossom("rain2_1", count=20, border=50, xspeed=0, yspeed=(100, 500), start=0, fast=True)

transform tr_rain3:
    xpos 18 ypos -88 alpha 0.3 xzoom .34 yzoom .4 additive_blend
    linear 60 xpos -27 ypos 133 alpha 0.0 xzoom .34 yzoom 1
    repeat
image rain3 = At("rain", tr_rain3)

image rain3_0 = SnowBlossom("rain3", count=40, border=50, xspeed=0, yspeed=(100, 500), start=0, fast=True)

transform tr_rain4:
    xpos 64 ypos -22 alpha 0.4 additive_blend
    linear .9 xpos 57 ypos 181 alpha 0.0
    repeat
image rain4 = At("rain2", tr_rain4)

image rain4_0 = SnowBlossom("rain4", count=20, border=50, xspeed=0, yspeed=(100, 500), start=0, fast=True)

transform tr_rain5:
    xpos 75 ypos 137 alpha 0.3 xzoom 2 yzoom 2 additive_blend
    linear .9 xpos 75 ypos 259 alpha 0.0
    repeat
image rain5 = At("rain2", tr_rain5)

image rain5_0 = SnowBlossom("rain5", count=20, border=50, xspeed=0, yspeed=(100, 500), start=0, fast=True)


transform tr_bigrain1:
    xpos -100 ypos -3 alpha 0.4 xzoom 2 yzoom 1 additive_blend
    linear 60 xpos -60 ypos 454 alpha 0.0 xzoom 1.8 yzoom 1
    repeat
image bigrain1 = At("rain", tr_rain1)

image bigrain1_0 = SnowBlossom("rain1", count=20, border=50, xspeed=0, yspeed=(100, 200), start=0, fast=True)

transform tr_bigrain2:
    xpos 242 ypos 129 alpha 0.4 xzoom 3 yzoom 2 additive_blend
    linear 60 xpos 227 ypos 467 alpha 0.0 xzoom 3 yzoom 1.7
    repeat
image bigrain2 = At("rain", tr_rain2)

image bigrain2_0 = SnowBlossom("bigrain2", count=10, border=50, xspeed=0, yspeed=(100, 500), start=0, fast=True)


## Puddles ###########
transform tr_puddlelight1:
    xpos 493 ypos 400 alpha 0 xzoom .26 yzoom -.26  additive_blend
    block:
        linear 4 yoffset 40 xoffset 0 alpha 0.2 xzoom .7 yzoom -.64 additive_blend
        linear 1 alpha 0
        linear 1 yoffset 0 xoffset 0 alpha 0 xzoom .26 yzoom -.26
        repeat
image puddlelight1 = At("surface", tr_puddlelight1)

image surface1_0 = River("puddlelight1", count=20, border=0, xspeed=-20, yspeed=(10, 50), start=2, fast=True, xspawn=(580,700), yspawn=(410,550), ybottom=550)
image surface2_0 = River("puddlelight1", count=20, border=0, xspeed=-20, yspeed=(10, 50), start=2, fast=True, xspawn=(150,300), yspawn=(440,550), ybottom=550)
image surface3_0 = River("puddlelight1", count=20, border=0, xspeed=(-30,-20), yspeed=(10, 50), start=2, fast=True, xspawn=(560,580), yspawn=(420,550), ybottom=600)
image surface4_0 = River("puddlelight1", count=20, border=50, xspeed=-15, yspeed=(10, 50), start=2, fast=True, xspawn=(480,490), yspawn=(410,550), ybottom=600)

transform tr_puddlelight2:
    xpos 493 ypos 400 alpha 0 xzoom .6 yzoom -.6  additive_blend
    block:
        linear 4 yoffset 40 xoffset -10 alpha 0.3 xzoom 1.5 yzoom -1.3 additive_blend
        linear 1 alpha 0
        pause 1 yoffset 0 xoffset 0 alpha 0 xzoom .6 yzoom -.6
        repeat
image puddlelight2 = At("surface", tr_puddlelight2)

image surface5_0 = River("puddlelight2", count=5, border=0, xspeed=(-20, -15), yspeed=(10, 70), start=10, fast=True, xspawn=(450,900), yspawn=(0,350), ybottom=350)
image surface6_0 = River("puddlelight2", count=5, border=50, xspeed=(-30,-20), yspeed=(10, 70), start=10, fast=True, xspawn=(480,490), yspawn=(440,600), ybottom=600)



## Chapter 4






## Chapter 6

define audio.run_wait ="sfx/run_wait.ogg"



transform tr_strangle1:
    xalign 0.0
    linear 11.5 xoffset -80


transform tr_strangle2:
    alpha 0.0 xpos 8
    block:
        linear 0.5 alpha 1.0 xpos -26
        linear 0.5 alpha 0.0 xpos -34
        linear 0.25 alpha 0.0 xpos +30 #blank
        linear 0.5 alpha 0.5 xpos -25
        linear 0.5 alpha 0.0 xpos -22
        linear 0.1 alpha 0.0 xpos +59 #blank
        linear 0.5 alpha 0.6 xpos -28
        linear 0.5 alpha 0.0 xpos -14
        linear 0.1 alpha 0.0 xpos +32 #blank
        linear 0.5 alpha 0.6 xpos -60
        linear 0.5 alpha 0.0 xpos -38
        linear 0.15 alpha 0.0 xpos +84 #blank
        linear 0.5 alpha 1.0 xpos -61
        linear 0.5 alpha 0.0 xpos -16
        linear 0.5 alpha 0.0 xpos +101 #blank
        block:
            linear 0.5 alpha 1.0 xpos -34
            linear 0.5 alpha 0.0 xpos -8
            linear 0.25 alpha 0.0 xpos +42 #blank
            repeat 2
        linear 0.5 alpha 1.0 xpos -34
        linear 0.5 alpha 0.0 xpos -8
        linear 1 alpha 0.0 xpos +42 #blank
        block:
            linear 0.5 alpha 1.0 xpos -34
            linear 0.5 alpha 0.0 xpos -8
            linear 1 alpha 0.0 xpos +42 #blank
            repeat 3
        time 7.5
        repeat

transform tr_strangle3:
    alpha 0.0 xpos -4
    block:
        time 9.9
        block:
            linear 0.5 alpha 0.6 xpos -29
            linear 0.5 alpha 0 xpos -22
            linear 1 alpha 0 xpos +47
            repeat 4
        time 8.75
        repeat






## Chapter 7

image romania quiver = At("images/romania/romania cry nyaa.png", quivering)
transform quivering:
    xpos -40, yalign 0.0
    block:
        block:
            linear 0.08 xoffset -4
            linear 0.08 xoffset 0
            repeat 2
        linear 0.08 xoffset -6
        linear 0.08 xoffset 0
        linear 0.08 xoffset -3
        linear 0.08 xoffset 0
        block:
            linear 0.08 xoffset -4
            linear 0.08 xoffset 0
            repeat 5
        repeat


image sweat = Fixed(
    tr_sweat0("sweat_drop"),
    tr_sweat1("sweat_drop"),
    tr_sweat2("sweat_drop"),
)

transform tr_sweat0:
    xpos 119 ypos 181 zoom 0.84 alpha 1.0 rotate 0
    block:
        linear 0.4 xpos 122 ypos 197 zoom 1.0 alpha 0.0 rotate -9
        pause 1.5 xpos 119 ypos 181 zoom 0.84 alpha 1.0 rotate 0
        repeat

transform tr_sweat1:
    alpha 0.0
    time 0.25
    xpos 139 ypos 152 zoom 0.84 alpha 1.0 rotate 0
    block:
        linear 0.4 xpos 140 ypos 162 zoom 1.0 alpha 0.0 rotate -9
        pause 0.3 xpos 139 ypos 152 zoom 0.84 alpha 1.0 rotate 0
        repeat

transform tr_sweat2:
    alpha 0.0
    time 0.6
    xpos 164 ypos 176 zoom 0.84 alpha 1.0 rotate 0
    block:
        linear 0.4 xpos 165 ypos 195 zoom 1.0 alpha 0.0 rotate 9
        pause 1.5 xpos 164 ypos 176 zoom 0.84 alpha 1.0 rotate 0
        repeat



init python:
    circle_frames = []
    for i in range(24):
        frame = "images/vfx/circle/circle{:02}.png".format(i)
        circle_frames.append((frame, 0.065, None))

image circle_anim = NonLoopAnimation(*sum(circle_frames, ()))

init python:
    circle_frames1 = []
    for i in range(24):
        frame = "images/vfx/circle/circle{:02}.png".format(i)
        circle_frames1.append((frame, 0.030, None))

image circle_anim1 = NonLoopAnimation(*sum(circle_frames1, ()))


transform tr_snow1:
    parallel:
        xpos 379 ypos 47 alpha 0.3 xzoom .5 yzoom .4 additive_blend
        linear 8 xpos 110 ypos 212 alpha 0.9 xzoom 1 yzoom 1
        repeat
    parallel:
        rotate 360
        linear 15 rotate 0
        repeat

image snow2_1 = At("snow2", tr_snow1)
image snow1_0 = SnowBlossom("snow2_1", count=25, border=50, xspeed=(0,20), yspeed=(100, 200), start=5, fast=True)


transform tr_snowfront1:
    parallel:
        xpos 379 ypos 47 alpha 0.3 xzoom 1 yzoom 1 additive_blend
        linear 8 xpos 110 ypos 212 alpha 0.9 xzoom 1 yzoom 1
        repeat
    parallel:
        rotate 360
        linear 12 rotate 0
        repeat

image snowfront = At("snow", tr_snowfront1)
image snowfront_0 = SnowBlossom("snowfront", count=10, border=50, xspeed=(0,20), yspeed=300, start=0, fast=True)

image snow2_0 = SnowBlossom("snow2_1", count=25, border=50, xspeed=(0,20), yspeed=(100, 200), start=5, fast=True)
image snowfront2_0 = SnowBlossom("snowfront", count=5, border=50, xspeed=(0,50), yspeed=300, start=2, fast=True)





transform tr_sparkle2:
    parallel:
        linear 1 alpha 0.5 xzoom .2 yzoom .2 additive_blend
        linear 1 alpha 0.9 xzoom 1 yzoom 1
        repeat
    parallel:
        rotate 0
        linear 2 rotate 360
        repeat

image sparkle2_1 = At("sparkle1", tr_sparkle2)
image sparkle2_0 = Radiate("sparkle2_1", count=5, speed=(200, 300), border=100, start=0, fast=True)


transform tr_sparkle5:
    parallel:
        linear 1 alpha 0.0 xzoom .6 yzoom .6 additive_blend
        linear 1 alpha 0.9 xzoom 1.2 yzoom 1.2
        repeat
    parallel:
        rotate 0
        linear 2 rotate 360
        repeat

image sparkle5_1 = At("sparkle2", tr_sparkle5)
image sparkle5_0 = Radiate("sparkle5_1", count=5, speed=(300,500), border=100, start=10, fast=True)


transform tr_sparklebig:
    parallel:
        linear 1 alpha 0.5 xzoom .00001 yzoom .00001 additive_blend
        linear 1 alpha 0.9 xzoom 1 yzoom 1
        repeat
    parallel:
        rotate 0
        linear 2 rotate 360
        repeat

image sparklebig_1 = At("sparkle1", tr_sparklebig)
image sparklebig_0 = Radiate("sparklebig_1", count=5, speed=(300, 500), border=100, start=0, fast=True)


transform tr_sparklebig2:
    parallel:
        linear 1 alpha 0.5 xzoom .3 yzoom .3 additive_blend
        linear 1 alpha 0.9 xzoom 1 yzoom 1
        repeat
    parallel:
        rotate 0
        linear 2 rotate 360
        repeat

image sparklebig2_1 = At("sparkle1", tr_sparklebig2)
image sparklebig2_0 = SnowBlossom("sparklebig2_1", count=20, border=100, xspeed=(0,20), yspeed=-290, start=0.5, fast=True, distribution='linear', animation=True)



transform tr_sparklebig3:
    parallel:
        linear 1 alpha 0.5 xzoom .3 yzoom .3 additive_blend
        linear 1 alpha 0.9 xzoom .5 yzoom .5
        repeat
    parallel:
        rotate 0
        linear 2 rotate 360
        repeat

image sparklebig3_1 = At("sparkle1", tr_sparklebig3)
image sparklebig3_0 = SnowBlossom("sparklebig3_1", count=20, border=50, xspeed=(-10,15), yspeed=-310, start=0.1, fast=True)





transform tr_sparklebig4:
    parallel:
        linear 1 alpha 0.5 xzoom .4 yzoom .4 additive_blend
        linear 1 alpha 0.9 xzoom .8 yzoom .8
        repeat
    parallel:
        rotate 0
        linear 2 rotate 360
        repeat

image sparklebig4_1 = At("sparkle1", tr_sparklebig4)
image sparklebig4_0 = SnowBlossom("sparklebig4_1", count=20, border=60, xspeed=(5,25), yspeed=-300, start=0.3, fast=True, animation=False)








