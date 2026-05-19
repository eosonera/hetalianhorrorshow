

label story2:
    stop music
    scene bg exterior7
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第二話　アメリカの怖い話。{/size}" id story2_3fcfeae8

    scene bg classroom1

    play music "music/International_Uplifting_Dance-full_length_track.ogg"
    pause 0.2
    show america large normal at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    with Dissolve(0.25)

    story "俺の番かい？\nああ、二番でも構わないんだぞ。\n気を使ってくれなくても平気さ！" id story2_ec3298b7

    show america large sup eyesclosed
    with {'master': Dissolve(0.3)}

    story "俺だっていつもいつも\nナンバーワンにこだわってる\nわけじゃないからな。" id story2_4d148afe
    nvl clear

    scene bg classroom4
    show england sweat oh at pos_transform(xpos=140, yalign=0.0)
    $ eng.screen = 'left_3'
    eng "嘘だ！お前いつも\n一番にこだわるだろ" id story2_2c0b6678

    show america sup eyesclosed at pos_transform(xpos=400, yalign=0.0)
    $ ame.screen = 'right_3'
    ame "ＮＯ！\nプライドに関わる\nところだけだよ！" id story2_49a1d355


    show bulgaria conniving:
        xpos -50, yalign 0.0
        time 0.2
        block:
            easeout 0.3 yoffset 40
            easein 0.2 yalign 0.0 yoffset -5
            ease 0.2 yoffset 0

    pause 0.6
    $ bul.screen = 'left_4'
    bul "その漫才、\n始まると長そうなんで\nちょっちょと怖い話\nしちゃってくれますか？" id story2_2ad11d81

    show england blush shout2
    $ eng.screen = 'left_1'
    $ _pending_window_transform = (shake_2s1)
    $ _pending_sound = ("sfx/ding27.ogg", "sound")
    eng "漫才じゃないぞ！" id story2_89e31498

    show america howdy
    $ ame.screen = 'right_3'
    ame "ＯＫ！それじゃあ\n俺の体験した怖い話を\n披露させてもらうんだぞ！" id story2_8cef616d

    stop music fadeout 1.0
    scene bg classroom_window
    show nvl_textbox
    play music "music/hate.ogg" 
    show america large normal at pos_transform(xpos=350, ypos=-40)

    story "\nあれは俺が民家に迫りくる\nバッファローの大群を\n一頭一頭キャッチして\n手作業で向きを変えていた時の話…。" id story2_b80f9fac
    nvl clear

    stop music fadeout 1.0

    scene bg classroom1
    play music "music/FilmEdge_Casual_Z008-QuirkyBounce-Sorbo.ogg"
    show bulgaria conniving at pos_transform(xpos=100, yalign=0.0)
    $ bul.screen = 'left_3'
    bul "あ。\nそれじゃない話で\nお願いします" id story2_3f21d0b0

    show america whatyousay at pos_transform(xpos=200, yalign=0.0)
    $ ame.screen = 'center_4long'
    $ _pending_window_transform = (shake_0m1)
    $ _pending_sprite_transform = [("america", ame_2s1)]
    $ _pending_sound = ("sfx/hit35.ogg", "sound")
    ame "Ｗｈａｔ！？" id story2_f1213b36
    $ _skip_appear_effect = True
    extend "\n君はバッファローの群れが\n家に向かってきても怖くないのかい？" id story2_c752e978
    $ _skip_appear_effect = False
    stop sound

    show germany squint exasperated at pos_transform(xpos=470, yalign=0.0)
    $ ger.screen = 'right_4long'
    ger "確かに怖いと言えば怖いが\n怖いの方向性があまりにも\n斜め上すぎるだろう！" id story2_3611319e

    show america eek
    $ ame.screen = 'center_4long'
    $ _pending_window_transform = (shake_2s2)
    $ _pending_sound = ("sfx/ding27.ogg", "sound")
    ame "バッファローのボスが俺めがけて\n突進してくるシーンは全俺が震えるほど\nスリルに満ち溢れてるんだぞ！\n吹き飛ばされたけど民家は守ったんだ！" id story2_ecb25a40
    stop sound

    show bulgaria forreal
    $ bul.screen = 'left_4'
    $ _pending_window_transform = (shake_2s3)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    bul "もうバッファローより\nアメリカさん自体が\n怖ぇーっす！" id story2_f9650383
    stop sound

    show america worried
    $ ame.screen = 'center_3long'
    ame "こうなったらとっておきの\nゾンビとモンスターがマウンテンになる\nあの話をするしかないようだね…！" id story2_51f85803

    show bulgaria worried
    $ bul.screen = 'left_4'
    bul "もーちょい\n身近に感じる怖い話\nプリーズなんだわー！"  id story2_aa907b78

    show america eksdee
    $ ame.screen = 'center_4long'
    ame "ＯＫ！安心してくれたまえ！\nこれ以外にもスケアリーな話は\n用意しているんだぞ！" id story2_ec3fa10c

    stop sound
    stop music fadeout 1.0
    scene bg classroom5 at pan_to_top
    show nvl_textbox
    play music "music/hate.ogg" 
    show america large normal at pos_transform(xpos=350, ypos=-40)
    with Dissolve(0.25)

    story "{size=+5}\nこれは俺がエリア５１で\n宇宙人に会った時の話だ…。{/size}" id story2_09fd4bfd
    nvl clear

    ## Glass Cutscene #########################################
    scene bg classroom_window at pan_to_top
    stop music fadeout 1.0
    play sound ["<silence .5>", "sfx/crash16_b.ogg"]
    queue sound "sfx/crash16_b.ogg"
    queue sound "sfx/crash16_b.ogg"
    queue sound "sfx/crash16_b.ogg"
    queue sound "sfx/crash16_b.ogg"
    queue sound "sfx/crash16_b.ogg"
    show bulgaria waah at bul_glass
    show japan shocked at jpn_glass behind bulgaria
    show finland waah at fin_glass behind japan
    show england scream at eng_glass
    show germany shocked whatsthat at ger_glass behind england

    pause 5.5
    show black:
        alpha 0.4
    
    show glass_smash
    $ na2.screen = 'center_3long'
    $ _pending_window_transform = (shake_2s1)
    queue sound "sfx/wa-bam.ogg"
    na2 "{size=+6}――ッ！！？{/size}" id story2_7eab1ce8

    scene bg classroom1
    stop sound
    play music "music/Visit_to_the_Zoo.ogg"
    show america large sup eyesclosed at pos_transform(xpos=-40, ypos=-150)
    $ ame.screen = 'center_3long'
    ame "あれは俺がエリア５１で\nインベーダゲームをしていた時\n急に上司に呼ばれて…" id story2_65cd50a5

    show germany shocked whatsthat at pos_transform(xpos=550,yalign=0.0) behind america
    $ ger.screen = 'right_4'
    $ _pending_window_transform = (shake_2s4)
    $ _pending_sprite_transform = [("germany", shake_2s4)]
    $ _pending_sound = ("sfx/bam05.ogg", "sound")
    ger "{size=+3}は…早まるな\nアメリカーッ！！{/size}" id story2_144b3000
    stop sound

    show england blush shout2 at pos_transform(xpos=430, yalign=0.0) behind germany:
        xpos 430 yalign 0
        time 0.5
        block:
            easeout 0.2 yoffset -30
            easein 0.3 yoffset 20
            repeat
    $ eng.screen = 'center_3long'
    play sound1 "sfx/ding51.ogg"
    $ _pending_sound = ("sfx/ding51.ogg", "sound")
    eng "そそそそそうだぞ！\nそれ国家機密レベルだろ！？\n聞かされる俺らも危ないだろ！" id story2_909b71e5
    stop sound
    stop sound1

    show england at stop_offset with move
    show bulgaria cry shout behind america:
        xpos 40 yalign 0
        time 0.5
        block:
            linear 0.15 xoffset +5
            linear 0.15 xoffset -5
            repeat
    
    $ bul.screen = 'left_3'
    bul "ちょ…俺ら消される\nタイプの怖さは\n求めてねーんだわー！" id story2_3551935b

    show america large eksdee
    $ ame.screen = 'left_4'
    ame "ＨＡＨＡＨＡ！\nいきなり怖がってくれて\n嬉しいんだぞ！" id story2_23caa78b
    window show
    show bulgaria at stop_offset with {'master':move}
    show america large hahahaha with {'master':Dissolve(0.2)}:
        time 0.2
        parallel:
            easein 0.5 yoffset +160
        parallel:
            linear 0.4 xoffset 0
            linear 0.1 xoffset -2
            linear 0.1 xoffset +2
            linear 0.1 xoffset 0

    $ _skip_appear_effect = True
    $ ame.screen = 'left_4'
    ame "なんだいイギリス\n君のその顔！！\nＤＤＤＤＤＤＤＤ！" id story2_b720c3fa
    $ _skip_appear_effect = False
    window auto

    show america large howdy:
        time 0.2
        block:
            easein 0.5 yoffset +10

    pause 0.5
    $ ame.screen = 'left_4'
    ame "さっきのスリルと感動の\nバッファローの話に比べたら\nキッズ用のファンタジーさ！\n安心して聞いてくれ！" id story2_072bd0c2

    show bulgaria cry waah:
        time 0.5
        block:
            linear 0.15 xoffset +5
            linear 0.15 xoffset -5
            repeat
    $ bul.screen = 'left_3'
    bul "その言葉\n信じるわー！\nマジ頼むんだわー！" id story2_62232ffc

    show america large youreallyare
    $ ame.screen = 'left_4'
    ame "怖がらなくていいよ！\n手の込んだジョークを\n大まじめにやる上司が\n怖い話だからさ！" id story2_de4c902d

    stop music fadeout 1.0
    scene bg classroom1 at pan_to_bottom
    pause 0.2
    show america large normal at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    with Dissolve(0.25)
    play music "sfx/16_Talking_Computer_1.ogg" loop volume 0.4

    story "それで上司に呼び出された俺は\nエリア５１の地下２１階を\n上司と二人で進んでいったんだ…。" id story2_c6b074f3
    
    show bg tech2 behind nvl_textbox
    with {'master': Dissolve(0.2)}
    pause 0.5
    show america large huh
    with {'master': Dissolve(0.2)}  
    story "２１階…？\nエリア５１の地下って１７階までって\n聞いていたけどどういうことだい？\n俺は上司にストレートに質問してみた。" id story2_5abb5092
    nvl clear

 
    story "「先ほど、紹介したい人がいるといったね。\n　その人のためにこの階はあるんだ…」" id story2_38514aff
    show america large sigh
    with {'master': Dissolve(0.25)} 
    extend "\n\nだって。君、それアンサーになってないよ…。" id story2_d4e0c4dd
    nvl clear

    story "「…君にまで隠し事をしてしまって\n　本当に申し訳ないと思っている。\n　今から紹介する彼は…{color=#B5C1FC}宇宙人{/color}なんだ。\n　そしてこのエリア５１で働いている」" id story2_3770d437
    show america large yell sweat
    with {'master': Dissolve(0.3)}  
    story "宇宙人だって…！？\nエリア５１で宇宙人が\n働いてるっていうのかい！？" id story2_30c814b8
    nvl clear

    show bg tech behind nvl_textbox
    with Dissolve(0.5)
    pause 0.2
    hide america
    with Dissolve(0.5)

    story "\n「紹介しよう。\n　合衆国が技術提携を結んでいる\n　ＧＨ５３４７３星雲の\n　ＹＵ７８３４２星から\n　合衆国の視察に来た\n　ＭＡＴＡ・メッテシーア君だ」" id story2_18250913

    ## Alien Cutscene    
    play sound ["<silence .75>", "sfx/brisk_walk.ogg"]
    story "\n\nそこに現れたのは…{nw=1.0}" id story2_8552af69
    show alien_anim
    show alien at mata_pos
    with flashbulb
    pause 3.0
    nvl clear
    stop music fadeout 0.5

    scene bg tech at pan_to_top
    show nvl_textbox
    show alien at pos_transform(xpos=500, ypos=40)
    pause 0.5

    $ _pending_sound = ("sfx/ka-bam.ogg", "sound")
    $ _pending_camera_transform = [([shake_2s5], "master"), ([shake_0m10], "screens")]
    story "　\n　\n　\n　\n　\n俺のルームメイトの\nトニーのそっくりさんだったんだ…！！" id story2_b042fccd
    nvl clear
    $ _pending_camera_transform = None 

    camera
    camera screens

    play music "music/22_ohmy.ogg"

    play sound ["<silence 0.2>", "sfx/ding12.ogg"]
    show tony with {'master': Dissolve(0.2)}:
        xpos 400 ypos 280
        easein 0.3 yoffset -20
        easein 0.2 yoffset +20
        easein 0.3 yoffset 0

    
    story "　\n「どうぞ、よろしく。\n　国の方と会うのは公式では初めてです。\n　私の星には貴方のような方はいないので\n　よろしかったらお話を聞かせてください」\n\nなんてトニーのそっくりさんは\n宇宙人設定で話しかけてくるんだよ！" id story2_c4fd8fea
    nvl clear
    hide tony
    
    story "　\nその辺のおじさんが「私は宇宙人です」\nなんて話しかけてきたら笑っちゃうだろ？\n俺もおかしくなっちゃってさ。" id story2_b9d1a22f
    
    story "\n「もー驚かさないでくれよ！\n　上司が真面目な顔で宇宙人なんて言うから\n　一瞬、信じそうになったじゃないか！」" id story2_409dfccd
    nvl clear

    show alien sweat2
    with {'master': Dissolve(0.4)} 
    story "　\nそしたら上司も「宇宙人」君も\nポカーンとした顔をしてるんだよ。\n　\nもー君達。\n俺がこの宇宙人ドッキリに引っかかったら\nHetatubeに動画アップする\nつもりだったんだろ！？" id story2_5ab8cca2
    nvl clear
    
    story "でもそのトニーのそっくりさんが\n結構ユニークで面白い奴でさ！\n　\n「Hello！　トニーのそっくりさん！\n　わー君本当にそっくりだね！\n　トニーの親戚かい？」\n\nって俺が言ったら" id story2_f48c6d62
    nvl clear

    story "{k=8}　\n「え。あ。いや普通に宇宙人ですよ…？\n　トニーさんって…？」\n\nなんて言い出すんだよ！\n分かった今日一日君は宇宙人キャラでいくんだな！\nＯＫ！　俺も付き合ってやるんだぞ！{/k}" id story2_f7f24f4c
    nvl clear
    
    story "{k=3}「なんだいその設定！面白くていいよ。\n　星の名前はもう少し覚えやすくて\n　かっこいい方が良いぞ！\n　映画にした時に覚えられないと困るだろう？」{/k}" id story2_ddc443ca
    pause 0.3
    show alien sweat:
        time 0.6
        linear 0.1 xoffset +21 yoffset +17
        linear 0.1 xoffset 0 yoffset 0
        linear 0.1 xoffset +10 yoffset -9
        linear 0.1 xoffset 0 yoffset 0
        linear 0.1 xoffset -5 yoffset +5
        linear 0.1 xoffset 0 yoffset 0

    #with {'master': Dissolve(0.4)} 
    pause 0.8
    story "{k=8}「えー…、嘘ーん…。\n　この見た目の時点で\n　あっ宇宙人だ。って思いません？\n　それに多分そのトニーさんも宇宙人っすよ」{/k}" id story2_4be20c23
    nvl clear

    story "トニーは正真正銘のアメリカ人だぞ！\n街を歩けばちょくちょく\n見かけるタイプじゃないか！\nそれを宇宙人って君…ＤＤＤＤＤ！\n\nそれに君、君。\nここはアメリカ合衆国だぞ？\n特殊メイクは朝飯前なのだよ！" id story2_e51a00d1
    nvl clear
    
    story "だから俺は言った。\n\n「ははあ。\n　君が本当に宇宙人だっていうなら\n　ミステリーサークルが作れるはずだよ！」" id story2_585c8f64
    nvl clear
    
    story "「あ、私…、" id story2_615a20e3
    show alien sweat2
    with {'master': Dissolve(0.25)}
    extend "\n　フォトショップ 【Ｃ Ｃ ｜クロップサークル】は\n　専門外なんでちょっと使えない、ですね…。\n　なんかごめんなさい…」\n　\nなんだい！やっぱり君、\nただのトニーのそっくりさんじゃないか！" id story2_0654576b
    nvl clear

    story "俺のルームメイトの\nそっくりさんを見つけたからって\nこんな回りくどいドッキリを\n仕掛けてくるなんて…！\n\n俺の上司も意外に\nキュートな所あるだろう？" id story2_3f1d93c3
    nvl clear
    show alien -sweat2
    with {'master': Dissolve(0.25)}
    story "ひとしきり笑った後は\n彼ともすぐ仲良くなれたよ。\n　\n彼、連続ドラマが好きらしくってさ。\n色んなドラマがあるっていうのに\nザ・リバーが一番好きなんて\nセンスが宇宙っぽいかもしれないね。" id story2_0826bd8a
    nvl clear
    hide alien
    play music "sfx/16_Talking_Computer_1.ogg" loop volume 0.4 fadeout 2

   
    story "ドラマの話で盛り上がってたら\n彼が思い出したように" id story2_a83e8ea7
    show bg tech3 behind nvl_textbox
    show alien:
        xpos 570 ypos 40
        block:
            easeout 0.2 yoffset -30
            ease 0.15 yoffset 10
            easeout 0.15 yoffset -20
            ease 0.15 yoffset 0

    pause 0.3
    extend "\n\n「あ、リバーで思い出したんですけど\n　私の船乗ってみます？\n　リバーのあの船よりは便利ですよ」\n\nなんていうからさ。" id story2_ef7600bc
    nvl clear

    
    story "「へぇ！君の船か！\n　是非とも乗ってみたいんだぞ！」\n\nクルージングも好きだからね。\n真っ先にＹｅｓ！って答えたよ。\nエリア５１に勤めていると\nクルージング船が買えるんだな。" id story2_0aa5539a
    nvl clear
    play sound ["<silence 0.02>", "sfx/Crystals.wav"]
    hide alien with {'master': Dissolve(1)}

    story "「ちょっと待ってください。今呼びます」\n　\nなんて彼はいうんだよ。" id story2_7d7893fe
    story "ここは地下の研究所だぞ？\n流石に川は流れてないよ！\nそれに呼べば来る船ってユニークだね！\nもしかして君の愛犬の名前が「船」なのかい？\nジョークまで面白いなんて君って最高だね！" id story2_74211b8e
    nvl clear

    show white screen behind nvl_textbox
    with fade_white

    play sound "sfx/UFO 2.wav"
    play sound1 "sfx/Alien sex.wav"
    ## UFO cutscene
    story "　\n　\n　\n…それで彼が宙に円を描くと、{nw=1.0}" id story2_b5a2284d
    show circle_anim1 
    show ufo_anim behind nvl_textbox with circle_dissolve3
    extend "\n大きな音と振動の後、奥から{nw=2.0}" id story2_80fb1745

    
    nvl clear
    scene blue screen
    stop sound
    stop sound1
    play sound "sfx/Hard beep.wav" loop
    
    story "　\n《　ユナイテッドステイツ検閲　》\n\n《　ユナイテッドステイツ検閲　》\n\n《　ユナイテッドステイツ検閲　》\n\n《　ユナイテッドステイツ検閲　》\n\n《　ユナイテッドステイツ検閲　》{nw=1.0}" id story2_9546b191
    nvl clear
    stop sound

    scene bg classroom1 at pan_to_top
    play music "music/19_playful.ogg"
    pause 0.2
    show america large eksdee at pos_transform(xpos=-40, ypos=-150)
    $ ame.screen = 'center_3long'
    ame "そんなわけで俺とトニーは\n新しい友達のマタと\n暮らし始めたってわけだ！" id story2_5b7a5a6a

    show japan worried grimace at pos_transform(xpos=500, yalign=0.0) behind america
    $ jpn.screen = 'right_3'
    jpn "今のお話は私達が\n聞いてよかったので\nしょうか…？" id story2_9e1fbadb



    show bulgaria conniving at pos_transform(xpos=650, yalign=0.0)
    $ bul.screen = 'right_4'
    bul "…お話しあざーっす！\n俺は何も聞いていない\n機密情報なんて\n聞いてないんだわー…" id story2_6d14a5f3

    show finland ohdear behind america:
        xpos -50 yalign 0.0
        time 0.4
        block:
            easeout 0.2 yoffset -40
            ease 0.15 yoffset 10
            easeout 0.15 yoffset -30
            ease 0.15 yoffset 0

    $ fin.screen = 'left_3'
    fin "あはは…\nきょ、今日は\n空が綺麗ですね！" id story2_c892c3cc

    hide finland
    hide america
    hide bulgaria
    hide japan
    pause 0.2

    stop music fadeout 4.0

    jump story3