label meeting:

    ## Bulgaria NVL #######################
    scene bg hallway at pan_to_top
    show dust at dust1_transform
    show dust_1 at dust1_transform1
    show sunlight2_0 at sun_rroom1_0
    show sunlight2_1 at sun_rroom1_1
    with Dissolve(0.2)
    
    play music "music/collision_course_paolo_bolio_hq.ogg"
    pause 0.3
    show bulgaria large hmmm at dark_pos
    show nvl_textbox
    

    story "俺が怖い話を聞く司会進行役…。"

    story "…イタリアを木の枝でつつくくらいしか\n出番なかったころにしてみたら\n大躍進じゃね？。"
    
    show bulgaria large conniving
    with {'master': Dissolve(0.25)}
    story "ＷＷ２で木の枝でつつく以外にも\nわりかし何やってんだお前って\n行動してたのは国内がバラバラだったから、\nしょーがねーんだわ…。"

    nvl clear
    show bulgaria large fufufu-n
    
    story "うん。だから大目にみてにゃん。\nにゃんってつけとけば、\nだいたい許してもらえるらしいって\n誰かが言ってたにゃん。\nにゃんにゃんなんだわー。\nにゃんにゃん。
    "
    nvl clear
    hide bulgaria 
    pause 0.2
    

    scene bg hallway2 at pan_to_bottom
    with fade_white

    show dust at dust1_transform
    show dust_1 at dust1_transform1
    #show sunlight2_0 at sun_rroom1_0
    #show sunlight2_1 at sun_rroom1_1
    
    show bulgaria large hmmm at dark_pos
    show nvl_textbox
    

    story"\nにゃんにゃんしているうちに、\n俺が怖い話を聞く事になる部屋についた。"
    nvl clear

    show bulgaria large ooh
    story"ちなみに、この建物は電気の供給が止まろうが、\n何者かが乗り込んでこようが、\n何重にも非常時への対策が張られていて\n大人数でも避難しやすいように作られている。"

    show bulgaria large ah
    with {'master': Dissolve(0.25)}
    story"つまり怖い話の最中、\nイギ太郎が何かを召還しても、\nアメ助が怪力を振るおうと、\n俺の命は保証されている。…はず。"

    nvl clear
    
    story "だからドアを開けた瞬間、\nアメリカのスーパーボールが\n俺の顔面に直撃する事はないと信じたい…！"

    stop music fadeout 4
    show bulgaria large cry well
    with {'master': Dissolve(0.25)}
    story"そんなんされたら\n俺よゆうで吹き飛んじゃうんだわ…！！"
    nvl clear
    pause 0.2
    hide bulgaria 
    pause 0.2
    show white screen behind nvl_textbox
    with {'master': Dissolve(1.0)}
    play sound "sfx/door_sfx.wav"
    story"\n\n俺は意を決してドアを開ける。"
    nvl clear
    


    ## Eng Cutscene #########################################


    scene bg engdoodles at blackboard
    show upperhalf at blue_upper_half_transform
    with fade_white_slow
    play music "music/KidsTrax653_KC07-MuppetsOnTheTitanic-Julin.ogg"

    #show sunlight2
    show upperleft_yellow at upplerleft_yellow_transform
    
    show lightblue at lightblue_transform
    
    play sound "sfx/scribbles.ogg"
    queue sound ["<silence 0.11>", "sfx/footsteps.ogg"]
    play sound1 ["<silence 11.58>","sfx/ding12.ogg"]
    play sound2 ["<silence 12.98>","sfx/ding24.ogg"]

    show england large fufufu-n at eng_blackboard

    pause 15

    ## Meeting ##############################################

    scene bg classroom1
    pause 0.2
    show england blush shout2 at pos_transform(x=140, yalign=0.0)
    
    play sound ["<silence .3>", "sfx/hit32_d.ogg"]
    $ eng.screen = 'left_3'
    $ window_transform = mb_shake3
    eng"あっ、\nブルガリア…！"
    $ window_transform = None

    show bulgaria ooh at pos_transform(x=440, yalign=0.0)
    
    $ bul.screen = 'right_1'
    bul"…………。"

    show england blush shout
    play sound ["<silence 1.0>", "sfx/bang07.ogg"]
    $ eng.screen = 'left_4'
    $ window_transform = mb_shake4
    eng"いっ忙しい中、来てやったんだ。\nれれれ礼の一つでもっ\n言ってほしいものだな！"
    $ window_transform = None

    show bulgaria hey
    $ bul.screen = 'right_3'
    bul"うーい。あざーっす！\nあと微妙な似顔絵\nあざーっす！！"

    show england at s_shake_horiz
    $ eng.screen = 'left_4long'
    eng"ちげぇよ！\nこれはもう俺が来たときには\n描かれててだな！\n決して俺が描いたものじゃ…！"

    show england at stop_offset_delay
    show england at pos_transform(x=140, yalign=0.0)
    with {'master':move}
    show bulgaria conniving
    bul"イギリスさんって\n黒板見ると似顔絵\n描きたくなるタチなんすか？"

    show england blush shout3
    $ eng.screen = 'left_3'
    eng"ううっ、\nだから違う…！"

    show bulgaria hey
    bul"似顔絵あざーっす\nあざーっす！！"

    



    scene bg classroom3 at pan_to_top
    play sound ["<from 0.45 to 2>sfx/door_sfx.wav", "sfx/hallwaywalk.ogg"] fadeout 1.0 fadein 1.0
    pause 1
    show japan goodness at pos_transform(x=340, yalign=0.0)
    
    $ jpn.screen = 'center_3'
    jpn"失礼します。\nおやブルガリアさん。\nもう来てらしたんですか。"

    stop sound fadeout 4
    show japan apologies
    jpn"お待たせしてしまい\nすいません。\n今日は怖い話の会ですよね。"

    show bulgaria normal at pos_transform(x=560, yalign=0.0)
    $ bul.screen = 'right_4'
    bul"いや俺も今\n来たところなんで\n全然平気なんだわー。\n怖い話会場ここっす。"

    show bulgaria smile
    bul"そんで早速黒板に\n怪奇現象が起きたんで\nイギリスのお絵かき\n鑑賞しません？"

    show england blush shout at pos_transform(x=70, yalign=0.0) behind japan
    $ eng.screen = 'left_3'
    eng"だ…だからっ！\n描いたのは\n俺じゃないぞ！"

    show japan chuckle
    jpn"こんにちはイギリスさん。\nこれは…、なんとも\n可愛らしい絵ですね。"

    show england nostalgic laugh
    $ eng.screen = 'left_4long'
    eng"よう日本。\nふふん！俺の絵じゃないが\nそういう感想もあるな。\n俺の絵じゃないが！"

    stop music fadeout 4




    scene bg classroom_door at pan_to_top
    play sound "sfx/door_sfx.wav"
    play music "music/FilmEdge_Casual_Z008-QuirkyBounce-Sorbo.ogg" fadeout 1.0
    pause 0.5

    show germany normal at center
    
    $ ger.screen = 'center_3'
    ger"む、もうすでに\n来ていたのか。"

    show japan goodness at pos_transform(x=100, yalign=0.0) behind germany
    $ jpn.screen = 'center_3'
    jpn"ああ、ドイツさん\nこんにち…"

    show bulgaria eek at pos_transform(x=580, yalign=0.0)
    hide japan
    play sound ["<silence .5>", "sfx/bam10.ogg"]
    show bulgaria eek
     
    $ bul.screen = 'right_3'
    show bulgaria eek at s_shake3
    $ window_transform = s_shake3
    bul"ギャー！！\nドイツー！！"
    $ window_transform = None

    show germany exasperated
    ger"…なぜ、いちいち\n俺を見るたび\nお前は叫ぶんだ…。"

    show bulgaria eek at stop_offset
    show bulgaria cry waa at pos_transform(x=580, yalign=0.0)
    $ bul.screen = 'right_4'
    bul"そ、そりゃ叫びますよ！\nいづもいづも…、俺のごと\n目のかだきにする\nじゃないですかぁ…。"
    
    show bulgaria cry shout
    bul"ううう…俺だって\n頑張ってんすよぉ…。"

    show germany ohno
    $ ger.screen = 'center_4long'
    ger"あっあれは目の敵に\nしてるのではなく！"
    ger"少々貴様の成績が悪いから、\nもう少し本気を出して\n頑張ってもらいたいと思ってだな…。"

    show germany eyes-half-lidded exasperated
    ger"あー…、なんだその…、\n結果を急ぐあまり言い方が\nきつくなっていたかもしれん。\n今度からは気を付ける…。"

    show bulgaria cry thatsright
    bul"ほんどうですかっ！？\nあざーっすあざーっす！"

    show finland heynow at pos_transform(x=60, y=30) behind germany
    show finland heynow at jump
    play sound "sfx/ding30.ogg"
    
    $ fin.screen = 'left_4long'
    fin"ドイツさんまた甘やかすー。\n頑張ってるのはみんな一緒ですよ。\n厳しい事を言うのも当然です。"

    show finland heynow at stop_offset
    show finland mmmm at stop_offset
    show finland mmmm at pos_transform(x=60, y=30)
    with move
    fin"ブッさんもドイツさんの\n愛の鞭だと思って\n受け止めてくださいよう。"

    show bulgaria guh
    play sound ["<silence .7>", "sfx/hit22.ogg"]
    $ window_transform = mb_shake5
    $ bul.screen = 'right_4long'
    bul"ぐあっ！\n正論直で打ち込むの\n止めてください！！\nその通りでございます！"
    hide bulgaria
    $ window_transform = None
    with {'master': Dissolve(0.3)}

    show england fufufu-n2 at pos_transform(x=580, yalign=0.0)
    $ eng.screen = 'right_4'
    eng"フィンランド。\nこいつダメなやつほど\n過保護になる癖があるんだ\nわかってやれ。"

    show finland nnh
    fin"…あっ。そうでしたか…！\nごめんなさい！\nドイツさんの好きなものに\n口挟むなんて無粋な真似を…！"

    show finland smiling
    $ fin.screen = 'left_4long'
    fin"あっ！たしかに僕も、\nちょっとダメな所があった方が\n可愛いなぁって思いますよ！ええ！"

    show germany shocked whatsthat
    play sound ["<silence .3>", "sfx/hit34.ogg"]
    $ ger.screen = 'center_4long'
    $ window_transform = mb_shake6
    ger "ちょっと待て！\nその言い方だと俺がダメなヤツに弱い\nダメな奴みたいではないか！"
    $ window_transform = None

    show england smirksmirk
    $ eng.screen = 'right_1'
    eng "その通りだろ？"

    show germany blush yell
    stop music fadeout 4
    play sound ["sfx/footsteps.ogg", "sfx/footsteps_arriving.ogg"]
    ger "だ…断じて\nそのような事はない！\n…むっ？"

    scene bg classroom_window at pan_to_top
    play sound "sfx/door_sfx.wav"
    play music "music/International_Uplifting_Dance-full_length_track.ogg"
    pause 0.3
    show america med normal at pos_transform(x=100, y=-50)
    show aphrodite 2 behind america at aphro_intro
    show bear_grylls 2 behind america at bear_intro
    show jeremy 2 behind bear_grylls at jeremy_intro
    $ ame.screen = 'center_4long'
    ame "Ｈｅｙ！今日怖い話をするって\n聞いてたんだけど会場は\nここでいいのかい！？"

    scene bg classroom3 at pan_to_top
    pause 0.1
    show japan goodness at pos_transform(x=500, yalign=0.0)
    show finland nnh at pos_transform(x=60, y=30)
    

    $ jpn.screen = 'right_3'
    jpn "はっ、アメリカさん！\nどうもこんにち……"

    show finland ohdear
    
    play sound ["<silence .3>","sfx/ding48.ogg"]
    $ fin.screen = 'left_1'
    $ window_transform = mb_shake7
    fin "えっ、もしかして…！"
    $ window_transform = None

    scene bg classroom_door at pan_to_top
    show america med smiling at pos_transform(x=100, y=-60)
    
    show aphrodite 1 behind america at aphro_intro
    show bear_grylls 1 behind america at bear_intro
    show jeremy 1 behind bear_grylls at jeremy_intro
    
    play sound ["<silence 2>","sfx/gun14_c.ogg"]
    $ fin.screen = 'left_4long'
    $ window_transform = mb_shake8
    fin "えっその後ろの方…\nアフ○ダイテ・ジョーンズ！？\nジェレ○ー・ウェイド…\nとベア・グリ○ス…じゃないですか！？"
    $ window_transform = None

    scene bg classroom1 at pan_to_bottom
    show america freedom smile at center
    
    show aphrodite 1 behind america at aphro_intro
    show bear_grylls 1 behind america at bear_intro
    show jeremy 1 behind bear_grylls at jeremy_intro

    $ ame.screen = 'center_4long'
    ame "よく気が付いたね！今日のために\nホラーのスペシャルメンバーを\n集めてきたんだよ！！"

    show england white-eyed shout at pos_transform(x=100, yalign=0.0) behind america
    
    $ eng.screen = 'left_4'
    play sound ["<silence .8>","sfx/hit34.ogg"]
    $ window_transform = s_shake4
    eng "ホラーっぽいのは\n最初の一人だけだろ！！\nそれに他二人は\nイギリス人じゃねーか！"
    $ window_transform = None

    show america hahahaha
    
    $ ame.screen = 'center_4long'
    ame "ノープロブレムだぞ！\n彼らの話す怖い話に\n期待しててくれよみんな！\n俺も楽しみだぞ！"

    show finland ohdear at pos_transform(xalign=1.0, yalign=0.0, yoffset=30) behind america
    
    show finland at jump2
    $ fin.screen = 'right_1'
    play sound ["<silence .3>","sfx/ding78.ogg"]
    fin "わーっ！わーっ！"
    
    play music "music/19_playful.ogg" fadeout 1.0
    scene bg classroom4 at pan_to_top
    show bulgaria ooh at pos_transform(x=500, yalign=0.0)
    
    $ bul.screen = 'right_4'
    bul "あっ、ルーマニアいわく\n今回俺ら国限定らしいんで\nそのかたら帰ってもらっても\nよろしいっすか？"

    show america med whatyousay at pos_transform(x=200, y=-70)
    
    $ ame.screen = 'center_3long'
    play sound ["<silence .9>", "sfx/hit34.ogg"]
    $ window_transform = mb_shake9
    ame "なんだってっ！？\n君は彼らの怖い話を\n聞きたくないのかい…！？"
    $ window_transform = None

    show finland curious at pos_transform(x=700, y=30) behind bulgaria
    
    show finland at jump3
    play sound ["<silence .3>", "sfx/ding11.ogg"]
    $ fin.screen = 'right_3'
    fin "うわあああ、\n僕は聞きたいです！"

    show finland at stop_offset
    show bulgaria smile
    
    bul "国際怖い話なんで\nアメリカさんの口から\n聞かせて下さいっす！"
    
    show america med sup eyesclosed
    
    $ ame.screen = 'center_1'
    ame "…ＯＫ。分かったよ。"
    hide bulgaria
    hide finland
    

    show america sigh
    $ ame.screen = 'left_4'
    ame "今日はありがとう。"
    $ _skip_appear_effect = True
    show aphrodite 1 behind america at pos_transform(xoffset=-20, yalign=0)
    with {'master': Dissolve(1.0)}
    extend "\nアフロ○イテ…。"
    show jeremy 1 behind aphrodite at pos_transform(xoffset=100, yalign=0)
    with {'master': Dissolve(1.0)}   
    extend "ジェレ○ー…。"
    show bear_grylls 1 behind america at pos_transform(xoffset=600, yalign=0)
    with {'master': Dissolve(1.0)}
    extend "\nベア・グリ○ス…。"
    $ ame.screen = 'left_4'
    extend "\nみんな、死なないでくれ。"
    $ _skip_appear_effect = False
    

    show america med cry
    with {'1': Dissolve(0.2)}
    hide aphrodite 1
    hide bear_grylls 1
    hide jeremy 1
    with {'master': Dissolve(1.0)}
    $ ame.screen = 'center_3'
    ame "Ｓｅｅ　ｙｏｕ…みんな…。"

    hide aphrodite 1
    hide bear_grylls 1
    hide jeremy 1

    show america med sigh
    show finland nyaaaa at pos_transform(x=30, y=30) behind america
    show finland at jump4
    
    play sound ["<silence 1.2>", "sfx/ding12.ogg"]
    $ fin.screen = 'left_4long'
    fin "すごいです！実物初めて見ました！\nすぐ行っちゃいましたけど…！\n僕けっこうアメリカさんの家の\nテレビ見る方なので嬉しかったです！"
    show finland at stop_offset

    show england med fu-n at pos_transform(x=580, y=-70)
    
    $ eng.screen = 'right_4long'
    eng "それでそんなに興奮してたのか…。\nそういえばフィンランドが作る\nテレビ番組ってなんかゆるいよな…。"

    show finland smileee
    
    $fin.screen = 'left_3'
    fin "はい。ずっと見てると\n脳がとろけそうになると\n皆さんから好評頂いてます。"

    show england med mmm
    
    $ eng.screen = 'right_1'
    eng "好評…？"

    scene bg classroom3 at pan_to_top
    
    pause 0.2
    show japan ummm at pos_transform(x=370, yalign=0.0)
    
    $ jpn.screen = 'right_4long'
    jpn "すいません、みなさん。\n私のタイミングが悪く…\n挨拶をしそびれてしまいましたので\n改めて挨拶させてください。"

    show finland smiling at pos_transform(x=-80, y=30) behind japan
    
    $ fin.screen = 'left_3'
    fin "あっ僕こそすいません！\nモイっ！日本さん"

    show america d at pos_transform(x=60, yalign=0.0) behind japan
    
    $ ame.screen = 'left_1'
    ame "Ｈｅｌｌｏ！日本！"

    show england fu-n at pos_transform(x=500, yalign=0.0)
    
    $ eng.screen = 'right_1'
    eng "よう、日本。{size=-8}セカンド。{/size}"

    show germany chuckle at pos_transform(x=630, yalign=0.0) behind england
    
    $ ger.screen = 'right_3'
    ger "日本、今日は\nよろしく頼む。"

    show japan shocked shy
    
    $ jpn.screen = 'center_3'
    jpn "いっ…一斉！？\n…ありがとうございます。\n宜しくお願い致します。"

    scene bg classroom_window at pan_to_top
    
    pause 0.2
    show bulgaria normal at pos_transform(x=140, yalign=0.0)
    
    $ bul.screen = 'left_3'
    bul "どうもどうもなんだわー。\nって俺は二回目っすね。"

    show japan contemplation at pos_transform(x=550, yalign=0.0)
    show japan at bow
    $ jpn.screen = 'right_3'
    jpn "ええ、二回目ですが、\n改めまして宜しく\nお願い致します。"


    show bulgaria fufufu-n
    
    bul "どもどもです…。"


    stop music fadeout 4
    scene bg classroom2 at pan_to_bottom1
    
    play sound "sfx/birdcalls.ogg"
    pause 0.2
    $ bul.screen = 'center_3'
    bul "で…時間を２０分も\nオーバーしてるのに\n２人も来ないんだわ…。"

    $ eng.screen = 'right_4long'
    eng "一人スペインだろ？\nあいつが重要なビジネスの事と\n親分面できること以外で\n時間通りに来ると思うなよ。"

    $ ame.screen = 'center_3long'
    ame"彼なら今カフェで\n日光浴してるんじゃないかな？\nもうすぐにでも始めないかい？"

    $ bul.screen = 'center_3'
    bul "うーい。\nじゃ、はじめまーす。"

    $ eng.screen = 'right_3'
    play sound ["<silence .3>", "sfx/hit32_d.ogg"] fadeout 1.0
    $ window_transform = mb_shake10
    eng "怖い話の始まりが\nそんなけだるげで\n良いのかよ！？"
    $ window_transform = None
    pause 0.5

    scene bg exterior8 at pan_to_top
    #show sunlight2
    with fade_white
    na "こうして国際怖い話の会は\nふわふわした感じで始まったのだった…。"
    pause 0.5

    jump story1