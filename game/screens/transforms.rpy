
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

## Transitions ######################################################################

define fade_white = Fade(0.5, 0.0, 0.5, color="#fff")
image white screen = "#fff" 



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





####################################################################################
## Transforms ######################################################################
####################################################################################


## Menu animations ###########################################################


transform anim_game_menu:
    yoffset 27
    linear .83:
        yoffset 0


transform anim_doily:
    xycenter(151,408)
    rotate -40
    linear .83:
        xycenter(151,408)
        rotate 0
    

transform menu_jump:
    on hover:
        linear .61 yoffset -6
        yoffset 0
        repeat
    on idle:
        yoffset 0

transform menu_hover_float:
    on hover:
        linear 0.7 yoffset -15
        linear 0.7 yoffset 0
        repeat
    on idle:
        yoffset 0




## BG animations ######################################################################

transform pan_to_top:
    yalign 1.0
    linear 1.6 yalign 0.0

transform pan_to_top_ext0:
    yalign 1.0
    easein 7 yalign 0.0

transform pan_to_bottom:
    yalign 0.0
    easein 1 yalign 1.0

transform pan_to_bottom1:
    yalign 0.0
    easein 1.5 yoffset -70

## Cutscenes ######################################################################


## England blackboard 

transform blackboard:
    block:
        linear 12 xoffset -400 yoffset -70

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


## Shakes ######################################################################


transform mb_shake:
    time .5
    linear 0.1 xoffset -21 yoffset -17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0
    
transform mb_shake_long:
    time 1.2
    linear 0.1 xoffset -21 yoffset -17
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake2:
    time .5
    linear 0.1 xoffset -21 yoffset +17
    linear 0.1 xoffset +10 yoffset -10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake3:
    time .5
    linear 0.1 xoffset -22 yoffset -21
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -18 yoffset +19
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset -11 yoffset +8
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake4:
    time 1.5
    linear 0.1 xoffset +22 yoffset -22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset -6
    linear 0.1 xoffset 0 yoffset 0


transform s_shake1:
    0.5
    block:
        linear 0.1 xoffset -8 yoffset -8
        linear 0.1 xoffset +8 yoffset +8
        repeat 2
    linear 0.1 xoffset 0 yoffset 0

transform s_shake2:
    0.4
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset -8 yoffset +8
    linear 0.1 xoffset +8 yoffset -8
    linear 0.1 xoffset 0 yoffset 0

transform s_shake3:
    0.4
    linear 0.1 xoffset -12 yoffset +12
    linear 0.2 xoffset +4 yoffset -4
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset 0 yoffset 0

transform s_shake_horiz:
    0.1
    block:
        linear 0.15 xoffset +10
        linear 0.15 xoffset -10
        repeat

transform jump:
    0.1
    easeout 0.3 yoffset -100
    easein 0.2 yalign 0.0 yoffset +40
    easeout 0.2 yoffset 0



## Sprite anim ######################################################################

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

transform stop_offset:
    xoffset 0 yoffset 0

transform stop_offset_delay:
    0.8
    xoffset 0 yoffset 0



## Sprite positions ######################################################################



init python:
    def pos_transform(x=None, y=None, xalign=None, yalign=None, xoffset=None, yoffset=None):
        t = Transform()
        if x is not None:
            t.xpos = x
        if y is not None:
            t.ypos = y
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

