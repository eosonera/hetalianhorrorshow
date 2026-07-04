## Misc menu open screen ################################################################

screen menu_open2():
    tag menu
    modal True
    
    use game_menu2(_("Menu")):
        style_prefix "open"

#################################################################################
## Misc Menu screen #############################################################
#################################################################################

screen game_menu2(title):
    style_prefix "game_menu2"

    add "gui/menu_game/bg_game_menu2.png"
    add "gui/menu_game/menu_flower.png"

    if main_menu:
        key "mousedown_3" action Return()

    vbox:
        style_prefix "gm"
        xalign 1.0
        yalign 0.0
        text "hetascanlations\n[config.name!t] remake\nversion [config.version]"

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
            action ShowMenu("preferences")

    

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
        


style game_menu2_vscrollbar:
    unscrollable "hide"

style gm_text is gui_text
style gm_text:
    size 9
    color "#fff"
    text_align 1.0


#################################################################################
## About screen ################################################################
#################################################################################

screen about():
    tag menu
    
    use game_menu2(("About"))

    add "gui/menu_game/about.png":
        xpos 138
        ypos 109
    
    add "gui/scrollbar/log_1.png":
        xpos 681
        ypos 196

    if renpy.variant("mobile"):
        imagebutton:
            xalign 1.0
            yalign 0
            idle "gui/button/return.png"
            action ShowMenu("menu_open2")

    style_prefix "about"
    controller_viewport:
        xpos 227
        ypos 202
        xsize 450
        ysize 230
        mousewheel True draggable renpy.variant("touch") pagekeys True
        id "about_viewport" vscroll_style "nudge"
        scroll_delay (0.2, 0.2)
        extra_scroll dict(up=-100, down=100)
        trap_focus ("up", "down", "left", "right")
        scrollbars "vertical" yinitial 0.0
        which_stick "both"
        focus_scroll True

        vbox:
            spacing 10
            label _("[config.name!t] remake")
            text _("バージョン [config.version!t]")
            text _("hetascanlationsチームによる『The Hetalian Horror Show』の完全ファンリメイクおよび翻訳版。")
            null height 10
            
            vbox:
                spacing 10
                label _("リメイク版クレジット")
                hbox:
                    style_prefix "about1"
                    label ("{a=https://eosonera.tumblr.com/}eosonera{/a}")
                    text _("制作")
                hbox:
                    style_prefix "about1"
                    label ("{a=http://spaghettifelice.tumblr.com/}spaghetti{/a}")
                    text _("英語訳")
                null height 5
                hbox:
                    style_prefix "about1"
                    label ("{a=https://www.tumblr.com/sunflowerpieivan}sunflowerpieivan{/a}")
                    text _("ロシア語訳")
                hbox:
                    style_prefix "about1"
                    label ("{a=http://y4nderenka.livejournal.com/profile}renka{/a}")
                    text _("以前の英語訳")  
            

                null height 10

                label _("Ren'Pyコード")

                hbox:
                    style_prefix "about1"
                    label ("Badmustard")
                    text ("Ren'Py save game names")
                hbox:
                    style_prefix "about1"
                    label ("Feniksdev")
                    text ("Marquee for Ren'Py, Controller Support")

                null height 10

                label _("特別な感謝")

                vbox:
                    style_prefix "about1"
                    spacing 5
                    label ("donamoeba")
                    label ("jammerlea")
                    label ("lysandre")
                    label ("Em")
                    label ("nekotalia")
                    null height 10
                    label ("yunyomal")
                    label ("mosaku")
                    

    text _("{a=https://ja.renpy.org/}Ren'Py{/a} を使用して作成 [renpy.version_only].\n\n[renpy.license!t]"):
        style_prefix "renpyabout"
        xalign 0.0
        yalign 1.0
        xsize 350

    vbar value YScrollValue("about_viewport") style "about_vscrollbar":
        xpos 673
        ypos 202

        
            


style hyperlink_text:
    color "#b1fff3"

style about1_label:
    xsize 150

style about1_label_text is history_text

style about1_text:
    color "#583F34"
    textalign 0.0
    size 16

style renpyabout_text:
    size 12
    color "#fff"
    outlines [(1.2, "#597a87", 0, 0)]


style about_label_text is about_text:
    size 20
style about_text:
    color "#583F34"
    size 14


style about_vscrollbar is history_vscrollbar
style about_vscrollbar:
    unscrollable "hide"


#################################################################################
## Misc Options ################################################################
#################################################################################


screen preferences():

    tag menu

    use game_menu2(("Preferences"))

    if renpy.variant("mobile"):
        imagebutton:
            xalign 1.0
            yalign 0
            idle "gui/button/return.png"
            action ShowMenu("menu_open2")

    add "gui/menu_game/about.png":
        xpos 138
        ypos 109

    style_prefix "pref2"
    viewport:
        xpos 230
        ypos 200
        xsize 520
        ysize 250

        mousewheel False draggable False pagekeys False
        #scrollbars "vertical"
        has vbox
        spacing 12

        hbox:
            box_wrap True
            spacing 5
            
            if renpy.variant("pc") or renpy.variant("web"):
                vbox:
                    spacing 10
                    xsize 220

                    vbox:
                        label _("ディスプレイ")
                        null height 10
                        hbox:
                            spacing 3
                            add "gui/button/check_0.png":
                                ypos -3
                                alpha (1.0 if _preferences.fullscreen == False else 0.0)
                            textbutton _("ウィンドウ"):
                                # Ensures this button is selected when not in fullscreen.
                                selected not preferences.fullscreen
                                action Preference("display", "window")
                        hbox:
                            spacing 3
                            add "gui/button/check_0.png":
                                ypos -3
                                alpha (1.0 if _preferences.fullscreen == True else 0.0)
                            textbutton _("フルスクリーン"):
                                action Preference("display", "fullscreen")

                
                    vbox:
                        label _("セーブメモ")
                        null height 10
                        hbox:
                            spacing 10
                            hbox:
                                spacing 3
                                add "gui/button/check_0.png":
                                    ypos -3
                                    alpha (1.0 if persistent.saveName == True else 0.0)
                                textbutton _("On"):
                                    action [SetVariable("persistent.saveName", True)]
                            hbox:
                                spacing 3
                                add "gui/button/check_0.png":
                                    ypos -3
                                    alpha (1.0 if persistent.saveName == False else 0.0)
                                textbutton _("Off"):
                                    action [SetVariable("persistent.saveName", False)]

                    vbox:
                        label _("セーブプレビュー")
                        null height 10
                        hbox:
                            spacing 10
                            hbox:
                                spacing 3
                                add "gui/button/check_0.png":
                                    ypos -3
                                    alpha (1.0 if persistent.savePreview == True else 0.0)
                                textbutton _("On"):
                                    action [SetVariable("persistent.savePreview", True)]
                            hbox:
                                spacing 3
                                add "gui/button/check_0.png":
                                    ypos -3
                                    alpha (1.0 if persistent.savePreview == False else 0.0)
                                textbutton _("Off"):
                                    action [SetVariable("persistent.savePreview", False)]

            vbox:
                spacing 10
                xsize 220
                vbox:
                    label _("未読スキップ")
                    null height 10
                    hbox:
                        spacing 10
                        hbox:
                            spacing 3
                            add "gui/button/check_0.png":
                                ypos -3
                                alpha (1.0 if _preferences.skip_unseen == True else 0.0)
                            textbutton _("On"):
                                action Preference("skip", "all")
                        hbox:
                            spacing 3
                            add "gui/button/check_0.png":
                                ypos -3
                                alpha (1.0 if _preferences.skip_unseen == False else 0.0)
                            textbutton _("Off"):
                                action Preference("skip", "seen")

                vbox:
                    label _("選択肢のスキップ続行")
                    null height 10
                    hbox:
                        spacing 10
                        hbox:
                            spacing 3
                            add "gui/button/check_0.png":
                                ypos -3
                                alpha (1.0 if _preferences.skip_after_choices == True else 0.0)
                            textbutton _("On"):
                                action Preference("after choices", "skip")
                        hbox:
                            spacing 3
                            add "gui/button/check_0.png":
                                ypos -3
                                alpha (1.0 if _preferences.skip_after_choices == False else 0.0)
                            textbutton _("Off"):
                                action Preference("after choices", "stop")


    frame:
        xalign 0.0
        yalign 1.0
        #xfill True
        vbox:
            spacing 10
            textbutton _("セーブデータを削除"):
                action Confirm(_("セーブデータを削除しますか？"),
                Function(delete_all_saves), no=None)
                style "remover_button"
            textbutton _("保持データを削除"):
                action Confirm(_("保持データを削除しますか？\nデフォルトの設定値に復元して、この操作は元に戻せません。"),
                Function(persistent._clear, progress=True), no=None)
                style "remover_button"


define remover_button_text_size = 20

style pref2_label_text:
    size 16

style remover_button_text:
    color "#ff0000"
    size remover_button_text_size
    hover_color "#000"
    outlines [(1.2, "#fff", 0, 0)]


style pref2_button_text:
    color "#583F34"
    hover_color '#A0684A'
    yalign 0.5


#style pref2_vscrollbar is history_vscrollbar





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
    hover_color '#A0684A'

style help_vscrollbar is history_vscrollbar
style help_vscrollbar:
    unscrollable "hide"





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
            scrollbars "vertical" yinitial 0

            frame:
                vbox:
                    spacing 0
                    for name, code in list_languages:
                        textbutton ("[name]"):
                            action [Language(code)]#, Function(renpy.restart_interaction)]
                        

style language_button_text is gui_text

style language_button is radio_button
style language_button_text:
    color "#583F34"
    hover_color '#A0684A'
    size 20
    xalign 1.0
style language_vscrollbar is font_vscrollbar
style language_vscrollbar:
    unscrollable "hide"

