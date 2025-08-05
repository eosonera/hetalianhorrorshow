    
    
    
default list_languages = [
    ("日本語", None),
    ("English", "english"),
]

define config.enable_language_autodetect = True

## Language screen #################################################################

screen language():
    tag menu
    modal True
    use game_menu2(_("Language"))

    style_prefix "language"

    add "gui/bg font.png":
        xpos 251
        ypos 86

    viewport:
        xpos 323
        ypos 167
        xsize 330
        ysize 200
        mousewheel True draggable True pagekeys True
        scrollbars "vertical" yinitial 1.0

        frame:
            vbox:
                spacing 0
                for name, code in list_languages:
                    textbutton ("[name]"):
                        action Language(code)
                        

style language_button_text is gui_text

style language_button is radio_button
style language_button_text:
    color "#42352D"
    hover_color '#5e422b'
    size 20
    xalign 1.0
style about_vscrollbar is font_popup_vscrollbar
style language_vscrollbar:
    unscrollable gui.unscrollable
