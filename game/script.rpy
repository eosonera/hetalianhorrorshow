
 
## Start ############################################################


default persistent.game_finished = False

label start:
    play music "9_townscape.ogg"

    scene bg romania_room at pan_to_top
    with blur_fade

    #show dust2 at dust2_transform
    show dust at dust1_transform
    show dust_1 at dust1_transform1
    show sunlight at sunlight2_transform0
    show sunlight2_1 at sun_rroom1_1

    na "「７カ国が集まる国際怖い話会合があるから
    \n　そこで話を聞いてきてくれないかなー？」\n{vspace=12}
    {space=155}その一言でそれは始まった。"

    scene bg romania_room3 at pan_to_top

    show sunlight2_0 at sun_rroom3_0
    show sunlight2_1 at sun_rroom3_1
    show dust at dust1_transform
    show dust_1 at dust1_transform1
    #show dust2 at dust2_transform
    show orange
    show yellow
    with fade_white


    show bulgaria ooh at pos_transform(x=440, yalign=0.0)
    with dissolve
    $ bul.screen = 'right_1'
    bul "えっ俺が？"

    show romania at pos_transform(x=70, yalign=0.0) behind bulgaria
    with dissolve
    $ rom.screen = 'left_3'
    rom "ごめんね～。\nほんとはおいらが\nやりたかったんだけどさー。"
    show romania worried at pos_transform(x=70, yalign=0.0)
    with dissolve
    $ rom.screen = 'left_4'
    rom "{size=-2}魔術部のイギ…\nほにゃららさんに{size=-5}ごほごほっ{/size}\nいつやるんだって\nせっつかれてるしー…。{/size}"
    show romania cry uuu
    with dissolve
    rom "{size=-2}でも…その、上司に、お前\nそんな事してる暇ないだろって\n言われちゃってー…。{/size}"

    show bulgaria mm
    with dissolve
    $ bul.screen = 'right_4'
    bul"いやそれ俺もだけどね。\n俺も遊ぶ暇あったら\n内職しろって\n言われてるんだわー。"

    show romania whatsthaat
    with dissolve
    rom "そうだったの！？\nでもお前いっつも\nフラフラしてるじゃんかー！"

    $ bul.screen = 'right_3'
    show bulgaria forreal
    with dissolve
    bul "ふざけんなー！\n自分で行けオラァ！"

    show romania cry nyaa
    with dissolve
    $ rom.screen = 'left_4'
    rom "なんて友だち甲斐が\nないんだよー！頼むよー！\n頼める人がいないんだよー"

    show bulgaria conniving
    with dissolve
    $ bul.screen = 'right_1'
    bul "ロシアさんは？"

    show romania scared
    with dissolve
    $ rom.screen = 'left_3'
    rom "え！？ えーと…。\nロシアさんは{size=-5}存在自体がー…\n怖いっていうか…。{/size}"

    show bulgaria yeahyeah
    with dissolve
    $ bul.screen = 'right_3'
    bul "そこら辺は\n…否定はしないわー"

    show romania cry nyaa
    with dissolve
    $ rom.screen = 'left_3'
    
    $ window_transform = mb_shake
    rom "お願いだよー！！\nお菓子あげるから！"
    $ window_transform = None

    show bulgaria conniving
    with dissolve
    bul "お菓子でつられる\n年じゃねーんだわー"

    show romania what
    with dissolve
    $ rom.screen = 'left_1'
    rom "ブルガリア今年何歳？"

    show bulgaria fufufu-n
    with dissolve
    $ bul.screen = 'right_3'
    bul "んー ま、\nかれこれ…３？"

    show romania ooh
    with dissolve
    if preferences.language != None:
        $ rom.screen = 'left_3'
    rom "３００じゃないよね?"

    show bulgaria conniving
    with dissolve
    $ bul.screen = 'right_1'
    bul "んーん♪"

    show romania eh
    with dissolve
    $ rom.screen = 'left_1'
    rom "３０００？"

    show bulgaria howdy
    with dissolve
    $ window_transform = mb_shake
    $ bul.screen = 'right_1'
    bul "もう一声ぇっ！"
    $ window_transform = None

    show romania whatsthaat
    with dissolve
    rom "３万！？ ないよー！"

    show bulgaria fufufu-n
    with dissolve
    play sound ["<silence .4>", "sfx/gun14_c.ogg"]
    show bulgaria fufufu-n at s_shake1
    $ bul.screen = 'right_3'
    $ window_transform = s_shake1
    bul "俺三万歳！！\nつまり俺の国力は\n３万あるんだわー！"
    
    
    show bulgaria fufufu-n at pos_transform(x=440, yalign=0.0)
    show romania angry yell
    with dissolve
    play sound ["<silence .4>", "sfx/bang07.ogg"]
    show romania angry yell at s_shake2
    $ rom.screen = 'left_1'
    $ window_transform = s_shake2
    rom "こいつ盛ったぁー！！"
    show romania at pos_transform(x=70, yalign=0.0)

    $ window_transform = None
    show bulgaria howdy
    with dissolve
    $ bul.screen = 'right_3'
    bul "盛ってねーから！\nそういうわけで俺の方が\n年上だから俺はいかない！"

    show romania whatsthaat
    with dissolve
    $ rom.screen = 'left_4long'
    rom "やーだー！その理屈わかんないよー\n頼むよー！行ってよー！\nいらとお前の付き合いだろー！！"

    with dissolve
    show bulgaria conniving eyesclosed
    play sound ["<silence .5>", "sfx/BUBBLY.WAV"]
    show bulgaria fufufu-n at humming
    $ bul.screen = 'right_3'
    bul "ぷぷぷぷ～\nぷんにょにょ～（鼻歌）"
    
    show romania holdon
    with dissolve
    play sound "sfx/ding74.ogg"
    $ rom.screen = 'left_4long'
    rom "やだー変な歌うたいながら\nおいらの周りまわらないでー。\nやめてよー"

    play sound "sfx/Disintergrate.wav"
    $ bul.screen = 'right_3'
    bul "ふんごっ\nふんごっ（鼻歌）"

    show romania waaahh
    with dissolve
    $ rom.screen = 'left_1'
    rom "わーんわーん！！"

    $ rom.screen = 'left_4'
    rom "どうすればいいんだよぅこれー。"
    $ _skip_appear_effect = True
    show romania whattheheck
    with {'master': dissolve}
    $ window_transform = mb_shake_long
    extend "\n…あっ！そうだ！\nこの仕事すると…目立てるよ！"
    $ window_transform = None
    $ _skip_appear_effect = False

    show bulgaria fufufu-n at stop_offset
    show bulgaria whatisthat at pos_transform(x=440, yalign=0.0)
    with move
    
    $ bul.screen = 'right_1'
    bul "何！！？"

    show romania heynoow
    with dissolve
    $ rom.screen = 'left_4long'
    rom"他のみんなと対等な目線で\n話せるよー！"

    show bulgaria ooh
    with dissolve
    $ bul.screen = 'right_3'
    bul "つまり…\nどういうことだ？"

    show romania sup
    with dissolve
    rom "だから！司会進行として！\nいつもは上からにゃーにゃー\n言ってくるみんなをブルガリアが\n先導できるってこと！！"

    show romania sigh eyesclosed
    with dissolve
    $ rom.screen = 'left_4long'
    rom "思い出してよ\nおいらたちの近代…"

    stop music fadeout 1
    show bulgaria sweat
    with dissolve
    $ bul.screen = 'right_1'    
    bul"俺たちの近代…"

    hide bulgaria
    hide romania
    scene black
    with fade

    $ na2.screen = 'right_3'
    na2"またブルガリアと\nルーマニアか…。"

    $ na2.screen = 'left_4long'
    na2"この二国って加入してから\n足引っ張ってるだけですよね。\nだから反対してたんですよ。"

    $ na2.screen = 'right_4long'
    na2"せんせー！\nブルガリア君とルーマニア君が\n出稼ぎに来て邪魔臭いです。"

    $ na2.screen = 'center_4long'
    na2"ブルガリア君とルーマニア君って\nＥＵに必要ですか？\nこいつら追い出してトルコ入れた方が\n有意義だと思いますー"

    scene bg romania_room2 at pan_to_top
    show dust at dust1_transform
    show dust_1 at dust1_transform1
    show sunlight2_0 at sun_rroom2_0
    show sunlight2_1 at sun_rroom1_1
    with fade_white

    play music "FilmEdge_Casual_Z010-ISay-Dellay.ogg" fadeout 1

    show bulgaria cry shout at pos_transform(x=440, yalign=0.0)
    with dissolve
    $ bul.screen = 'right_7big'
    bul "うう…、ちくしょうちくしょう…。\nユーロ圏の新聞めー…。\n人の気持ちもしらねーで\n普通にこういう事書くんだわ…。\n手厳しいんだわー…。うっうっ…。\n金がねェンだよ…！国内建て直す\n金が手に入るまで働くしかねぇんだわ…。"
    
    show romania waaahh at pos_transform(x=80, yalign=0.0)
    with dissolve
    $ rom.screen = 'left_4long'
    rom "泣かないでよぉブルガリア…！\nおいらブルガリアを悲しませたくて\n思い出させたわけじゃないよぉ…"

    show bulgaria forreal
    with dissolve
    $ bul.screen = 'right_1'
    bul "俺、やる…！"
    
    show romania cry eh
    with dissolve
    $ rom.screen = 'left_1'
    rom "ブルガリア…！！"
    
    show bulgaria hey2
    with dissolve
    play sound ["<silence .7>", "sfx/gun14_c.ogg"]
    $ bul.screen = 'right_3'
    $ window_transform = mb_shake2
    bul "ちょっくら司会進行として\n国としての存在感\nアピッてくるんだわ！！"
    $ window_transform = None

    show romania inspired
    with dissolve
    $ rom.screen = 'left_3'
    rom "そうだよブルガリア！\nその意気だよ\n頑張ろうねぇ～！！"

    
    show bulgaria hey
    with dissolve
    play sound ["<silence .5>", "sfx/bam10.ogg"]
    show bulgaria hey at s_shake1
    $ window_transform = s_shake1
    bul "そしてこのゲームの\n主役も頂くんだわ！"
    $ window_transform = None

    show romania cry eh
    with dissolve
    $ rom.screen = 'left_1'
    rom "…え！？"

    scene bg exterior at pan_to_top_ext0
    show dust at dust1_transform
    show dust_1 at dust1_transform1
    show sunlight2_0_1 at sun_ext_0
    show sunlight2_1_1 at sun_ext_1
    with fade_white
    stop music fadeout 4
    na "こうしてブルガリアさんは、\n集められた７カ国から怖い話を聞く\nべく今日の会場へと向かう事になったのだった。"
    
    jump meeting






