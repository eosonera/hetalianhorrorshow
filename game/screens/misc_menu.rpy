#################################################################################
## Language screen ##############################################################
#################################################################################

screen language():

    modal True

    style_prefix "language"

    if renpy.variant("mobile"):
        imagebutton:
            xalign 1.0
            yalign 0
            idle "gui/button/return.png"
            action ShowMenu("menu_open2")

    add "gui/menu_game/font.png":
        xpos 251
        ypos 86

    button:
        if main_menu:
            action Hide("language")
        else:
            action Return()
        background None
        xysize (900, 600)
        focus_mask None

    frame:
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
    color "#583F34"
    hover_color '#5e422b'
    size 20
    xalign 1.0
style about_vscrollbar is font_vscrollbar
style language_vscrollbar:
    unscrollable "hide"



translate english python:
    gui.kerning_dialogue = 0
    gui.kerning_narrator = 0



#################################################################################
## Misc Options ################################################################
#################################################################################

if renpy.variant("mobile"):
    default persistent.saveName = False
else:
    default persistent.saveName = True

screen preferences():

    tag menu

    use game_menu2(_("Preferences"))

    if renpy.variant("mobile"):
        imagebutton:
            xalign 1.0
            yalign 0
            idle "gui/button/return.png"
            action ShowMenu("menu_open2")

    add "gui/menu_game/about.png":
        xpos 138
        ypos 109

    viewport:
        xpos 230
        ypos 202
        xsize 468
        ysize 232

        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        has vbox

        hbox:
            box_wrap True
            spacing 10

            if renpy.variant("pc") or renpy.variant("web"):
                # Only need fullscreen/windowed on desktop and web builds

                vbox:
                    spacing 10
                    style_prefix "radio"
                    label _("ディスプレイ")
                    textbutton _("ウィンドウ"):
                        # Ensures this button is selected when
                        # not in fullscreen.
                        selected not preferences.fullscreen
                        action Preference("display", "window")
                    textbutton _("フルスクリーン"):
                        action Preference("display", "fullscreen")

            vbox:
                spacing 0
                style_prefix "check"
                #label _("スキップ")
                textbutton _("未読テキストもスキップ"):
                    action Preference("skip", "toggle")
                textbutton _("選択肢の後もスキップ継続"):
                    action Preference("after choices", "toggle")
                #textbutton _("トランジションもスキップ"):
                    #action InvertSelected(Preference("transitions", "toggle"))
            
            if renpy.variant("pc") or renpy.variant("web"):
                vbox:
                    style_prefix "radio"
                    label _("Save game names")
                    textbutton _("Yes") action [SetVariable("persistent.saveName", True)]
                    textbutton _("No") action [SetVariable("persistent.saveName", False)]

        style_prefix "remover"
        null height 50
        textbutton ("DELETE ALL SAVE DATA"):
            action Confirm(_("全てのセーブデータを消去しますか？"), Function(delete_all_saves), no=None)

style remover_button_text:
    color "#ff0000"
    size 20
    hover_color "#000"
    outlines [(1.2, "#fff", 0, 0)]


#################################################################################
## About screen ################################################################
#################################################################################

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.


screen about():
    tag menu
    
    use game_menu2(_("About"))

    add "gui/menu_game/about.png":
        xpos 138
        ypos 109
    
    add "gui/scrollbar/log_1.png":
        xpos 684
        ypos 201

    if renpy.variant("mobile"):
        imagebutton:
            xalign 1.0
            yalign 0
            idle "gui/button/return.png"
            action ShowMenu("menu_open2")

    style_prefix "about"
    viewport:
        xpos 227
        ypos 202
        xsize 462
        ysize 230
        mousewheel True draggable True pagekeys True
        scrollbars "vertical" yinitial 1.0


        vbox:
            spacing 10
            label _("[config.name!t] remake")
            text _("バージョン [config.version!t]")
            text _("Full fan remake and translation of The Hetalian Horror Show by the hetascanlations team.")
            null height 10
            
            vbox:
                spacing 10
                label _("クレジット")
                hbox:
                    style_prefix "about1"
                    label _("制作")
                    text ("{a=https://eosonera.tumblr.com/}eosonera{/a}")
                hbox:
                    style_prefix "about1"
                    label _("English translation")
                    text ("{a=https://eosonera.tumblr.com/}spaghetti{/a}")

        
            


style hyperlink_text:
    color "#b1fff3"

style about1_label:
    xsize 150

style about1_label_text is about1_text
style about1_text is history_text


style about_label_text is about_text:
    size 20
style about_text:
    color "#583F34"
    size 14


style about_vscrollbar is history_vscrollbar
style about_vscrollbar:
    unscrollable "hide"


#################################################################################
## Help screen #################################################################
#################################################################################

screen help():

    tag menu

    default device = "keyboard"
    modal False

    use game_menu2(_("Help"))

    add "gui/menu_game/about.png":
        xpos 138
        ypos 109

    frame:
        hbox:
            ypos 140
            xalign 0.56
            spacing 20
            
            style_prefix "help1"
            textbutton _("キーボード") action SetScreenVariable("device", "keyboard")
            textbutton _("マウス") action SetScreenVariable("device", "mouse")

            if GamepadExists():
                textbutton _("ゲームパッド") action SetScreenVariable("device", "gamepad")
                
        viewport:
            xalign 0.65
            ypos 200
            xsize 500
            ysize 250
            mousewheel True draggable True pagekeys True
            scrollbars "vertical"
            style_prefix "help"

            vbox:
                xalign 0.5
                spacing 10

                if device == "keyboard":
                    use keyboard_help
                elif device == "mouse":
                    use mouse_help
                elif device == "gamepad":
                    use gamepad_help


screen keyboard_help():

    hbox:
        label _("エンター")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("スペース")
        text _("台詞を読み進める。ただしボタンは選択しない。")

    hbox:
        label _("方向キー")
        text _("インターフェースを移動する。")

    hbox:
        label _("ESC")
        text _("ゲームメニューを開く。")

    hbox:
        label _("Ctrl")
        text _("押し続けている間スキップする。")

    hbox:
        label _("Tab")
        text _("スキップモードに切り替える。")

    hbox:
        label _("Page Up")
        text _("前の台詞に戻る。")

    hbox:
        label _("Page Down")
        text _("ロールバック中、次の台詞に進む。")

    hbox:
        label "H"
        text _("インターフェースを隠す。")

    hbox:
        label "S"
        text _("スクリーンショットを撮る。")


screen mouse_help():

    hbox:
        label _("左クリック")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("中クリック")
        text _("インターフェースを隠す。")

    hbox:
        label _("右クリック")
        text _("ゲームメニューを開く。")

    hbox:
        label _("マウスホイール上回転")
        text _("前の台詞に戻る。")

    hbox:
        label _("マウスホイール下回転")
        text _("ロールバック中、次の台詞に進む。")


screen gamepad_help():

    hbox:
        label _("Ｒトリガー\nＡ／下ボタン")
        text _("台詞を読み進める。またはボタンを選択する。")

    hbox:
        label _("Ｌトリガー\nＬボタン")
        text _("前の台詞に戻る。")

    hbox:
        label _("Ｒボタン")
        text _("ロールバック中、次の台詞に進む。")

    hbox:
        label _("方向パッド\n左右スティック")
        text _("インターフェースを移動する。")

    hbox:
        label _("スタート、ガイド、 B / Right ボタン")
        text _("ゲームメニューを開く。")

    hbox:
        label _("Ｙ／上ボタン")
        text _("インターフェースを隠す。")

    textbutton _("キャリブレート"):
        xalign 1.0
        style_prefix "help1"
        action GamepadCalibrate()


style help1_button is confirm_button
style help1_button_text is confirm_button_text
style help1_button_text:
    xsize 400

style help_text:
    size 12

style help_label:
    xsize 130

style help_label_text:
    size 12
    xalign 0
    textalign 0

style help_button_text:
    hover_color '#5e422b'

style help_vscrollbar is history_vscrollbar
style help_vscrollbar:
    unscrollable "hide"


## Misc menu open screen ################################################################

screen menu_open2():
    tag menu
    use game_menu2(_("Menu")):
        style_prefix "open"

#################################################################################
## Misc Menu screen #############################################################
#################################################################################

screen game_menu2(title):
    style_prefix "game_menu2"

    add "gui/menu_game/bg_game_menu2.png"
    add "gui/menu_game/menu_flower.png"

    frame:

        imagebutton:
            xpos 50
            ypos 160
            idle "gui/menu_game/menu_05.png"
            if not renpy.variant("mobile"):
                at menu_jump
            action ShowMenu("about")

        imagebutton:
            xpos 50
            ypos 216
            idle "gui/menu_game/menu_06.png"
            if not renpy.variant("mobile"):
                at menu_jump
            action Show("preferences")

    

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            imagebutton:
                xpos 50
                ypos 272
                idle "gui/menu_game/menu_07.png"
                at menu_jump
                action ShowMenu("help")

        imagebutton:
            xpos 700
            ypos 432
            idle "gui/menu_game/5mainmenu.png"
            if not renpy.variant("mobile"):
                at menu_hover_float
            if main_menu:
                action Return()
            else:
                action MainMenu(confirm=True, save=False)

        if renpy.variant("mobile") and not main_menu:
            imagebutton:
                xalign 1.0
                yalign 0
                idle "gui/button/return.png"
                action Return()
        
        text _("Made with {a=https://ja.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"):
            xalign 0.0
            yalign 1.0
            xsize 350
            

style game_menu2_text:
    size 12
    color "#fff"
    outlines [(1.2, "#597a87", 0, 0)]


style game_menu2_vscrollbar:
    unscrollable "hide"