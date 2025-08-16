

label story1:
    scene bg exterior6 at pan_to_top
    with dissolve
    na "{size=+2}第一話　フィンランドの怖い話。{/size}"
    
    scene bg classroom1 at pan_to_bottom

    play music "music/orchestral_interlude_the_bar_chord_hq.ogg"
    pause 0.2
    show finland large normal at pos_transform(x=450, y=-40)
    show nvl_textbox


    story "わっ、僕が一番でいいのでしょうか？\nヨーロッパや北欧の国の名前並べる時\nいつも僕は中頃か後ろだったりするので、\n一番目ってちょっと嬉しいですね。
    "
    nvl clear

    show finland large nnh
    with {'master': Dissolve(0.3)}

    story "あっブっさん一つ聞いても？\n怖い話ってやはり幽霊的なものですか？\nそれとも人間が怖い話ですか？
    "

    story "{color=#ADB1B9}「怖かったら何でもいいっすよ」{/color}"

    nvl clear

    show finland large smiling
    with {'master': Dissolve(0.3)}
    story "そうですか！\nでしたらちょうど良い話があります"
    nvl clear

    scene bg forest2 at pan_to_top_slow
    show nvl_textbox
    

    story "あれは初冬の事でした…。\n\n僕の家は冬になるとお日様が\nほとんど見えなくなります。"
    nvl clear

    scene bg forest3
    show nvl_textbox
    

    story "お日様が見えないと、\nなんだか気分も落ち込みます。"

    show bg forest4 at pan_to_bottom behind nvl_textbox
    with {'master': Dissolve(0.3)}

    story "だからそんな日は人や機械や人工物が\n全く見えない場所に行きたくなるんですよね。\nだからちょっとの食料とコーヒーをもって\n僕は森に入ったんです…。
    "
    nvl clear

    scene bg classroom1 at pan_to_top
    show bulgaria stumped at pos_transform(x=440, yalign=0.0)
    

    $ bul.screen = 'right_1'
    bul "なにそれ怖い"

    show finland ummm at pos_transform(x=60, y=30)
    

    $ fin.screen = 'left_3'
    fin "えええっ！？\nぼ、僕まだ怖い話\n言ってないですよ…？"

    scene bg forest at pan_to_bottom
    show nvl_textbox
    

    story "ごっほん、それでですねー。\n僕は数日分の食料を詰め込み、\n森の中を進みました。"
    story "日が出てるのは数時間ですから、\n野宿する場所を早く\n見つけなければなりません。"

    nvl clear

    story "\n自然の中って、いいですよ。"
    story "森に入っていくときの苔を踏む音。\n苔って種類によって\n踏んだ時の音が違うんです。"
    story "さくさく。\nぎゅっぎゅっ。\nざく、ざく。\nもふっもふっ。"
    story "僕はざくざく派です！"

    nvl clear

    scene bg forest3 at pan_to_bottom
    show nvl_textbox
    

    story "紅葉の季節も終わり、\n森は灰色っぽくなりましたが、\n苔やベリーの木にはまだ色があって、\n音と色を楽しみながら\n森を進むのも良い物です。"
    story "聞こえるのは自分の息と服の音、足音。\nそれから時々鳥の声。\n沢山の音であふれた生活が\n遠い昔のようです。"
    
    nvl clear

    scene bg classroom1 at pan_to_bottom
    show finland large giggle at pos_transform(x=440, y=-20)
    show nvl_textbox
    
   
    story "途中、森と同じ色をした\nカモシカ君に出会い手を振ると\n目線で挨拶を返してくれます。\n良い子たちなんですよ。"

    nvl clear

    show finland large nnh
    with {'master': Dissolve(0.3)}

    story "あっでもヘラジカ君には\n気を付けて下さいね。\nヘラジカ君酔った勢いで\n人跳ねますから…。\n\n毎年僕も跳ねられるんですよね…。\n強すぎます…。"
    nvl clear
    

    scene bg night at pan_to_top
    show nvl_textbox
    

    story "トコトコ歩いていくと\nちょうど良いくぼみがありまして\n僕はそこで数日間過ごすことにしました。"
    
    show bg stars at pan_to_top behind nvl_textbox
    with {'master': Dissolve(0.3)}   
    
    story "森の中の夜もいいんですよ。\n夜はとっても長いんですけど、\n音も空も昼間より賑やかになります。"

    nvl clear

    story "フクロウの声があちこちから聞こえて、\n時々はもってなんだか合唱してるみたいです。\n空にはたくさんの星が目に見えない速度で\nぐるーっと回ります。"
    story "僕たちからすれば空に描いた光る点々でも、\n一つ一つが大きな星なんですよね…。\n宇宙は大きいなぁ…。"
    nvl clear

    scene bg night at pan_to_top
    show nvl_textbox
    

    story "コーヒーを飲みながら、\n考え事をしたり、しなかったり、\nただそこにある物を眺めたり…\nそんなふうに過ごします。"
    story "それから眠くなったら寝ます！\nいつも時間に縛られてますから\n森にいる日は夜更かししても\nとっても早く寝てもいいのです。"
    nvl clear

    scene white screen
    show nvl_textbox
    with fade_white
    play music "music/Winter.ogg" fadeout 4

    story "……………。"
    story "…次の日の朝、\n起きると真っ白でした。"

    scene bg snowy2 at pan_to_top_slow
    show nvl_textbox
    with fade_white
    story "そう、雪が降ったんです！\n雪！雪ー！"

    nvl clear

    story "森の木も土も、少しだけ色を残していた\nコケやベリーの木もみんな真っ白！"
    story "そして僕はまだ誰も踏んでいない\n真っ白に囲まれている！！"
    show bg snowy at pan_to_bottom behind nvl_textbox
    with {'master': Dissolve(0.3)}  
    
    story "僕は嬉しくなって\n足跡を付け始めました。"
    nvl clear

    stop music fadeout 4
    
    window show
    story "僕はいつもなら気を付けて歩くところを\n雪の美しさにかまけて\n油断してしまったんです…！"
    
    
    $ window_transform = ripple
    show bg water behind nvl_textbox
    with {'master':circle_dissolve}
    pause 1.0
    show bg water
    with {'master':sshake}
    $ window_transform = sshake
    play sound1 ("sfx/attack00.ogg")
    window auto
    story "ずぶっ！！" 
    $ window_transform = None


    story "…？　踏み出した足が急に軽くなりました。"
    nvl clear

    
    story "そして…、"
    play music "music/echo.ogg"
    story "ずぶずぶずぶずぶっ！！"
    show bg water with sshake 
    play sound1 ("sfx/attack00.ogg")
    story "僕の足がどんどん雪の中に\n吸い込まれていく！？"
    nvl clear

    story "そこは湖にうっすら張った氷に\n雪が乗ってるだけの\n危険な場所だったんです…！"
    story "そんな場所に踏み入れてしまった僕の体は\n足先からずぶずぶと薄い氷の\nその先へと向かっていきます。"
    nvl clear
    
    scene bg forest2 at pan_to_top_slow
    show nvl_textbox
    with fade_white
    story "助けを呼ぼうにも僕自身人がいない場所を\n選んできているので絶望的です。\n携帯電話の類も全部\nおいてきてしまっています。"
    story "ポケットにあるのはサルミアッキのみ！\nサルミアッキはおいしいけれど\n僕のピンチを救ってはくれない！"
    nvl clear

    scene bg water
    show nvl_textbox
    with fade_white
    
    story "なんとか地上に残った片足で踏ん張りましたが、\nふわふわした雪が、僕の足のバランスを奪います。"
    play sound "sfx/crash18_f.ogg"
    
    story "バキバキバキっ！"
    story "氷が派手に割れたー！"

    show bg ripples1 behind nvl_textbox
    with {'master': Dissolve(0.3)}

    play sound "sfx/LIGHTNNG.wav"
    play sound1 ("sfx/SPLASH3.wav")
    story "おひゃあ！もう駄目だ…！\n落ちる…！"
    nvl clear


    play sound "sfx/WATER03.wav"
    story "ええと…僕たち国ですから\nこういう事で死ぬことはないですし、\n皆さんもそれをよくご存じですから、\n聞いてる分には怖くないかもしれませんがっ、\n本当に怖かったんですよ…。"
    
    show bg water at pan_to_top behind nvl_textbox
    with {'master': Dissolve(0.3)}
    story "それに！苦しさは人間も僕らも一緒！\n生きながら苦しい時間が続くって\n最悪じゃないですか…。"
    nvl clear
    stop music fadeout 0.5
    
    scene bg ripples1
    show nvl_textbox
    

    story "そして僕の体は冷たい湖の中に…。\n苦しい！息ができない…！"
    stop sound

    scene black
    show nvl_textbox
    

    story "\n\n\n\n\n\n…と思ったのも一瞬でした。"
    nvl clear

    show white screen behind nvl_textbox
    story "\nフードに何かが引っかかったような感触がして\n何が起こったのか確認する間もなく、\n僕の体は一気に引っ張られました！"
    play sound "sfx/SPLASH04.wav"
    
    scene bg forest2 at pan_to_top_slow
    show nvl_textbox
    with fade_white
    story "ばしゃあ！と音がして少しの衝撃。\nと同時に濡れた肌に風を感じます。"
    nvl clear
    
    story "\nここは…雪の上？\n湖の底から体が勝手に地上に…？"
    story "\n\n…何が起こったんだろう？"
    story "\n\nそこに誰かがいる気がします。\nこんな森の中に誰が…？"
    nvl clear

    story "\n僕の意識はどんどん遠くなっていって…\nすとんと落ちるように気絶してしまいました。"


    ## Sweden animation #############
    show swe1 at swe1_transform behind nvl_textbox
    show swe2 at swe2_transform behind nvl_textbox
    show swe3 at swe3_transform behind nvl_textbox   

    show expression wrapmist behind nvl_textbox
    show expression wrapmist1 behind nvl_textbox

    pause 0.5

    story "……………。"
    nvl clear

    hide screen marquee_screen
    hide screen marquee_screen2

    scene bg home at pan_to_bottom
    show nvl_textbox
    with fade_white

    story "気が付くと僕は自分の家で寝ていたんです。\n今までの事は夢だと思いましたが、\n溺れた時の服が乾燥機に入ってたんですよ…。"
    nvl clear
    pause 1.0

    scene bg classroom_window at pan_to_bottom
    show finland large sup at pos_transform(x=450, y=-40)
    show nvl_textbox
    
    play music "music/19_playful.ogg"

    story "きっとあれは妖精です！\n妖精が僕を助けてくれたんですよ…！"

    show finland large mmm
    with {'master': Dissolve(0.3)}

    story "\nでもこんな事を僕が言うと\n「酒飲んでたんだべ！」とか\n「仲間…（ニヨニヨ）」とか\n言われて信じていただけないので\n今日の今日まで心の中に留めておりました！"
    nvl clear

    show finland large heheh2
    with {'master': Dissolve(0.3)}
    story "こんな現代に人を助けてくれる妖精が\n生きてるってすごくないですか？\nある意味怖くはないですか？"
    nvl clear    
    
    scene bg classroom1 at pan_to_top
    show bulgaria ooh at pos_transform(x=600, yalign=0.0)
    

    $ bul.screen = 'right_1'
    bul "…………。"

    $ bul.screen = 'right_3'
    bul "ひどくふわふわした話\nあざーっした！"

    show finland waah at pos_transform(x=350, y=30)
    

    $ fin.screen = 'center_4long'
    fin "ふわふわした話！！？"
    $ _skip_appear_effect = True
    extend "\nえっ、すいません！\n僕結構真面目に怖い話を\nしたんですけれど…。"
    $ _skip_appear_effect = False

    show finland ohdear
    

    fin "妖精が助けてくれるって\n怖くないですか…？"

    show america smiling at pos_transform(x=120, yalign=0.0)
    $ ame.screen = 'right_3'
    ame "なかなかふわふわしていて\n面白かったぞ！"

    show england smirksmirk at pos_transform(x=0, yalign=0.0)
    $ eng.screen = 'right_4long'
    eng "俺は嫌いじゃない。\nいいんじゃないか。\nフィンランドらしく\nふわふわしていて。"

    show finland nyaaaa
    play sound ["<silence 0.6>", "sfx/crumple04.ogg"]
    $ fin.screen = 'center_3'
    fin "ふわふわってどういう\n意味でのふわふわ\nなんですかー！"


    scene bg classroom2 at pan_to_bottom1
    
    pause 0.2


    $ bul.screen = 'right_3'
    bul "じゃあ次の\nふわふわした話\nお願いしゃーす！"

    $ jpn.screen = 'center_3'
    jpn "ふわふわした話…！？\nすいません、用意して\nおりませんでした…。"

    $ fin.screen = 'right_3'
    fin "わーごめんなさい！\nしなくて大丈夫です！"

    stop music



    jump story2