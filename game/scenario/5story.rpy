

label story5:
    stop music
    scene bg exterior9 at pan_to_top
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第五話　イギリスの怖い話。{/size}" id story5_54b9aadf

    show white screen onlayer bottom

    scene bg classroom_window at pan_to_top
    play music "music/16_mr_music_box_theme.ogg"
    pause 0.2
    show england large ello at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    with Dissolve(0.25)
    story "お前たち喜べ！\nやっとお待ちかねの俺の話が聞けるぞ。\nちゃんと幽霊も出てくるしな。" id story5_8d00cedc
    nvl clear
    show england large cocky
    story "そう、突然にだ…。" id story5_9bbdc960
    nvl clear


    show bg classroom2 at pan_to_bottom1 behind nvl_textbox
    show england large frown
    story "あの日はフランスが押し付けてきた\n謎のきのこの調理法に頭を抱えていた。" id story5_c078f8b7
    show england large blush shout
    with {'master': Dissolve(0.2)}
    story "冷蔵庫に放置しようものなら\n\n「あっ、ごめんごめーん。\n　今度はもっと料理初心者にも\n　優しい高級食材持ってくるからー\n　調理器具もー。子供用のほしいー？」" id story5_7c1520e6
    story "なんて満面のしたり顔で\n行ってくるに違いない…！" id story5_6a3cf795
    nvl clear

    show england large heheheh2
    story "しかし俺だって言われてばかりじゃない。\n　\nどんな食材もミンチにして\nクリームと混ぜて、パイに包めば\nだいたい美味しくなるということを\n俺は知っているからだ…！" id story5_f45868f5
    show england large wanker
    with {'master': Dissolve(0.2)}
    story "はっ、昔のままだと\n高を括ってるフランスのやつに\n俺の料理さばきを\n見せてやりたかったな！" id story5_35e88f2c
    nvl clear
    
    show england large ello
    story "フランスの食材さえ\n自在にアレンジできる程度には\n上達してるってわけだ。\n　\nさらには余ったパイ生地で\n星を見るパイまで作るくらい\n時間と食材にも優しいんだぞ。" id story5_14c20671
    story "\nお前らもそろそろ\n俺に対する認識を改める時期に\n来てるんじゃないか？" id story5_19b7bd1f
    nvl clear
    
    show england large mmm
    story "だが俺が料理の腕を振るっていた\nまさにあの瞬間。" id story5_cf4ddedf
    story "\nあれは突然やってきた…！" id story5_47e598fd
    nvl clear

    show england large frown
    story "俺がパイが焼きあがるまでの時間を利用して\n前日の残りのウナギゼリーに\nオーストラリアが俺の家のポストに\n２７日に１回のペースで\n突っ込んでくるペジマイトを\n塗りつけていた時だった…。" id story5_835ced99
    stop music fadeout 2
    
    show bulgaria conniving at pos_transform(xpos=300, yalign=0.0) behind england
    with {'master': Dissolve(0.25)} 
    story "（メニューのせいで\n　話に集中できねぇ…）" id story5_d50a0986
    nvl clear

    scene black
    with Dissolve(0.25)
    story "そこに…{nw=1}" id story5_d6bb6989
    nvl clear

    scene bg classroom1
    with Dissolve(0.25)

    show england blush shout at pos_transform(xpos=200, yalign=0.0)
    $ eng.screen = 'center_3long'
    
    $ _pending_camera_transform = [([shake_5s1], "master"), ([shake_5s1], "screens")]
    $ _pending_sound = ("sfx/gun09.ogg", "sound")
    eng "知らないゴーストが\nいたんだ…！" id story5_d971867a

    $ _pending_camera_transform = None
    stop sound

    show america yell sweat at pos_transform(xpos=400, yalign=0.0) behind england
    $ ame.screen = 'right_3'
    $ _pending_window_transform = (shake_5s2)
    $ _pending_sound = ("sfx/gun09_r.ogg", "sound")
    ame "ゴ…ゴーストが…っ\n君の目の前に…っ！？\nなんて恐ろしいんだっ！" id story5_492388cf


    stop sound

    show bulgaria conniving at pos_transform(xpos=0, yoffset=1.0) behind england
    $ bul.screen='left_1'
    $ _pending_window_transform = (shake_2s6)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    bul "幽霊唐突すぎる！" id story5_274d4766

    stop sound

    show england heheheh2
    $ eng.screen = 'center_1'
    eng "怖いのはここからだ。" id story5_343eeea9

    show england cocky
    $ eng.screen = 'center_4long'
    eng "俺の家では幽霊も住民票で\n管理されていて誰がどこにいるのか\nほとんど把握できる。" id story5_e84aa9f3

    show england angry shout
    
    $ eng.screen = 'center_3'
    eng "だが知らない\n幽霊が家にいた。\nこれはつまり…！" id story5_ca05b6a5
    stop music fadeout 3.0
    play sound "sfx/run_wait.ogg"
    pause 0.5

    scene bg classroom_door
    play sound2 ["<silence .5>", "sfx/doorheavy.ogg"]
    play music "music/KidsTrax653_KC07-MuppetsOnTheTitanic-Julin.ogg"
    pause 0.5
    play sound1 ["<silence .2>", "sfx/ding27.ogg"]
    show spain smiling:
        xpos 420 yalign 0.0
        time .2
        easeout 0.15 yoffset -40
        ease 0.15 yoffset 10
        easeout 0.15 yoffset -30
        ease 0.15 yoffset 0
        easeout 0.15 yoffset -5
        ease 0.15 yoffset 0

    pause 1
    $ spa.screen = 'right_4'
    spa "遅れてごめんなー。\nみんなの分\nチュロス作ってきたさかい\n許したってなぁ。" id story5_098fcbd0
    stop sound

    show england scream at pos_transform(xpos=300, yalign=0.0)
    $ eng.screen = 'center_1'
    $ _pending_window_transform = (shake_5s3)
    $ _pending_sound = ("sfx/hit40_b.ogg", "sound")
    eng "…かっ……！" id story5_cc5962b4
    stop sound

    show spain worried at pos_transform(xpos=420, yalign=0.0)
    $ spa.screen = 'right_3'
    spa "あ！かんにん。\n邪魔してもうた？" id story5_775802c5

    show england blush shout
    $ eng.screen = 'center_3'
    eng "邪魔も邪魔だっ！！\n俺の話の一番盛り上がる所で\n入ってくるなバカっ！！" id story5_66145a49

    show spain ahaha
    $ spa.screen = 'right_1'
    spa "かんにん☆" id story5_7e2ea414

    show england sweat blush whatthehell
    $ eng.screen = 'center_3'
    eng "ぐぎぎぎぎぎぎ…！！\nスペイン貴様…！" id story5_a9d08782

    show bulgaria ooh at pos_transform(xpos=100, yoffset=1.0) behind spain
    $ bul.screen='left_3'
    
    bul "あっ別にあとで\n文章にするから\n全然大丈夫っすよ。" id story5_94cee313

    show england blush shout3
    $ eng.screen = 'center_4long'
    eng "俺のプライドの問題だ！\n後日、お前のところに行って\nもう一度最初から最後まで\n聞かせてやる！" id story5_dc9f3461

    show bulgaria whatisthat:
        pause 0.5
        easein 0.5 xpos 700
    pause 1
    $ bul.screen='right_4'
    $ _pending_window_transform = (shake_5s4)
    $ _pending_sprite_transform = [("bulgaria", [shake_5s4, bul_5s])]
    bul "あっこういう時は\n語尾ににゃんってつけると\n何でも許してもらえる\nらしいっすよ。" id story5_ffdbc5f6
    
    $ _pending_sprite_transform = [("spain smiling", pos_transform(xpos=420, yalign=0.0), Dissolve(0.2))]
    show spain oh
    $ spa.screen = 'right_3'
    spa "そうなん？\nごめんにゃんやでー。" id story5_67d9ca09

    show england blush shout:
        pause 0.5
        easein 0.5 xpos 100
    pause 1
    $ eng.screen = 'center_3'

    $ _pending_window_transform = (shake_5s5)
    $ _pending_sound = ("sfx/ding61.ogg", "sound")
    eng "ムカつくから\nやめろ！！" id story5_7c8ffea7
    stop sound

    show spain isee
    show england sweat oh
    show america large eksdee at pos_transform(xpos=350, ypos=400)
    show america:
        pause 0.5
        easein 0.3 ypos 0
        easein 0.25 ypos 100
    pause 1
    $ ame.screen = 'left_4'
    $ _pending_sprite_transform = [("america", [shake_5s5, ame_5s])]
    $ _pending_window_transform = (shake_5s5)
    $ _pending_sound = ("sfx/ding27.ogg", "sound")
    ame "Ｇｒｅａｔ！\nチュロス！\nチュロスじゃないか！\n俺は君に会いたかった！" id story5_e134b004
    $ _pending_window_transform = None

    stop sound
    stop music fadeout 3

    jump story6