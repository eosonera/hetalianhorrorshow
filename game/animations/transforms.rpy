####################################################################################
## Transitions ######################################################################
####################################################################################

define fade_white = Fade(0.5, 0.0, 0.5, color="#fff")
define fade_red = Fade(0.5, 0.0, 0.5, color="#ff0000")
define fade_white_slow = Fade(0.5, 1.0, 0.5, color="#fff")
image white screen = "#fff" 
image bg white = "#fff" 
image red screen = "#ff0000" 
image blue screen = "#0000FF"

define circle_dissolve = ImageDissolve("images/vfx/circle_dissolve2.png", 0.3, reverse=True)
define circle_dissolve2 = ImageDissolve("images/vfx/circle_dissolve2.png", 1, reverse=True)
define circle_dissolve3 = ImageDissolve("images/vfx/circle_dissolve2.png", 0.3, reverse=True)

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




## Sprite anim ######################################################################

transform bow:
    yoffset 0
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

transform nvl_narrow:
    xsize 300