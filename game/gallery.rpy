## Gallery ############################################################
##
##
##
##

define gal = Character(None,
    window_background="textbox_gush.png",
    window_xalign=0,
    window_yalign=0,
    window_xsize=700,
    what_xpos=162,
    what_ypos=468,
    ctc="ctc_button",
    ctc_position="nestled")

label gallery:

    if persistent.game_finished:
        play music "9_townscape.ogg" fadeout 1
        scene bg exterior1

        gal "ダウンロードとプレイありがとうございます！\n楽しんでいただければ幸せです。"

        show aphrodite 0
        show jeremy 0 
        show bear_grylls 0
        gal "おまけ\n目隠しなしのア○ロダイテ・ジョーンズ\nベ○グリルスとジェレ○ーウェイド。"
        hide aphrodite 0
        hide jeremy 0 
        hide bear_grylls 0

        show japansan rain
        gal "おまけ画像。あめにほんさん。\n元の画像は結構明るい。"
        
        show sweden
        gal "スウェーデン。"
        
        
    else:
        stop music fadeout 1
        scene bg exterior6
        gal "クリアーすると解放されます。"
        
    return
