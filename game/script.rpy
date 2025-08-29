
 
## Start ############################################################


default persistent.game_finished = False

label start:
    scene white screen
    with blur_fade
    play music "music/9_townscape.ogg" 

    scene bg romania_room


    na "「７カ国が集まる国際怖い話会合があるから\n　そこで話を聞いてきてくれないかなー？」\n{vspace=12}{space=155}その一言でそれは始まった。" id start_8479585a

    scene bg romania_room3
    with fade_white

    show bulgaria ooh at pos_transform(xpos=440, yalign=0.0)
    
    $ bul.screen = 'right_1'
    bul "えっ俺が？" id start_d72426f3

    show romania normal at pos_transform(xpos=70, yalign=0.0) behind bulgaria
    
    $ rom.screen = 'left_3'
    rom "ごめんね～。\nほんとはおいらが\nやりたかったんだけどさー。" id start_4d123f7b
    show romania worried at pos_transform(xpos=70, yalign=0.0)
    
    $ rom.screen = 'left_4'
    rom "{size=-2}魔術部のイギ…\nほにゃららさんに{size=-5}ごほごほっ{/size}\nいつやるんだって\nせっつかれてるしー…。{/size}" id start_f8af57b9
    show romania cry uuu
    rom "{size=-2}でも…その、上司に、お前\nそんな事してる暇ないだろって\n言われちゃってー…。{/size}" id start_fe490979

    show bulgaria mm
    $ bul.screen = 'right_4'
    bul"いやそれ俺もだけどね。\n俺も遊ぶ暇あったら\n内職しろって\n言われてるんだわー。" id start_6074a98b

    show romania whatsthaat
    rom "そうだったの！？\nでもお前いっつも\nフラフラしてるじゃんかー！" id start_8f7e5e1b

    $ bul.screen = 'right_3'
    show bulgaria forreal
    bul "ふざけんなー！\n自分で行けオラァ！" id start_fe5ba20e

    show romania cry nyaa
    $ rom.screen = 'left_4'
    rom "なんて友だち甲斐が\nないんだよー！頼むよー！\n頼める人がいないんだよー" id start_d6cfb26b

    show bulgaria conniving
    $ bul.screen = 'right_1'
    bul "ロシアさんは？" id start_c66e6f28

    show romania scared
    $ rom.screen = 'left_3'
    rom "え！？ えーと…。\nロシアさんは{size=-5}存在自体がー…\n怖いっていうか…。{/size}" id start_028db6fd

    show bulgaria yeahyeah
    $ bul.screen = 'right_3'
    bul "そこら辺は\n…否定はしないわー" id start_4a9432bb

    show romania cry nyaa
    $ rom.screen = 'left_3'
    
    $ window_transform = shake_0p1
    rom "お願いだよー！！\nお菓子あげるから！" id start_c71f0dd7
    $ window_transform = None

    show bulgaria conniving
    $ bul.screen = 'right_3'
    bul "お菓子でつられる\n年じゃねーんだわー" id start_bc7df12d

    show romania what
    $ rom.screen = 'left_1'
    rom "ブルガリア今年何歳？" id start_b3b001cd

    show bulgaria heheh
    $ bul.screen = 'right_3'
    bul "んー ま、\nかれこれ…３？" id start_1fcc0816

    show romania ooh
    rom "３００じゃないよね?" id start_3d397b61

    show bulgaria conniving
    $ bul.screen = 'right_1'
    bul "んーん♪" id start_59e783b8

    show romania eh
    $ rom.screen = 'left_1'
    rom "３０００？" id start_d37301ef

    show bulgaria ello
    $ window_transform = shake_0p1
    $ bul.screen = 'right_1'
    bul "もう一声ぇっ！" id start_239fc5ac
    $ window_transform = None

    show romania whatsthaat
    rom "３万！？ ないよー！" id start_6b148d73

    show bulgaria heheh
    play sound ["<silence .8>", "sfx/gun14_c.ogg"]
    $ bul.screen = 'right_3'
    show bulgaria heheh:
        0.8
        block:
            linear 0.1 xoffset -8 yoffset -8
            linear 0.1 xoffset +8 yoffset +8
            repeat 2
        linear 0.1 xoffset 0 yoffset 0
    $ window_transform = shake_0p2
    bul "俺三万歳！！\nつまり俺の国力は\n３万あるんだわー！" id start_97b31921
    $ window_transform = None
    
    
    show bulgaria heheh at pos_transform(xpos=440, yalign=0.0)
    show romania angry yell
    play sound ["<silence .4>", "sfx/bang07.ogg"]
    show romania angry yell:
        0.7
        linear 0.1 xoffset +8 yoffset +8
        linear 0.1 xoffset -8 yoffset -8
        linear 0.1 xoffset -8 yoffset +8
        linear 0.1 xoffset +8 yoffset -8
        linear 0.1 xoffset 0 yoffset 0
    $ rom.screen = 'left_1'
    $ window_transform = shake_0p3
    rom "こいつ盛ったぁー！！" id start_e5a62779
    $ window_transform = None

    show romania at pos_transform(xpos=70, yalign=0.0)
    show bulgaria ello
    
    $ bul.screen = 'right_3'
    bul "盛ってねーから！\nそういうわけで俺の方が\n年上だから俺はいかない！" id start_300040ae

    show romania whatsthaat
    $ rom.screen = 'left_4long'
    rom "やーだー！その理屈わかんないよー\n頼むよー！行ってよー！\nいらとお前の付き合いだろー！！" id start_c62956d7

    show bulgaria conniving eyesclosed
    play sound ["<silence .5>", "sfx/BUBBLY.WAV"]
    show bulgaria heheh:
        0.5
        block:
            parallel:
                ease 0.6 xoffset -150
                ease 0.6 xoffset +150
            parallel:
                ease 0.3 yoffset 0
                ease 0.3 yoffset -15
                ease 0.3 yoffset 0
                ease 0.3 yoffset -15
            repeat
    $ bul.screen = 'right_3'
    bul "ぷぷぷぷ～\nぷんにょにょ～（鼻歌）" id start_091ebbd4
    
    show romania holdon
    play sound "sfx/ding74.ogg"
    $ rom.screen = 'left_4long'
    rom "やだー変な歌うたいながら\nおいらの周りまわらないでー。\nやめてよー" id start_5ef33473

    play sound "sfx/Disintergrate.wav"
    $ bul.screen = 'right_3'
    bul "ふんごっ\nふんごっ（鼻歌）" id start_76f6ac0e

    show romania waaahh
    $ rom.screen = 'left_1'
    rom "わーんわーん！！" id start_fcb03828

    $ rom.screen = 'left_4'
    rom "どうすればいいんだよぅこれー。" id start_7c634a5e
    $ _skip_appear_effect = True
    show romania whattheheck
    with {'master': dissolve}
    $ window_transform = shake_0p4
    extend "\n…あっ！そうだ！\nこの仕事すると…目立てるよ！" id start_6f8a9988
    $ window_transform = None
    $ _skip_appear_effect = False

    show bulgaria whatisthat at stop_offset
    with move
    show bulgaria whatisthat at pos_transform(xpos=440, yalign=0.0)
    
    
    $ bul.screen = 'right_1'
    bul "何！！？" id start_63665121

    show romania heynoow
    $ rom.screen = 'left_4long'
    rom"他のみんなと対等な目線で\n話せるよー！" id start_028c8b01

    show bulgaria ooh
    $ bul.screen = 'right_3'
    bul "つまり…\nどういうことだ？" id start_c0e5473b

    show romania sup
    $ rom.screen = 'left_4long'
    rom "だから！司会進行として！\nいつもは上からにゃーにゃー\n言ってくるみんなをブルガリアが\n先導できるってこと！！" id start_ebbafdad

    show romania sigh eyesclosed
    $ rom.screen = 'left_4long'
    rom "思い出してよ\nおいらたちの近代…" id start_15292df2

    stop music fadeout 1
    show bulgaria sweat
    $ bul.screen = 'right_1'    
    bul"俺たちの近代…" id start_d9ee66bd

    hide bulgaria
    hide romania
    scene black
    with fade

    $ na2.screen = 'right_3'
    na2"またブルガリアと\nルーマニアか…。" id start_70786b2a

    $ na2.screen = 'left_4long'
    na2"この二国って加入してから\n足引っ張ってるだけですよね。\nだから反対してたんですよ。" id start_ab6fbfcb

    $ na2.screen = 'right_4long'
    na2"せんせー！\nブルガリア君とルーマニア君が\n出稼ぎに来て邪魔臭いです。" id start_b1038b62

    $ na2.screen = 'center_4long'
    na2"ブルガリア君とルーマニア君って\nＥＵに必要ですか？\nこいつら追い出してトルコ入れた方が\n有意義だと思いますー" id start_cc76127d

    scene bg romania_room2 at pan_to_top
    with fade_white

    play music "music/FilmEdge_Casual_Z010-ISay-Dellay.ogg" fadeout 1

    show bulgaria cry shout at pos_transform(xpos=440, yalign=0.0)
    
    $ bul.screen = 'right_7big'
    bul "うう…、ちくしょうちくしょう…。\nユーロ圏の新聞めー…。\n人の気持ちもしらねーで\n普通にこういう事書くんだわ…。\n手厳しいんだわー…。うっうっ…。\n金がねェンだよ…！国内建て直す\n金が手に入るまで働くしかねぇんだわ…。" id start_1db23734
    
    show romania waaahh at pos_transform(xpos=80, yalign=0.0)
    
    $ rom.screen = 'left_4long'
    rom "泣かないでよぉブルガリア…！\nおいらブルガリアを悲しませたくて\n思い出させたわけじゃないよぉ…" id start_1bce4555

    show bulgaria forreal
    $ bul.screen = 'right_1'
    bul "俺、やる…！" id start_1530bf19
    
    show romania cry eh
    $ rom.screen = 'left_1'
    rom "ブルガリア…！！" id start_d4d62c12
    
    show bulgaria hey2
    play sound ["<silence .7>", "sfx/gun14_c.ogg"]
    $ bul.screen = 'right_3'
    $ window_transform = shake_0p5
    bul "ちょっくら司会進行として\n国としての存在感\nアピッてくるんだわ！！" id start_fc180838
    $ window_transform = None

    show romania inspired
    $ rom.screen = 'left_3'
    rom "そうだよブルガリア！\nその意気だよ\n頑張ろうねぇ～！！" id start_0f5baf6e

    
    show bulgaria hey
    play sound ["<silence .5>", "sfx/bam10.ogg"]
    show bulgaria hey:
        0.8
        block:
            linear 0.1 xoffset -8 yoffset -8
            linear 0.1 xoffset +8 yoffset +8
            repeat 2
        linear 0.1 xoffset 0 yoffset 0
    $ window_transform = shake_0p2
    bul "そしてこのゲームの\n主役も頂くんだわ！" id start_c6e01564
    $ window_transform = None

    show romania cry eh
    $ rom.screen = 'left_1'
    rom "…え！？" id start_caf63c9d

    scene bg exterior
    with fade_white
    stop music fadeout 4
    na "こうしてブルガリアさんは、\n集められた７カ国から怖い話を聞く\nべく今日の会場へと向かう事になったのだった。" id start_8302b42c
    jump meeting






