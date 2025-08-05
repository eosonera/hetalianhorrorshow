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


################################################################################
## GUI Configuration Variables
################################################################################

default _game_menu_screen = "menu_open"

## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#5B4A40'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#42352D'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#aaaaaa'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#5e422b'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#5B4A40'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#8888887f'


## The colors used for dialogue and menu choice text.
define gui.text_color = '#42352D'
define gui.interface_text_color = '#42352D'


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = gui.preference("font", default="msgothic.ttc")

# translate japanese python:
#     gui.text_font = "SourceHanSans-Light.otf"

# translate japanese style default:
#     language "japanese-strict"
 

## The font used for character names.
define gui.name_text_font = "msgothic.ttc"

## The font used for out-of-game text.
define gui.interface_text_font = "msgothic.ttc"

## The size of normal dialogue text.
define gui.text_size = 16

## The size of character names.
define gui.name_text_size = 22

## The size of text in the game's user interface.
define gui.interface_text_size = 16

## The size of labels in the game's user interface.
define gui.label_text_size = 17

## The size of text on the notify screen.
define gui.notify_text_size = 12

## The size of the game's title.
define gui.title_text_size = 36


## Main and Game Menus #########################################################

## The images used for the main and game menus.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"




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
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 556
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(71, 4, 71, 4)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.

define gui.slot_button_borders = Borders(8, 8, 8, 8)
define gui.slot_button_text_size = 10
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color



## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 29

## The vertical position of the skip indicator.
define gui.skip_ypos = 8

## The vertical position of the notify screen.
define gui.notify_ypos = 32

## The spacing between menu choices.
define gui.choice_spacing = 16

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 3

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 8

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0


## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


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

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"



## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at 
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(30, 10, 30, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 20
        gui.name_text_size = 26
        gui.notify_text_size = 18
        gui.interface_text_size = 22
        gui.button_text_size = 22
        gui.label_text_size = 24

        ## Adjust the location of the textbox.
        gui.textbox_height = 169
        gui.name_xpos = 57
        gui.dialogue_xpos = 64
        gui.dialogue_width = 774

        ## Change the size and spacing of various things.
        gui.slider_size = 26

        gui.choice_button_width = 872
        gui.choice_button_text_size = 22

        gui.navigation_spacing = 15
        gui.pref_button_spacing = 8

        gui.history_height = 134
        gui.history_text_width = 486

        gui.quick_button_text_size = 15


        ## NVL-mode.
        gui.nvl_height = 120

        gui.nvl_name_width = 215
        gui.nvl_name_xpos = 229

        gui.nvl_text_width = 644
        gui.nvl_text_xpos = 243
        gui.nvl_text_ypos = 4

        gui.nvl_thought_width = 872
        gui.nvl_thought_xpos = 15

        gui.nvl_button_width = 872
        gui.nvl_button_xpos = 15
