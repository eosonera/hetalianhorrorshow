## Localization ################################################################


define gui.language = "unicode"
    
default list_languages = [
    ("日本語", None),
    ("English", "english"),
    ("Русский", "russian"),
]


## Language config ######################################################################



## NVL
define story_indent = Character(None,
    kind = nvl,
    window_style="nvl_window1",
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
    #define gui.language = "unicode"
    memo_text_size = 12
    remover_button_text_size = 20
    chars_in_savename = 26
    gui.text_size = 14
    gui.choice_button_text = 16
    gui.nvl_text_size = 18
    gui.nvl_width = 600
    gui.nvl_width2 = gui.nvl_width - 200
    gal_text_size = 14
    confirm_prompt_text_kerning = -1
    gui.kerning_dialogue = 1
    gui.kerning_narrator = -2
    gui.kerning_nvl = -5



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
    window_size_left3 = (300, 130)
    window_size_left4 = (340, 130)
    window_size_left4long = (420, 150)
    window_size_center1 = (420, 130)
    window_size_center3 = (280, 130)
    window_size_center3long = (420, 130)
    window_size_center4long = (385, 150)


## Names for history screen
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
    #define gui.language = "unicode"
    memo_text_size = 12
    remover_button_text_size = 14
    chars_in_savename = 26
    gui.text_size = 14
    gui.choice_button_text = 16
    gui.nvl_text_size = 18
    gui.nvl_width = 600
    gui.nvl_width2 = gui.nvl_width - 200
    gal_text_size = 14
    confirm_prompt_text_kerning = -1
    gui.kerning_dialogue = 0
    gui.kerning_narrator = -2
    gui.kerning_nvl = -5
    

translate russian python:
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


## Textbox sizes
translate russian python:
    narr_window_size = (490, 200)
    window_size_right1 = (300, 130)
    window_size_right3 = (310, 130)
    window_size_right4 = (280, 100)
    window_size_right4long = (420, 150)
    window_size_right7big =(280, 100)
    window_size_left1 = (280, 130)
    window_size_left3 = (300, 130)
    window_size_left4 = (340, 130)
    window_size_left4long = (460, 150)
    window_size_center1 = (420, 130)
    window_size_center3 = (280, 130)
    window_size_center3long = (435, 130)
    window_size_center4long = (385, 150)

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

old russian
    narr_window_size = (700, 200)
    window_size_right1 = (300, 130)
    window_size_right3 = (450, 130)
    window_size_right4 = (380, 100)
    window_size_right4long = (500, 150)
    window_size_right7big =(320, 100)
    window_size_left1 = (280, 130)
    window_size_left3 = (380, 130)
    window_size_left4 = (400, 130)
    window_size_left4long = (500, 150)
    window_size_center1 = (420, 130)
    window_size_center3 = (300, 130)
    window_size_center3long = (435, 130)
    window_size_center4long = (450, 150)

"""



init -1 python:
    def my_language_fallback(locale, region):
        
        if locale == "ja":
            return None
            
        elif locale == "ru":
            return "russian"
            
        #elif locale == "es":
            #return "spanish"
            
        return "english" 


    config.locale_to_language_function = my_language_fallback
    config.enable_language_autodetect = True