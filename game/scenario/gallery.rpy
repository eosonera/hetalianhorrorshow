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
        text_size=gal_text_size,
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
    what_outlines = [(1.2, "#2E3E59", 0, 0)],
    ctc="ctc_button",
    ctc_position="nestled")

label gallery:

    if persistent.game_finished:
        play music "music/9_townscape.ogg" fadeout 1
        
        scene bg exterior1 at pan_to_top
        
        with fade_white

        window show
        
        $ gal.screen = 'gallery_textbox'
        gal "ダウンロードとプレイありがとうございます！\n楽しんでいただければ幸せです。" id gallery_840ee7e0
        show aphrodite 0 at aphro1
        with {'master': Dissolve(1.0)}
        show jeremy 0 at jeremy1
        with {'master': Dissolve(1.0)}
        show bear_grylls 0 at bear1
        with {'master': Dissolve(1.0)}
        pause 1.5
        gal "おまけ\n目隠しなしのア○ロダイテ・ジョーンズ\nベ○グリルスとジェレ○ーウェイド。" id gallery_e2430e66
        
        $ _skip_appear_effect = True
        scene japansan rain
        with {'master': Dissolve(0.5)}
        
        gal "おまけ画像。あめにほんさん。\n元の画像は結構明るい。" id gallery_7f7c0376
        
        scene sweden
        with {'master': Dissolve(0.5)}

        $ gal.screen = 'gallery_textbox'
        gal "スウェーデン。" id gallery_4ead79be
        $ _skip_appear_effect = False
        window auto
        
        
    else:
        stop music fadeout 1
        scene bg exterior6

        $ gal.screen = 'gallery_textbox'
        gal "クリアーすると解放されます。" id gallery_b94bc3f3
        
    return
