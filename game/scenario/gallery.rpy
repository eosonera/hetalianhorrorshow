## Gallery ############################################################
##
##
##
##

#define gallery_font_size = say_dialogue_size - 5

define gal = Character(None,
    window_background="textbox/normal.png",
    what_xpos=162,
    what_ypos=468,
    what_size = 16,
    what_color = "#fff",
    what_outlines = [(1.2, "#67787C", 0, 0)],
    what_line_spacing = 10,
    ctc="ctc_button",
    ctc_position="nestled")

label gallery:

    if persistent.game_finished:
        play music "9_townscape.ogg" fadeout 1
        
        scene bg exterior1 at pan_to_top
        
        with fade_white

        window show
        gal "ダウンロードとプレイありがとうございます！\n楽しんでいただければ幸せです。"
        show aphrodite 0 at aphro1
        with {'master': Dissolve(1.0)}
        show jeremy 0 at jeremy1
        with {'master': Dissolve(1.0)}
        show bear_grylls 0 at bear1
        with {'master': Dissolve(1.0)}
        pause 1.5
        gal "おまけ\n目隠しなしのア○ロダイテ・ジョーンズ\nベ○グリルスとジェレ○ーウェイド。"
        window auto

        scene japansan rain
        with dissolve
        gal "おまけ画像。あめにほんさん。\n元の画像は結構明るい。"
        
        scene sweden
        with dissolve
        gal "スウェーデン。"
        
        
    else:
        stop music fadeout 1
        scene bg exterior6
        show dust2 at dust2_transform
        gal "クリアーすると解放されます。"
        
    return
