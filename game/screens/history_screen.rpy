
#################################################################################
## History screen ##############################################################
#################################################################################
## https://www.renpy.org/doc/html/history.html

define config.history_current_dialogue = False


screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    button:
        action Return()
        background None
        xysize (900, 600)
        focus_mask None
        keyboard_focus False
        mouse False

    use game_menu(_("History"))
    add "gui/menu_game/backlog.png":
        xpos 138
        ypos 109
    add "gui/scrollbar/log_1.png":
        xpos 684
        ypos 201
    
    frame:
        style_prefix "history"
        controller_viewport:
            xpos 227
            ypos 202
            xsize 462
            ysize 230
            id "hist_vp"
            mousewheel True draggable True pagekeys True
            scrollbars "vertical"
            yinitial 1.0
            which_stick "both"
            focus_scroll True

            vbox:
                spacing 30
                for h in _history_list:
                    frame:
                        vbox:
                            spacing 10
                            if h.who:
                                label "【　{}　】".format(name_map.get(h.who, h.who)) style 'history_name':
                                    substitute False
                                    xsize 200   
                            else:
                                null height 0

                            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                            text what:
                                substitute False

            if not _history_list:
                label _(" ")

        vbar value YScrollValue("hist_vp") style "history_vscrollbar":
            xpos 674
            ypos 202


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_name:
    xalign 0

style history_name_text is history_text

style history_text:
    textalign 0.0
    size 16
    color "#fff"
    outlines [(1.2, "#597a87", 0, 0)]

style history_label:
    xfill True

style history_vscrollbar:
    xsize 16
    ysize 232
    yoffset -5
    thumb "gui/slider/thumb_0.png"
    hover_thumb "thumb_hover_anim"


## History Config #####################################################################

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 99

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 109
define gui.history_name_ypos = 0
define gui.history_name_width = 109
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 120
define gui.history_text_ypos = 2
define gui.history_text_width = 430
define gui.history_text_xalign = 0.0