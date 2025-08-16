

label story7:
    scene bg hallway2
    na "{size=+2}第七話　最後の怖い話。{/size}"
    scene bg classroom_window
    play music "music/Carol_of_the_Bells_ESPN_(Album_Version).ogg"
    show russia 2 large ahahahaha at pos_transform(x=-70, y=-90)
    $ rus.screen = 'center_3'
    rus"大丈夫。\n僕は怖くないよ？"
    
    scene bg classroom1

    menu:

        "成り行きに任せる":
            jump donothing

        "俺が止める！！":
            jump stophim


    label stophim:
        #$ menu_flag = False
        
        show bulgaria med eek at pos_transform(x=440,y=-40)
        $ bul.screen = 'right_3'
        bul "ロ…ロシアさんっ！\nちょっとそれは\nやめるんだわー！"

        scene bg exterior1 at pan_to_top
        na "こうしてブルガリアさんの機転により、\nこの場を丸く収める事が出来たのだった。"

        na "ロシアさんの薬を噂っぽくぼかして７話目にして、\n後日イギリスが一人で１００話も語ったため\n１０７つの怖い話として校内新聞に載せられた。"

        na "全てそこそこほどほどに\n綺麗にまとまる！　　　　…はずだった。"
        stop music

        scene black
        play music "music/11_liarliar.ogg"

        $ bul.screen = 'center_1'
        bul "………ん！？"
        $ bul.screen = 'left_3'
        bul "…あれ？\n俺、何してたっけ？"

        scene white screen

        $ bul.screen = 'center_1'
        bul "えっなんだこれ！？"
        $ bul.screen = 'center_3'
        bul "えええ！？\nちょ…なにが\nどうなってんだわー！？"

        $ rus.screen = 'left_3'
        rus "おはようブルガリア君！\n君の英雄的行為\nかっこよかったよ"

        bul "ロシアさん…！？\nえ、あざっす…"
        $ bul.screen = 'center_3'
        $ _skip_appear_effect = True
        bul "でも何でこんな展開\nになるんだわー！？\nあっ、いや。ですかー！"
        $ _skip_appear_effect = False

        $ rus.screen = 'left_3'
        rus "君が代わりに\nなるんだーって\n言ったじゃない"

        $ bul.screen = 'center_3'
        bul "こういうのじゃなくて\nもっとカッコイイ\n感じの身代わりでぇ…！！"
        $ _skip_appear_effect = True
        bul "割と俺とロシアさんとの\n関係だって良好な方\nじゃないっすかー！！"
        $ _skip_appear_effect = False


        $ rus.screen = 'left_3'
        rus "しょうがないよ\nこういう役回りの子が\n出るのが伝統だもの"

        $ bul.screen = 'center_3'
        bul "伝統！？　伝統って\nなんなんだわー！！？"

        $ rus.screen = 'left_1'
        rus "しらないにゃん♪"

        $ bul.screen = 'center_3'
        bul "え…それって…\nだってあの時ロシアさん\nいなかったじゃ…"

        $ rus.screen = 'left_3'
        rus "これ？　何でも許して\nもらえる魔法の言葉だよ\nあっ、そうだ！"

        $ rus.screen = 'left_3'
        rus "目立てて\n良かったね♪"

        $ bul.screen = 'center_3'
        bul "最初っから…！\n最初っからー！！"

        $ rus.screen = 'left_4'
        rus "君達の会話って\n流しっぱなしにすると\n癒し効果があるから好きだよ"        

        scene bg exterior at pan_to_top
        show screen staffroll() nopredict
        $ bul.screen = 'left_4'
        bul "あ！でもよく考えたら\n確かにおいしい\nポジションですわ！\nあざーっす！あざーっす！{nw=5.0}"

        $ rus.screen = 'center_3'
        rus "君って意外と\n神経図太いよね{nw=2.0}"

        scene bg exterior4
        pause 7
        scene bg exterior5
        pause 7
        scene bg exterior6
        pause 7
        scene bg exterior8 at pan_to_top
        pause
        stop music

        $ persistent.game_finished = True
        return

    label donothing:
        #$ menu_flag = True

        
        play music "music/39_USbattlesong.ogg"
        show america med angry yell at pos_transform(x=100,y=-30)
        $ ame.screen = 'right_3'
        ame "やめるんだロシア！\n君がやめないのなら\n俺が君を止めるまでだ！"

        scene bg classroom_window
        show russia large smiling at pos_transform(x=200,y=-50)
        $ rus.screen = 'right_4long'
        rus "ふふっ\nそのお願いは聞けないかなぁ。\nそれに今の君に\nそんな力はないでしょう？"
        show russia large squint

        $ ame.screen = 'left_4long'
        ame "確かに今の俺には\n君に対抗できる力が出せない。\nだがそれで俺は諦めない！"

        scene bg classroom1
        show america large angry yell at pos_transform(x=100,y=-50)
        $ ame.screen = 'right_3'
        ame "そうとも！\n信じていれば！\n夢は叶うんだぞ！"

        scene bg classroom_window

        show russia 2 large cry yaaah at pos_transform(x=0,y=-30)
        $ rus.screen = 'right_4long'
        rus "そんな…！\n君のどこにそんな力が！？\n嘘だよこんなの…！"

        show white screen
        pause 0.5

        stop music

        scene bg exterior2
        show america d at pos_transform(x=300,y=30)
        $ ame.screen = 'center_3long'
        ame "っていう映画を\n作ろうと思ってるんだよ！\nどうだい面白そうだろう！"

        show russia mmph at pos_transform(x=50,y=30) behind america
        $ rus.screen = 'left_3'
        rus "えーまた僕を悪役にするの？\nアメリカ君、君って\n逆に僕のこと好きでしょ？"

        show screen staffroll() nopredict

        show america youreallyare
        $ ame.screen = 'center_3'
        ame "おいおい！\nどうして\nそうなるんだい！？{nw=5.0}"

        $ rus.screen = 'left_4'
        rus "だって多少時代背景や\n舞台設定に無理があっても\n何が何でも僕を黒幕\nしたがるじゃない…。{nw=5.0}"

        $ rus.screen = 'left_4long'
        rus "そこまでして僕黒幕オチを\n多用する背景には\n僕への好意があるんじゃないかと\n疑わざるを得ないよ。{nw=5.0}"
        
        $ ame.screen = 'center_3long'
        ame "ＮＯＯＯ！\n黒幕と陰謀っていったら\n君ってイメージなだけだよ！！{nw=5.0}"

        $ rus.screen = 'left_4long'
        rus "そうかなぁ。\n君よりはクリーンなつもりだよ？\nだって何が起こっても\n背後は僕！って言われるじゃない。{nw=5.0}"

        show russia smiling ufufu

        $ rus.screen = 'left_4long'
        rus "…まあその通りなんだけど。\nそれってとってもわかりやすくて\nみんなから見えてるわけだから\n陰謀や黒幕とは言えないよ。{nw=5.0}"

        $ ame.screen = 'right_4'
        ame "た、確かに…！\n映画的にも黒幕予想が\nイージーすぎて\nナンセンスだね！{nw=5.0}"


        scene bg exterior4

        $ rus.screen = 'left_3'
        rus "じゃあ今度は\n誰黒幕にする？{nw=5.0}"

        $ ame.screen = 'center_3'
        ame "君以外で…？！\nどうやれっていうんだい！{nw=5.0}"
        
        $ rus.screen = 'left_3'
        rus "こうしていつも通りの\nアメリカ君の映画が\nできるわけだね。{nw=5.0}"

        $ rus.screen = 'left_4long'
        rus "フランス君ほどとは\n言わないけどひねろうよ。\nスペイン君みたいに\n最後の５分で暴走するのも良いね。。{nw=5.0}"

        $ ame.screen = 'center_3'
        ame "それなら最近\n新しいタイプの\nエンディングを考えて…！{nw=5.0}"

        $ rus.screen = 'left_4'
        rus "家の中の怪奇現象は全部\n宇宙人がやってましたオチと\n友だちが悪魔化して全滅オチ\nじゃないよね？{nw=5.0}"

        $ ame.screen = 'center_3'
        ame "くっ！\n君厳しいよ！{nw=5.0}"


        pause


        $ persistent.game_finished = True
        return




    