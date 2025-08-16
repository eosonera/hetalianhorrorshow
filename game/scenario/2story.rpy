

label story2:
    scene bg exterior7 at pan_to_top
    with dissolve
    na "{size=+2}第二話　アメリカの怖い話。{/size}"

    scene bg classroom1 at pan_to_bottom

    play music "music/International_Uplifting_Dance-full_length_track.ogg"
    pause 0.2
    show america large normal at pos_transform(x=350, y=-40)
    show nvl_textbox
    with Dissolve(0.25)

    story "俺の番かい？\nああ、二番でも構わないんだぞ。\n気を使ってくれなくても平気さ！"

    show america large sup eyesclosed
    with {'master': Dissolve(0.3)}

    story "俺だっていつもいつも\nナンバーワンにこだわってる\nわけじゃないからな。"
    nvl clear

    scene bg classroom4 at pan_to_top
    show england sweat oh at pos_transform(x=140, yalign=0.0)
    $ eng.screen = 'left_3'
    eng "嘘だ！お前いつも\n一番にこだわるだろ"

    show america sup eyesclosed at pos_transform(x=400, yalign=0.0)
    $ ame.screen = 'right_3'
    ame "ＮＯ！\nプライドに関わる\nところだけだよ！"

    show bulgaria conniving at pos_transform(x=-50, yalign=0.0)
    $ bul.screen = 'left_4'
    bul "その漫才、\n始まると長そうなんで\nちょっちょと怖い話\nしちゃってくれますか？"

    show england blush shout2
    $ eng.screen = 'left_1'
    play sound ["<silence .3>","sfx/ding27.ogg"]
    eng "漫才じゃないぞ！"

    show america freedom smile
    $ ame.screen = 'right_3'
    ame "ＯＫ！それじゃあ\n俺の体験した怖い話を\n披露させてもらうんだぞ！"

    stop music fadeout 1.0
    scene bg classroom_window at pan_to_top
    show nvl_textbox
    play music "music/hate.ogg" 
    show america large normal at pos_transform(x=350, y=-40)

    story "\nあれは俺が民家に迫りくる\nバッファローの大群を\n一頭一頭キャッチして\n手作業で向きを変えていた時の話…。"
    nvl clear

    stop music fadeout 1.0

    scene bg classroom1 at pan_to_top
    play music "music/FilmEdge_Casual_Z008-QuirkyBounce-Sorbo.ogg"
    show bulgaria conniving at pos_transform(x=100, yalign=0.0)
    $ bul.screen = 'left_3'
    bul "あ。\nそれじゃない話で\nお願いします"

    show america whatyousay at pos_transform(x=200, yalign=0.0)
    $ ame.screen = 'center_4long'
    play sound ["<silence .2>", "sfx/hit22.ogg"]
    #$ window_transform = 
    $ _skip_appear_effect = True
    ame "Ｗｈａｔ！？"
    #$ window_transform = None
    extend "\n君はバッファローの群れが\n家に向かってきても怖くないのかい？"
    $ _skip_appear_effect = False

    show germany eyes-half-lidded exasperated at pos_transform(x=470, yalign=0.0)
    $ ger.screen = 'right_4long'
    ger "確かに怖いと言えば怖いが\n怖いの方向性があまりにも\n斜め上すぎるだろう！"

    show america eek
    $ ame.screen = 'center_4long'
    play sound ["<silence 1.5>","sfx/ding27.ogg"]
    ame "バッファローのボスが俺めがけて\n突進してくるシーンは全俺が震えるほど\nスリルに満ち溢れてるんだぞ！\n吹き飛ばされたけど民家は守ったんだ！"

    show bulgaria forreal
    $ bul.screen = 'left_4'
    play sound ["<silence .2>", "sfx/hit34.ogg"]
    bul "もうバッファローより\nアメリカさん自体が\n怖ぇーっす！"

    show america worried
    $ ame.screen = 'center_3long'
    ame "こうなったらとっておきの\nゾンビとモンスターがマウンテンになる\nあの話をするしかないようだね…！"

    show bulgaria worried
    $ bul.screen = 'left_4'
    bul "もーちょい\n身近に感じる怖い話\nプリーズなんだわー！"    

    show america d
    $ ame.screen = 'center_4long'
    ame "ＯＫ！安心してくれたまえ！\nこれ以外にもスキュアリーな話は\n用意しているんだぞ！"

    stop sound
    stop music fadeout 1.0
    scene bg classroom5 at pan_to_top
    show nvl_textbox
    play music "music/hate.ogg" 
    show america large normal at pos_transform(x=350, y=-40)
    with Dissolve(0.25)

    story "これは俺がエリア５１で\n宇宙人に会った時の話だ…。"
    nvl clear

    ## Glass Cutscene #########################################
    scene bg classroom_window at pan_to_top
    stop music fadeout 1.0
    play sound "sfx/crash16_b.ogg"
    queue sound "sfx/crash16_b.ogg"
    queue sound "sfx/crash16_b.ogg"
    queue sound "sfx/crash16_b.ogg"
    queue sound "sfx/crash16_b.ogg"
    show bulgaria waah at pos_transform(x=0, yalign=0.0)
    show japan shocked at jpn_glass behind bulgaria
    show finland waah at fin_glass behind japan
    show england white-eyed shout at eng_glass
    show germany shocked whatsthat at ger_glass behind england

    pause 5.0
    show black:
        alpha 0.4
    queue sound "sfx/wa-bam.ogg" fadein 0.1
    show glass_smash
    $ na2.screen = 'center_3long'
    na2 "{size=+6}――ッ！！？{/size}"

    scene bg classroom1
    stop sound
    play music "music/Visit_to_the_Zoo.ogg"
    show america large sup eyesclosed at pos_transform(x=-40, y=-150)
    $ ame.screen = 'center_3long'
    ame "あれは俺がエリア５１で\nインベーダゲームをしていた時\n急に上司に呼ばれて…"

    show germany shocked whatsthat at pos_transform(x=550, yalign=0.0) behind america
    $ ger.screen = 'right_4'
    play sound ["<silence 0.2>","sfx/bam05.ogg"]
    ger "は…早まるな\nアメリカーッ！！！"

    show england blush shout2 at pos_transform(x=430, yalign=0.0) behind germany
    $ eng.screen = 'center_3long'
    play sound ["<silence .3>","sfx/ding51.ogg"]
    eng "そそそそそうだぞ！\nそれ国家機密レベルだろ！？\n聞かされる俺らも危ないだろ！"

    show bulgaria cry shout at pos_transform(x=40, yalign=0.0) behind america
    $ bul.screen = 'left_3'
    bul "ちょ…俺ら消される\nタイプの怖さは\n求めてねーんだわー！"

    show america large d
    $ ame.screen = 'left_4'
    ame "ＨＡＨＡＨＡ！\nいきなり怖がってくれて\n嬉しいんだぞ！"
    window show
    show america large hahahaha
    with {'master':Dissolve(0.25)}
    #$ window_transform = 
    $ _skip_appear_effect = True
    ame "なんだいイギリス\n君のその顔！！\nＤＤＤＤＤＤＤＤ！"
    #$ window_transform = None
    $ _skip_appear_effect = False
    window auto

    show america large freedom smile
    $ ame.screen = 'left_4'
    ame "さっきのスリルと感動の\nバッファローの話に比べたら\nキッズ用のファンタジーさ！\n安心して聞いてくれ！"

    show bulgaria cry waah
    $ bul.screen = 'left_3'
    bul "その言葉\n信じるわー！\nマジ頼むんだわー！"

    show america large youreallyare
    $ ame.screen = 'left_4'
    ame "怖がらなくていいよ！\n手の込んだジョークを\n大まじめにやる上司が\n怖い話だからさ！"

    stop music fadeout 1.0
    scene bg classroom1 at pan_to_bottom
    pause 0.2
    show america large normal at pos_transform(x=350, y=-40)
    show nvl_textbox
    with Dissolve(0.25)
    play music "sfx/16_Talking_Computer_1.ogg" loop volume 0.4

    story "それで上司に呼び出された俺は\nエリア５１の地下２１階を\n上司と二人で進んでいったんだ…。"
    
    show bg tech2 at pan_to_top behind nvl_textbox
    show america large huh
    with {'master': Dissolve(0.3)}  
    story "２１階…？\nエリア５１の地下って１７階までって\n聞いていたけどどういうことだい？\n俺は上司にストレートに質問してみた。"
    nvl clear

 
    story "「先ほど、紹介したい人がいるといったね。\n　その人のためにこの階はあるんだ…」"
    show america large sigh
    with {'master': Dissolve(0.25)} 
    extend "\n\nだって。君、それアンサーになってないよ…。"
    nvl clear

    story "「…君にまで隠し事をしてしまって\n　本当に申し訳ないと思っている。\n　今から紹介する彼は…{color=#B4C2DF}宇宙人{/color}なんだ。\n　そしてこのエリア５１で働いている」"
    show america large yell sweat
    with {'master': Dissolve(0.3)}  
    story "宇宙人だって…！？\nエリア５１で宇宙人が\n働いてるっていうのかい！？"
    nvl clear

    show bg tech behind nvl_textbox
    with Dissolve(0.5)
    pause 0.2
    hide america
    with Dissolve(0.5)

    story "\n「紹介しよう。\n　合衆国が技術提携を結んでいる\n　ＧＨ５３４７３星雲の\n　ＹＵ７８３４２星から\n　合衆国の視察に来た\n　ＭＡＴＡ・メッテシーア君だ」"

    ## Alien Cutscene    
    #play sound ["<silence .75>", "sfx/brisk_walk.ogg"]
    story "\n\nそこに現れたのは…{nw=1.0}" 
    show bg tech3 #at tech3_pos behind nvl_textbox
    show alien at mata_pos
    with flash
    pause 3.0
    nvl clear
    stop music fadeout 0.5

    scene bg tech at pan_to_top
    show nvl_textbox
    show alien at pos_transform(x=500, y=40)
    pause 0.5
    play sound ["<silence 0.75>", "sfx/ka-bam.ogg"] volume 0.7
    show tony at tony_pos with Dissolve(0.25)
    story "　\n　\n　\n　\n　\n俺のルームメイトの\nトニーのそっくりさんだったんだ…！！" with sshake
    nvl clear

    play music "music/22_ohmy.ogg"
    

    story "　\n「どうぞ、よろしく。\n　国の方と会うのは公式では初めてです。\n　私の星には貴方のような方はいないので\n　よろしかったらお話を聞かせてください」\n\nなんてトニーのそっくりさんは\n宇宙人設定で話しかけてくるんだよ！"
    nvl clear
    hide tony
    
    story "　\nその辺のおじさんが「私は宇宙人です」\nなんて話しかけてきたら笑っちゃうだろ？\n俺もおかしくなっちゃってさ。"
    
    story "\n「もー驚かさないでくれよ！\n　上司が真面目な顔で宇宙人なんて言うから\n　一瞬、信じそうになったじゃないか！」"
    nvl clear

    show alien sweat2
    with {'master': Dissolve(0.4)} 
    story "　\nそしたら上司も「宇宙人」君も\nポカーンとした顔をしてるんだよ。\n　\nもー君達。\n俺がこの宇宙人ドッキリに引っかかったら\nHetatubeに動画アップする\nつもりだったんだろ！？"
    nvl clear
    
    story "でもそのトニーのそっくりさんが\n結構ユニークで面白い奴でさ！\n　\n「Hello！　トニーのそっくりさん！\n　わー君本当にそっくりだね！\n　トニーの親戚かい？」\n\nって俺が言ったら"
    nvl clear

    story "{k=8}　\n「え。あ。いや普通に宇宙人ですよ…？\n　トニーさんって…？」\n\nなんて言い出すんだよ！\n分かった今日一日君は宇宙人キャラでいくんだな！\nＯＫ！　俺も付き合ってやるんだぞ！{/k}"
    nvl clear
    
    story "{k=8}「なんだいその設定！面白くていいよ。\n　星の名前はもう少し覚えやすくて\n　かっこいい方が良いぞ！\n　映画にした時に覚えられないと困るだろう？」{/k}"
    show alien sweat
    with {'master': Dissolve(0.4)} 

    story "{k=8}「えー…、嘘ーん…。\n　この見た目の時点で\n　あっ宇宙人だ。って思いません？\n　それに多分そのトニーさんも宇宙人っすよ」{/k}"
    nvl clear

    story "トニーは正真正銘のアメリカ人だぞ！\n街を歩けばちょくちょく\n見かけるタイプじゃないか！\nそれを宇宙人って君…ＤＤＤＤＤ！\n\nそれに君、君。\nここはアメリカ合衆国だぞ？\n特殊メイクは朝飯前なのだよ！"
    nvl clear
    
    story "だから俺は言った。\n\n「ははあ。\n　君が本当に宇宙人だっていうなら\n　ミステリーサークルが作れるはずだよ！」"
    nvl clear
    
    story "「あ、私…、"
    show alien sweat2
    with {'master': Dissolve(0.25)}
    extend "\n　フォトショップ 【Ｃ Ｃ ｜クロップサークル】は\n　専門外なんでちょっと使えない、ですね…。\n　なんかごめんなさい…」\n　\nなんだい！やっぱり君、\nただのトニーのそっくりさんじゃないか！"
    nvl clear

    story "俺のルームメイトの\nそっくりさんを見つけたからって\nこんな回りくどいドッキリを\n仕掛けてくるなんて…！\n\n俺の上司も意外に\nキュートな所あるだろう？"
    nvl clear
    show alien -sweat2
    with {'master': Dissolve(0.25)}
    story "ひとしきり笑った後は\n彼ともすぐ仲良くなれたよ。\n　\n彼、連続ドラマが好きらしくってさ。\n色んなドラマがあるっていうのに\nザ・リバーが一番好きなんて\nセンスが宇宙っぽいかもしれないね。"
    nvl clear
    hide alien
    play music "sfx/16_Talking_Computer_1.ogg" loop volume 0.4

    show bg tech3 behind nvl_textbox
    story "ドラマの話で盛り上がってたら\n彼が思い出したように"
    show alien at pos_transform(x=570,y=40)
    story "「あ、リバーで思い出したんですけど\n　私の船乗ってみます？\n　リバーのあの船よりは便利ですよ」\n\nなんていうからさ。"
    nvl clear

    
    story "「へぇ！君の船か！\n　是非とも乗ってみたいんだぞ！」\n\nクルージングも好きだからね。\n真っ先にＹｅｓ！って答えたよ。\nエリア５１に勤めていると\nクルージング船が買えるんだな。"
    nvl clear
    play sound ["<silence 0.75>", "sfx/Crystals.wav"]
    hide alien

    queue sound "sfx/UFO 2.wav"
    queue sound "sfx/Alien sex.ogg"
    story "「ちょっと待ってください。今呼びます」\n　\nなんて彼はいうんだよ。"
    story "ここは地下の研究所だぞ？\n流石に川は流れてないよ！\nそれに呼べば来る船ってユニークだね！\nもしかして君の愛犬の名前が「船」なのかい？\nジョークまで面白いなんて君って最高だね！"
    nvl clear

    show white screen behind nvl_textbox
    with fade_white

    ## UFO cutscene
    story "　\n　\n　\n…それで彼が宙に円を描くと、\n大きな音と振動の後、奥から{nw=5.0}"
    show ufo1 at ufo1_pos behind nvl_textbox
    show ufo2 at ufo2_pos behind nvl_textbox
    show ufo3 at ufo3_pos behind nvl_textbox
    show ufo4 at ufo4_pos behind nvl_textbox
    pause 5.0

    
    nvl clear
    scene blue screen
    stop sound
    #play sound "sfx/Hard beep.wav" loop
    
    story "　\n《　ユナイデットステイツ検閲　》\n\n《　ユナイデットステイツ検閲　》\n\n《　ユナイデットステイツ検閲　》\n\n《　ユナイデットステイツ検閲　》\n\n《　ユナイデットステイツ検閲　》{nw=1.0}"
    nvl clear
    stop sound

    scene bg classroom1 at pan_to_top
    play music "music/19_playful.ogg"
    pause 0.2
    show america large d at pos_transform(x=-40, y=-150)
    $ ame.screen = 'center_3long'
    ame "そんなわけで俺とトニーは\n新しい友達のマタと\n暮らし始めたってわけだ！"

    show japan worried grimace at pos_transform(x=500, yalign=0.0) behind america
    $ jpn.screen = 'right_3'
    jpn "今のお話は私達が\n聞いてよかったので\nしょうか…？"



    show bulgaria conniving at pos_transform(x=650, yalign=0.0)
    $ bul.screen = 'right_4'
    bul "…お話しあざーっす！\n俺は何も聞いていない\n機密情報なんて\n聞いてないんだわー…"

    show finland ohdear at pos_transform(x=-50, yalign=0.0) behind america
    $ fin.screen = 'left_3'
    fin "あはは…\nきょ、今日は\n空が綺麗ですね！"

    hide finland
    hide america
    hide bulgaria
    hide japan
    pause 0.2

    jump story3