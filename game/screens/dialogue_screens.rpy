
## Say screens ##################################################################

default _skip_appear_effect = False
default window_transform = None

## Transforms

transform appear_textbox:
    yzoom .8 yoffset 68 alpha 0
    linear 0.3:
        alpha 1.0
        yzoom 1
        yoffset 0



############################
# Base reusable textbox
############################
screen textbox(who, what, image_path, frame_pos=None, window_pos=None, window_size=None, text_size=None, text_kerning=None, text_line_spacing=None, style_prefix_name=None, appear_effect=None):

    if appear_effect and not _skip_appear_effect:
        add Image(image_path) at appear_effect
    else:
        add Image(image_path)

    if who is not None and frame_pos:
        frame:
            xpos frame_pos[0]
            ypos frame_pos[1]
            add "gui/name_icons/[who].png"

    window at window_transform:
        if window_pos:
            xpos window_pos[0]
            ypos window_pos[1]
        if window_size:
            xsize window_size[0]
            ysize window_size[1]

        text what:
            id "what"
            if text_size is not None:
                size text_size
            if text_kerning is not None:
                kerning text_kerning
            if text_line_spacing is not None:
                line_spacing text_line_spacing


############################
# Variants
############################

screen narrator(who, what):
    use textbox(who, what, "images/textbox/center.png",
        
        window_pos=(160, 210),
        window_size=narr_window_size,
        text_size=text_size_narr,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="narrator",
        text_line_spacing=gui.line_spacing,
        appear_effect=appear_textbox
    )

screen right_1(who, what):
    use textbox(who, what, "images/textbox/right_1.png",
        frame_pos=(608, 234),
        window_pos=(609, 292),
        window_size=window_size_right1,
        text_size=text_size_right1,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="right_1",
        appear_effect=appear_textbox
    )

screen right_3(who, what):
    use textbox(who, what, "images/textbox/right_3.png",
        frame_pos=(394, 247),
        window_pos=(396, 292),
        window_size=window_size_right3,
        text_size=text_size_right3,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="right_3",
        appear_effect=appear_textbox
    )

screen right_4(who, what):
    use textbox(who, what, "images/textbox/right_4.png",
        frame_pos=(501, 328),
        window_pos=(502, 380),
        window_size=window_size_right4,
        text_size=text_size_right4,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="right_4",
        appear_effect=appear_textbox
    )

screen right_4long(who, what):
    use textbox(who, what, "images/textbox/right_4long.png",
        frame_pos=(419, 335),
        window_pos=(420, 388),
        window_size=window_size_right4long,
        text_size=text_size_right4long,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="right_4long",
        appear_effect=appear_textbox
    )

screen right_7big(who, what):
    use textbox(who, what, "images/textbox/right_7big.png",
        frame_pos=(404, 253),
        window_pos=(407, 307),
        window_size=window_size_right7big,
        text_size=text_size_right7big,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="right_7big",
        appear_effect=appear_textbox
    )

screen left_1(who, what):
    use textbox(who, what, "images/textbox/left_1.png",
        frame_pos=(28, 279),
        window_pos=(31, 333),
        window_size=window_size_left1,
        text_size=text_size_left1,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="left_1",
        appear_effect=appear_textbox
    )

screen left_3(who, what):
    use textbox(who, what, "images/textbox/left_3.png",
        frame_pos=(36, 246),
        window_pos=(37, 300),
        window_size=window_size_left3,
        text_size=text_size_left3,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="left_3",
        appear_effect=appear_textbox
    )

screen left_4(who, what):
    use textbox(who, what, "images/textbox/left_4.png",
        frame_pos=(37, 289),
        window_pos=(40, 341),
        window_size=window_size_left4,
        text_size=text_size_left4,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="left_4",
        appear_effect=appear_textbox
    )

screen left_4long(who, what):
    use textbox(who, what, "images/textbox/left_4long.png",
        frame_pos=(45, 293),
        window_pos=(50, 348),
        window_size=window_size_left4long,
        text_size=text_size_left4long,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="left_4long",
        appear_effect=appear_textbox
    )

screen center_1(who, what):
    use textbox(who, what, "images/textbox/center_1.png",
        frame_pos=(293, 298),
        window_pos=(294, 352),
        window_size=window_size_center1,
        text_size=text_size_center1,
        text_kerning=gui.kerning_dialogue - 2,
        style_prefix_name="center_1",
        appear_effect=appear_textbox
    )

screen center_3(who, what):
    use textbox(who, what, "images/textbox/center_3.png",
        frame_pos=(278, 358),
        window_pos=(280, 411),
        window_size=window_size_center3,
        text_size=text_size_center3,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="center_3",
        appear_effect=appear_textbox
    )

screen center_3long(who, what):
    use textbox(who, what, "images/textbox/center_4long.png",
        frame_pos=(197, 312),
        window_pos=(198, 365),
        window_size=window_size_center3long,
        text_size=text_size_center3long,
        text_kerning=gui.kerning_dialogue,
        style_prefix_name="center_3long",
        appear_effect=appear_textbox
    )

screen center_4long(who, what):
    use textbox(who, what, "images/textbox/center_4long.png",
        frame_pos=(197, 312),
        window_pos=(198, 365),
        window_size=window_size_center4long,
        text_size=text_size_center4long,
        text_kerning=gui.kerning_dialogue - 1,
        style_prefix_name="center_4long",
        appear_effect=appear_textbox
    )




############################
# Default 'say' screen
############################
screen say(who, what):
    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"



############################
# Styles
############################


style say_dialogue:
    properties gui.text_properties("dialogue")
    color "#583F34"
    outlines [(1.2, "#fff", 0, 0)]
    font gui.preference("font", default="msgothic.ttf")
    size gui.text_size
    kerning gui.kerning_dialogue
    line_spacing gui.line_spacing
    adjust_spacing False
    line_overlap_split -5

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label

style window:
    xalign 0
    yalign 0
    xsize 700
    ysize 130

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.0
    yalign 0.5




## Dialogue Config ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.




## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue1_xpos = 20
define gui.dialogue1_ypos = 40

## The maximum width of dialogue text, in pixels.
define gui.dialogue1_xalign = 0.0








## NVL screen ##################################################################


screen nvl(dialogue, items=None):

    window at window_transform:
        style "nvl_window"

        vbox:
            spacing 31

            use nvl_dialogue(dialogue)

            ## Displays the menu, if given
            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"



screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


define config.nvl_list_length = 6
define config.nvl_page_ctc = "ctc_button"

# The style for the NVL "textbox"
style nvl_window:
    is default
    xsize gui.nvl_width
    padding (32, 61, 0, 70)

define ruby_text_size = 14
define ruby_kern_size = 2

style ruby_style is default: 
    size ruby_text_size
    kerning ruby_kern_size
    yoffset -35
    color None


define transp = Color((0, 0, 0, 0))

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    size gui.nvl_text_size
    kerning gui.kerning_dialogue + 4
    color "#fff"
    outlines [(2, "#2E3A54", 0, 0)]
    font gui.preference("font", default="msgothic.ttf")
    line_spacing gui.line_spacing +4
    #min_width 885
    ruby_style style.ruby_style




style nvl_button:
    xpos 675
    xanchor 0.0

## NVL-Mode Config ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
# define gui.nvl_borders = Borders(0, 8, 0, 15)

# ## The maximum number of NVL-mode entries Ren'Py will display. When more entries
# ## than this are to be show, the oldest entry will be removed.
# define gui.nvl_list_length = 6

# ## The height of an NVL-mode entry. Set this to None to have the entries
# ## dynamically adjust height.
# define gui.nvl_height = 81

# ## The spacing between NVL-mode entries when gui.nvl_height is None, and between
# ## NVL-mode entries and an NVL-mode menu.
# define gui.nvl_spacing = 8

# ## The position, width, and alignment of the label giving the name of the
# ## speaking character.
# define gui.nvl_name_xpos = 303
# define gui.nvl_name_ypos = 0
# define gui.nvl_name_width = 106
# define gui.nvl_name_xalign = 1.0

# ## The position, width, and alignment of the dialogue text.
# define gui.nvl_text_xpos = 317
# define gui.nvl_text_ypos = 6
# define gui.nvl_text_width = 415
# define gui.nvl_text_xalign = 0.0

# ## The position, width, and alignment of nvl_thought text (the text said by the
# ## nvl_narrator character.)
# define gui.nvl_thought_xpos = 169
# define gui.nvl_thought_ypos = 0
# define gui.nvl_thought_width = 549
# define gui.nvl_thought_xalign = 0.0

# ## The position of nvl menu_buttons.
# define gui.nvl_button_xpos = 317
# define gui.nvl_button_xalign = 0.0
