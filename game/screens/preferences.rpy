
## Preferences  ##########################################################


#################################################################################
## Volume ################################################################
#################################################################################

init python:
    renpy.music.register_channel("sound1", mixer= "sfx", loop=False)
    renpy.music.register_channel("sound2", mixer= "sfx", loop=False)

    def linear_volume_display(mixer):
        raw = preferences.get_volume(mixer)
        if raw <= 0.0:
            return 0
        import math
        slider = math.log10(raw) / 2 + 1
        return int(slider * 100)


screen volume_popup():

    tag menu
    modal True
    use game_menu(_("Volume"))
    
    
    add "gui/menu_game/music.png":
        xpos 270
        ypos 123

    style_prefix "volume_popup"
    frame:
        xpos 338
        ypos 198
        xsize 284
        ysize 120

        vbox:
            xalign 0.0
            style "volume_popup_text"
            spacing 25
            text _("BGM")
            text _("効果音")
            text _("セリフ")
            
        vbox:
            xalign 1.0
            spacing 25
            xsize 32
            $ music_volume = linear_volume_display("music")
            $ sfx_volume = linear_volume_display("sfx")
            $ voice_volume = linear_volume_display("voice")
            text ("Mute" if music_volume == 0 else "MAX" if music_volume == 100 else str(music_volume))
            text ("Mute" if sfx_volume == 0 else "MAX" if sfx_volume == 100 else str(sfx_volume))
            text ("Mute" if voice_volume == 0 else "MAX" if voice_volume == 100 else str(voice_volume))

        vbox:
            xoffset 65
            yoffset -9
            spacing 5
            bar value Preference("music volume")
            bar value Preference("sfx volume")
            bar value Preference("voice volume")
                    
                    

style volume_popup_text:
    size 16
    xalign 1.0


style volume_popup_slider:
    ysize 36
    xsize 154
    right_bar Frame("gui/slider/volume_bar_empty.png", tile=None)
    left_bar Frame("gui/slider/volume_bar_full.png", tile=None)
    thumb_offset 15
    thumb "gui/slider/thumb_0.png"
    hover_thumb "gui/slider/thumb_1.png"

        
#################################################################################
## Text speed popup ################################################################
#################################################################################

screen text_speed_popup():
    tag menu
    modal True
    use game_menu(_("Text Speed"))

    style_prefix "text_speed"
    add "gui/slider/speed.png":
        xpos 270
        ypos 162
    frame:
        style "text_speed_slider"
        xpos 315
        ypos 166
        bar value Preference("text speed")

style text_speed_slider:
    xsize 115
    ysize 50
    left_bar Frame("gui/slider/bar_1.png", tile=None)
    right_bar Frame("gui/slider/bar_0.png", tile=None)
    thumb_offset 0
    thumb "gui/slider/slider_0.png"
    hover_thumb "gui/slider/slider_1.png"
    bar_invert True

#################################################################################
## Auto text speed popup ################################################################
#################################################################################


screen autotext_speed_popup():
    tag menu
    modal True
    use game_menu(_("Autotext Speed"))

    style_prefix "text_speed"
    add "gui/slider/speed.png":
        xpos 270
        ypos 212
    frame:
        style "text_speed_slider"
        xpos 315
        ypos 217
        bar value Preference("auto-forward time")

#################################################################################
## Font popup ################################################################
#################################################################################


screen font():
    tag menu
    modal True
    use game_menu(_("Font"))

    style_prefix "font"

    add "gui/menu_game/font.png":
        xpos 251
        ypos 86

    add "gui/scrollbar/scrollbar.png":
        xpos 578
        ypos 172

    default list_fonts = [
        ("IBMPlexSans", "IBMPlexSans.ttf"),
        (_("MS ゴシック"), "msgothic.ttc"),
        (_("Source Han Sans Lite"), "SourceHanSans-Light.otf")
        # (_("BIZ UD明朝 Medium"), "msgothic.ttc"),
        # (_("BIZ UDゴシック"), "msgothic.ttc"),
        # (_("BIZ UDP明朝 Medium"), "msgothic.ttc"),
        # (_("メイリオ"), "msgothic.ttc"),
        # (_("Malgun Gothic Semilight"), "msgothic.ttc"),
        # (_("Meiryo UI"), "msgothic.ttc"),
        # (_("MS UI Gothic"), "msgothic.ttc"),
        # (_("Noto Sans JP"), "msgothic.ttc"),
        # (_("Noto Sans JP Black"), "msgothic.ttc"),
        # (_("Noto Sans JP Demilight"), "msgothic.ttc"),
        # (_("Noto Sans JP Light"), "msgothic.ttc"),
        # (_("Noto Sans JP Medium"), "msgothic.ttc"),
        # (_("Noto Sans JP Thin"), "msgothic.ttc"),
        # (_("UD デジタル 教科書体 N-B"), "msgothic.ttc")
    ]

    viewport:
        xpos 324
        ypos 168
        xsize 276
        ysize 202
        mousewheel True draggable True pagekeys True
        scrollbars "vertical" yinitial 1.0

        frame:
            vbox:
                spacing 0
                ysize 28
                for name, file in list_fonts:
                    textbutton ("[name]"):
                        action gui.SetPreference("font", file)

style font_button is radio_button

style font_button:
    padding (35, 0, 0, 0)
    

style font_button_text:
    color "#42352D"
    size 14
    xalign 1.0

style font_vscrollbar:
    xsize 25
    ysize 105
    yoffset 45
    thumb_offset 15
    thumb "gui/scrollbar/scrollbar_thumb.png"



        


## Styles ###################




### PREF
style pref_label:
    top_margin 8
    bottom_margin 2

style pref_label_text:
    yalign 1.0
    color "#597a87"


## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    is pref_label_text

style radio_vbox:
    spacing 0

style radio_button:
    properties gui.button_properties("radio_button")
    selected_foreground "gui/button/check_0.png"
    padding (35, 0, 0, 0)

## CHECK
style check_label:
    is pref_label
style check_label_text:
    is pref_label_text

style check_vbox:
    is pref_vbox
    spacing 0

style check_button:
    selected_foreground "gui/button/check_0.png"
    padding (35, 6, 6, 6)

style check_button_text:
    properties gui.text_properties("check_button")

## SLIDER
style slider_label:
    is pref_label
style slider_label_text:
    is pref_label_text

style slider_slider:
    xsize 247

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 8

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 317