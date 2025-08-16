####################################################################################
## Transitions ######################################################################
####################################################################################

define fade_white = Fade(0.5, 0.0, 0.5, color="#fff")
define fade_white_slow = Fade(0.5, 1.0, 0.5, color="#fff")
image white screen = "#fff" 
image blue screen = "#0000FF"

define circle_dissolve = ImageDissolve("images/vfx/circle_dissolve2.png", 0.3, reverse=True)

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

transform pan_to_top_slow:
    yalign 1.0
    linear 3.0 yalign 0.0

transform pan_to_top_ext0:
    yalign 1.0
    easein 7 yalign 0.0

transform pan_to_bottom:
    yalign 0.0
    easein 1 yalign 1.0

transform pan_to_bottom1:
    yalign 0.0
    easein 1.5 yoffset -70



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
    time 1.0
    linear 0.1 xoffset +22 yoffset -22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset -6
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake5:
    time .5
    linear 0.1 xoffset +15 yoffset -15
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -9 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +4 yoffset -4
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake6:
    time .5
    linear 0.1 xoffset +21 yoffset -17
    linear 0.1 xoffset -10 yoffset +10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake7:
    time .3
    linear 0.1 xoffset -21 yoffset +17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake8:
    time 2
    linear 0.1 xoffset -22 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake9:
    time 0.9
    linear 0.1 xoffset +22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform mb_shake10:
    time 0.3
    linear 0.1 xoffset +18 yoffset +18
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
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
    0.5
    linear 0.1 xoffset -18 yoffset +18
    linear 0.2 xoffset +9 yoffset -9
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +8 yoffset +8
    linear 0.1 xoffset 0 yoffset 0

transform s_shake_horiz:
    0.1
    block:
        linear 0.15 xoffset +10
        linear 0.15 xoffset -10
        repeat

transform s_shake4:
    0.8
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset -8 yoffset +8
    linear 0.1 xoffset +8 yoffset -8
    linear 0.1 xoffset 0 yoffset 0



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

transform jump:
    0.1
    easeout 0.3 yoffset -100
    easein 0.2 yalign 0.0 yoffset +40
    easeout 0.2 yoffset 0

transform jump2:
    0.3
    easeout 0.3 yoffset -20
    ease 0.2 yoffset 30

transform jump3:
    yoffset 0
    0.4
    easeout 0.3 yoffset -40
    ease 0.2 yoffset 10
    easeout 0.2 yoffset -30
    ease 0.15 yoffset 0

transform jump4:
    yoffset 0
    1.2
    easeout 0.3 yoffset -30
    ease 0.2 yoffset 10
    easeout 0.2 yoffset -20
    ease 0.15 yoffset 0

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

