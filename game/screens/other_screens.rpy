
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.


screen about():
    tag menu
    
    use game_menu2(_("About"))

    add "gui/menu_game/backlog.png":
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

        
            


style hyperlink_text:
    color "#b1fff3"

style about1_label:
    xsize 150

style about1_label_text is about1_text
style about1_text is history_text


style about_label_text is about_text:
    size 20
style about_text:
    color "#42352D"
    size 14


style about_vscrollbar is history_vscrollbar
style about_vscrollbar:
    unscrollable "hide"



## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"
    modal False

    use game_menu2(_("Help"))

    add "gui/menu_game/backlog2.png":
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


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text ("")


init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)