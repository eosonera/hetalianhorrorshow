    
## Animated images ######################################################################

init python:
    ctc_frames = []
    for i in range(3):
        frame = f"gui/button/ctc_{i}.png"
        ctc_frames.append((frame, 0.1))

image ctc_button = Animation(*sum(ctc_frames, ()))

## Transitions ######################################################################

define fade_white = Fade(0.5, 0.0, 0.5, color="#fff")

## Transforms ######################################################################

transform namebox_float:
    yoffset -30  # Adjust based on how far above the bubble you want it
    xoffset 0

transform title_main_menu:
    zoom 2.0
    rotate -190

    linear .430:
        zoom 1.0
        rotate 0
    
transform title_float:
    linear xpos 266 ypos 456
    
    repeat

transform hover_float:
    on hover:
        linear 1 yoffset -5
        linear 1 yoffset 0
        repeat
    on idle:
        yoffset 0

transform fade_in_title:
    alpha 0.0
    linear 1.25 alpha 1.0

transform center:
    xalign 0.5
    yalign 0.5

transform normal:
    xalign 0.5
    yalign 0

transform mid_right:
    xalign 0.72
    yalign 0.0

transform mid_left:
    xalign 0.12
    yalign 0.0

transform sprite_shake:
    0.5
    block:
        linear 0.1 xoffset -8 yoffset -8
        linear 0.1 xoffset +8 yoffset +8
        repeat 2

transform shake2:
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset -8 yoffset +8
    linear 0.1 xoffset +8 yoffset -8

transform humming:

    0.5
    block:
        parallel:
            ease 0.6 xoffset -150
            ease 0.6 xoffset +150
        parallel:
            ease 0.6 yoffset -15
            #ease 0.3 yoffset 0
            ease 0.6 yoffset +15
            #ease 0.3 yoffset 0
        repeat
