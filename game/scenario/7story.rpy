

label story7:
    stop music
    scene bg hallway2
    with Dissolve(0.2)
    pause 0.2
    play sound "sfx/hallwaywalk.ogg"
    na "{size=+2}第七話　最後の怖い話。{/size}" id story7_860b727e

    show white screen onlayer bottom
    
    ## New scene
    scene bg classroom_door
    play sound1 "sfx/door_sfx.wav"
    show romania med normal:
        xpos 200 ypos -40 alpha 0

    $ na2.screen = 'left_1'

    $ _pending_music = ("music/carnaval_de_paris_elliot_simons.ogg", 0.0, 0.0)
    $ _pending_sound = ("sfx/ding30.ogg", "sound")
    $ _pending_sprite_transform = [("romania", rom_7s1)]
    na2 "失礼しまーす！" id story7_9dd7a492


    ## New scene
    scene bg classroom1

    show romania fufufu at pos_transform(xpos=150, yalign=0.0)
    $ rom.screen = 'center_3'
    rom "えっと、みんな！\n今日は集まってくれて\nありがとうなんだよー" id story7_378a8f1f

    show america hahahaha at pos_transform(xpos=340, yalign=0.0) behind romania
    $ ame.screen = 'right_4'
    ame "ルーマニアじゃないか！\nもしかして７つ目の\n怖い話をするのって\n君だったのかい！？" id story7_5b3c969a

    show romania eh
    $ rom.screen = 'center_3'
    rom "あ！ううん！\n７人目はおいら\nじゃないんだよー" id story7_2edc087d
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
    rom "えっと…、そうそう！\n今日のお礼と\n差し入れに来ましたっ！" id story7_3dca6e2d
    $ _skip_appear_effect = False

    show romania pained
    show england hm at pos_transform(xpos=-20, yalign=0.0) behind romania
    $ eng.screen = 'left_3'
    eng "そうなのかよ\nちょうど６人全員\n話終えたところだぞ" id story7_ad38888c

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
    spa "もしかして\n７人目誘うの\n忘れ取ったんちゃうか？\nどじっこさんやなぁ！" id story7_4b8bd771
    stop sound

    show romania shocked nya:
        pause 0.2
        linear 0.1 xoffset -20 yoffset 20
        linear 0.1 xoffset 0 yoffset 0
    pause 0.2
    $ rom.screen = 'center_3'
    rom "あ、えと、\nこの後、来るんだよー！{nw}" id story7_002d0375
    $ _skip_appear_effect = True
    show romania tired sweat hehe
    with {'master': Dissolve(0.25)}  
    extend "\nすぐに…うん…" id story7_9790a031
    $ _skip_appear_effect = False

    show spain sup
    $ spa.screen = 'right_3'
    spa "そか！そんなら\n安心やんなー！" id story7_0d830a7f

    show finland smiling behind america:
        xpos 350 ypos 30
        0.5
        block:
            linear 0.15 xoffset +8
            linear 0.15 xoffset -8
            repeat
    pause 0.6
    $ fin.screen = 'right_3'
    fin "モイ！\nルーマニア君\n差し入れってなに！？" id story7_15becd0d
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
    rom "あっ、そうだ！\nお菓子とジュース…！\n…えと今配るんだよー！" id story7_4d0cca12

    show finland sup
    $ fin.screen = 'center_1'
    fin "やったー！" id story7_a37a4537

    show america eksdee2
    $ ame.screen = 'right_1'
    ame "Ｙｅａｈ！！" id story7_0cf73366

    show spain fufufu
    $ spa.screen = 'right_4'
    spa "手作りのクッキーとケーキて\nなんやのそれーかわええなぁ\n年頃の女の子みたいな\nラインナップやんなぁ" id story7_5688e25d

    show romania sweat laugh
    $ rom.screen = 'center_3'
    $ _pending_sprite_transform = [("romania", rom_7s2)]
    rom "えへへ…そうかなー…\nあっイギリスもお菓子\nどうぞなんだよー" id story7_0caf85f6


    show england heheheh2
    $ eng.screen = 'left_1'
    eng "ん、頂こうか" id story7_9feff1de

    ## New scene
    scene bg classroom4

    show england med smirksmirk at pos_transform(xpos=500, ypos=-40)
    $ eng.screen = 'right_4'
    eng "しかしお前も俺たちに\n怖い話をさせるなんて\n面白い催し考えたな" id story7_ed6a12e3

    show england med sneersneer2
    $ eng.screen = 'right_4'
    eng "そして\nそのメンバーとして\n俺を呼ぶセンスも良い\n褒めてやってもいいぞ！" id story7_3b1b5942

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
    rom "…あ、あははは…\nありがとうなんだよー" id story7_56a4d789

    show bulgaria med waah behind romania:
        xpos -200 ypos -40
        easeout 0.3 xpos -50 ypos -40
    $ bul.screen='left_3'
    pause 0.5

    $ _pending_sprite_transform = [("bulgaria", bul_7s3), ("romania", rom_7s3)]
    bul "ちょー…\nお前忙しいとか\n言ってただろー" id story7_85994eed

    show bulgaria med stumped at stop_offset
    $ bul.screen = 'left_3'
    $ _pending_sound = ("sfx/ding76.ogg", "sound")
    $ _pending_sprite_transform = [("romania med shocked nya", pos_transform(xpos=100, ypos=-40), Dissolve(0.2))]
    bul "ん。あれ？\nあとこの集会って\n魔術部のイギ太郎が…" id story7_aa94871d


    show romania tired sweat laugh
    $ rom.screen = 'center_3'
    rom "え？　あっ！ちょうど\n時間が出来たというか！\n{size=-5}{color=#C0C0C0}…ちょっと待っててねー{/color}{/size}" id story7_ad8be397

    show bulgaria med stumped
    $ bul.screen='left_1'
    bul "　　？" id story7_3b83e8e1
    pause 0.3

    ## New scene
    scene bg classroom_window
    with PushMove(0.5, "pushleft")
    pause 0.3
    
    show romania med tired sweat:
        xpos 200 ypos -40
        easein 0.8 xpos 310


    show bulgaria med sideglance noway at pos_transform(xpos=160, ypos=-40)
    $ rom.screen = 'right_4'
    $ _pending_sprite_transform = [("romania", rom_7s4)]
    rom "あのねブルガリア…\nえとその…\n今のうちに帰った方が\n良いんだよー…" id story7_ed821300


    show bulgaria med sideglance sweat:
        xpos 160 ypos -40
        linear 0.08 xoffset 0
        linear 0.08 xoffset 8
        linear 0.08 xoffset -8
        linear 0.08 xoffset 4
        linear 0.08 xoffset -4
        linear 0.1 xoffset 0
    with {'master': None}
    pause 0.5
    $ bul.screen='center_3long'
    bul "なんでなんだわ！？\nまさかお前おいしいところ\n持って行こうって腹じゃ…！" id story7_7e1aef07

    show romania med tired shout
    $ rom.screen = 'right_3'
    $ _pending_sprite_transform = [("bulgaria med sideglance sweat crap", pos_transform(xpos=160, ypos=-40), Dissolve(0.2))]
    rom "ちがうよう…！\nいいからできるだけ\n早く帰るんだよー！" id story7_78b4c722



    show bulgaria med conniving
    $ bul.screen='center_1'
    bul "…なんかヤバイ？" id story7_9a4a8e97

    show romania med sigh eyesclosed
    $ rom.screen = 'right_1'
    rom "だよー…ごめん…" id story7_3d0f0081

    show bulgaria med light sweat
    $ bul.screen='center_3'
    bul "おっけ\nじゃあ後は任せた" id story7_ee4d9049

    show bulgaria med hmmm
    pause 0.1

    stop music fadeout 3
    show romania med smiling:
        pause 0.5
        easein 1.0 xpos 500
    $ rom.screen = 'right_3'
    rom "うん！\n今日はありがとう\nなんだよー" id story7_7d6a98b4

    stop music fadeout 3

    ## Bulletin board
    scene bg bulletin_board
    play sound "sfx/footsteps_arriving.ogg"
    $ na2.screen = 'center_1'
    na2 "こーんにちはー。" id story7_c0ae8bd3

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
    rus "やぁ、みんなお待たせ\nごめんね。準備に少し\n手間取っちゃって…" id story7_51ca0ab3

    ## New scene
    scene bg classroom1

    pause 0.2
    
    show romania shocked eh at pos_transform(xpos=-40, yalign=0.0)
    show england scream at pos_transform(xpos=430, yalign=0.0)
    pause 0.2
    show america hmmm at pos_transform(xpos=100, yalign=0.0)

    $ rom.screen = 'left_1'
    $ _pending_sprite_transform = [("romania", rom_7s5)]
    $ _pending_sound = ("sfx/hit76_a.ogg", "sound")
    rom "にゃー！！？" id story7_65241561


    show romania quiver
    show sweat

    show america sup eyesclosed
    $ ame.screen = 'left_4long'
    ame "ロシア！最後に話すのは\n君だったのかい。\nまさに見計らってたかのような\nナイスタイミングじゃないか！" id story7_e52d93f4

    
    show russia smiling ufufu at pos_transform(xpos=600, yalign=0.0) behind england
    $ rus.screen = 'right_4'
    rus "うふふ、\n見破られちゃったね。\nもーアメリカ君には\n敵わないなぁ。" id story7_2a6e2e94

    
    show england blush shout2
    $ eng.screen = 'right_3'
    $ _pending_window_transform = (shake_7s1)
    $ _pending_sound = ("sfx/hit27.ogg", "sound")
    eng "お…お前かっ！\nまあなんとなく\nそんな気はしていたがな！" id story7_95375b13


    pause 0.1
    show russia happy
    pause 0.1
    hide sweat
    show romania:
        xpos -40 yalign 0
        "romania sorry" with Dissolve(0.2)
        0.4
        easeout 0.2 yoffset -20
        easein 0.15 yoffset 10
        easeout 0.15 yoffset -10
        easein 0.15 yoffset 5
        ease 0.15 yoffset 0
    with {'master': None}

    pause 2.0

    ## Russia NVL #############################################
    scene bg classroom1
    pause 0.2
    show russia large happy at pos_transform(xpos=300, ypos=-10)
    show nvl_textbox
    with Dissolve(0.25)

    story "それじゃあ最後は僕の番だね。\nんー。どうしよう。\n怖い話なんて知らないな。\nどうしようかな？{nw=0.2}" id story7_effdb45f
    show russia large smiling ufufu with {'master': Dissolve(0.2)}
    
    extend "\n\nそうだ！ここに僕宛の\nお手紙があるからこれを読もう。\nうん。それがいいね。" id story7_58cff93f
    nvl clear

    show russia large hmmm with {'master': Dissolve(0.2)}

    story "まず一通目だよ。なになに…。\n\n{color=#FFE5FC}「ろしあさんは\n　ふとっているのですか？」{/color}" id story7_b6819907
    
    show russia large shocked with {'master': Dissolve(0.2)}

    story "…………。\n僕の家は寒いから\nちょっと骨太なだけだよ。" id story7_a29d84b8
    show russia large smiling ufufu with {'master': Dissolve(0.2)}

    extend "\n…手紙を送ってくれた君って\n割と近くに住んでるんだね！" id story7_a926d614
    nvl clear

    story "さて次の手紙を読むよ。{nw=0.2}" id story7_7dee5968

    show russia large chuckle with {'master': Dissolve(0.2)}
    extend "\n\n{color=#FFE5FC}「ろしあさんへ\n　国境なんていうものがあるから\n　けんかするんだとおもいます\n　世界中の国境をなくせば\n　みんなのこころやかんがえが\n　一つになるはずです」{/color}" id story7_65dba745
    nvl clear

    show russia large smiling ufufu with {'master': Dissolve(0.2)}
    pause 0.5

    story "小さいのに世界の事を\n考えてるなんてすごいね！" id story7_dcbac35a
    story "じゃあまずは小さい所から\nはじめてみようよ。" id story7_12280337
    nvl clear

    story "まず君の家の敷地っていう概念を取っ払って\n君の家の家族を色んな家族と\nぐちゃぐちゃに混ぜたり\n取り替えたりしてみようよ。\n君と知らない人のこころやかんがえが\nひとつになるはずだよ。\n　\n大きくても小さくても\n君が望んでる事だもの。\nがんばろう！" id story7_d3753c7e
    nvl clear

    show russia large glum with {'master': Dissolve(0.3)}

    story "{k=3}みんな別々の個性があって\n僕はそれが好きだから\n心や考え方が一つになっちゃったら\nつまらなくて僕は泣いて過ごすと思うな。{/k}" id story7_a64bca0e
    
    show russia large smiling with {'master': Dissolve(0.2)}
    story "抵抗しないアメリカ君やイギリス君\nなんかとってもつまらないでしょう？" id story7_5d4645c7
    nvl clear

    show russia large chuckle with {'master': Dissolve(0.2)}
    story "でも僕、君の考え方好きだよ。" id story7_03435446

    show russia large happy with {'master': Dissolve(0.2)}
    story "でも完全にひとつになっちゃうのは\n難しいし、つまらない事だけれど\n個性豊かなみんなが\nひとつの家で一緒に暮らしたら\n賑やかで楽しいと思うんだ！" id story7_600e25c8
    nvl clear

    show russia large glum with {'master': Dissolve(0.2)} 
    story "でもそれって実現するの\n今のままだととっても難しいよね…。\n　\n手を強く握って連れてきた子って\n目を離したすきに\nいなくなっちゃうでしょう？\nまったくリトアニアったら…。" id story7_d399208a
    nvl clear

    show russia large hmmm with {'master': Dissolve(0.2)} 
    story "でもなでなでし続けるだけだと\nにこにこはしてくれるけれど、\n一緒に暮らせるまで長そうだし…。\n　\nそこで僕は考えたんだ。" id story7_b625f22c
    nvl clear

    show russia large glum with {'master': Dissolve(0.2)} 
    story "どうやったら今のままの\nみんなが僕の家に来てくれるのか。\n　\n昔みたいに僕が連れてくる形じゃなくて、\nみんなの方から自主的にね！\nその方がいいよね。" id story7_9d53603d
    nvl clear

    show russia large smiling with {'master': Dissolve(0.2)} 
    story "みんながみんなのままなんだけど\n僕の事が大好きになっちゃう\nお薬を作ったんだ！\n　\nこんな感じかなぁって\n練ったりちぎったり溶解してみたら\nできたんだよ！" id story7_e8013caf
    nvl clear

    show russia large chuckle with {'master': Dissolve(0.2)} 
    story "大丈夫！安心してね！\n性格は全然変わらないから\n口では嫌だって言えるし\n抵抗だってできるよ。" id story7_a64eb484
    stop music fadeout 3
    
    extend "\n　\nでも僕が強くお願いすると\n逆らえなくなっちゃうんだ。" id story7_89c732c4
    nvl clear

    show russia large smiling with {'master': Dissolve(0.2)} 
    story "ここまで言ったらわかっちゃうかもな。\nうん、そうだよ。\n今日のこの会は僕が…" id story7_d2ed5b41
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
    $ _pending_sound = ("sfx/bam.ogg", "sound")
    $ _pending_camera_transform = [([sshake1], "screens")]
    rom "ご…ごめんなさいっ！\nごめんよごめんよー\nみんなーっ！" id story7_afcde6d2
    $ _pending_camera_transform = None

    camera screens

    ## New scene
    scene bg classroom_door2
    show germany shocked at pos_transform(xpos=400, yalign=0.0)
    show finland oh at pos_transform(xpos=100, ypos=30)
    show japan shocked at pos_transform(xpos=370, yalign=0.0)

    $ fin.screen = 'left_1'
    fin "えっそれどういう…" id story7_09841c42

    ## New scene
    scene bg classroom1 at pan_to_bottom
    show romania large cry nyaa at pos_transform(xpos=300, ypos=-80)
    $ rom.screen = 'right_4long'
    rom "ロシアさんちに\nおいらの弟がひと人ぢ…\nじゃない友好的ホームステイ\nしてるんだよー…！" id story7_b8b3afeb
    
    $ _skip_appear_effect = True
    $ rom.screen = 'right_4long'
    rom "それでその…\n今配ったお菓子に…！\nううっ…ごめんよぅ…\nおいらがふがいないばっかりに…" id story7_b7c0ba93
    $ _skip_appear_effect = False


    show russia large smiling ufufu behind romania:
        xpos -90 ypos -30
        pause 0.3
        easein 1.0 xpos 0
    show romania large cry nyaa
    $ rus.screen = 'left_3'
    $ _pending_window_transform = (shake_7s2)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    $ _pending_sprite_transform = [("romania large cry", shake_7s2, Dissolve(0.2))]
    rus "もう！ルーマニア君\n先にネタバレしちゃ\nだめだよー。" id story7_79b6d094

    pause 0.5

    ## New scene
    scene bg classroom_door2 at pan_to_top
    show germany shocked at pos_transform(xpos=630, yalign=0.0)
    show finland oh at pos_transform(xpos=-80, ypos=30)
    show japan shocked at pos_transform(xpos=100, yalign=0.0)
    show america whatyousay at pos_transform(xpos=400, yalign=0.0)

    $ fin.screen = 'left_3'
    fin "え…？　もしかして\nお菓子とジュースに\n今の話の薬が…？" id story7_6aebc3e7

    show america eksdee
    $ ame.screen = 'right_4long'
    ame "ＤＤＤＤＤ！\nそんなイギリスの\nファンタジーみたいな薬\n作れるわけないんだぞ！" id story7_ae8f0180

    show england blush shout at pos_transform(xpos=200, yalign=0.0)
    $ eng.screen = 'center_3long'
    eng "そ、そうだ…！\nそんな薬あるわけないだろ！\n{size=-5}ってお前俺に対してどんな認識なんだよ！{/size}" id story7_f01bac54

    ## New scene
    scene bg classroom_window

    show russia large smiling at pos_transform(xpos=200, ypos=-80)
    $ rus.screen = 'right_4'
    rus "んーどうかな？\n時間が立てば\n分かるんじゃないかな" id story7_85172fa2

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
    fin "謀りましたね！\n僕お菓子僕いっぱい\n食べちゃったん\nですけど…！" id story7_3f048254

    show england scream at pos_transform(xpos=200, yalign=0.0)
    $ eng.screen = 'center_3'
    eng "何真に受けてんだ！\nそんな薬あって\nたまるか！" id story7_6924f121

    show germany shocked at pos_transform(xpos=500, yalign=0.0)
    show germany ohno
    $ ger.screen = 'right_4long'
    ger "いや、あながち嘘では\nないかもしれん！\n昔からロシアはやれば\n何故か出来てしまうんだ！" id story7_a545eee0

    show germany blush yell
    $ ger.screen = 'right_4long'
    ger "思い出せ！今まで\n「よくわからないけど\n　すごいものが出来たよー！」\nという事が何度あった！？" id story7_c516660c

    show germany yell eyesclosed
    $ ger.screen = 'right_4long'
    ger "どうやったら\nお前にそれが作れる！？\nということを平気でやるのが\nロシアではないのか！" id story7_6208f4e2

    show england sweat blush whatthehell
    $ eng.screen = 'center_3'
    eng "…………思い当たる\n節しかない…！" id story7_3dd0a280

    show japan blush sweat embarassed at pos_transform(xpos=450, yalign=0.0) behind england 
    $ jpn.screen = 'right_4long'
    jpn "例えもし本当に\n効果があったとしても\n永続的に脳をコントロールし\n続けることはできないはず…！" id story7_749dc914

    show spain oh behind finland:
        xpos 50 yalign 0.0
        linear 0.4
        easeout 0.3 yoffset -40
        easein 0.2 yoffset 40
        easeout 0.2 yoffset -30
        easeout 0.2 yoffset 0
    $ spa.screen = 'center_4long'
    spa "せやけど一時的でも\nコントロールされとる間に\n次の飲まされたら\n終わりなんちゃう？" id story7_48aa3636

    show england scream
    $ eng.screen = 'center_3'
    eng "あああああああ！！\nいやだ！いやすぎる！" id story7_c962e036

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
    spa "あっせやけどお願い聞こえんくらい\n離れたら大丈夫や思うで！\nほな！帰ろかー！" id story7_3bf446ee
    
    $ _skip_appear_effect = True
    show spain med shocked with {'master': Dissolve(0.25)} 
    $ spa.screen = 'center_4long'
    $ _pending_window_transform = (shake_7s3)
    extend "\n…ドアノブつめたっ！" id story7_7a388682
    $ _skip_appear_effect = False


    ## New scene
    scene bg aura1
    play music "music/Carol_of_the_Bells_ESPN.ogg"
    show snow1_0 onlayer vfx_back
    show snowfront_0 onlayer vfx_front
    show circle_anim onlayer vfx_front
    pause 0.005
    show russia 2 normal onlayer chara with {'chara':circle_dissolve2}:
        xpos 100 ypos -30
        pause 1.5
        linear 1 xpos 220
    $ rus.screen = 'right_4'
    rus "効いてくるまで\n少し時間がかかるから\nもうちょっとだけ\nこの部屋にいようね。" id story7_e767e6e2
    hide circle_anim

    show russia 2 sigh onlayer chara:
        xpos 220 ypos -30
    $ rus.screen = 'right_4'
    $ _pending_sprite_transform = [("russia 2 normal", pos_transform(xpos=220, ypos=-30), Dissolve(0.2))]
    rus "ごめんね。みんな。\nでもこれから僕たち\nとっても仲良くなれるから\nみんな幸せだよね？" id story7_83848811

    play sound "sfx/ding30.ogg"
    show romania cry nyaa onlayer chara behind russia:
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
    rom "うわーん！\n皆ごめんよごめんよー！\nこんなのってないよー" id story7_c61548e2

    
    scene onlayer chara
    scene bg aura2

    show america angry worried onlayer chara at pos_transform(xpos=500, yalign=0.0)
    $ ame.screen = 'right_3'
    $ _pending_window_transform = (shake_7s4)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    ame "くそっ！\nこれじゃあ寒すぎて…\n力が出ないじゃないか！" id story7_3f5fd2bf
    stop sound

    show england blush shout2 onlayer chara:
        xpos 340 yalign 0
        time 0.5
        block:
            linear 0.07 xoffset +5
            linear 0.07 xoffset -5
            repeat
    $ eng.screen = 'center_3'
    eng "なんだよこの雪！\nいつもの力が出せれば\nこんな奴なんかに…！！" id story7_8bac0689

    show bulgaria cry waah onlayer chara at pos_transform(xpos=70, yalign=0.0)
    $ bul.screen = 'left_3'
    bul "それある意味\n死亡フラグなんだわー" id story7_51fcdbe8

    hide england
    hide america
    hide bulgaria
    with {'chara':Dissolve(0.2)}

    ## New scene
    scene bg aura1
    #show snow1_0
    #show snowfront_0
    with Dissolve(0.1)
    
    show russia 2 large worried onlayer chara with {'chara': Dissolve(0.3)} :
        xpos -70 ypos -90
    $ rus.screen = 'right_4long'
    $ _pending_sprite_transform = [("russia 2 large sigh", pos_transform(xpos=-70, ypos=-90), Dissolve(0.2))]
    rus "う～ん。なんでこういう\n反応になっちゃうのかな？\n僕なりに頑張って君たちに\n歩み寄ってみたんだけれど…。" id story7_98c5cd80

    show russia 2 large ahahahaha
    $ rus.screen = 'center_3'
    rus"大丈夫。\n僕は怖くないよ？" id story7_e50d5526

    hide snowfront_0
    hide snow1_0
    hide russia
    
    ## Choice scene
    scene bg aura2

    menu:

        "成り行きに任せる":
            jump donothing

        "俺が止める！！":
            jump stophim




label stophim:
    play music "music/Dancing_Fool.ogg"

    show snow2_0 onlayer vfx_back
    show snowfront2_0 onlayer vfx_front

    show bulgaria med eek onlayer chara at pos_transform(xpos=440,ypos=-40)
    $ bul.screen = 'right_4'
    bul "ロ…ロシアさんっ！\nちょっとそれは\nやめるんだわー！" id stophim_a4c8c443

    show romania med shocked eh onlayer chara behind bulgaria:
        xpos 0 ypos -40
        parallel:
            linear 1 xoffset 140
        parallel:
            linear 0.1 yoffset 0
            easein 0.2 yoffset -40
            easein 0.2 yoffset 30
            easein 0.2 yoffset -20
            easein 0.2 yoffset 10
            easein 0.1 yoffset -5
            easein 0.1 yoffset 0

    pause 1
    $ rom.screen = 'left_3'
    rom "ちょっ！\n何言ってるんだよー\nそれならおいらが…" id stophim_109c1aca

    show bulgaria med conniving
    $ bul.screen = 'right_7big'
    bul "（まあ俺とロシアさんって\n　なかよし！とは言えないまでも\n　他のヨーロッパの国よりは\n　仲が良好な方だと思うから\n　こんな事をしても多分\n　それほどひどい事には\n　ならないはずなんだわー！）" id stophim_5102abb4

    show romania med tired sweat laugh
    $ rom.screen = 'left_3'
    rom "（あ…、あー…）" id stophim_8a71a952

    show bulgaria med conniving eyesclosed
    $ bul.screen = 'right_4long'
    bul "（この裏事情がなかったら\n　普通に帰ってたんだわ…\n　他の皆さんにも良い所\n　お見せできるしな。うん）" id stophim_0fc4d76e

    show romania med tired sweat laugh
    $ rom.screen = 'left_4long'
    rom "（そうなんだねー！\n　この場も救って\n　対外アピールも出来ちゃう\n　ブルガリア流石なんだよー）" id stophim_20a5e4d8

    show bulgaria med ello
    $ bul.screen = 'right_4long'
    bul "俺は菓子を食っていない！\n盾になってでも！みなさんを！\nお守りするんだわー！" id stophim_6775b8a1


    ## New scene
    hide bulgaria
    hide romania

    scene bg aura1

    show russia 2 large hmmm isee onlayer chara at pos_transform(xpos=-200, ypos=-50)
    $ rus.screen = 'right_4'
    rus "え…。君がみんなの\n盾になるっていうの\nブルガリア君？" id stophim_1321376f

    show russia large mmph onlayer chara:
        xpos 200 ypos -40
    
    $ rus.screen = 'left_1'
    rus "んー…。" id stophim_fd42778c

    hide snow2_0
    hide snowfront2_0
    show russia large chuckle onlayer chara
    $ rus.screen = 'left_4'
    rus "わかった。\n君がそう言うなら\n今日は止めておくね" id stophim_70418c9f

    hide russia

    ## New scene
    scene bg classroom1

    show romania med shocked eh at pos_transform(xpos=400, ypos=-40)
    show bulgaria med conniving at pos_transform(xpos=100,ypos=-40)
    play music "music/carnaval_de_paris_elliot_simons.ogg"
    $ bul.screen = 'left_3'
    bul "えっ、まじっすか！\nあざーっす！\nあざーっす！" id stophim_025e173f

    $ rom.screen = 'right_1'
    rom "すごい！本当に！？" id stophim_06388748

    show england waahahaha at pos_transform(xpos=-90,yalign=0.0) behind bulgaria
    $ eng.screen = 'left_4long'
    eng "はははは！ロシア、お前が\nこの程度で引っ込むとは\nやはり薬ははったりだったか！\n多分はったりだ！はったりだよな…？" id stophim_d2a17599

    ## New scene
    scene bg exterior1 at pan_to_top
    na "こうしてブルガリアさんの機転により、\nこの場を丸く収める事が出来たのだった。" id stophim_249636d1

    $ _skip_appear_effect = True
    na "ロシアさんの薬を噂っぽくぼかして７話目にして、\n後日イギリスが一人で１００話も語ったため\n１０７つの怖い話として校内新聞に載せられた。" id stophim_0b8ee69b

    na "全てそこそこほどほどに\n綺麗にまとまる！　　　　…はずだった。" id stophim_2ab3c212
    $ _skip_appear_effect = False
    stop music fadeout 1

    ## New scene
    scene black
    pause 0.3

    $ bul.screen = 'center_1'
    bul "………ん！？" id stophim_e7131160

    scene bg bul0
    $ bul.screen = 'left_3'
    bul "…あれ？\n俺、何してたっけ？" id stophim_2e6b0042

    scene bg bul1
    play music "music/collision_course_paolo_bolio_hq.ogg"
    $ bul.screen = 'center_1'
    bul "えっなんだこれ！？" id stophim_77f4beb2

    $ bul.screen = 'center_3'
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    $ _pending_camera_transform = [([shake_7s5], "master"), ([shake_7s5], "screens")]
    bul "えええ！？\nちょ…なにが\nどうなってんだわー！？" id stophim_b286e950
    $ _pending_camera_transform = None
    camera at reset
    camera screens at reset


    $ rus.screen = 'left_3'
    rus "おはようブルガリア君！\n君の英雄的行為\nかっこよかったよ" id stophim_886905b6

    scene bgbul 2 at pan_bul2
    show bulvfx
    $ bul.screen = 'center_3'
    bul "ロシアさん…！？\nえ、あざっす…" id stophim_c6628b52
    
    $ bul.screen = 'center_3'
    $ _pending_window_transform = (shake_7s9)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    bul "でも何でこんな展開\nになるんだわー！？\nあっ、いや。ですかー！" id stophim_1b277827

    $ rus.screen = 'left_3'
    rus "君が代わりに\nなるんだーって\n言ったじゃない" id stophim_259d5e1c

    show bgbul 3
    $ bul.screen = 'center_3'
    bul "こういうのじゃなくて\nもっとカッコイイ\n感じの身代わりでぇ…！！" id stophim_4420e5b9
    $ _skip_appear_effect = True
    bul "割と俺とロシアさんとの\n関係だって良好な方\nじゃないっすかー！！" id stophim_782d8e5b
    $ _skip_appear_effect = False


    $ rus.screen = 'left_3'
    rus "しょうがないよ\nこういう役回りの子が\n出るのが伝統だもの" id stophim_e61ef841

    show bgbul 5
    $ bul.screen = 'center_3'
    bul "伝統！？　伝統って\nなんなんだわー！！？" id stophim_00738668

    $ rus.screen = 'left_1'
    rus "しらないにゃん♪" id stophim_33de9b00

    show bgbul 4
    $ bul.screen = 'center_3'
    bul "え…それって…\nだってあの時ロシアさん\nいなかったじゃ…" id stophim_37131345

    $ rus.screen = 'left_3'
    rus "これ？　何でも許して\nもらえる魔法の言葉だよ\nあっ、そうだ！" id stophim_dbc52dbc
    
    $ rus.screen = 'left_3'
    $ _pending_window_transform = (shake_7s6)
    $ _pending_sound = ("sfx/ding27.ogg", "sound")
    rus "目立てて\n良かったね♪" id stophim_d118f906
    stop sound

    
    show bgbul 3
    $ bul.screen = 'center_3'
    
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    $ _pending_stop_music = 2
    $ _pending_camera_transform = [([sshake], "screens")]
    bul "最初っから…！\n最初っからー！！" id stophim_6cb88e8b
    $ _pending_camera_transform = None


    $ rus.screen = 'left_4'
    rus "君達の会話って\n流しっぱなしにすると\n癒し効果があるから好きだよ" id stophim_0ba32b4e

    scene bg exterior
    show staffroll:
        ypos 600
    play music "music/11_liarliar.ogg"

    show staffroll with {'master': None}:
        linear 4 ypos 40
    
    $ bul.screen = 'left_4'
    $ _pending_window_transform = (shake_7s7)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    bul "あ！でもよく考えたら\n確かにおいしい\nポジションですわ！\nあざーっす！あざーっす！{nw=2}" id stophim_3556432d
    
    show staffroll with {'master': None}:
        linear 4 ypos -450

    $ rus.screen = 'center_3'
    rus "君って意外と\n神経図太いよね{nw=3}" id stophim_e1c6c2ea

    show staffroll with {'master': None}:
        linear 3 ypos -770
    pause 2.5

    show bg exterior4 behind staffroll
    show staffroll with {'master': None}:
        linear 7 ypos -1630
    pause 6.5

    show bg exterior5 behind staffroll
    show staffroll with {'master': None}:
        linear 7 ypos -2305
    pause 6.2

    show bg exterior6 behind staffroll
    show staffroll with {'master': None}:
        linear 7 ypos -2765
    pause 6.5

    show bg exterior8 behind staffroll
    show staffroll with {'master': None}:
        easein 8 ypos -3000
    pause 8
    show staffroll with {'master': None}:
        ypos -3000
        linear 3.5 alpha 0
    pause 3.5

    stop music fadeout 3
    pause 1

    $ persistent.game_finished = True

    $ quick_menu = False

    scene white screen with fade_white
    
    pause 0.5
    
    return

label donothing:
    show snow2_0 onlayer vfx_back
    show snowfront2_0 onlayer vfx_front

    $ audio_crossFade(1, "music/39_USbattlesong.ogg")
    show america med angry yell onlayer chara at pos_transform(xpos=100,ypos=-30)
    $ ame.screen = 'right_3'
    ame "やめるんだロシア！\n君がやめないのなら\n俺が君を止めるまでだ！" id donothing_9e5b1917

    hide america

    scene bg aura1
    show russia large smiling onlayer chara at pos_transform(xpos=200,ypos=-50)
    $ rus.screen = 'right_4long'
    rus "ふふっ\nそのお願いは聞けないかなぁ。\nそれに今の君に\nそんな力はないでしょう？" id donothing_d70e96ff
    show russia large happy

    $ ame.screen = 'left_4long'
    $ _pending_window_transform = (shake_7s8)
    $ _pending_sound = ("sfx/hit51.ogg", "sound")
    ame "確かに今の俺には\n君に対抗できる力が出せない。\nだがそれで俺は諦めない！" id donothing_b8455794

    hide russia
    window show
    scene bg aura2
    show america large angry yell onlayer chara at pos_transform(xpos=100,ypos=-50)
    
    $ ame.screen = 'right_3'
    ame "そうとも！\n信じていれば！\n夢は叶うんだぞ！{nw=0.5}" id donothing_4db270a6
    play sound "sfx/BIGBEAST.WAV"
    camera at ripple2
    camera screens at ripple2
    hide snow2_0
    hide snowfront2_0
    show bg aura3 with {'master':circle_dissolve2}

    show sparkle_up onlayer vfx_back
    show sparkle_radiate onlayer vfx_front
    extend "{nw=2}"
    camera at sshake_long
    camera screens
    extend "{nw=2}"
    hide america with {'chara':Dissolve(0.2)}
    hide sparkle_radiate with {'vfx_front':Dissolve(0.2)}
    pause 0.5
    window auto



    scene bg aura1
    camera at sshake_long
    show russia 2 large cry yaaah onlayer chara at pos_transform(xpos=0,ypos=-30)
    play sound "sfx/MONSTER1.WAV"
    $ rus.screen = 'right_4long'
    rus "そんな…！\n君のどこにそんな力が！？\n嘘だよこんなの…！{nw=1}" id donothing_7b331410

    stop music fadeout 3
    stop music1 fadeout 3
    $ quick_menu = False

    play sound2 "sfx/Jurassic loop.wav"
    hide sparkle_up
    hide russia
    camera
    show white screen
    pause 6
    
    camera
    stop sound
    play music "music/International_Uplifting_Dance-full_length_track.ogg"

    scene bg exterior2 at pan_to_top
    $ quick_menu = True
    show america eksdee at pos_transform(xpos=300,ypos=30)
    $ ame.screen = 'center_3long'
    ame "っていう映画を\n作ろうと思ってるんだよ！\nどうだい面白そうだろう！" id donothing_a2cc0ec7

    show staffroll with {'master': None}:
        ypos 600
    show russia mmph at pos_transform(xpos=50,ypos=30) behind america
    $ rus.screen = 'left_3'
    rus "えーまた僕を悪役にするの？\nアメリカ君、君って\n逆に僕のこと好きでしょ？" id donothing_7c44211d

    show staffroll with {'master': None}:
        linear 4 ypos 230 # next nw + 1

    show america youreallyare
    $ ame.screen = 'center_3'
    ame "おいおい！\nどうして\nそうなるんだい！？{nw=3}" id donothing_8317ac46

    show staffroll with {'master': None}:
        linear 5.5 ypos -320

    show russia happy
    $ rus.screen = 'left_4'
    rus "だって多少時代背景や\n舞台設定に無理があっても\n何が何でも僕を黒幕\nしたがるじゃない…。{nw=3.5}" id donothing_427f0b6c

    show staffroll with {'master': None}:
        linear 6 ypos -980

    show russia smiling ufufu
    $ rus.screen = 'left_4long'
    rus "そこまでして僕黒幕オチを\n多用する背景には\n僕への好意があるんじゃないかと\n疑わざるを得ないよ。{nw=4.5}" id donothing_049c45b4

    show staffroll with {'master': None}:
        linear 5 ypos -1470

    show america whatyousay
    $ ame.screen = 'center_3long'
    ame "ＮＯＯＯ！\n黒幕と陰謀っていったら\n君ってイメージなだけだよ！！{nw=3.7}" id donothing_cea25ed6

    show staffroll with {'master': None}:
        linear 6 ypos -1980

    show russia glum
    $ rus.screen = 'left_4long'
    rus "そうかなぁ。\n君よりはクリーンなつもりだよ？\nだって何が起こっても\n背後は僕！って言われるじゃない。{nw=4.5}" id donothing_b92b412d

    show staffroll with {'master': None}:
        linear 6 ypos -2410

    show russia smiling ufufu
    $ rus.screen = 'left_4long'
    rus "…まあその通りなんだけど。\nそれってとってもわかりやすくて\nみんなから見えてるわけだから\n陰謀や黒幕とは言えないよ。{nw=4}" id donothing_9f34fc55


    show staffroll with {'master': None}:
        linear 6 ypos -2660

    show america sneer
    $ ame.screen = 'right_4'
    ame "た、確かに…！\n映画的にも黒幕予想が\nイージーすぎて\nナンセンスだね！{nw=3}" id donothing_d19cefa0

    hide america
    hide russia
    show bg exterior4

    pause 1

    show staffroll with {'master': None}:
        linear 2.5 ypos -2780

    $ rus.screen = 'left_3'
    rus "じゃあ今度は\n誰黒幕にする？{nw=1.5}" id donothing_f443eb14

    show staffroll with {'master': None}:
        linear 3 ypos -2870

    $ ame.screen = 'center_3'
    ame "君以外で…？！\nどうやれっていうんだい！{nw=2}" id donothing_75f5c236

    show staffroll with {'master': None}:
        linear 4 ypos -2970

    $ rus.screen = 'left_3'
    rus "こうしていつも通りの\nアメリカ君の映画が\nできるわけだね。{nw=3}" id donothing_780e2b04

    show staffroll with {'master': None}:
        easein 3.7 ypos -3000

    $ rus.screen = 'left_4long'
    rus "フランス君ほどとは\n言わないけどひねろうよ。\nスペイン君みたいに\n最後の５分で暴走するのも良いね。{nw=3.7}" id donothing_158654f4
    
    show staffroll with {'master': None}:
        ypos -3000
        linear 3.2 alpha 0.0

    $ ame.screen = 'center_3'
    ame "それなら最近\n新しいタイプの\nエンディングを考えて…！{nw=2.2}" id donothing_820f8046


    $ rus.screen = 'left_4'
    rus "家の中の怪奇現象は全部\n宇宙人がやってましたオチと\n友だちが悪魔化して全滅オチ\nじゃないよね？{nw=4}" id donothing_00bfdef7
    

    stop music fadeout 3
    $ ame.screen = 'center_3'
    ame "くっ！\n君厳しいよ！{nw=2}" id donothing_fa690420

    pause 1
    $ persistent.game_finished = True

    $ quick_menu = False

    scene white screen with fade_white
    pause 0.5
    
    return

    