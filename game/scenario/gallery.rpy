## Gallery ############################################################
##
##
##
##

#define gallery_font_size = say_dialogue_size - 5

screen gallery_textbox(who, what):
    use textbox(who, what, "images/textbox/normal.png",
        window_pos=(162, 468),
        window_size=(570, 300),
        text_size=gui.text_size - 4,
        style_prefix_name="gallery",
        appear_effect=appear_gallery
    )


transform appear_gallery:
    yoffset 40 alpha 0.4
    linear 0.25:
        alpha 1.0 yoffset 0


define gal = Character(None,
    window_background="textbox/normal.png",
    what_color = "#fff",
    what_outlines = [(1.2, "#67787C", 0, 0)],
    ctc="ctc_button",
    ctc_position="nestled")

label gallery:

    if persistent.game_finished:
        play music "music/9_townscape.ogg" fadeout 1
        
        scene bg exterior1 at pan_to_top
        
        with fade_white

        window show
        
        $ gal.screen = 'gallery_textbox'
        gal "ダウンロードとプレイありがとうございます！\n楽しんでいただければ幸せです。"
        show aphrodite 0 at aphro1
        with {'master': Dissolve(1.0)}
        show jeremy 0 at jeremy1
        with {'master': Dissolve(1.0)}
        show bear_grylls 0 at bear1
        with {'master': Dissolve(1.0)}
        pause 1.5
        gal "おまけ\n目隠しなしのア○ロダイテ・ジョーンズ\nベ○グリルスとジェレ○ーウェイド。"
        
        $ _skip_appear_effect = True
        scene japansan rain
        with {'master': Dissolve(0.5)}
        
        gal "おまけ画像。あめにほんさん。\n元の画像は結構明るい。"
        
        scene sweden
        with {'master': Dissolve(0.5)}

        $ gal.screen = 'gallery_textbox'
        gal "スウェーデン。"
        $ _skip_appear_effect = False
        window auto
        
        
    else:
        stop music fadeout 1
        scene bg exterior6
        show dust2 at dust2_transform
        $ gal.screen = 'gallery_textbox'
        gal "クリアーすると解放されます。"
        
    return
