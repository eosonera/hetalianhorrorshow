init:
    transform additive_blend:
        additive 1.0

## VFX ######################################################################



transform dark_tint:
    matrixcolor TintMatrix("#adadad")

image dust = "images/vfx/dust.png"
image dust_1 = "images/vfx/dust.png"
image dust2 = "images/vfx/dust.png"
        
transform dust1_transform:
    pos(0, 200) alpha 0.3 additive_blend
    linear 2.5 xoffset 200 alpha 0.0

transform dust1_transform1:
    pos(0, 200) alpha 0.3 additive_blend
    linear 2.5 xoffset 300 yoffset -100 alpha 0.0

transform dust2_transform:
    xycenter(596,394) size(1500,800) xzoom 0.5 yzoom 0.4 rotate 0 additive_blend
    parallel:
        linear 60 rotate 360 additive_blend
        repeat
    parallel:
        linear 13 xycenter(491,368)
        linear 13 xycenter(399,348)
        repeat
    parallel:
        linear 13 xzoom 0.65 yzoom 0.67
        linear 13 xzoom 0.5 yzoom 0.4
        repeat

transform rotation:
    xalign .5 yalign .5
    rotate 0
    linear 5 rotate 360 #5 seconds, 360 degrees
    repeat

#############


image sunlight2_0 = At("images/vfx/sunlight2.png", sunlight2_transform0)
image sunlight2_1 = At("images/vfx/sunlight2.png", sunlight2_transform1)
image sunlight2_0_1 = At("images/vfx/sunlight2.png", sunlight2_transform0_1)
image sunlight2_1_1 = At("images/vfx/sunlight2.png", sunlight2_transform0_1)

transform sunlight2_transform0:
    alpha 0.0 rotate 1
    time 0.88
    block:
        linear 7.72 alpha 0.15 rotate -35 additive_blend
        linear 6.7 alpha 0.0 rotate -58
        linear 0.88 alpha 0.0 rotate 1
        repeat
        
transform sunlight2_transform1:
    alpha 0.0 rotate -20
    time 8.3
    block:
        linear 6.83 alpha 0.2 rotate -50 additive_blend
        linear 6 alpha 0.0 rotate -70
        linear 8.3 alpha 0.0 rotate -20
        repeat

transform sunlight2_transform0_1:
    alpha 0.0 rotate 1
    time 0.26
    block:
        linear 4 alpha 0.15 rotate -35 additive_blend
        linear 3.4 alpha 0.0 rotate -58
        linear 5 alpha 0.0 rotate 1
        repeat


transform sun_rroom1_0:
    xycenter(-200,0)

transform sun_rroom1_1:
    xycenter(-200,32)

transform sun_rroom3_0:
    xycenter(430,85) xzoom 0.71 yzoom 0.92
    time 0.88
    block:
        linear 7.72 xzoom 0.76 yzoom 0.76
        linear 6.7 xzoom 1.0 yzoom 1.0
        linear 0.88 xycenter(430,85) xzoom 0.71 yzoom 0.92
        repeat

transform sun_rroom3_1:
    xycenter(370,30) xzoom 0.32 yzoom 0.44
    time 8.3
    block:
        linear 6.83 xzoom 0.80 yzoom 0.60
        linear 6 xzoom 1.0 yzoom 1.0
        linear 8.3 xzoom 0.32 yzoom 0.44
        repeat

transform sun_rroom2_0:
    xycenter(509,65) xzoom 0.47 yzoom 0.58
    time 0.88
    block:
        linear 7.72 xzoom 1.0 yzoom 1.0
        linear 6.7 xzoom 1.0 yzoom 1.0
        linear 0.88 xycenter(509,65) xzoom 0.47 yzoom 0.58
        repeat

transform sun_ext_0:
    xycenter(509,-100) xzoom 0.47 yzoom 0.58
    time 0.26
    linear 4 xzoom 1.0 yzoom 1.0
    linear 3.42 xzoom 1.0 yzoom 1.0
    linear 4.95 xycenter(509,65) xzoom 0.47 yzoom 0.58
    block:
        linear 4 xzoom 1.0 yzoom 1.0
        linear 3.42 xzoom 1.0 yzoom 1.0
        linear 4.95 xycenter(509,65) xzoom 0.47 yzoom 0.58
        repeat

transform sun_ext_1:
    xycenter(509,-100) xzoom 0.47 yzoom 0.58
    time 9.6
    block:
        linear 4 xzoom 1.0 yzoom 1.0
        linear 3.4 xzoom 1.0 yzoom 1.0
        linear 5 xycenter(509,-100) xzoom 0.47 yzoom 0.58
        repeat

########

image orange = At("images/vfx/orange.png", orange_transform0)
transform orange_transform0:
    align(0.5,0.5)
    alpha 0.0
    time 3.38
    block:
        linear 1.7 alpha 0.19 additive_blend
        linear 1.7 alpha 0.0
        time 20
        repeat

image yellow = At("images/vfx/upperleft_yellow.png", yellow_transform0)
transform yellow_transform0:
    align(0.5,0.5)
    alpha 0.0
    time 14.26
    block:
        linear 1.7 alpha 0.15 additive_blend
        linear 1.7 alpha 0.0
        time 20
        repeat