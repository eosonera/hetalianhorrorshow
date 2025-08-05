# The script of the game goes in this file.


## Characters ############################################################
##
##
##
##

#define fadeWithText = { "master" : Dissolve(1.0) }

define na = Character(None,
    window_background="textbox_center.png",
    window_xalign=0,
    window_yalign=0,
    window_xsize=700,
    what_xpos=180,
    what_ypos=210,
    what_color="#5B4A40",
    what_outlines=[( 0.5, "#fff", 0, 0 )],
    what_size=18,
    ctc="ctc_button",
    ctc_position="nestled",)

define na2 = Character(None,
    image="na2",
    window_xsize=700,
    ctc="ctc_button",
    ctc_position="nestled")

define bul = Character(_("ブルガリア"),
    image="bulgaria",
    ctc="ctc_button",
    ctc_position="nestled")

define rom = Character(_("ルーマニア"),
    image="romania",
    ctc="ctc_button",
    ctc_position="nestled")

define nar_nvl = nvl_narrator
    #ctc="ctc_button",
    #ctc_position="nestled",
 
## Start ############################################################
## The game starts here.
##
##
##

default persistent.game_finished = False

label start:
    play music "9_townscape.ogg"


    scene bg romania_room at top


    na "「７カ国が集まる国際怖い話会合があるからそこで話を聞いてきてくれないかなー？
    \n\n{space=200}その一言でそれは始まった。"

    scene bg romania_room3 at top
    with dissolve


    show bulgaria ooh at mid_right
    with dissolve
    #$ bul.window_style = "red_window"
    bul "えっ俺が？"

    show romania at mid_left behind bulgaria
    with dissolve
    rom "ごめんね～。\nほんとはおいらが\nやりたかったんだけどさー。"
    show romania worried at mid_left
    with dissolve
    rom "魔術部のイギ…\nほにゃららさんにごほごほっ\nいつやるんだって\nせっつかれてるしー…。"
    show romania cry_uuu
    with dissolve
    rom "でも…その、上司に、お前\nそんな事してる暇ないだろって\n言われちゃってー…。"

    show bulgaria mm
    with dissolve
    bul"いやそれ俺もだけどね。\n俺も遊ぶ暇あったら\n内職しろって\n言われてるんだわー。"

    show romania whatsthaat
    with dissolve
    rom "そうだったの！？\nでもお前いっつも\nフラフラしてるじゃんかー！"

    show bulgaria forreal
    with dissolve
    bul "ふざけんなー！\n自分で行けオラァ！"

    show romania cry_nyaa
    with dissolve
    rom "なんて友だち甲斐が\nないんだよー！頼むよー！\n頼める人がいないんだよー"

    show bulgaria conniving
    with dissolve
    bul "ロシアさんは？"

    show romania scared
    with dissolve
    rom "え！？ えーと…。\nロシアさんは存在自体がー…\n怖いっていうか…。"

    show bulgaria yeahyeah
    with dissolve
    bul "そこら辺は\n…否定はしないわー"

    show romania cry_nyaa
    with dissolve
    rom "お願いだよー！！\nお菓子あげるから！"

    show bulgaria conniving
    with dissolve
    bul "お菓子でつられる\n年じゃねーんだわー."

    show romania what
    with dissolve
    rom "ブルガリア今年何歳？"

    show bulgaria fufufu-n
    with dissolve
    bul "んー ま、\nかれこれ…３？"

    show romania ooh
    with dissolve
    rom "３００じゃないよね?"

    show bulgaria conniving
    with dissolve
    bul "んーん♪"

    show romania eh
    with dissolve
    rom "３０００？"

    show bulgaria howdy
    with dissolve
    bul "もう一声ぇっ！"

    show romania whatsthaat
    with dissolve
    rom "３万！？ ないよー！"

    show bulgaria fufufu-n
    with dissolve
    play sound "sfx/gun14_c.ogg"
    show bulgaria fufufu-n at sprite_shake
    bul "俺三万歳！！\nつまり俺の国力は\n３万あるんだわー！"
    
    
    show bulgaria fufufu-n at mid_right
    show romania angry_yell
    with dissolve
    play sound "sfx/bang07.ogg"
    show romania angry_yell at shake2
    rom "こいつ盛ったぁー！！"
    show romania angry_yell at mid_left

    

    show bulgaria howdy
    with dissolve
    bul "盛ってねーから！\nそういうわけで俺の方が\n年上だから俺はいかない！"

    show romania whatsthaat
    with dissolve
    rom "やーだー！その理屈わかんないよー\n頼むよー！行ってよー！\nいらとお前の付き合いだろー！！"

    with dissolve
    show bulgaria conniving_eyesclosed
    play sound ["<silence .5>", "sfx/BUBBLY.WAV"]
    show bulgaria fufufu-n at humming
    bul "ぷぷぷぷ～\nぷんにょにょ～（鼻歌）"
    
    show romania holdon
    with dissolve
    play sound "sfx/ding74.ogg"
    rom "やだー変な歌うたいながら\nおいらの周りまわらないでー。\nやめてよー"

    play sound "sfx/Disintergrate.wav"
    bul "ふんごっ\nふんごっ（鼻歌）"

    show romania waaahh
    with dissolve
    rom "わーんわーん！！"

    rom "どうすればいいんだよぅこれー。"

    show romania whattheheck
    with dissolve
    rom "…あっ！そうだ！\nこの仕事すると…目立てるよ！"

    show bulgaria fufufu-n at mid_right
    show bulgaria whatisthat at mid_right
    
    bul "何！！？"

    show romania heynoow
    with dissolve
    rom"他のみんなと対等な目線で\n話せるよー！"

    show bulgaria ooh
    with dissolve
    bul "つまり…\nどういうことだ？"

    show romania sup
    with dissolve
    rom "だから！司会進行として！\nいつもは上からにゃーにゃー\n言ってくるみんなをブルガリアが\n先導できるってこと！！"

    show romania sigh_eyesclosed
    with dissolve
    rom "思い出してよ\nおいらたちの近代…"

    stop music fadeout 1
    show bulgaria sweat
    with dissolve    
    bul"俺たちの近代…"

    hide bulgaria
    hide romania
    scene black
    with fade

    na2"またブルガリアと\nルーマニアか…。"

    na2"この二国って加入してから\n足引っ張ってるだけですよね。\nだから反対してたんですよ。"

    na2"せんせー！\nブルガリア君とルーマニア君が\n出稼ぎに来て邪魔臭いです。"

    na2"ブルガリア君とルーマニア君って\nＥＵに必要ですか？\nこいつら追い出してトルコ入れた方が\n有意義だと思いますー"

    scene bg romania_room2 at top
    with dissolve

    play music "FilmEdge_Casual_Z010-ISay-Dellay.ogg" fadeout 1

    show bulgaria cry_shout at mid_right
    with dissolve
    bul "うう…、ちくしょうちくしょう…。\nユーロ圏の新聞めー…。\n人の気持ちもしらねーで\n普通にこういう事書くんだわ…。\n手厳しいんだわー…。うっうっ…。\n金がねェンだよ…！国内建て直す\n金が手に入るまで働くしかねぇんだわ…。"
    
    show romania waaahh at mid_left
    with dissolve
    rom "泣かないでよぉブルガリア…！\nおいらブルガリアを悲しませたくて\n思い出させたわけじゃないよぉ…"

    show bulgaria forreal
    with dissolve
    bul "俺、やる…！"
    
    show romania cry_eh
    with dissolve
    rom "ブルガリア…！！"
    
    show bulgaria hey2
    with dissolve
    play sound "sfx/gun14_c.ogg"
    bul "ちょっくら司会進行として\n国としての存在感\nアピッてくるんだわ！！"

    show romania inspired
    with dissolve
    rom "そうだよブルガリア！\nその意気だよ\n頑張ろうねぇ～！！"

    
    show bulgaria hey
    with dissolve
    play sound ["<silence .5>", "sfx/bam10.ogg"]
    show bulgaria hey at sprite_shake
    bul "そしてこのゲームの\n主役も頂くんだわ！"

    show romania cry_eh
    with dissolve
    rom "…え！？"

    scene bg exterior1 at top

    na "こうしてブルガリアさんは、\n集められた７カ国から怖い話を聞くべく\n今日の会場へと向かう事になったのだった。"


    # The game ends here
    $ persistent.game_finished = True
    return






