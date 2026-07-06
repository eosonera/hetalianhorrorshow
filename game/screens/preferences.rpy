
## Preferences  ##########################################################


#################################################################################
## Volume ################################################################
#################################################################################

init python:
    renpy.music.register_channel("sound1", mixer= "sfx", loop=False)
    renpy.music.register_channel("sound2", mixer= "sfx", loop=False)

    renpy.music.register_channel("music1", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)


    def linear_volume_display(mixer):
        raw = preferences.get_volume(mixer)
        if raw <= 0.0:
            return 0
        import math
        slider = math.log10(raw) / 2 + 1
        return int(slider * 100)


    def audio_crossFade(fadeTime, music):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = "music"
            newChannel = "music1"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
            oldChannel = "music1"
            newChannel = "music"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = None
            newChannel = "music"
            
        if oldChannel is not None:
            renpy.music.stop(channel= oldChannel, fadeout=fadeTime)
            
        if newChannel is not None:
            renpy.music.play(music, channel=newChannel, loop=None,fadein=fadeTime)


screen volume():

    #tag menu
    #modal True
    #use game_menu(_("Volume"))
    
    
    add "gui/menu_game/music.png":
        xpos 270
        ypos 123

    style_prefix "volume"
    frame:
        xpos 338
        ypos 198
        xsize 284
        ysize 120

        vbox:
            xalign 0.0
            style "volume_text"
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
            text (_("Mute") if music_volume == 0 else _("MAX") if music_volume == 100 else str(music_volume))
            text (_("Mute") if sfx_volume == 0 else _("MAX") if sfx_volume == 100 else str(sfx_volume))
            text (_("Mute") if voice_volume == 0 else _("MAX") if voice_volume == 100 else str(voice_volume))

        vbox:
            xoffset 65
            yoffset -9
            spacing 5
            bar value Preference("music volume")
            bar value Preference("sfx volume")
            bar value Preference("voice volume")
                    
                    

style volume_text:
    size 16
    xalign 1.0


style volume_slider:
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

default preferences.text_cps = 40

screen text_speed():
    #tag menu
    #modal True
    #use game_menu(_("Text Speed"))

    style_prefix "text_speed"
    add "gui/slider/speed.png":
        xpos 270
        ypos 162
    frame:
        style "text_speed_slider"
        xpos 315
        ypos 166
        bar value Preference("text speed") range (0, 80)

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


screen autotext_speed():
    #tag menu
    #modal True
    #use game_menu(_("Autotext Speed"))

    style_prefix "autotext_speed"
    add "gui/slider/speed.png":
        xpos 270
        ypos 212
    frame:
        style "autotext_speed_slider"
        xpos 315
        ypos 217
        bar value Preference("auto-forward time")

style autotext_speed_slider:
    xsize 115
    ysize 50
    left_bar Frame("gui/slider/bar_1.png", tile=None)
    right_bar Frame("gui/slider/bar_0.png", tile=None)
    thumb_offset 0
    thumb "gui/slider/slider_0.png"
    hover_thumb "gui/slider/slider_1.png"
    bar_invert False

#################################################################################
## Font popup ################################################################
#################################################################################


screen font():
    #tag menu
    #modal True
    #use game_menu(_("Font"))

    style_prefix "font"

    add "gui/menu_game/font.png":
        xpos 272
        ypos 101

    add "gui/scrollbar/scrollbar.png":
        xpos 599
        ypos 187

    default list_fonts = [
        (("IBMPlexSans"), "IBMPlexSans.ttf"),
        (_("MS Pゴシック"), "mspgothic.ttf"),
        (_("MS ゴシック"), "msgothic.ttf"),
        
        (_("BIZ UD明朝 Medium"), "BIZ-UDMinchoM.ttf"),
        (_("BIZ UDゴシック"), "BIZ-UDGothicR.ttf"),
        (_("BIZ UDP明朝 Medium"), "BIZ-UDPMinchoM.ttf"),
        (_("BIZ UDPゴシック"), "BIZ-UDPGothicR.ttf"),
        (_("メイリオ"), "meiryo.ttf"),
        (("Meiryo UI"), "meiryoui.ttf"),
        (("MS UI Gothic"), "msuigothic.ttf"),

        (_("UD デジタル 教科書体 N-B"), "UDDigiKyokashoN-B.ttf"), # monospace bold
        (_("UD デジタル 教科書体 NK-B"), "UDDigiKyokashoNK-B.ttf"), #alphanumeric characters and kana are proportionally spaced, bold
        (_("UD デジタル 教科書体 NK-R"), "UDDigiKyokashoNK-R.ttf"), #alphanumeric characters and kana are proportionally spaced, regular
        (_("UD デジタル 教科書体 NP-B"), "UDDigiKyokashoNP-B.ttf"), #alphanumeric characters are proportionally spaced, bold
        (_("UD デジタル 教科書体 NP-R"), "UDDigiKyokashoNP-R.ttf"), #alphanumeric characters are proportionally spaced, regular
        (_("UD デジタル 教科書体 N-R"), "UDDigiKyokashoN-R.ttf"), #monospace regular


        (_("游ゴシック"), "YuGoth.ttf"),
        (_("游ゴシック Light"), "YuGothL.ttf"),
        (_("游ゴシック Medium"), "YuGothM.ttf"),
        (_("Yu Gothic UI"), "YuGothUI.ttf"),
        (_("Yu Gothic UI Light"), "YuGothUIL.ttf"),
        (("Yu Gothic UI Semibold"), "YuGothUISemibold.ttf"),
        (_("Yu Gothic UI Semilight"), "YuGothUISemilight.ttf"),
    ]

    default list_fonts_jp = [
        "UDDigiKyokashoN-B.ttf",
        "UDDigiKyokashoNK-B.ttf",
        "UDDigiKyokashoNK-R.ttf",
        "UDDigiKyokashoN-R.ttf",
    ]

    controller_viewport:
        xpos 337
        ypos 183
        xsize 284
        ysize 202
        mousewheel True draggable renpy.variant("touch") pagekeys True
        id "my_viewport" vscroll_style "nudge"
        scroll_delay (0.2, 0.2)
        extra_scroll dict(up=-100, down=100)
        trap_focus ("up", "down", "left", "right")
        scrollbars "vertical" yinitial 0

        frame:
            has vbox
            spacing -10
            for name, file in list_fonts:
                if file in list_fonts_jp and _preferences.language != "None":
                    continue
                hbox:
                    add "gui/button/check_0.png":
                        ypos -3
                        alpha (1.0 if gui.preference("font") == file else 0.0)
                    textbutton ("[name!t]"):
                        style "font_button"
                        action gui.SetPreference("font", file)
                        
    vbar value YScrollValue("my_viewport") style 'font_vscrollbar' keyboard_focus False:
        xpos 596
        ypos 188

style font_button
    #properties gui.button_properties("radio_button")
    #selected_foreground "gui/button/check_2.png"
    #padding (35, 0, 0, 0)
    #yalign 0.5
    

style font_button_text:
    color "#583F34"
    hover_color "#A0684A" 
    size 16
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