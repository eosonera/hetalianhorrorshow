
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        has vbox

        hbox:
            box_wrap True

            if renpy.variant("pc") or renpy.variant("web"):
                # Only need fullscreen/windowed on desktop and web builds

                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window"):
                        # Ensures this button is selected when
                        # not in fullscreen.
                        selected not preferences.fullscreen
                        action Preference("display", "window")
                    textbutton _("Fullscreen"):
                        action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                label _("Skip")
                textbutton _("Unseen Text"):
                    action Preference("skip", "toggle")
                textbutton _("After Choices"):
                    action Preference("after choices", "toggle")
                textbutton _("Transitions"):
                    action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        null height (4 * gui.pref_spacing)



### PREF
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 159

## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    is pref_label_text

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (35, 6, 6, 6)

## CHECK
style check_label:
    is pref_label
style check_label_text:
    is pref_label_text

style check_vbox:
    is pref_vbox
    spacing 0

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
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


## Volume popup ################################################################
##
## 
##
## 
## 

screen volume_popup():

    tag menu
    use game_menu(_("Preferences"))
    style_prefix "volume_popup"
    add "gui/music.png":
        xpos 270
        ypos 123

    frame:
        style "volume_popup_frame"
        xpos 300
        ypos 200
        xsize 300
        ysize 120

        hbox:
            spacing 30
            vbox:
                spacing 25
                xsize 100
                text _("BGM")
                text _("SFX")
                text _("Dialogue")
            vbox:
                #style_prefix "volume_popup_slider"
                spacing 25
                bar value Preference("music volume")
                bar value Preference("sfx volume")
                bar value Preference("voice volume")

    textbutton _("Return"):
        action Return()
        xpos 580
        ypos 350
        
style volume_popup_text:
    size 16
    xalign 1.0

style volume_popup_slider:
    ysize 13
    xsize 155
    right_bar Frame("gui/slider/volume_bar_empty.png", tile=gui.slider_tile)
    left_bar Frame("gui/slider/volume_bar_full.png", tile=gui.slider_tile)
    thumb_offset 30
    thumb "gui/slider/thumb_0.png"
    hover_thumb "thumb_hover_anim"

        
    

## Text speed popup ################################################################
##


screen text_speed_popup():
    tag menu
    modal True
    use game_menu(_("Preferences"))

    style_prefix "text_speed"
    add "gui/slider/speed.png":
        xpos 270
        ypos 162
    frame:
        style "text_speed_slider"
        xpos 300
        ypos 174
        xsize 300
        ysize 120

        vbox:
            bar value Preference("text speed")

    textbutton _("Return"):
        action Return()
        xpos 450
        ypos 220

style text_speed_slider:
    ysize 11
    xsize 153
    base_bar Frame("gui/slider/bar.png", tile=gui.slider_tile)
    thumb "gui/slider/slider_0.png"
    thumb_offset 22
    hover_thumb "slider_hover_anim"
    bar_invert True


## Auto text speed popup ################################################################
##


screen autotext_speed_popup():
    tag menu
    modal True
    use game_menu(_("Preferences"))

    style_prefix "text_speed"
    add "gui/slider/speed.png":
        xpos 270
        ypos 212
    frame:
        style "text_speed_slider"
        xpos 300
        ypos 230
        xsize 300
        ysize 120

        vbox:
            bar value Preference("auto-forward time")

    textbutton _("Return"):
        action Return()
        xpos 450
        ypos 270
