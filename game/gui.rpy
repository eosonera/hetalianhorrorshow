################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(900, 600)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True
define config.log = "log.txt"




define gui.text_size = 20
define gui.kerning_dialogue = 4
define gui.line_spacing = 10
define narr_text_size = (610, 200)
define gal_text_size = 16

define gui.choice_button_text = 20

define gui.nvl_text_size = gui.text_size + 2
define gui.nvl_width = 900
define gui.nvl_window_1_width = gui.nvl_width
define gui.nvl_width2 = gui.nvl_width

define text_size_narr = gui.text_size + 2
define text_size_right1 = gui.text_size
define text_size_right3 = gui.text_size
define text_size_right4 = gui.text_size
define text_size_right4long = gui.text_size
define text_size_right7big = gui.text_size
define text_size_left1 = gui.text_size
define text_size_left3 = gui.text_size
define text_size_left4 = gui.text_size - 1
define text_size_left4long = gui.text_size - 1
define text_size_center1 = gui.text_size
define text_size_center3 = gui.text_size - 1
define text_size_center3long = gui.text_size
define text_size_center4long = gui.text_size - 3


define narr_window_size = (700, 200)
define window_size_right1 = (300, 130)
define window_size_right3 = (375, 130)
define window_size_right4 = (350, 130)
define window_size_right4long = (480, 130)
define window_size_right7big =(490, 130)
define window_size_left1 = (280, 130)
define window_size_left3 = (350, 130)
define window_size_left4 = (380, 130)
define window_size_left4long = (480, 130)
define window_size_center1 = (420, 130)
define window_size_center3 = (340, 130)
define window_size_center3long = (480, 130)
define window_size_center4long = (480, 150)


################################################################################
## GUI Configuration Variables
################################################################################

default _game_menu_screen = "menu_open"

## Colors ######################################################################

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#583F34'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#583F34'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#583F34'

define gui.hover_color = '#583F34'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#8888887f'


## The colors used for dialogue and menu choice text.
define gui.text_color = '#583F34'
define gui.interface_text_color = '#583F34'


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "msgothic.ttf"

# translate japanese python:
#     gui.text_font = "SourceHanSans-Light.otf"


## The font used for out-of-game text.
define gui.interface_text_font = "msgothic.ttf"


## The size of character names.
define gui.name_text_size = 9

## The size of text in the game's user interface.
define gui.interface_text_size = 16

## The size of labels in the game's user interface.
define gui.label_text_size = 17




## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(3, 3, 3, 3)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(13, 3, 3, 3)

define gui.check_button_borders = Borders(13, 3, 3, 3)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(8, 3, 8, 3)

define gui.quick_button_borders = Borders(8, 3, 8, 0)
define gui.quick_button_text_size = 10

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(3, 3, 3, 3)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(29, 29, 29, 29)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(12, 4, 36, 4)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(12, 4, 29, 4)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 18
define gui.scrollbar_size = 9
define gui.slider_size = 18

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(3, 3, 3, 3)
define gui.scrollbar_borders = Borders(3, 3, 3, 3)
define gui.slider_borders = Borders(3, 3, 3, 3)

## Vertical borders.
define gui.vbar_borders = Borders(3, 3, 3, 3)
define gui.vscrollbar_borders = Borders(3, 3, 3, 3)
define gui.vslider_borders = Borders(3, 3, 3, 3)




## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at 
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "japanese-strict"


################################################################################
## Mobile devices
################################################################################

# init python:

#     ## This increases the size of the quick buttons to make them easier to touch
#     ## on tablets and phones.
#     @gui.variant
#     def touch():

#         gui.quick_button_borders = Borders(30, 10, 30, 0)

#     ## This changes the size and spacing of various GUI elements to ensure they
#     ## are easily visible on phones.
#     @gui.variant
#     def small():

#         ## Font sizes.
#         gui.text_size = 20
#         gui.name_text_size = 26
#         gui.notify_text_size = 18
#         gui.interface_text_size = 22
#         gui.button_text_size = 22
#         gui.label_text_size = 24

#         ## Adjust the location of the textbox.
#         gui.textbox_height = 169
#         gui.name_xpos = 57
#         gui.dialogue_xpos = 64
#         gui.dialogue_width = 774

#         ## Change the size and spacing of various things.
#         gui.slider_size = 26

#         gui.choice_button_width = 872
#         gui.choice_button_text_size = 22

#         gui.navigation_spacing = 15
#         gui.pref_button_spacing = 8

#         gui.history_height = 134
#         gui.history_text_width = 486

#         gui.quick_button_text_size = 15


#         ## NVL-mode.
#         gui.nvl_height = 120

#         gui.nvl_name_width = 215
#         gui.nvl_name_xpos = 229

#         gui.nvl_text_width = 644
#         gui.nvl_text_xpos = 243
#         gui.nvl_text_ypos = 4

#         gui.nvl_thought_width = 872
#         gui.nvl_thought_xpos = 15

#         gui.nvl_button_width = 872
#         gui.nvl_button_xpos = 15
