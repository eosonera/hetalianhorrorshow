

label story4:
    stop music
    scene bg exterior3
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第四話　ドイツの怖い話。{/size}" id story4_0323968c
    
    show white screen onlayer bottom

    scene bg classroom1 at pan_to_top
    play music "music/11_weisswurst.ogg"
    pause 0.2
    show germany large phew at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    
    story "もう俺の番か。\nふむ、参ったな。" id story4_0de11457

    show germany large hmph
    with {'master': Dissolve(0.2)} 
    story "…俺はここ数日、あー…\n俗にいう怪奇現象に\n悩まされていてだな…。" id story4_441a4c9e

    show germany large squint
    with {'master': Dissolve(0.2)} 
    story "ルーマニアに相談した所、\n今日の集会で話してほしいと頼まれて\n来たわけなのだが…。" id story4_3f0b9594
    nvl clear
    
    show germany large angry eyesclosed
    story "ちょうど昨日、\n解決してしまったのだ。" id story4_c4a631ad
    story "{color=#D7D7D7}「じゃあ解決するまでのお話し\n　聞かせてほしいっす」{/color}" id story4_071eaeaa
    nvl clear

    stop music fadeout 4
    show germany large exasperated
    story "分かった。\nでは俺の家で起こった\n怪奇現象の話をしよう。" id story4_472a74c9
    nvl clear
    
    scene black
    show nvl_textbox
    play music "music/approach quietly.ogg"
    story "俺の家では、数日前から\n奇怪な現象が起こるようになった。" id story4_ae0630bf

    show bg armor0 behind nvl_textbox

    
    story "その怪奇現象というのが\n家の廊下に飾ってある鎧が\n夜な夜な動くというものだ。" id story4_bda42bac
    nvl clear

    scene bg classroom1 at pan_to_top
    show germany large phew at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    with Dissolve(0.25)
    
    story "……………。\n　\nああー…笑ってくれ。\n今にして思えば何故こんな現象に\n本気で恐怖していたのか……。" id story4_c761605a
    nvl clear

    scene bg armor0
    show nvl_textbox
    with Dissolve(0.25)

    story "ある朝、装飾品として置いてある\n鎧の位置が昨日と変わっているように感じた。\nそれに昨日より表面に光沢が増してるようだ。\nその時は気に留めもしなかったのだが…。" id story4_bb381755
    story "だがその日から\n深夜になると家の中から\n鎧のきしむ音や、剣がぶつかる音が\n聞こえてくるようになったのだ…。" id story4_87ff0c57
    nvl clear
    
    story "最初は音だけであったが、\n３日目あたりから鎧は\n俺の前に姿を現すようになった。" id story4_c0cc4035
    story "もちろん遭遇してすぐ\n追いかけたが…。" id story4_6b52a727
    story "重い金属を全身に\n纏っているというのに、\n鎧は俺の全速力の追跡を\nやすやすと振り切った。" id story4_a76262fd
    nvl clear
    
    story "それに、俺の家の厳重な\nセキュリティー下にありながら\n警報すらならさず現れる鎧…。\n　\n一体…何者なんだ！\n何故俺の家に現れる！\n訴えたいことがあるなら\n口頭か筆記してくれ！" id story4_2f1085a7
    nvl clear
    
    story "…ごほん。仕方がないので\n俺は鎧を観察することにした。\n　\n観察して分かったのが\n鎧との遭遇場所は仕事部屋付近が多い。\nそして何故かパソコンを勝手に起動させる。" id story4_7bc20324
    nvl clear
    story "今まで超常現象の類は、\n全て科学で説明できると思っていたのだが\n家中のセキュリティのかいくぐり、\n俺が全力で追いかけても\n追いつけない鎧…。\n\nこれは科学で証明できるのか？\n鎧の持ち主が幽霊になって\n往年の甲冑姿で現れたのでは？\nと考えるようになっていた。" id story4_bfce9e9b
    nvl clear
    story "俺が調べたところ\nこの鎧を作らせた最初の持ち主は\n一度もこの鎧を着用して\n戦場には立っていない…。" id story4_d09a6f13
    story "この鎧自体最初から\n実用性よりもデザインを重視した\n装飾用の鎧だったのだ。\nなぜ現代になって\n甲冑姿で現れるようになったのか\n謎は深まるばかりだった。" id story4_21f00a1b
    nvl clear
    story "おかしな点はもう一つある。\n　\n夜になると俺の家に現れる動く鎧は\n年代も製造された場所も違う二つの鎧の\nパーツを繋ぎあわせて一つの鎧にしていた。\n　\n鎧の持ち主が鎧に取り憑いたのならば\n果たしてそんなことをするだろうか？" id story4_440ccdcf
    nvl clear


    scene bg classroom4 at pan_to_bottom
    pause 0.2
    play sound ["sfx/ding31.ogg"]
    show germany blush yell at pos_transform(xpos=500, yalign=0.0)
    show japan blush sweat annoyed:
        xpos 140 yalign 0.0
        block:
            linear 0.07 xoffset -2
            linear 0.07 xoffset 2
            repeat

    $ ger.screen='right_3'    
    ger "すまないが日本\nまだだ。まだ耐えてくれ" id story4_717cf02b
    $ jpn.screen='center_1'
    jpn "すいません…" id story4_5801e524

    stop music fadeout 1
    scene black
    show nvl_textbox
    $ na2.screen='center_1'
    na2 "そして昨日。" id story4_be15ea8f
    show bg armor behind nvl_textbox
    with {'master': Dissolve(0.25)} 
    play music "music/echo.ogg"
    story "\n\n\n…鎧が俺の寝室に\n座っているではないか！" id story4_589fc39b
    nvl clear
    story "\n\nこの鎧…、何者なんだ…！！" id story4_2b2a9f2e
    story "最近、眠りが浅く\n小さな物音でも起きてしまう俺に\n気づかれずに侵入するとは…！" id story4_65a1f530
    nvl clear

    scene bg armor2
    show nvl_textbox
    with flashbulb
    show nvl_textbox with {'master': Dissolve(0.25)} 
    $ _pending_sprite_transform = [("nvl_textbox", shake_4s1)]
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    story "\n「誰だっ！！」{nw=1}" id story4_97013b54
    extend "\n俺が問い詰めると…！" id story4_db9e14d2
    nvl clear
    stop sound
    
    scene bg oresama
    show nvl_textbox
    with flash    
    $ _pending_sound = ("sfx/wa-bam.ogg", "sound")
    $ _pending_camera_transform = [([sshake], "master"), ([sshake], "screens")]
    story "{size=+15}　\n　\n「俺様だっ！！」{/size}" id story4_f7379636
    nvl clear
    stop sound
    $ _pending_camera_transform = None

    camera
    camera screens
    scene bg classroom1 at pan_to_bottom
    $ audio_crossFade(0.25, "music/11_weisswurst.ogg")
    show germany squint exasperated at pos_transform(xpos=500, yalign=0.0)
    $ ger.screen = 'right_1'
    ger "…という話だ。" id story4_27a4b855

    
    show england blush shout at pos_transform(xpos=200, yalign=0.0)
    $ eng.screen = 'center_3long'
    $ _pending_window_transform = (shake_4s3)
    $ _pending_sound = ("sfx/hit34.ogg", "sound")
    eng "最初から犯人\nお前の兄貴しかいねーだろ！" id story4_1e926c4b

    show germany exasperated
    $ ger.screen = 'right_4'
    ger "いやしかし\n怪奇現象の初日に\n本人に証言を求めた所\n自分ではないと…！" id story4_c85d1002

    show finland suup at pos_transform(xpos=340, yalign=0.0) behind germany
    $ fin.screen = 'center_3'
    fin "それ\n信じちゃったんですか！？" id story4_79172393

    show japan worried grimace at pos_transform(xpos=0, yalign=0.0)
    $ jpn.screen = 'left_3'
    jpn "御兄弟仲が良くて\n楽しそうですね。" id story4_4991f3de

    stop music1 fadeout 1



    jump story5