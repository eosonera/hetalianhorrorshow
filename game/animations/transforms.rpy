####################################################################################
## Transitions ######################################################################
####################################################################################

define fade_white = Fade(0.5, 0.0, 0.5, color="#fff")
define fade_red = Fade(0.5, 0.0, 0.5, color="#ff0000")
define fade_white_slow = Fade(0.5, 1.0, 0.5, color="#fff")
image white screen = "#fff" 
image bg white = "#fff" 
image blue screen = "#0000FF"

define circle_dissolve = ImageDissolve("images/vfx/circle_dissolve2.png", 0.3, reverse=True)
define circle_dissolve2 = ImageDissolve("images/vfx/circle_dissolve2.png", 1, reverse=True)
define circle_dissolve3 = ImageDissolve("images/vfx/circle_dissolve2.png", 1, reverse=True)

transform blur_fade(duration=2.0, *, new_widget=None, old_widget=None):

    # Set how long the transition lasts.
    delay duration

    # Center it
    xcenter 0.5
    ycenter 0.5

    old_widget
    events False
    blur 0
    ease (duration / 2):
        blur 8

    new_widget
    events True
    blur 8
    linear (duration / 2):
        blur 0

transform zoominzoomout(duration=1.0, *, new_widget=None, old_widget=None):

    delay duration

    xcenter .5
    ycenter .5

    old_widget
    zoom 1.0
    events True
    easeout (duration / 2):
        xcenter .375
        zoom 4

    new_widget
    events True
    zoom 4 xcenter .375
    easein (duration / 2):
        zoom 1.0
        xcenter .5



####################################################################################
## Transforms ######################################################################
####################################################################################



## BG animations ######################################################################

transform pan_to_top:
    yalign 1.0
    easein 1.6 yalign 0.0

transform pan_to_top_slow:
    yalign 1.0
    linear 3.0 yalign 0.0

transform pan_to_top_ext0:
    yalign 1.0
    easein 7 yalign 0.0

transform pan_to_top_dur(dur=1.6):
    yalign 1.0
    easein dur yalign 0.0

transform pan_to_bottom:
    yalign 0.0
    easein 1 yalign 1.0

transform pan_to_bottom1:
    yalign 0.0
    easein 1.5 yoffset -70

transform delay_blackscreen_hide:
    alpha 1.0
    pause 1.5
    linear 0.5 alpha 0.0

## Shakes ######################################################################


transform shake_0p1:
    time .5
    linear 0.1 xoffset -21 yoffset -17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0p2:
    0.5
    block:
        linear 0.1 xoffset -8 yoffset -8
        linear 0.1 xoffset +8 yoffset +8
        repeat 2
    linear 0.1 xoffset 0 yoffset 0

transform shake_0p3:
    0.4
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset -8 yoffset +8
    linear 0.1 xoffset +8 yoffset -8
    linear 0.1 xoffset 0 yoffset 0

transform shake_0p4:
    time 1.2
    linear 0.1 xoffset -21 yoffset -17
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0p5:
    time .5
    linear 0.1 xoffset -21 yoffset +17
    linear 0.1 xoffset +10 yoffset -10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0




transform shake_0m1:
    time .5
    linear 0.1 xoffset -22 yoffset -21
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -18 yoffset +19
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset -11 yoffset +8
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m2:
    time 1.0
    linear 0.1 xoffset +22 yoffset -22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset -6
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m3:
    time .5
    linear 0.1 xoffset +15 yoffset -15
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -9 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +4 yoffset -4
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m4:
    time .5
    linear 0.1 xoffset +21 yoffset -17
    linear 0.1 xoffset -10 yoffset +10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m5:
    time .3
    linear 0.1 xoffset -21 yoffset +17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m6:
    time 2
    linear 0.1 xoffset -22 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m7:
    time 0.8
    linear 0.1 xoffset +22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m8:
    time 0.3
    linear 0.1 xoffset +18 yoffset +18
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0


transform shake_0m9:
    0.5
    linear 0.1 xoffset -18 yoffset +18
    linear 0.2 xoffset +9 yoffset -9
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +8 yoffset +8
    linear 0.1 xoffset 0 yoffset 0


transform shake_0m10:
    1.5
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset -8 yoffset +8
    linear 0.1 xoffset +8 yoffset -8
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m11:
    time 1.5
    linear 0.1 xoffset +22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0


transform shake_1s1:
    time 0.8
    linear 0.1 xoffset -22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s1:
    time .5
    linear 0.1 xoffset -12 yoffset -12
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -8 yoffset +9
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset -2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s2:
    time 1.5
    linear 0.1 xoffset -22 yoffset +22
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset -12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s3:
    0.5
    linear 0.1 xoffset +22 yoffset +22
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset +12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s4:
    time 0.5
    linear 0.1 xoffset -21 yoffset -17
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s5:
    time .8
    linear 0.1 xoffset -22 yoffset -21
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -18 yoffset +19
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset -11 yoffset +8
    linear 0.1 xoffset 0 yoffset 0


transform shake_2s6:
    time 0.2
    linear 0.1 xoffset -22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s7:
    time 0.4
    linear 0.1 xoffset -22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0


transform shake_2s8:
    time 1.6
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -4 yoffset -4
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0


transform shake_3s1:
    time 0.4
    block:
        linear 0.07 xoffset -12 yoffset 12
        linear 0.07 xoffset 0 yoffset 0
        repeat 3
    linear 0.07 xoffset 8 yoffset 8
    linear 0.07 xoffset 0 yoffset 0
    linear 0.05 xoffset -8 yoffset 8
    linear 0.05 xoffset 0 yoffset 0
    linear 0.07 xoffset -4 yoffset 4
    linear 0.07 xoffset 0 yoffset 0

transform shake_3s2:
    time 1
    linear 0.1 xoffset -21 yoffset +17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_3s3:
    time 3
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +8 yoffset -8
    linear 0.1 xoffset -4 yoffset -4
    linear 0.1 xoffset +2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0

transform shake_4s1:
    time 0.2
    linear 0.05 xoffset -42 yoffset -40
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +20 yoffset -20
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +10 yoffset +10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -6 yoffset -6
    linear 0.05 xoffset 0 yoffset 0


transform shake_4s2:
    time 0.2
    linear 0.05 xoffset +42 yoffset +40
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -20 yoffset -20
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +10 yoffset -10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -6 yoffset +6
    linear 0.05 xoffset 0 yoffset 0


transform shake_4s3:
    time 0.8
    linear 0.1 xoffset -32 yoffset +30
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +3 yoffset -3
    linear 0.1 xoffset 0 yoffset 0

transform shake_5s1:
    time 0.5
    linear 0.05 xoffset -42 yoffset -40
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +30 yoffset -30
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +10 yoffset +10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -6 yoffset -6
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +3 yoffset +3
    linear 0.05 xoffset 0 yoffset 0

transform shake_5s2:
    time 0.5
    linear 0.1 xoffset -30 yoffset -30
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset -6
    linear 0.1 xoffset 0 yoffset 0


transform shake_5s3:
    time 0.5
    linear 0.1 xoffset +20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0


transform shake_5s4:
    time .7
    linear 0.1 xoffset -22 yoffset -21
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -3 yoffset -3
    linear 0.1 xoffset 0 yoffset 0

transform shake_5s5:
    0.9
    linear 0.1 xoffset -20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -4 yoffset +4
    linear 0.1 xoffset 0 yoffset 0


transform shake_6s1:
    time .5
    linear 0.1 xoffset +20 yoffset +17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0

transform shake_6s2:
    time .5
    linear 0.1 xoffset +30 yoffset +27
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0


transform shake_7s1:
    time .5
    linear 0.1 xoffset +20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s2:
    time 1.5
    linear 0.1 xoffset +15 yoffset -15
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -9 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +4 yoffset -4
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s3:
    time 0.5
    linear 0.1 xoffset +20 yoffset +20
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s4:
    time 0.5
    linear 0.1 xoffset -30 yoffset -30
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0


transform shake_7s5:
    time .5
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s6:
    time .5
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -2 yoffset -2
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s7:
    time 1
    linear 0.1 xoffset -20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -2 yoffset -2
    linear 0.1 xoffset 0 yoffset 0


transform shake_7s8:
    time 1
    linear 0.1 xoffset +20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s9:
    time 0.5
    linear 0.1 xoffset +20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0


## Sprite anim ######################################################################




transform bow:
    yoffset 0
    0.5
    easein 0.45 yoffset +35
    easein 0.3 yoffset 0




transform stop_offset:
    xoffset 0 yoffset 0

transform stop_offset_delay:
    0.8
    xoffset 0 yoffset 0



## Sprite positions ######################################################################



init python:
    def pos_transform(xpos=None, ypos=None, xalign=None, yalign=None, xoffset=None, yoffset=None):
        t = Transform()
        if xpos is not None:
            t.xpos = xpos
        if ypos is not None:
            t.ypos = ypos
        if xalign is not None:
            t.xalign = xalign
        if yalign is not None:
            t.yalign = yalign
        if xoffset is not None:
            t.xoffset = xoffset
        if yoffset is not None:
            t.yoffset = yoffset
        return t


transform dark_pos:
    matrixcolor TintMatrix("#ebebeb")
    xpos 440 yalign 0.0

transform center:
    xalign 0.5
    yalign 0.0

