init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

## Animated images ######################################################################

init python:
    ctc_frames = []
    for i in range(3):
        frame = f"gui/button/ctc_{i}.png"
        ctc_frames.append((frame, 0.1))

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


## VFX ######################################################################
image dust2:
    "images/vfx/dust.png"
    



## Transitions ######################################################################

define fade_white = Fade(0.5, 0.0, 0.5, color="#fff")

## Transforms ######################################################################

init python:

    class TrackCursor(renpy.Displayable):
        def __init__(self, child):
            super(TrackCursor, self).__init__()
            self.child = renpy.displayable(child)
            self.x = None
            self.y = None

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x, self.y + 20))
            return rv

        def event(self, ev, x, y, st):
            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                renpy.redraw(self, 0)




transform namebox_float:
    yoffset -30
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

transform fade_in_title:
    alpha 0.0
    linear 1.25 alpha 1.0



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

## Sprite positions ######################################################################

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