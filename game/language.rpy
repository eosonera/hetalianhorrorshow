## Language config ######################################################################

define config.enable_language_autodetect = True
    
default list_languages = [
    ("日本語", None),
    ("English", "english"),
    ("Русский", "russian"),
]




translate english python:
    gui.text_size = 14
    
    gui.choice_button_text = 16

    gui.nvl_text_size = 18
    gui.nvl_width = 680
    gui.nvl_width2 = gui.nvl_width - 200
    gal_text_size = 14

    

## NVL
define story_indent = Character(None,
    kind = nvl,
    window_style="nvl_window1",
    #what_prefix="  ",
    ctc="ctc_button",
    ctc_position="nestled",)

define story_short = Character(None,
    kind = nvl,
    window_style="nvl_window2",
    ctc="ctc_button",
    ctc_position="nestled",)

style nvl_window1:
    is default
    xsize gui.nvl_width
    padding (20, -31, 0, -31) #left, top, right, bottom

style nvl_window2:
    is default
    xsize gui.nvl_width2


## Names for history screen
translate english python:
    name_map = {
        "bulgaria": ("Bulgaria"),
        "romania": ("Romania"),
        "england": ("England"),
        "japan": ("Japan"),
        "germany": ("Germany"),
        "finland": ("Finland"),
        "america": ("America"),
        "spain": ("Spain"),
        "russia": ("Russia"),
    }

## Text sizes
translate english python:
    text_size_narr = gui.text_size + 2
    text_size_right1 = gui.text_size
    text_size_right3 = gui.text_size
    text_size_right4 = gui.text_size
    text_size_right4long = gui.text_size
    text_size_right7big = gui.text_size
    text_size_left1 = gui.text_size
    text_size_left3 = gui.text_size
    text_size_left4 = gui.text_size
    text_size_left4long = gui.text_size
    text_size_center1 = gui.text_size
    text_size_center3 = gui.text_size
    text_size_center3long = gui.text_size
    text_size_center4long = gui.text_size


## Textbox sizes (width,height)
translate english python:
    narr_window_size = (490, 200)
    window_size_right1 = (300, 130)
    window_size_right3 = (310, 130)
    window_size_right4 = (280, 100)
    window_size_right4long = (420, 150)
    window_size_right7big =(280, 100)
    window_size_left1 = (280, 130)
    window_size_left3 = (320, 130)
    window_size_left4 = (340, 130)
    window_size_left4long = (480, 150)
    window_size_center1 = (420, 130)
    window_size_center3 = (310, 130)
    window_size_center3long = (470, 130)
    window_size_center4long = (480, 150)




translate russian python:
    name_map = {
        "bulgaria": ("Болгария"),
        "romania": ("Румыния"),
        "england": ("Англия"),
        "japan": ("Япония"),
        "germany": ("Германия"),
        "finland": ("Финляндия"),
        "america": ("Америка"),
        "spain": ("Испания"),
        "russia": ("Россия"),
    }


## Text sizes
translate russian python:
    text_size_narr = gui.text_size + 2
    text_size_right1 = gui.text_size
    text_size_right3 = gui.text_size
    text_size_right4 = gui.text_size
    text_size_right4long = gui.text_size
    text_size_right7big = gui.text_size
    text_size_left1 = gui.text_size
    text_size_left3 = gui.text_size
    text_size_left4 = gui.text_size - 1
    text_size_left4long = gui.text_size - 1
    text_size_center1 = gui.text_size
    text_size_center3 = gui.text_size
    text_size_center3long = gui.text_size
    text_size_center4long = gui.text_size - 1


## Textbox sizes
translate russian python:
    narr_window_size = (750, 200)
    window_size_right1 = (300, 130)
    window_size_right3 = (375, 130)
    window_size_right4 = (350, 130)
    window_size_right4long = (480, 130)
    window_size_right7big =(490, 130)
    window_size_left1 = (280, 130)
    window_size_left3 = (350, 130)
    window_size_left4 = (470, 130)
    window_size_left4long = (480, 130)
    window_size_center1 = (420, 130)
    window_size_center3 = (340, 130)
    window_size_center3long = (480, 130)
    window_size_center4long = (480, 150)

translate russian python:
    gui.text_size = 12
    
    gui.choice_button_text = 16

    gui.nvl_text_size = 18
    gui.nvl_width = 680
    gui.nvl_width2 = gui.nvl_width - 200
    gal_text_size = 14


    """
narr_window_size = (700, 200)
window_size_right1 = (300, 130)
window_size_right3 = (375, 130)
window_size_right4 = (350, 130)
window_size_right4long = (480, 130)
window_size_right7big =(490, 130)
window_size_left1 = (280, 130)
window_size_left3 = (350, 130)
window_size_left4 = (380, 130)
window_size_left4long = (480, 130)
window_size_center1 = (420, 130)
window_size_center3 = (340, 130)
window_size_center3long = (480, 130)
window_size_center4long = (480, 150)
"""