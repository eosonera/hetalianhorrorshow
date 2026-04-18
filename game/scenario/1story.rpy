

label story1:
    stop music
    scene bg exterior6
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第一話　フィンランドの怖い話。{/size}" id story1_18244fb9

    show white screen onlayer bottom
    
    scene bg classroom1

    play music "music/orchestral_interlude_the_bar_chord_hq.ogg"
    pause 0.2
    show finland large normal at pos_transform(xpos=450, ypos=-40)
    show nvl_textbox


    story "わっ、僕が一番でいいのでしょうか？\nヨーロッパや北欧の国の名前並べる時\nいつも僕は中頃か後ろだったりするので、\n一番目ってちょっと嬉しいですね。" id story1_eb82e6d4
    nvl clear

    show finland large nnh
    with {'master': Dissolve(0.2)}

    story "あっブっさん一つ聞いても？\n怖い話ってやはり幽霊的なものですか？\nそれとも人間が怖い話ですか？" id story1_3dea0bd1

    story "{color=#C0C0C0}「怖かったら何でもいいっすよ」{/color}" id story1_e584c917

    nvl clear

    show finland large smiling
    with {'master': Dissolve(0.2)}
    story "そうですか！\nでしたらちょうど良い話があります" id story1_dd069e56
    nvl clear

    scene bg forest2
    show nvl_textbox
    

    story "あれは初冬の事でした…。\n\n僕の家は冬になるとお日様が\nほとんど見えなくなります。" id story1_9722ed60
    nvl clear

    scene bg forest3
    show nvl_textbox
    

    story "お日様が見えないと、\nなんだか気分も落ち込みます。" id story1_39460519

    show bg forest4 behind nvl_textbox
    with {'master': Dissolve(0.3)}

    story "だからそんな日は人や機械や人工物が\n全く見えない場所に行きたくなるんですよね。\nだからちょっとの食料とコーヒーをもって\n僕は森に入ったんです…。" id story1_98bdc12e
    nvl clear

    scene bg classroom1
    show bulgaria stumped at pos_transform(xpos=440, yalign=0.0)
    

    $ bul.screen = 'right_1'
    bul "なにそれ怖い" id story1_f2c37f86

    show finland ummm at pos_transform(xpos=60, ypos=30)
    

    $ fin.screen = 'left_3'
    fin "えええっ！？\nぼ、僕まだ怖い話\n言ってないですよ…？" id story1_3cb4343e

    scene bg forest1
    show nvl_textbox
    

    story "ごっほん、それでですねー。\n僕は数日分の食料を詰め込み、\n森の中を進みました。" id story1_25772a1d
    story "日が出てるのは数時間ですから、\n野宿する場所を早く\n見つけなければなりません。" id story1_9f6fb536

    nvl clear

    story "\n自然の中って、いいですよ。" id story1_4bb829d1
    story "森に入っていくときの苔を踏む音。\n苔って種類によって\n踏んだ時の音が違うんです。" id story1_4ec0b15b
    story "さくさく。\nぎゅっぎゅっ。\nざく、ざく。\nもふっもふっ。" id story1_515c0840
    story "僕はざくざく派です！" id story1_9bbe293f

    nvl clear

    scene bg forest3
    show nvl_textbox
    

    story "紅葉の季節も終わり、\n森は灰色っぽくなりましたが、\n苔やベリーの木にはまだ色があって、\n音と色を楽しみながら\n森を進むのも良い物です。" id story1_3db3c991
    story "聞こえるのは自分の息と服の音、足音。\nそれから時々鳥の声。\n沢山の音であふれた生活が\n遠い昔のようです。" id story1_71bb5559
    
    nvl clear

    scene bg classroom1
    show finland large giggle at pos_transform(xpos=440, ypos=-20)
    show nvl_textbox
    
   
    story "途中、森と同じ色をした\nカモシカ君に出会い手を振ると\n目線で挨拶を返してくれます。\n良い子たちなんですよ。" id story1_5fc0b86d

    nvl clear

    show finland large nnh
    with {'master': Dissolve(0.2)}

    story "あっでもヘラジカ君には\n気を付けて下さいね。\nヘラジカ君酔った勢いで\n人跳ねますから…。\n\n毎年僕も跳ねられるんですよね…。\n強すぎます…。" id story1_57025bb1
    nvl clear
    

    scene bg night
    show nvl_textbox
    

    story "トコトコ歩いていくと\nちょうど良いくぼみがありまして\n僕はそこで数日間過ごすことにしました。" id story1_40ae678a
    
    show bg stars behind nvl_textbox
    with {'master': Dissolve(0.3)}   
    
    story "森の中の夜もいいんですよ。\n夜はとっても長いんですけど、\n音も空も昼間より賑やかになります。" id story1_67044706

    nvl clear

    story "\nフクロウの声があちこちから聞こえて、\n時々はもってなんだか合唱してるみたいです。\n空にはたくさんの星が目に見えない速度で\nぐるーっと回ります。" id story1_3d7cb46b
    story "僕たちからすれば空に描いた光る点々でも、\n一つ一つが大きな星なんですよね…。\n宇宙は大きいなぁ…。" id story1_b8b4a374
    nvl clear

    scene bg night
    show nvl_textbox
    

    story "コーヒーを飲みながら、\n考え事をしたり、しなかったり、\nただそこにある物を眺めたり…\nそんなふうに過ごします。" id story1_9bbc6b9f
    story "それから眠くなったら寝ます！\nいつも時間に縛られてますから\n森にいる日は夜更かししても\nとっても早く寝てもいいのです。" id story1_ea461b45
    nvl clear

    scene white screen
    show nvl_textbox
    with fade_white
    play music "music/Winter.ogg" fadeout 4

    story "……………。" id story1_e69e9c86
    story "…次の日の朝、" id story1_713cb033
    extend "\n起きると真っ白でした。" id story1_24e2072e

    scene bg snowy2
    show nvl_textbox
    with fade_white
    story "そう、雪が降ったんです！\n雪！雪ー！" id story1_a24db63d

    nvl clear

    story "森の木も土も、少しだけ色を残していた\nコケやベリーの木もみんな真っ白！" id story1_30985ce0
    story "そして僕はまだ誰も踏んでいない\n真っ白に囲まれている！！" id story1_fdc500c9
    show bg snowy behind nvl_textbox
    
    with {'master': Dissolve(0.3)}  
    
    story "僕は嬉しくなって\n足跡を付け始めました。" id story1_e700ed26
    nvl clear

    stop music fadeout 4
    
    window show
    story "僕はいつもなら気を付けて歩くところを\n雪の美しさにかまけて\n油断してしまったんです…！" id story1_ca0497ec
    
    
    ## Falls in water
    
    show bg water behind nvl_textbox
    with {'master':circle_dissolve}

    ## Ripple
    camera at ripple
    camera screens at ripple
    pause 1.5

    ## Shake

    camera at reset
    camera screens at reset
    play sound1 "sfx/attack00.ogg"
    window auto
    $ _pending_camera_transform = [([sshake], "camera"), ([sshake], "screens")]
    story "ずぶっ！！" id story1_247b3f31
    $ _pending_camera_transform = None

    story "…？　踏み出した足が急に軽くなりました。" id story1_b7efe14d
    nvl clear

    
    story "そして…、{nw}" id story1_a34218b1
    play music1 "music/echo.ogg"
    extend "\n\nずぶずぶずぶずぶっ！！{nw}" id story1_ae81ea49
    play sound1 ("sfx/attack00.ogg")
    camera at sshake
    camera screens at sshake
    extend "{nw=1}"
    extend "\n\n僕の足がどんどん雪の中に\n吸い込まれていく！？" id story1_58f5d7c0
    nvl clear
    camera
    camera screens

    story "そこは湖にうっすら張った氷に\n雪が乗ってるだけの\n危険な場所だったんです…！" id story1_7e157b70
    story "そんな場所に踏み入れてしまった僕の体は\n足先からずぶずぶと薄い氷の\nその先へと向かっていきます。" id story1_27af72b2
    nvl clear
    
    ## Flash to forest
    scene bg forest2
    show nvl_textbox
    with {'master': Dissolve(0.2)}
    story "助けを呼ぼうにも僕自身人がいない場所を\n選んできているので絶望的です。\n携帯電話の類も全部\nおいてきてしまっています。" id story1_5158e7b2
    story "ポケットにあるのはサルミアッキのみ！\nサルミアッキはおいしいけれど\n僕のピンチを救ってはくれない！" id story1_38e85ade
    nvl clear

    ## Back to water
    scene bg water
    show nvl_textbox
    with {'master': Dissolve(0.2)}
    
    story "なんとか地上に残った片足で踏ん張りましたが、\nふわふわした雪が、僕の足のバランスを奪います。" id story1_799336c0
    play sound "sfx/crash18_f.ogg"
    camera at sshake
    camera screens at sshake
    story "バキバキバキっ！{nw=0.5}" id story1_57af3057
    extend "\n氷が派手に割れたー！{nw=0.5}" id story1_b8725207
    camera
    camera screens

    window hide
    $ quick_menu = False
    hide nvl_textbox
    play sound "sfx/LIGHTNNG.wav"
    play sound1 "sfx/SPLASH3.wav"
    show bg ripples1 
    show ripples vfx
    with SquareScatter(time=0.5, grid=16)
    pause 30

    $ quick_menu = True
    window auto
    show nvl_textbox with {'master': Dissolve(0.2)}
    story "おひゃあ！もう駄目だ…！\n落ちる…！" id story1_4c08f6d0
    nvl clear


    play music "sfx/WATER03.wav" fadein 1
    story "ええと…僕たち国ですから\nこういう事で死ぬことはないですし、\n皆さんもそれをよくご存じですから、\n聞いてる分には怖くないかもしれませんがっ、\n本当に怖かったんですよ…。" id story1_b12e0b34
    
    hide ripples vfx
    show bg water behind nvl_textbox
    with {'master': Dissolve(0.3)}
    story "それに！苦しさは人間も僕らも一緒！\n生きながら苦しい時間が続くって\n最悪じゃないですか…。" id story1_35923771
    stop music1 fadeout 3

    nvl clear

    $ quick_menu = False
    scene bg ripples1
    with SquareScatter(time=0.5, grid=16)
    show ripples vfx
    show nvl_textbox
    show black behind nvl_textbox:
        alpha 0.0
    $ quick_menu = True
    
    $ _pending_stop_music = 1
    $ _pending_sprite_transform = [("black", unhide_s1)]
    story "\nそして僕の体は冷たい湖の中に…。\n苦しい！息ができない…！" id story1_9e7a8af0

    
    hide ripples vfx with {'master': Dissolve(0.3)}
    hide bg water

    story "\n\n\n\n\n\n…と思ったのも一瞬でした。" id story1_d3d01bda
    nvl clear

    show white screen behind nvl_textbox:
        alpha 0
    $ _pending_camera_transform = [([old_film_distort_x], "screens")]
    $ _pending_sprite_transform = [("white screen", unhide_s1)]
    story "\nフードに何かが引っかかったような感触がして\n何が起こったのか確認する間もなく、\n僕の体は一気に引っ張られました！" id story1_ef982f81
    camera at old_film_distort_x1
    camera screens at old_film_distort_x1
    $ _pending_camera_transform = None

    $ quick_menu = False
    
    hide nvl_textbox
    #hide white screen

    play sound "sfx/SPLASH4.wav" fadeout 1
    show bg forest2 with {'master': Dissolve(0.3)}
    show nvl_textbox
    pause 1
    camera
    camera screens

    $ quick_menu = True
    $ _pending_camera_transform = [([sshake], "camera"), ([sshake], "screens")]
    story "ばしゃあ！と音がして少しの衝撃。\nと同時に濡れた肌に風を感じます。" id story1_a3f5e0af
    $ _pending_camera_transform = None
    nvl clear
    camera
    
    story "\nここは…雪の上？\n湖の底から体が勝手に地上に…？" id story1_8d10c5dc
    story "…何が起こったんだろう？" id story1_8140aebe
    story "そこに誰かがいる気がします。\nこんな森の中に誰が…？" id story1_ec3a4cfa
    nvl clear

    story "\n僕の意識はどんどん遠くなっていって…\nすとんと落ちるように気絶してしまいました。" id story1_6a053c06


    ## Sweden animation #############
    show swe_anim behind nvl_textbox
    hide bg forest2
    show white screen behind swe_anim
    show wrapmist behind nvl_textbox:
        alpha 0.3 additive_blend
    show wrapmist1 behind nvl_textbox:
        alpha 0.3 additive_blend

    


    pause 1

    story "{cps=3}……………。{/cps}{nw}" id story1_15a4b966
    hide swe_anim with {'master': Dissolve(0.2)}
    extend ""
    nvl clear


    ####
    scene bg home
    show nvl_textbox
    with fade_white

    story "\n気が付くと僕は自分の家で寝ていたんです。\n今までの事は夢だと思いましたが、\n溺れた時の服が乾燥機に入ってたんですよ…。" id story1_2baf04c4
    nvl clear
    #pause 1.0

    #show white screen with blur_fade
    #pause 0.2

    scene bg classroom_window with fade_white
    show finland large sup at pos_transform(xpos=450, ypos=-40)
    show nvl_textbox
    
    play music "music/19_playful.ogg"

    story "きっとあれは妖精です！\n妖精が僕を助けてくれたんですよ…！" id story1_abd4b566

    show finland large mmm
    with {'master': Dissolve(0.2)}

    story "でもこんな事を僕が言うと\n「酒飲んでたんだべ！」とか\n「仲間…（ニヨニヨ）」とか\n言われて信じていただけないので\n今日の今日まで心の中に留めておりました！" id story1_c33d8f72
    nvl clear

    show finland large heheh2
    with {'master': Dissolve(0.2)}
    story "こんな現代に人を助けてくれる妖精が\n生きてるってすごくないですか？\nある意味怖くはないですか？" id story1_13ee2293
    nvl clear    
    
    scene bg classroom1
    show bulgaria ooh at pos_transform(xpos=600, yalign=0.0)
    

    $ bul.screen = 'right_1'
    bul "…………。" id story1_28ca9edf

    $ bul.screen = 'right_3'
    bul "ひどくふわふわした話\nあざーっした！" id story1_4b7f24c5

    show finland waah at pos_transform(xpos=350, ypos=30)
    

    $ fin.screen = 'center_4long'
    $ _pending_window_transform = (shake_0p3)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    fin "ふわふわした話！！？" id story1_9ab7897d
    $ _skip_appear_effect = True
    $ _pending_window_transform = None
    extend "\nえっ、すいません！\n僕結構真面目に怖い話を\nしたんですけれど…。" id story1_674410e3
    $ _skip_appear_effect = False

    show finland ohdear
    

    fin "妖精が助けてくれるって\n怖くないですか…？" id story1_9db0829d

    show america smiling at pos_transform(xpos=120, yalign=0.0)
    $ ame.screen = 'right_3'
    ame "なかなかふわふわしていて\n面白かったぞ！" id story1_ce2dd2ba

    show england smirksmirk at pos_transform(xpos=0, yalign=0.0)
    $ eng.screen = 'right_4long'
    eng "俺は嫌いじゃない。\nいいんじゃないか。\nフィンランドらしく\nふわふわしていて。" id story1_46462028

    show finland nyaaaa
    $ fin.screen = 'center_3'
    $ _pending_window_transform = (shake_1s1)
    $ _pending_sound = ("sfx/crumple04.ogg", "sound")
    fin "ふわふわってどういう\n意味でのふわふわ\nなんですかー！" id story1_921c0f53
    stop sound

    scene bg classroom2
    
    pause 0.2


    $ bul.screen = 'right_3'
    bul "じゃあ次の\nふわふわした話\nお願いしゃーす！" id story1_5ca81584

    $ jpn.screen = 'center_3'
    jpn "ふわふわした話…！？\nすいません、用意して\nおりませんでした…。" id story1_b0885707

    $ fin.screen = 'right_3'
    fin "わーごめんなさい！\nしなくて大丈夫です！" id story1_b5e4c11e

    stop music fadeout 3



    jump story2