init:
    transform additive_blend:
        additive 1.0

## VFX ######################################################################



transform dark_tint:
    matrixcolor TintMatrix("#adadad")


transform tr_dust1:
    pos(0, 200) alpha 0.3 additive_blend
    linear 2.5 xoffset 200 alpha 0.0

transform tr_dust0:
    pos(0, 200) alpha 0.3 additive_blend
    linear 2.5 xoffset 300 yoffset -100 alpha 0.0


image dust0_0 = At("dust", tr_dust0)
image dust1_0 = At("dust", tr_dust1)


transform tr_dust2:
    alpha 0.1 xzoom .5 yzoom .4 rotate 360 additive_blend
    parallel:
        linear 13.5 alpha 0.6 xzoom .65 yzoom .67 additive_blend
        linear 13.5 alpha 0.1 xzoom .5 yzoom .4
        repeat
    parallel:
        linear 60 rotate 0
        linear 60 rotate 360
        repeat

image dust2 = At("dust", tr_dust2)
image dust2_0 = Dust("dust2", count=10, xradius=200, yradius=50, center=(200,0), speed=(3, 2), start=10, fast=True)
image dust2_1 = Dust("dust2", count=5, xradius=200, yradius=50, center=(200,0), speed=(3, 2), start=10, fast=True)


transform rotation:
    xalign .5 yalign .5
    rotate 0
    linear 5 rotate 360 #5 seconds, 360 degrees
    repeat

### Sun


transform tr_sunlight1(cen1, cen2, cen3, alpha1, xzoom1, yzoom1, xzoom2, yzoom2, xzoom3, yzoom3):
    alpha 0 additive_blend xzoom xzoom1 yzoom xzoom1 xycenter cen1
    time 1.9
    block:
        linear 6.7 alpha alpha1 additive_blend xzoom xzoom2 yzoom yzoom2 xycenter cen2 #until 8.6
        linear 5.85 alpha 0 additive_blend xzoom xzoom3 yzoom yzoom3 xycenter cen3 #until 14.45
        pause 10.8 alpha 0 additive_blend xzoom xzoom1 yzoom xzoom1 xycenter cen1  #23.35+1.9
        repeat

transform tr_sunlight2(cen1, cen2, cen3, alpha1, xzoom1, yzoom1, xzoom2, yzoom2, xzoom3, yzoom3):
    alpha 0 additive_blend xzoom xzoom1 yzoom xzoom1 xycenter cen1 
    time 8.9
    block:
        linear 6.7 alpha alpha1 additive_blend xzoom xzoom2 yzoom yzoom2 xycenter cen2 #until 15.6
        linear 5.85 alpha 0 additive_blend xzoom xzoom3 yzoom yzoom3 xycenter cen3 #until 21.45
        pause 10.8 alpha 0 additive_blend xzoom xzoom1 yzoom xzoom1 xycenter cen1  #23.35
        repeat

transform spin_sun1:
    rotate 1
    time 1.9
    block:
        linear 6.7 rotate -35 #8.6
        linear 5.85 rotate -58 #14.45
        pause 10.8 rotate 1  #23.35
        repeat

transform spin_sun2:
    rotate 1
    time 8.9
    block:
        linear 6.7 rotate -35 #8.6
        linear 5.85 rotate -58 #14.45
        pause 10.8 rotate 1  #23.35
        repeat

transform spin_sun2_1:
    rotate -20
    time 8.9
    block:
        linear 6.7 rotate -50 #8.6
        linear 5.85 rotate -70 #14.45
        pause 10.8 rotate -20  #23.35
        repeat













# transform spin_sun:
#     rotate 0
#     linear 60 rotate 360
#     repeat

transform spin_sun_ccw:
    rotate 360
    linear 60 rotate 0
    repeat

transform spin_sun_cw:
    rotate 0
    linear 120 rotate 360
    repeat


# transform tr_sunlight(time_val, l1_dur, l2_dur, l3_dur, xcen, ycen, l1_alpha, l1_xzoom, l1_yzoom, l2_xzoom, l2_yzoom, l3_xzoom, l3_yzoom):
#     alpha 0.0 xcenter xcen ycenter ycen xzoom l3_xzoom yzoom l3_yzoom additive_blend
#     time time_val
#     block:
#         linear l1_dur xzoom l1_xzoom yzoom l1_yzoom alpha l1_alpha additive_blend
#         linear l2_dur xzoom l2_xzoom yzoom l2_yzoom alpha 0.0 additive_blend
#         linear l3_dur xzoom l3_xzoom yzoom l3_yzoom xcenter xcen ycenter ycen alpha 0.0 additive_blend
#         repeat

# transform tr_sunlight_norepeat(time_val, l1_dur, l2_dur, l3_dur, xcen, ycen, l1_alpha, l1_xzoom, l1_yzoom, l2_xzoom, l2_yzoom, l3_xzoom, l3_yzoom):
#     alpha 0.0 xcenter xcen ycenter ycen xzoom l3_xzoom yzoom l3_yzoom additive_blend
#     time time_val
#     block:
#         linear l1_dur xzoom l1_xzoom yzoom l1_yzoom alpha l1_alpha additive_blend
#         linear l2_dur xzoom l2_xzoom yzoom l2_yzoom alpha 0.0 additive_blend
#         linear l3_dur xzoom l3_xzoom yzoom l3_yzoom xcenter xcen ycenter ycen alpha 0.0 additive_blend

########






transform tr_orange3:
    alpha 0.0
    time 11.3
    block:
        linear 4.25 alpha 0.25 additive_blend
        linear 4.25 alpha 0.0 additive_blend
        time 32
        repeat

transform tr_orange2:
    alpha 0.0
    block:
        linear 4.25 alpha 0.25 additive_blend
        linear 4.25 alpha 0.0 additive_blend
        time 32
        repeat