label meeting:

    ## Bulgaria NVL #######################
    scene bg hallway
    with Dissolve(0.2)
    
    play music "music/collision_course_paolo_bolio_hq.ogg"
    pause 0.3
    show bulgaria large hmmm at dark_pos
    show nvl_textbox
    

    story "俺が怖い話を聞く司会進行役…。" id meeting_6f284491

    story "…イタリアを木の枝でつつくくらいしか\n出番なかったころにしてみたら\n大躍進じゃね？。" id meeting_f770514f
    
    show bulgaria large conniving
    with {'master': Dissolve(0.25)}
    story "ＷＷ２で木の枝でつつく以外にも\nわりかし何やってんだお前って\n行動してたのは国内がバラバラだったから、\nしょーがねーんだわ…。" id meeting_d12d006f

    nvl clear
    show bulgaria large heheh
    
    story "うん。だから大目にみてにゃん。\nにゃんってつけとけば、\nだいたい許してもらえるらしいって\n誰かが言ってたにゃん。\nにゃんにゃんなんだわー。\nにゃんにゃん。" id meeting_067e54c7

    nvl clear
    hide bulgaria 
    pause 0.2
    
    ## New scene
    scene bg hallway2
    with fade_white

    
    show bulgaria large hmmm at dark_pos
    show nvl_textbox
    

    story "\nにゃんにゃんしているうちに、\n俺が怖い話を聞く事になる部屋についた。" id meeting_d194fa59
    nvl clear

    show bulgaria large ooh
    story "ちなみに、この建物は電気の供給が止まろうが、\n何者かが乗り込んでこようが、\n何重にも非常時への対策が張られていて\n大人数でも避難しやすいように作られている。" id meeting_26cd72cd

    show bulgaria large ah
    with {'master': Dissolve(0.25)}
    story "つまり怖い話の最中、\nイギ太郎が何かを召還しても、\nアメ助が怪力を振るおうと、\n俺の命は保証されている。…はず。" id meeting_105c1e3d

    nvl clear
    
    story "だからドアを開けた瞬間、\nアメリカのスーパーボールが\n俺の顔面に直撃する事はないと信じたい…！" id meeting_fe4be6ef

    stop music fadeout 4
    show bulgaria large cry well
    with {'master': Dissolve(0.25)}
    story"そんなんされたら\n俺よゆうで吹き飛んじゃうんだわ…！！" id meeting_53fca0aa
    nvl clear
    pause 0.2
    hide bulgaria 
    pause 0.2
    show white screen behind nvl_textbox
    with {'master': Dissolve(1.0)}
    play sound "sfx/door_sfx.wav"
    story"\n\n俺は意を決してドアを開ける。" id meeting_9c59d4bd
    nvl clear
    


    ## Eng Cutscene #########################################

    $ quick_menu = False
    scene bg engdoodles
    with fade_white_slow
    play music "music/KidsTrax653_KC07-MuppetsOnTheTitanic-Julin.ogg"

    
    play sound "sfx/scribbles.ogg"
    queue sound ["<silence 0.11>", "sfx/footsteps.ogg"]
    play sound1 ["<silence 11.58>","sfx/ding12.ogg"]
    play sound2 ["<silence 12.98>","sfx/ding24.ogg"]

    show england large heheheh at eng_blackboard
    pause 15
    stop sound
    stop sound1
    stop sound2

    ## Meeting ##############################################

    scene bg classroom1
    $ quick_menu = True
    pause 0.2
    show england blush shout2 at pos_transform(xpos=140, yalign=0.0)
    
    
    $ eng.screen = 'left_3'
    $ _pending_window_transform = (shake_0m1)
    $ _pending_sound = ("sfx/hit32_d.ogg", "sound")
    eng "あっ、\nブルガリア…！" id meeting_6fdf6096
    stop sound

    show bulgaria ooh at pos_transform(xpos=440, yalign=0.0)
    
    $ bul.screen = 'right_1'
    bul "…………。" id meeting_28ca9edf

    show england blush shout
    $ eng.screen = 'left_4'
    $ _pending_window_transform = (shake_0m2)
    $ _pending_sound = ("sfx/bang07.ogg", "sound")
    eng "いっ忙しい中、来てやったんだ。\nれれれ礼の一つでもっ\n言ってほしいものだな！" id meeting_c63ce14a
    stop sound

    show bulgaria hey
    $ bul.screen = 'right_3'
    bul "うーい。あざーっす！\nあと微妙な似顔絵\nあざーっす！！" id meeting_11c14e61

    show england:
        0.1
        block:
            linear 0.15 xoffset +10
            linear 0.15 xoffset -10
            repeat
    $ eng.screen = 'left_4long'
    eng "ちげぇよ！\nこれはもう俺が来たときには\n描かれててだな！\n決して俺が描いたものじゃ…！" id meeting_4577a2fc

    show england at stop_offset_delay
    show england at pos_transform(xpos=140, yalign=0.0)
    with {'master':move}
    show bulgaria conniving
    bul "イギリスさんって\n黒板見ると似顔絵\n描きたくなるタチなんすか？" id meeting_93aa6207

    show england blush shout3
    $ eng.screen = 'left_3'
    eng "ううっ、\nだから違う…！" id meeting_c56e9700

    show bulgaria hey
    bul "似顔絵あざーっす\nあざーっす！！" id meeting_67061957


    ## New scene
    scene bg classroom3 at pan_to_top
    play sound ["<from 0.45 to 2>sfx/door_sfx.wav", "sfx/hallwaywalk.ogg"] fadeout 1.0 fadein 1.0
    pause 1
    show japan goodness at pos_transform(xpos=340, yalign=0.0)
    
    $ jpn.screen = 'center_3'
    jpn "失礼します。\nおやブルガリアさん。\nもう来てらしたんですか。" id meeting_ac6e7fc8

    stop sound fadeout 4
    show japan apologies
    $ jpn.screen = 'center_3'
    jpn "お待たせしてしまい\nすいません。\n今日は怖い話の会ですよね。" id meeting_ae0e0230

    show bulgaria normal at pos_transform(xpos=560, yalign=0.0)
    $ bul.screen = 'right_4'
    bul "いや俺も今\n来たところなんで\n全然平気なんだわー。\n怖い話会場ここっす。" id meeting_ccf88991

    show bulgaria smile
    bul "そんで早速黒板に\n怪奇現象が起きたんで\nイギリスのお絵かき\n鑑賞しません？" id meeting_66f0dfe9

    show england blush shout at pos_transform(xpos=70, yalign=0.0) behind japan
    $ eng.screen = 'left_3'
    eng "だ…だからっ！\n描いたのは\n俺じゃないぞ！" id meeting_2c8beb39

    show japan chuckle
    $ jpn.screen = 'center_3'
    jpn "こんにちはイギリスさん。\nこれは…、なんとも\n可愛らしい絵ですね。" id meeting_d497e58c

    show england nostalgic laugh
    $ eng.screen = 'left_4long'
    eng "よう日本。\nふふん！俺の絵じゃないが\nそういう感想もあるな。\n俺の絵じゃないが！" id meeting_1049dc72

    stop music fadeout 4



    ## New scene
    scene bg classroom_door at pan_to_top
    play sound "sfx/door_sfx.wav"
    play music "music/FilmEdge_Casual_Z008-QuirkyBounce-Sorbo.ogg" fadeout 1.0
    pause 0.5

    show germany normal at center
    
    $ ger.screen = 'center_3'
    ger "む、もうすでに\n来ていたのか。" id meeting_f507db78

    show japan goodness at pos_transform(xpos=100, yalign=0.0) behind germany
    $ jpn.screen = 'center_3'
    jpn "ああ、ドイツさん\nこんにち…" id meeting_a2386473

    show bulgaria eek at pos_transform(xpos=580, yalign=0.0)
    hide japan
    play sound ["<silence .5>", "sfx/bam10.ogg"]
     
    $ bul.screen = 'right_3'
    show bulgaria eek
    $ _pending_window_transform = (shake_0m9)
    $ _pending_sprite_transform = [("bulgaria", shake_0m9)]
    bul "ギャー！！\nドイツー！！" id meeting_aa6f5c9e
    stop sound

    show germany exasperated
    $ ger.screen = 'center_3'
    ger "…なぜ、いちいち\n俺を見るたび\nお前は叫ぶんだ…。" id meeting_017512fd

    show bulgaria eek at stop_offset
    show bulgaria cry waa at pos_transform(xpos=580, yalign=0.0)
    $ bul.screen = 'right_4'
    bul "そ、そりゃ叫びますよ！\nいづもいづも…、俺のごと\n目のかだきにする\nじゃないですかぁ…。" id meeting_8bc364fe
    
    show bulgaria cry shout
    $ bul.screen = 'right_4'
    bul "ううう…俺だって\n頑張ってんすよぉ…。" id meeting_1b4aaa87

    show germany ohno
    $ ger.screen = 'center_4long'
    ger "あっあれは目の敵に\nしてるのではなく！" id meeting_c7cb7a8f
    $ ger.screen = 'center_4long'
    ger "少々貴様の成績が悪いから、\nもう少し本気を出して\n頑張ってもらいたいと思ってだな…。" id meeting_6a78162d

    show germany squint exasperated
    $ ger.screen = 'center_4long'
    ger "あー…、なんだその…、\n結果を急ぐあまり言い方が\nきつくなっていたかもしれん。\n今度からは気を付ける…。" id meeting_7888aea4

    show bulgaria cry thatsright
    $ bul.screen = 'right_4'
    bul "ほんどうですかっ！？\nあざーっすあざーっす！" id meeting_ed02d8a3

    show finland heynow behind germany:
        xpos 60 ypos 30
        time 0.1
        block:
            easeout 0.3 yoffset -100
            easein 0.2 yalign 0.0 yoffset +40
            easeout 0.2 yoffset 0
    play sound "sfx/ding30.ogg"
    $ fin.screen = 'left_4long'
    fin "ドイツさんまた甘やかすー。\n頑張ってるのはみんな一緒ですよ。\n厳しい事を言うのも当然です。" id meeting_7d12a595
    stop sound

    show finland mmmm
    fin "ブッさんもドイツさんの\n愛の鞭だと思って\n受け止めてくださいよう。" id meeting_8399c926

    show bulgaria guh
    $ bul.screen = 'right_4long'
    $ _pending_window_transform = (shake_0m3)
    $ _pending_sound = ("sfx/hit22.ogg", "sound")
    bul "ぐあっ！\n正論直で打ち込むの\n止めてください！！\nその通りでございます！" id meeting_a79f8310
    hide bulgaria with {'master': Dissolve(0.3)}
    stop sound

    show england heheheh2 at pos_transform(xpos=580, yalign=0.0)
    $ eng.screen = 'right_4'
    eng "フィンランド。\nこいつダメなやつほど\n過保護になる癖があるんだ\nわかってやれ。" id meeting_70190d88

    show finland nnh
    fin "…あっ。そうでしたか…！\nごめんなさい！\nドイツさんの好きなものに\n口挟むなんて無粋な真似を…！" id meeting_ffe5f0ec

    show finland smiling
    $ fin.screen = 'left_4long'
    fin "あっ！たしかに僕も、\nちょっとダメな所があった方が\n可愛いなぁって思いますよ！ええ！" id meeting_8c935a5a

    show germany shocked whatsthat
    
    $ ger.screen = 'center_4long'
    $ _pending_window_transform = (shake_0m4)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    ger "ちょっと待て！\nその言い方だと俺がダメなヤツに弱い\nダメな奴みたいではないか！" id meeting_0c6d0b4d
    stop sound

    show england smirksmirk
    $ eng.screen = 'right_1'
    eng "その通りだろ？" id meeting_d33e8482

    show germany blush yell
    stop music fadeout 4
    play sound ["sfx/footsteps.ogg", "sfx/footsteps_arriving.ogg"]
    ger "だ…断じて\nそのような事はない！\n…むっ？" id meeting_d063b29e

    ## New scene
    scene bg classroom_window at pan_to_top
    play sound "sfx/door_sfx.wav"
    play music "music/International_Uplifting_Dance-full_length_track.ogg"
    pause 0.3
    show america med normal at pos_transform(xpos=100, ypos=-50)
    show aphrodite 2 behind america at aphro_intro
    show bear_grylls 2 behind america at bear_intro
    show jeremy 2 behind bear_grylls at jeremy_intro
    $ ame.screen = 'center_4long'
    ame "Ｈｅｙ！今日怖い話をするって\n聞いてたんだけど会場は\nここでいいのかい！？" id meeting_25982e53

    ## New scene
    scene bg classroom3 at pan_to_top
    pause 0.1
    
    show finland nnh at pos_transform(xpos=60, ypos=30)
    
    show japan goodness at pos_transform(xpos=500, yalign=0.0)
    $ jpn.screen = 'right_3'
    jpn "はっ、アメリカさん！\nどうもこんにち……" id meeting_ba69b9b0

    show finland ohdear
    $ fin.screen = 'left_1'
    $ _pending_window_transform = (shake_0m5)
    $ _pending_sprite_transform = [("finland", shake_0m5)]
    $ _pending_sound = ("sfx/ding48.ogg", "sound")
    fin "えっ、もしかして…！" id meeting_cfbaf66c
    stop sound

    ## New scene
    scene bg classroom_door at pan_to_top
    show america med smiling at pos_transform(xpos=100, ypos=-60)
    
    show aphrodite 1 behind america at aphro_intro
    show bear_grylls 1 behind america at bear_intro
    show jeremy 1 behind bear_grylls at jeremy_intro
    
    
    $ fin.screen = 'left_4long'
    $ _pending_window_transform = (shake_0m6)
    $ _pending_sound = ("sfx/gun14_c.ogg", "sound")
    fin "えっその後ろの方…\nアフ○ダイテ・ジョーンズ！？\nジェレ○ー・ウェイド…\nとベア・グリ○ス…じゃないですか！？" id meeting_78fe9b40
    stop sound

    ## New scene
    scene bg classroom1 at pan_to_bottom
    show america howdy at center
    
    show aphrodite 1 behind america at aphro_intro
    show bear_grylls 1 behind america at bear_intro
    show jeremy 1 behind bear_grylls at jeremy_intro

    $ ame.screen = 'center_4long'
    ame "よく気が付いたね！今日のために\nホラーのスペシャルメンバーを\n集めてきたんだよ！！" id meeting_0a9eaa0c

    show england scream at pos_transform(xpos=100, yalign=0.0) behind america
    
    $ eng.screen = 'left_4'
    $ _pending_window_transform = (shake_0m10)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    eng "ホラーっぽいのは\n最初の一人だけだろ！！\nそれに他二人は\nイギリス人じゃねーか！" id meeting_38b36246
    stop sound

    show america hahahaha
    
    $ ame.screen = 'center_4long'
    ame "ノープロブレムだぞ！\n彼らの話す怖い話に\n期待しててくれよみんな！\n俺も楽しみだぞ！" id meeting_4c2bc1e7
    
    show finland ohdear behind america at pos_transform(xalign=1.0, ypos=30)
    $ fin.screen = 'right_1'
    $ _pending_sprite_transform = [("finland", fin_m1)]
    $ _pending_sound = ("sfx/ding78.ogg", "sound")
    fin "わーっ！わーっ！" id meeting_419fd707
    
    play music "music/19_playful.ogg" fadeout 1.0
    stop sound

    ## New scene
    scene bg classroom_door2 at pan_to_top
    show bulgaria ooh at pos_transform(xpos=500, yalign=0.0)
    
    $ bul.screen = 'right_4'
    bul "あっ、ルーマニアいわく\n今回俺ら国限定らしいんで\nそのかたら帰ってもらっても\nよろしいっすか？" id meeting_a21737bc

    show america med whatyousay at pos_transform(xpos=200, ypos=-70)
    
    $ ame.screen = 'center_3long'
    $ _pending_window_transform = (shake_0m11)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    ame "なんだってっ！？\n君は彼らの怖い話を\n聞きたくないのかい…！？" id meeting_3ca06ef2
    stop sound

    show finland curious at pos_transform(xpos=700, ypos=30) behind bulgaria
    
    $ fin.screen = 'right_3'
    $ _pending_sprite_transform = [("finland", fin_m2)]
    $ _pending_sound = ("sfx/ding11.ogg", "sound")
    fin "うわあああ、\n僕は聞きたいです！" id meeting_9ae7959c
    stop sound

    show bulgaria smile
    
    bul "国際怖い話なんで\nアメリカさんの口から\n聞かせて下さいっす！" id meeting_7f59d522
    
    show america med sup eyesclosed
    
    $ ame.screen = 'center_1'
    ame "…ＯＫ。分かったよ。" id meeting_6c742b57
    hide bulgaria
    hide finland
    

    show america sigh
    $ ame.screen = 'left_4'
    $ _skip_appear_effect = True
    ame "今日はありがとう。{nw=1}" id meeting_edb082a2
    show aphrodite 1 behind america at pos_transform(xoffset=-20, yalign=0)
    with {'master': Dissolve(1.0)}
    extend "\nアフロ○イテ…。{nw=1}" id meeting_c494b965
    show jeremy 1 behind aphrodite at pos_transform(xoffset=100, yalign=0)
    with {'master': Dissolve(1.0)}   
    extend "ジェレ○ー…。{nw=1}" id meeting_d9ad4b8f
    show bear_grylls 1 behind america at pos_transform(xoffset=600, yalign=0)
    with {'master': Dissolve(1.0)}
    extend "\nベア・グリ○ス…。{nw=1}" id meeting_948f9926
    $ ame.screen = 'left_4'
    extend "\nみんな、死なないでくれ。" id meeting_c1259a18
    $ _skip_appear_effect = False
    

    show america med cry
    $ ame.screen = 'center_3'
    $ _pending_sprite_transform = [("aphrodite 1", hide_celeb), ("bear_grylls 1", hide_celeb), ("jeremy 1", hide_celeb)]
    ame "Ｓｅｅ　ｙｏｕ…みんな…。" id meeting_84f52b83

    hide aphrodite 1
    hide bear_grylls 1
    hide jeremy 1

    show america med sigh
    show finland nyaaaa at pos_transform(xpos=30,ypos=30) behind america
    $ fin.screen = 'left_4long'
    $ _pending_sprite_transform = [("finland", fin_m3, Dissolve(0.2))]
    $ _pending_sound = ("sfx/ding12.ogg", "sound")
    fin "すごいです！実物初めて見ました！\nすぐ行っちゃいましたけど…！\n僕けっこうアメリカさんの家の\nテレビ見る方なので嬉しかったです！" id meeting_83310ae5
    stop sound

    show england med hm at pos_transform(xpos=580, ypos=-70)
    $ eng.screen = 'right_4long'
    eng "それでそんなに興奮してたのか…。\nそういえばフィンランドが作る\nテレビ番組ってなんかゆるいよな…。" id meeting_038dc829

    show finland smileee
    
    $fin.screen = 'left_3'
    fin "はい。ずっと見てると\n脳がとろけそうになると\n皆さんから好評頂いてます。" id meeting_6dc2756c

    show england med mmm
    
    $ eng.screen = 'right_1'
    eng "好評…？" id meeting_91e8c642

    ## New scene
    scene bg classroom3
    
    pause 0.2
    show japan ummm at pos_transform(xpos=370, yalign=0.0)
    
    $ jpn.screen = 'right_4long'
    jpn "すいません、みなさん。\n私のタイミングが悪く…\n挨拶をしそびれてしまいましたので\n改めて挨拶させてください。" id meeting_18b5414e

    show finland smiling at pos_transform(xpos=-80, ypos=30) behind japan
    
    $ fin.screen = 'left_3'
    fin "あっ僕こそすいません！\nモイっ！日本さん" id meeting_1cc65628

    show america eksdee at pos_transform(xpos=60, yalign=0.0) behind japan
    
    $ ame.screen = 'left_1'
    ame "Ｈｅｌｌｏ！日本！" id meeting_444b0c42

    show england hm at pos_transform(xpos=500, yalign=0.0)
    
    $ eng.screen = 'right_1'
    eng "よう、日本。{size=-8}セカンド。{/size}" id meeting_353efc4b

    show germany chuckle at pos_transform(xpos=630, yalign=0.0) behind england
    
    $ ger.screen = 'right_3'
    ger "日本、今日は\nよろしく頼む。" id meeting_dbc0159a

    show japan shocked shy
    
    $ jpn.screen = 'center_3'
    jpn "いっ…一斉！？\n…ありがとうございます。\n宜しくお願い致します。" id meeting_e4ee19e9

    ## New scene
    scene bg classroom_window
    
    pause 0.2
    show bulgaria normal at pos_transform(xpos=140, yalign=0.0)
    
    $ bul.screen = 'left_3'
    bul "どうもどうもなんだわー。\nって俺は二回目っすね。" id meeting_ddcfcc6f

    show japan contemplation at pos_transform(xpos=550, yalign=0.0)
    $ jpn.screen = 'right_3'
    $ _pending_sprite_transform = [("japan", bow)]
    jpn "ええ、二回目ですが、\n改めまして宜しく\nお願い致します。" id meeting_14004e94


    show bulgaria heheh
    $ bul.screen = 'left_3'
    $ _pending_sprite_transform = [("bulgaria", bow)]
    bul "どもどもです…。" id meeting_e99f73e0


    stop music fadeout 4
    ## New scene
    scene bg classroom2
    
    play sound "sfx/birdcalls.ogg"
    pause 0.2
    $ bul.screen = 'center_3'
    bul "で…時間を２０分も\nオーバーしてるのに\n２人も来ないんだわ…。" id meeting_72ae2573

    $ eng.screen = 'right_4long'
    eng "一人スペインだろ？\nあいつが重要なビジネスの事と\n親分面できること以外で\n時間通りに来ると思うなよ。" id meeting_0bb90662

    $ ame.screen = 'center_3long'
    ame"彼なら今カフェで\n日光浴してるんじゃないかな？\nもうすぐにでも始めないかい？" id meeting_9630bdc7

    $ bul.screen = 'center_3'
    bul "うーい。\nじゃ、はじめまーす。" id meeting_c9537931

    $ eng.screen = 'right_3'
    stop sound fadeout 1.0
    $ _pending_window_transform = (shake_0m8)
    $ _pending_sound = ("sfx/hit32_d.ogg", "sound")
    eng "怖い話の始まりが\nそんなけだるげで\n良いのかよ！？" id meeting_8b295b55
    pause 0.5
    stop sound

    ## New scene
    scene bg exterior8 at pan_to_top
    #show sunlight2
    with fade_white
    na "こうして国際怖い話の会は\nふわふわした感じで始まったのだった…。" id meeting_831123b5
    pause 0.5

    jump story1