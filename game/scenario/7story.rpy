

label story7:
    stop music
    scene bg hallway2
    with Dissolve(0.2)
    pause 0.2
    play sound "sfx/hallwaywalk.ogg"
    na "{size=+2}第七話　最後の怖い話。{/size}"

    show white screen onlayer bottom
    
    ## New scene
    scene bg classroom_door
    play sound "sfx/door_sfx.wav"
    play music ["<silence 2.0>", "music/carnaval_de_paris_elliot_simons.ogg"]
    play sound1 ["<silence 1.3>", "sfx/ding30.ogg"]
    show romania med normal:
        xpos 200 ypos -40 alpha 0
        time 0.9
        linear 0.4 alpha 1
        easeout 0.15 yoffset -45
        ease 0.15 yoffset 10
        easeout 0.15 yoffset -35
        ease 0.15 yoffset 5
        easeout 0.15 yoffset -5
        ease 0.15 yoffset 0
    
    $ na2.screen = 'left_1'
    na2 "失礼しまーす！"

    ## New scene
    scene bg classroom1

    show romania fufufu at pos_transform(xpos=150, yalign=0.0)
    $ rom.screen = 'center_3'
    rom "えっと、みんな！\n今日は集まってくれて\nありがとうなんだよー"

    show america hahahaha at pos_transform(xpos=340, yalign=0.0) behind romania
    $ ame.screen = 'right_4'
    ame "ルーマニアじゃないか！\nもしかして７つ目の\n怖い話をするのって\n君だったのかい！？"

    show romania eh
    $ rom.screen = 'center_3'
    rom "あ！ううん！\n７人目はおいら\nじゃないんだよー"
    show romania shocked nya:
        linear 0.15 xoffset 0
        linear 0.15 xoffset 10
        linear 0.15 xoffset -10
        linear 0.15 xoffset 10
        linear 0.15 xoffset -10
        linear 0.15 xoffset 0
        easeout 0.15 yoffset -35
        ease 0.15 yoffset 5
        easeout 0.15 yoffset -20
        ease 0.15 yoffset 5
        ease 0.15 yoffset 0
    $ _skip_appear_effect = True
    rom "えっと…、そうそう！\n今日のお礼と\n差し入れに来ましたっ！"
    $ _skip_appear_effect = False

    show romania pained
    show england hm at pos_transform(xpos=-20, yalign=0.0) behind romania
    $ eng.screen = 'left_3'
    eng "そうなのかよ\nちょうど６人全員\n話終えたところだぞ"

    play sound ["<silence .2>", "sfx/ding27.ogg"]
    show spain wahaha behind america:
        xpos 550 yoffset 1.0
        time .2
        easeout 0.15 yoffset -30
        ease 0.15 yoffset 10
        easeout 0.15 yoffset -20
        ease 0.15 yoffset 0

    pause 0.6
    $ spa.screen = 'right_4'
    spa "もしかして\n７人目誘うの\n忘れ取ったんちゃうか？\nどじっこさんやなぁ！"
    stop sound

    show romania shocked nya:
        pause 0.2
        linear 0.1 xoffset -20 yoffset 20
        linear 0.1 xoffset 0 yoffset 0
    pause 0.2
    $ rom.screen = 'center_3'
    rom "あ、えと、\nこの後、来るんだよー！{nw}"
    $ _skip_appear_effect = True
    show romania tired sweat hehe
    with {'master': Dissolve(0.25)}  
    extend "\nすぐに…うん…"
    $ _skip_appear_effect = False

    show spain sup
    $ spa.screen = 'right_3'
    spa "そか！そんなら\n安心やんなー！"

    show finland smiling behind america:
        xpos 350 ypos 30
        0.5
        block:
            linear 0.15 xoffset +8
            linear 0.15 xoffset -8
            repeat
    pause 0.6
    $ fin.screen = 'right_3'
    fin "モイ！\nルーマニア君\n差し入れってなに！？"
    show finland at stop_offset with move

    show romania shocked eh:
        pause 0.2
        easeout 0.15 yoffset -30
        easein 0.15 yoffset 10
        easeout 0.15 yoffset -20
        easein 0.15 yoffset 5
        easeout 0.15 yoffset 0

    pause 0.4
    $ rom.screen = 'center_3'
    rom "あっ、そうだ！\nお菓子とジュース…！\n…えと今配るんだよー！"

    show finland sup
    $ fin.screen = 'center_1'
    fin "やったー！"

    show america eksdee2
    $ ame.screen = 'right_1'
    ame "Ｙｅａｈ！！"

    show spain fufufu
    $ spa.screen = 'right_4'
    spa "手作りのクッキーとケーキて\nなんやのそれーかわええなぁ\n年頃の女の子みたいな\nラインナップやんなぁ"

    show romania sweat laugh:
        pause 1.2
        easeout 0.15 yoffset -30
        easein 0.15 yoffset 5
        easeout 0.15 yoffset -20
        easein 0.15 yoffset 2
        easeout 0.15 yoffset 0

    $ rom.screen = 'center_3'
    rom "えへへ…そうかなー…\nあっイギリスもお菓子\nどうぞなんだよー"

    show england heheheh2
    $ eng.screen = 'left_1'
    eng "ん、頂こうか"

    ## New scene
    scene bg classroom4

    show england med smirksmirk at pos_transform(xpos=500, ypos=-40)
    $ eng.screen = 'right_4'
    eng "しかしお前も俺たちに\n怖い話をさせるなんて\n面白い催し考えたな"

    show england med sneersneer2
    $ eng.screen = 'right_4'
    eng "そして\nそのメンバーとして\n俺を呼ぶセンスも良い\n褒めてやってもいいぞ！"

    show england med sneersneer

    play sound ["<silence .4>", "sfx/ding62.ogg"]
    show romania med tired sweat hehe:
        xpos 100 ypos -40
        pause 0.4
        easeout 0.15 yoffset -30
        easein 0.15 yoffset 5
        easeout 0.15 yoffset -20
        easein 0.15 yoffset 5
        easeout 0.15 yoffset 0

    pause 0.9
    $ rom.screen = 'center_3'
    rom "…あ、あははは…\nありがとうなんだよー"

    show bulgaria med waah behind romania:
        xpos -200 ypos -40
        easeout 0.3 xpos -50 ypos -40
        pause 1.2
        linear 0.1 xoffset 15 yoffset -10
        linear 0.1 xoffset 0 yoffset 0

    show romania med tired sweat hehe:
        pause 2.5
        "romania med eh" with Dissolve(0.2)
        block:
            linear 0.1 xoffset -30 yoffset -30
            linear 0.1 xoffset 0 yoffset 0
            linear 0.1 xoffset -20 yoffset -20
            linear 0.1 xoffset 0 yoffset 0
            linear 0.1 xoffset -10 yoffset -10
            linear 0.1 xoffset 0 yoffset 0

    $ bul.screen='left_3'
    pause 0.5
    bul "ちょー…\nお前忙しいとか\n言ってただろー"

    show bulgaria med stumped at stop_offset
    play sound ["<silence 1.2>", "sfx/ding76.ogg"]
    show romania med eh:
        pause 1.2
        "romania med shocked nya" with Dissolve(0.2)
    $ bul.screen = 'left_3'
    bul "ん。あれ？\nあとこの集会って\n魔術部のイギ太郎が…"


    show romania tired sweat laugh
    $ rom.screen = 'center_3'
    rom "え？　あっ！ちょうど\n時間が出来たというか！\n{size=-5}{color=#D1CED5}…ちょっと待っててねー{/size}"

    show bulgaria med stumped
    $ bul.screen='left_1'
    bul "　　？"
    pause 0.3

    ## New scene
    scene bg classroom_window
    with PushMove(0.5, "pushleft")
    pause 0.3
    
    show romania med tired sweat:
        xpos 200 ypos -40
        easein 1.0 xpos 310
        pause 0.1
        linear 0.08 xoffset 0
        linear 0.08 xoffset 7
        linear 0.08 xoffset -7
        linear 0.08 xoffset 7
        linear 0.08 xoffset -7
        linear 0.08 xoffset 7
        linear 0.08 xoffset -7
        linear 0.1 xoffset 0

    show bulgaria med sideglance noway at pos_transform(xpos=160, ypos=-40)
    $ rom.screen = 'right_4'
    rom "あのねブルガリア…\nえとその…\n今のうちに帰った方が\n良いんだよー…"    

    show bulgaria med sideglance sweat:
        xpos 160 ypos -40
        linear 0.08 xoffset 0
        linear 0.08 xoffset 8
        linear 0.08 xoffset -8
        linear 0.08 xoffset 4
        linear 0.08 xoffset -4
        linear 0.1 xoffset 0
    pause 0.5
    $ bul.screen='center_3long'
    bul "なんでなんだわ！？\nまさかお前おいしいところ\n持って行こうって腹じゃ…！"

    show romania med tired shout
    show bulgaria med sideglance sweat:
        pause 0.8
        "bulgaria med sideglance sweat crap" with Dissolve(0.2)
    $ rom.screen = 'right_3'
    rom "ちがうよう…！\nいいからできるだけ\n早く帰るんだよー！"

    show bulgaria med conniving
    $ bul.screen='center_1'
    bul "…なんかヤバイ？"

    show romania med sigh eyesclosed
    $ rom.screen = 'right_1'
    rom "だよー…ごめん…"  

    show bulgaria med light sweat
    $ bul.screen='center_3'
    bul "おっけ\nじゃあ後は任せた"

    show bulgaria med hmmm
    pause 0.1

    stop music fadeout 3
    show romania med smiling:
        pause 0.5
        easein 1.0 xpos 500
    $ rom.screen = 'right_3'
    rom "うん！\n今日はありがとう\nなんだよー"  

    stop music fadeout 3

    ## Bulletin board
    scene bg bulletin_board
    play sound "sfx/footsteps_arriving.ogg"
    $ na2.screen = 'center_1'
    na2 "こーんにちはー。"

    play music "music/Curious.ogg"
    
    ## Enter Russia
    scene bg classroom_door
    show russia smiling ufufu:
        xpos 500 yalign 0
        pause 0.3
        easein 1.0 xpos 340
    with fade_white
    play sound1 "sfx/door_sfx.wav"
    $ rus.screen = 'left_3'
    rus "やぁ、みんなお待たせ\nごめんね。準備に少し\n手間取っちゃって…"

    ## New scene
    scene bg classroom1

    pause 0.2
    play sound ["<silence .5>", "sfx/hit76_a.ogg"]
    show romania shocked eh:
        xpos -40, yalign 0.0
        pause 0.6
        block:
            linear 0.08 xoffset -5
            linear 0.08 xoffset 0
            repeat
    show england scream at pos_transform(xpos=430, yalign=0.0)
    pause 0.2
    show america hmmm at pos_transform(xpos=100, yalign=0.0)

    $ rom.screen = 'left_1'
    rom "にゃー！！？" 

    stop sound

    show romania quiver
    show sweat

    show america sup eyesclosed
    $ ame.screen = 'left_4long'
    ame "ロシア！最後に話すのは\n君だったのかい。\nまさに見計らってたかのような\nナイスタイミングじゃないか！"

    
    show russia smiling ufufu at pos_transform(xpos=600, yalign=0.0) behind england
    $ rus.screen = 'right_4'
    rus "うふふ、\n見破られちゃったね。\nもーアメリカ君には\n敵わないなぁ。"

    play sound ["<silence .5>", "sfx/hit27.ogg"]
    show england blush shout2
    $ eng.screen = 'right_3'
    $ window_transform = shake_7s1
    eng "お…お前かっ！\nまあなんとなく\nそんな気はしていたがな！"
    $ window_transform = None

    pause 0.1
    show russia happy
    pause 0.1
    hide sweat
    show romania sorry:
        xpos -40 yalign 0
        0.4
        easeout 0.2 yoffset -20
        easein 0.15 yoffset 10
        easeout 0.15 yoffset -10
        easein 0.15 yoffset 5
        ease 0.15 yoffset 0
    with Dissolve(0.3)

    pause 2.0

    ## Russia NVL #############################################
    scene bg classroom1
    pause 0.2
    show russia large happy at pos_transform(xpos=300, ypos=-10)
    show nvl_textbox
    with Dissolve(0.25)

    story "それじゃあ最後は僕の番だね。\nんー。どうしよう。\n怖い話なんて知らないな。\nどうしようかな？"
    show russia large smiling ufufu
    with {'master': Dissolve(0.2)}
    
    story "そうだ！ここに僕宛の\nお手紙があるからこれを読もう。\nうん。それがいいね。"
    nvl clear

    show russia large hmmm
    with {'master': Dissolve(0.2)}

    story "まず一通目だよ。なになに…。"

    story "{color=#FFEDF7}「ろしあさんは\n　ふとっているのですか？」{/color}"
    
    show russia large shocked
    with {'master': Dissolve(0.2)}

    story "…………。\n僕の家は寒いから\nちょっと骨太なだけだよ。"
    show russia large smiling ufufu
    with {'master': Dissolve(0.2)}

    extend "\n…手紙を送ってくれた君って\n割と近くに住んでるんだね！"
    nvl clear

    story "さて次の手紙を読むよ。"

    show russia large chuckle
    with {'master': Dissolve(0.2)}
    story "{color=#FFEDF7}「ろしあさんへ\n　国境なんていうものがあるから\n　けんかするんだとおもいます\n　世界中の国境をなくせば\n　みんなのこころやかんがえが\n　一つになるはずです」{/color}"
    nvl clear

    show russia large smiling ufufu
    with {'master': Dissolve(0.3)}
    pause 0.5

    story "小さいのに世界の事を\n考えてるなんてすごいね！"
    story "じゃあまずは小さい所から\nはじめてみようよ。"
    nvl clear

    story "まず君の家の敷地っていう概念を取っ払って\n君の家の家族を色んな家族と\nぐちゃぐちゃに混ぜたり\n取り替えたりしてみようよ。\n君と知らない人のこころやかんがえが\nひとつになるはずだよ。\n　\n大きくても小さくても\n君が望んでる事だもの。\nがんばろう！"
    nvl clear

    show russia large glum
    with {'master': Dissolve(0.3)}

    story "みんな別々の個性があって\n僕はそれが好きだから\n心や考え方が一つになっちゃったら\nつまらなくて僕は泣いて過ごすと思うな。"
    
    show russia large smiling
    with {'master': Dissolve(0.2)}
    story "抵抗しないアメリカ君やイギリス君\nなんかとってもつまらないでしょう？"
    nvl clear

    story "でも僕、君の考え方好きだよ。"
    show russia large chuckle
    with {'master': Dissolve(0.2)}
    story "でも完全にひとつになっちゃうのは\n難しいし、つまらない事だけれど\n個性豊かなみんなが\nひとつの家で一緒に暮らしたら\n賑やかで楽しいと思うんだ！"
    nvl clear

    show russia large glum
    with {'master': Dissolve(0.2)} 
    story "でもそれって実現するの\n今のままだととっても難しいよね…。\n　\n手を強く握って連れてきた子って\n目を離したすきに\nいなくなっちゃうでしょう？\nまったくリトアニアったら…。"
    nvl clear

    show russia large hmmm
    with {'master': Dissolve(0.2)} 
    story "でもなでなでし続けるだけだと\nにこにこはしてくれるけれど、\n一緒に暮らせるまで長そうだし…。\n　\nそこで僕は考えたんだ。"
    nvl clear

    show russia large glum
    with {'master': Dissolve(0.2)} 
    story "どうやったら今のままの\nみんなが僕の家に来てくれるのか。\n　\n昔みたいに僕が連れてくる形じゃなくて、\nみんなの方から自主的にね！\nその方がいいよね。"
    nvl clear

    show russia large smiling
    with {'master': Dissolve(0.2)} 
    story "みんながみんなのままなんだけど\n僕の事が大好きになっちゃう\nお薬を作ったんだ！\n　\nこんな感じかなぁって\n練ったりちぎったり溶解してみたら\nできたんだよ！"
    nvl clear

    show russia large chuckle
    with {'master': Dissolve(0.2)} 
    story "大丈夫！安心してね！\n性格は全然変わらないから\n口では嫌だって言えるし\n抵抗だってできるよ。"
    stop music fadeout 3
    
    extend "\n　\nでも僕が強くお願いすると\n逆らえなくなっちゃうんだ。"
    nvl clear

    show russia large smiling
    with {'master': Dissolve(0.2)} 
    story "ここまで言ったらわかっちゃうかもな。\nうん、そうだよ。\n今日のこの会は僕が…"
    nvl clear


    ## New scene ############################################################
    scene bg classroom5
    show romania large nyaaa:
        xpos 300 ypos -80
        easeout 0.3 yoffset -40
        easein 0.2 yoffset 20
        easeout 0.1 yoffset -30
        easein 0.2 yoffset 10
        easeout 0.1 yoffset 0
    with zoominzoomout
    play music "music/what_happened_pierre_gerwig_langer.ogg"
    
    pause 0.2
    $ rom.screen = 'right_3'
    play sound ["<silence .5>", "sfx/bam.ogg"]
    camera screens at sshake1
    rom "ご…ごめんなさいっ！\nごめんよごめんよー\nみんなーっ！"
    camera screens

    ## New scene
    scene bg classroom_door2
    show germany shocked at pos_transform(xpos=400, yalign=0.0)
    show finland oh at pos_transform(xpos=100, ypos=30)
    show japan shocked at pos_transform(xpos=370, yalign=0.0)

    $ fin.screen = 'left_1'
    fin "えっそれどういう…"

    ## New scene
    scene bg classroom1 at pan_to_bottom
    show romania large cry nyaa at pos_transform(xpos=300, ypos=-80)
    $ rom.screen = 'right_4long'
    rom "ロシアさんちに\nおいらの弟がひと人ぢ…\nじゃない友好的ホームステイ\nしてるんだよー…！"
    
    $ _skip_appear_effect = True
    $ rom.screen = 'right_4long'
    rom "それでその…\n今配ったお菓子に…！\nううっ…ごめんよぅ…\nおいらがふがいないばっかりに…"
    $ _skip_appear_effect = False

    show russia large smiling ufufu behind romania:
        xpos -90 ypos -30
        pause 0.3
        easein 1.0 xpos 0
    show romania large cry nyaa:
        pause 1.6
        "romania large cry ehh" with Dissolve(0.2)
        pause 0.2
        linear 0.1 xoffset +15 yoffset -15
        linear 0.05 xoffset 0 yoffset 0
        linear 0.1 xoffset -9 yoffset -9
        linear 0.1 xoffset 0 yoffset 0
        linear 0.1 xoffset +4 yoffset -4
        linear 0.1 xoffset 0 yoffset 0


    play sound ["<silence 1.2>", "sfx/hit34.ogg"]
    $ window_transform = shake_7s2
    $ rus.screen = 'left_3'
    rus "もう！ルーマニア君\n先にネタバレしちゃ\nだめだよー。"
    $ window_transform = None

    pause 0.5

    ## New scene
    scene bg classroom_door2 at pan_to_top
    show germany shocked at pos_transform(xpos=630, yalign=0.0)
    show finland oh at pos_transform(xpos=-80, ypos=30)
    show japan shocked at pos_transform(xpos=100, yalign=0.0)
    show america whatyousay at pos_transform(xpos=400, yalign=0.0)

    $ fin.screen = 'left_3'
    fin "え…？　もしかして\nお菓子とジュースに\n今の話の薬が…？"

    show america eksdee
    $ ame.screen = 'right_4long'
    ame "ＤＤＤＤＤ！\nそんなイギリスの\nファンタジーみたいな薬\n作れるわけないんだぞ！"

    show england blush shout at pos_transform(xpos=200, yalign=0.0)
    $ eng.screen = 'center_3long'
    eng "そ、そうだ…！\nそんな薬あるわけないだろ！\n{size=-5}ってお前俺に対してどんな認識なんだよ！{/size}"

    ## New scene
    scene bg classroom_window

    show russia large smiling at pos_transform(xpos=200, ypos=-80)
    $ rus.screen = 'right_4'
    rus "んーどうかな？\n時間が立てば\n分かるんじゃないかな"

    ## New scene
    scene bg classroom1 at pan_to_bottom
    pause 0.2

    show finland ohno:
        xpos 0 ypos 10
        easeout 0.15 yoffset -40
        easein 0.15 yoffset 20
        easeout 0.1 yoffset -30
        easein 0.2 yoffset 10
        easeout 0.1 yoffset 0

    $ fin.screen = 'left_4'
    fin "謀りましたね！\n僕お菓子僕いっぱい\n食べちゃったん\nですけど…！"

    show england scream at pos_transform(xpos=200, yalign=0.0)
    $ eng.screen = 'center_3'
    eng "何真に受けてんだ！\nそんな薬あって\nたまるか！"

    show germany shocked at pos_transform(xpos=500, yalign=0.0)
    show germany ohno
    $ ger.screen = 'right_4long'
    ger "いや、あながち嘘では\nないかもしれん！\n昔からロシアはやれば\n何故か出来てしまうんだ！"

    show germany blush yell
    $ ger.screen = 'right_4long'
    ger "思い出せ！今まで\n「よくわからないけど\n　すごいものが出来たよー！」\nという事が何度あった！？"

    show germany yell eyesclosed
    $ ger.screen = 'right_4long'
    ger "どうやったら\nお前にそれが作れる！？\nということを平気でやるのが\nロシアではないのか！"

    show england sweat blush whatthehell
    $ eng.screen = 'center_3'
    eng "…………思い当たる\n節しかない…！"

    show japan blush sweat embarassed at pos_transform(xpos=450, yalign=0.0) behind england 
    $ jpn.screen = 'right_4long'
    jpn "例えもし本当に\n効果があったとしても\n永続的に脳をコントロールし\n続けることはできないはず…！"

    show spain oh behind finland:
        xpos 50 yalign 0.0
        linear 0.4
        easeout 0.3 yoffset -40
        easein 0.2 yoffset 40
        easeout 0.2 yoffset -30
        easeout 0.2 yoffset 0
    $ spa.screen = 'center_4long'
    spa "せやけど一時的でも\nコントロールされとる間に\n次の飲まされたら\n終わりなんちゃう？"

    show england scream
    $ eng.screen = 'center_3'
    eng "あああああああ！！\nいやだ！いやすぎる！"

    ## New scene
    scene bg classroom_door
    with PushMove(0.5, "pushleft")
    stop music fadeout 3.0
    show spain med wahaha:
        xpos 300 yalign 0
        easeout 0.15 yoffset -40
        easein 0.15 yoffset 20
        easeout 0.1 yoffset -30
        easein 0.2 yoffset 15
        easeout 0.1 yoffset -10
        easein 0.2 yoffset 5
        easeout 0.1 yoffset 0
    pause 0.8
    
    $ spa.screen = 'center_4long'
    spa "あっせやけどお願い聞こえんくらい\n離れたら大丈夫や思うで！\nほな！帰ろかー！"
    
    $ _skip_appear_effect = True
    show spain med shocked
    with {'master': Dissolve(0.25)} 
    $ window_transform = shake_7s3
    $ spa.screen = 'center_4long'
    extend "\n…ドアノブつめたっ！"
    $ _skip_appear_effect = False
    $ window_transform = None

    ## New scene
    scene bg aura1
    play music "music/Carol_of_the_Bells_ESPN.ogg"
    show snow1_0
    show snowfront_0
    show circle_anim
    pause 0.005
    show russia 2 normal behind snowfront_0 with {'master':circle_dissolve2}:
        xpos 100 ypos -30
        pause 1.5
        linear 1 xpos 220
    $ rus.screen = 'right_4'
    rus "効いてくるまで\n少し時間がかかるから\nもうちょっとだけ\nこの部屋にいようね。"
    hide circle_anim

    show russia 2 sigh:
        xpos 220 ypos -30
        pause 1.5
        "russia 2 normal" with Dissolve(0.2)
    $ rus.screen = 'right_4'
    rus "ごめんね。みんな。\nでもこれから僕たち\nとっても仲良くなれるから\nみんな幸せだよね？"

    play sound ["<silence 0.01>", "sfx/ding30.ogg"]
    show romania cry nyaa behind russia:
        xpos 70 yalign 0
        easeout 0.15 yoffset -40
        easein 0.15 yoffset 20
        easeout 0.1 yoffset -30
        easein 0.2 yoffset 15
        easeout 0.1 yoffset -10
        easein 0.2 yoffset 5
        easeout 0.1 yoffset 0
    pause 0.3
    $ rom.screen = 'center_3'
    rom "うわーん！\n皆ごめんよごめんよー！\nこんなのってないよー"

    ## New scene
    scene bg aura2
    show snow1_0
    show snowfront_0

    show america angry worried behind snowfront_0 at pos_transform(xpos=500, yalign=0.0)
    play sound ["<silence 0.5>", "sfx/hit34.ogg"]
    $ window_transform = shake_7s4
    $ ame.screen = 'right_3'
    ame "くそっ！\nこれじゃあ寒すぎて…\n力が出ないじゃないか！"
    $ window_transform = None

    show england blush shout2 behind snowfront_0:
        xpos 340 yalign 0
        time 0.5
        block:
            linear 0.07 xoffset +5
            linear 0.07 xoffset -5
            repeat
    $ eng.screen = 'center_3'
    eng "なんだよこの雪！\nいつもの力が出せれば\nこんな奴なんかに…！！"

    show bulgaria cry waah behind snowfront_0 at pos_transform(xpos=70, yalign=0.0)
    $ bul.screen = 'left_3'
    bul "それある意味\n死亡フラグなんだわー"


    ## New scene
    scene bg aura1
    show snow1_0
    show snowfront_0
    with Dissolve(0.1)
    
    show russia 2 large worried behind snowfront_0 with {'master': Dissolve(0.3)} :
        xpos -70 ypos -90
        pause 1.5
        "russia 2 large sigh" with Dissolve(0.2)
    $ rus.screen = 'right_4long'
    rus "う～ん。なんでこういう\n反応になっちゃうのかな？\n僕なりに頑張って君たちに\n歩み寄ってみたんだけれど…。"

    show russia 2 large ahahahaha
    $ rus.screen = 'center_3'
    rus"大丈夫。\n僕は怖くないよ？"
    
    ## Choice scene
    scene bg aura2

    menu:

        "成り行きに任せる":
            jump donothing

        "俺が止める！！":
            jump stophim




    label stophim:
        play music "music/Dancing_Fool.ogg"

        show snow2_0
        show snowfront2_0

        show bulgaria med eek at pos_transform(xpos=440,ypos=-40) behind snowfront2_0
        $ bul.screen = 'right_4'
        bul "ロ…ロシアさんっ！\nちょっとそれは\nやめるんだわー！"

        show romania med shocked eh behind bulgaria:
            xpos 0 ypos -40
            parallel:
                linear 1.4 xoffset 140
            parallel:
                easein 0.3 yoffset -40
                easein 0.2 yoffset 30
                easein 0.2 yoffset -40
                easein 0.2 yoffset 10
                easein 0.1 yoffset -20
                easein 0.1 yoffset 5
                easein 0.1 yoffset 0

        pause 1
        $ rom.screen = 'left_3'
        rom "ちょっ！\n何言ってるんだよー\nそれならおいらが…"

        show bulgaria med conniving
        $ bul.screen = 'right_7big'
        bul "（まあ俺とロシアさんって\n　なかよし！とは言えないまでも\n　他のヨーロッパの国よりは\n　仲が良好な方だと思うから\n　こんな事をしても多分\n　それほどひどい事には\n　ならないはずなんだわー！）"

        show romania med tired sweat laugh
        $ rom.screen = 'left_3'
        rom "（あ…、あー…）"

        show bulgaria med conniving eyesclosed
        $ bul.screen = 'right_4long'
        bul "（この裏事情がなかったら\n　普通に帰ってたんだわ…\n　他の皆さんにも良い所\n　お見せできるしな。うん）"

        show romania med tired sweat laugh
        $ rom.screen = 'left_4long'
        rom "（そうなんだねー！\n　この場も救って\n　対外アピールも出来ちゃう\n　ブルガリア流石なんだよー）"

        show bulgaria med ello
        $ bul.screen = 'right_4long'
        bul "俺は菓子を食っていない！\n盾になってでも！みなさんを！\nお守りするんだわー！"


        ## New scene
        scene bg aura1
        show snow2_0
        show snowfront2_0

        show russia 2 large hmmm isee at pos_transform(xpos=-200, ypos=-50) behind snowfront2_0
        $ rus.screen = 'right_4'
        rus "え…。君がみんなの\n盾になるっていうの\nブルガリア君？"

        show russia large mmph:
            xpos 200 ypos -40
        
        $ rus.screen = 'left_1'
        rus "んー…。"

        hide snow2_0
        hide snowfront2_0
        show russia large chuckle
        $ rus.screen = 'left_4'
        rus "わかった。\n君がそう言うなら\n今日は止めておくね"

        ## New scene
        scene bg classroom1

        show romania med shocked eh at pos_transform(xpos=400, ypos=-40)
        show bulgaria med conniving at pos_transform(xpos=100,ypos=-40)
        play music "music/carnaval_de_paris_elliot_simons.ogg"
        $ bul.screen = 'left_3'
        bul "えっ、まじっすか！\nあざーっす！\nあざーっす！"

        $ rom.screen = 'right_1'
        rom "すごい！本当に！？"

        show england waahahaha at pos_transform(xpos=-90,yalign=0.0) behind bulgaria
        $ eng.screen = 'left_4long'
        eng "はははは！ロシア、お前が\nこの程度で引っ込むとは\nやはり薬ははったりだったか！\n多分はったりだ！はったりだよな…？"

        ## New scene
        scene bg exterior1 at pan_to_top
        na "こうしてブルガリアさんの機転により、\nこの場を丸く収める事が出来たのだった。"

        $ _skip_appear_effect = True
        na "ロシアさんの薬を噂っぽくぼかして７話目にして、\n後日イギリスが一人で１００話も語ったため\n１０７つの怖い話として校内新聞に載せられた。"

        na "全てそこそこほどほどに\n綺麗にまとまる！　　　　…はずだった。"
        $ _skip_appear_effect = False
        stop music fadeout 1

        ## New scene
        scene black
        pause 0.3

        $ bul.screen = 'center_1'
        bul "………ん！？"

        scene bg bul0
        $ bul.screen = 'left_3'
        bul "…あれ？\n俺、何してたっけ？"

        scene bg bul1
        play music "music/collision_course_paolo_bolio_hq.ogg"
        $ bul.screen = 'center_1'
        bul "えっなんだこれ！？"
        play sound ["<silence 0.5>", "sfx/hit34.ogg"]
        camera at shake_7s5
        camera screens at shake_7s5
        $ bul.screen = 'center_3'
        bul "えええ！？\nちょ…なにが\nどうなってんだわー！？"

        camera
        camera screens

        $ rus.screen = 'left_3'
        rus "おはようブルガリア君！\n君の英雄的行為\nかっこよかったよ"

        scene bgbul 2 at pan_bul2
        show bulvfx
        $ bul.screen = 'center_3'
        bul "ロシアさん…！？\nえ、あざっす…"
        $ bul.screen = 'center_3'
        play sound ["<silence 0.5>", "sfx/hit34.ogg"]
        $ _skip_appear_effect = True
        $ window_transform = shake_7s9
        bul "でも何でこんな展開\nになるんだわー！？\nあっ、いや。ですかー！"
        $ _skip_appear_effect = False
        $ window_transform = None

        $ rus.screen = 'left_3'
        rus "君が代わりに\nなるんだーって\n言ったじゃない"

        show bgbul 3
        $ bul.screen = 'center_3'
        bul "こういうのじゃなくて\nもっとカッコイイ\n感じの身代わりでぇ…！！"
        $ _skip_appear_effect = True
        bul "割と俺とロシアさんとの\n関係だって良好な方\nじゃないっすかー！！"
        $ _skip_appear_effect = False


        $ rus.screen = 'left_3'
        rus "しょうがないよ\nこういう役回りの子が\n出るのが伝統だもの"

        show bgbul 5
        $ bul.screen = 'center_3'
        bul "伝統！？　伝統って\nなんなんだわー！！？"

        $ rus.screen = 'left_1'
        rus "しらないにゃん♪"

        show bgbul 4
        $ bul.screen = 'center_3'
        bul "え…それって…\nだってあの時ロシアさん\nいなかったじゃ…"

        $ rus.screen = 'left_3'
        rus "これ？　何でも許して\nもらえる魔法の言葉だよ\nあっ、そうだ！"

        play sound ["<silence 0.5>", "sfx/ding27.ogg"]
        $ window_transform = shake_7s6
        $ rus.screen = 'left_3'
        rus "目立てて\n良かったね♪"
        $ window_transform = None
        stop sound

        play sound "sfx/hit34.ogg"
        camera screens at sshake
        show bgbul 3
        $ bul.screen = 'center_3'
        bul "最初っから…！\n最初っからー！！"
        camera screens
        stop music fadeout 2

        $ rus.screen = 'left_4'
        rus "君達の会話って\n流しっぱなしにすると\n癒し効果があるから好きだよ"        

        scene bg exterior
        play music "music/11_liarliar.ogg"
        show screen staffroll() nopredict
        play sound ["<silence 1>", "sfx/hit34.ogg"]
        $ window_transform = shake_7s7
        $ bul.screen = 'left_4'
        bul "あ！でもよく考えたら\n確かにおいしい\nポジションですわ！\nあざーっす！あざーっす！{nw=5.0}"
        $ window_transform = None

        $ rus.screen = 'center_3'
        rus "君って意外と\n神経図太いよね{nw=2.0}"

        scene bg exterior4
        pause
        scene bg exterior5
        pause 7
        scene bg exterior6
        pause 7
        scene bg exterior8
        pause
        stop music

        $ persistent.game_finished = True
        return

    label donothing:
        show snow1_0
        show snowfront_0

        $ audio_crossFade(1, "music/39_USbattlesong.ogg")
        show america med angry yell behind snowfront_0 at pos_transform(xpos=100,ypos=-30)
        $ ame.screen = 'right_3'
        ame "やめるんだロシア！\n君がやめないのなら\n俺が君を止めるまでだ！"

        scene bg aura1
        show snow1_0
        show snowfront_0
        show russia large smiling behind snowfront_0 at pos_transform(xpos=200,ypos=-50)
        $ rus.screen = 'right_4long'
        rus "ふふっ\nそのお願いは聞けないかなぁ。\nそれに今の君に\nそんな力はないでしょう？"
        show russia large happy

        $ ame.screen = 'left_4long'
        play sound ["<silence 1>", "sfx/hit51.ogg"]
        $ window_transform = shake_7s8
        ame "確かに今の俺には\n君に対抗できる力が出せない。\nだがそれで俺は諦めない！"
        $ window_transform = None

        window show
        scene bg aura2
        show snow2_0
        show snowfront2_0
        show america large angry yell behind snowfront_0 at pos_transform(xpos=100,ypos=-50)
        
        $ ame.screen = 'right_3'
        play sound ["<silence 0.5>", "sfx/BIGBEAST.WAV"]
        ame "そうとも！\n信じていれば！\n夢は叶うんだぞ！{nw=0.5}"
        camera at ripple2
        camera screens at ripple2
        hide snow2_0
        hide snowfront2_0
        show bg aura3 behind america with {'master':circle_dissolve2}

        show sparkle_up behind america
        show sparkle_radiate 
        extend "{nw=2}"
        camera at sshake_long
        camera screens
        extend "{nw=2}"
        pause 0.5
        window auto


        scene bg aura1
        camera at sshake_long
        show russia 2 large cry yaaah at pos_transform(xpos=0,ypos=-30)
        show sparkle_up behind russia
        play sound "sfx/MONSTER1.WAV"
        $ rus.screen = 'right_4long'
        rus "そんな…！\n君のどこにそんな力が！？\n嘘だよこんなの…！{nw=1}"

        stop music fadeout 3
        stop music1 fadeout 3

        play sound2 "sfx/Jurassic loop.wav"
        show white screen
        pause 6
        
        camera
        stop sound
        play music "music/International_Uplifting_Dance-full_length_track.ogg"

        scene bg exterior2 at pan_to_top
        show america eksdee at pos_transform(xpos=300,ypos=30)
        $ ame.screen = 'center_3long'
        ame "っていう映画を\n作ろうと思ってるんだよ！\nどうだい面白そうだろう！"

        show russia mmph at pos_transform(xpos=50,ypos=30) behind america
        $ rus.screen = 'left_3'
        rus "えーまた僕を悪役にするの？\nアメリカ君、君って\n逆に僕のこと好きでしょ？"

        show screen staffroll() nopredict

        show america youreallyare
        $ ame.screen = 'center_3'
        ame "おいおい！\nどうして\nそうなるんだい！？{nw=5.0}"

        show russia happy
        $ rus.screen = 'left_4'
        rus "だって多少時代背景や\n舞台設定に無理があっても\n何が何でも僕を黒幕\nしたがるじゃない…。{nw=5.0}"

        show russia smiling ufufu
        $ rus.screen = 'left_4long'
        rus "そこまでして僕黒幕オチを\n多用する背景には\n僕への好意があるんじゃないかと\n疑わざるを得ないよ。{nw=5.0}"
        
        show america whatyousay
        $ ame.screen = 'center_3long'
        ame "ＮＯＯＯ！\n黒幕と陰謀っていったら\n君ってイメージなだけだよ！！{nw=5.0}"

        show russia glum
        $ rus.screen = 'left_4long'
        rus "そうかなぁ。\n君よりはクリーンなつもりだよ？\nだって何が起こっても\n背後は僕！って言われるじゃない。{nw=5.0}"

        show russia smiling ufufu
        $ rus.screen = 'left_4long'
        rus "…まあその通りなんだけど。\nそれってとってもわかりやすくて\nみんなから見えてるわけだから\n陰謀や黒幕とは言えないよ。{nw=5.0}"

        show america sneer
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
        rus "フランス君ほどとは\n言わないけどひねろうよ。\nスペイン君みたいに\n最後の５分で暴走するのも良いね。{nw=5.0}"

        $ ame.screen = 'center_3'
        ame "それなら最近\n新しいタイプの\nエンディングを考えて…！{nw=5.0}"

        $ rus.screen = 'left_4'
        rus "家の中の怪奇現象は全部\n宇宙人がやってましたオチと\n友だちが悪魔化して全滅オチ\nじゃないよね？{nw=5.0}"

        stop music fadeout 3
        $ ame.screen = 'center_3'
        ame "くっ！\n君厳しいよ！{nw=5.0}"


        pause 5.0


        $ persistent.game_finished = True
        return




    