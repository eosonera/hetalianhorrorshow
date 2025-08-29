

label story4:
    stop music
    scene bg exterior3
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第四話　ドイツの怖い話。{/size}"
    
    show white screen onlayer bottom

    scene bg classroom1 at pan_to_top
    play music "music/11_weisswurst.ogg"
    pause 0.2
    show germany large phew at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    
    story "もう俺の番か。\nふむ、参ったな。"

    show germany large hmph
    with {'master': Dissolve(0.2)} 
    story "…俺はここ数日、あー…\n俗にいう怪奇現象に\n悩まされていてだな…。"

    show germany large squint
    with {'master': Dissolve(0.2)} 
    story "ルーマニアに相談した所、\n今日の集会で話してほしいと頼まれて\n来たわけなのだが…。"
    nvl clear
    
    show germany large angry eyesclosed
    story "ちょうど昨日、\n解決してしまったのだ。"
    story "{color=#ADB1B9}「じゃあ解決するまでのお話し\n　聞かせてほしいっす」{/color}"
    nvl clear

    stop music fadeout 4
    show germany large exasperated
    story "分かった。\nでは俺の家で起こった\n怪奇現象の話をしよう。"
    nvl clear
    
    scene black
    show nvl_textbox
    play music "music/approach quietly.ogg"
    story "俺の家では、数日前から\n奇怪な現象が起こるようになった。"

    show bg armor0 behind nvl_textbox

    
    story "その怪奇現象というのが\n家の廊下に飾ってある鎧が\n夜な夜な動くというものだ。"
    nvl clear

    scene bg classroom1 at pan_to_top
    show germany large phew at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    with Dissolve(0.25)
    
    story "……………。\n　\nああー…笑ってくれ。\n今にして思えば何故こんな現象に\n本気で恐怖していたのか……。"
    nvl clear

    scene bg armor0
    show nvl_textbox
    with Dissolve(0.25)

    story "ある朝、装飾品として置いてある\n鎧の位置が昨日と変わっているように感じた。\nそれに昨日より表面に光沢が増してるようだ。\nその時は気に留めもしなかったのだが…。"
    story "だがその日から\n深夜になると家の中から\n鎧のきしむ音や、剣がぶつかる音が\n聞こえてくるようになったのだ…。"
    nvl clear
    
    story "最初は音だけであったが、\n３日目あたりから鎧は\n俺の前に姿を現すようになった。"
    story "もちろん遭遇してすぐ\n追いかけたが…。"
    story "重い金属を全身に\n纏っているというのに、\n鎧は俺の全速力の追跡を\nやすやすと振り切った。"
    nvl clear
    
    story "それに、俺の家の厳重な\nセキュリティー下にありながら\n警報すらならさず現れる鎧…。\n　\n一体…何者なんだ！\n何故俺の家に現れる！\n訴えたいことがあるなら\n口頭か筆記してくれ！"
    nvl clear
    
    story "…ごほん。仕方がないので\n俺は鎧を観察することにした。\n　\n観察して分かったのが\n鎧との遭遇場所は仕事部屋付近が多い。\nそして何故かパソコンを勝手に起動させる。"
    nvl clear
    story "今まで超常現象の類は、\n全て科学で説明できると思っていたのだが\n家中のセキュリティのかいくぐり、\n俺が全力で追いかけても\n追いつけない鎧…。\n\nこれは科学で証明できるのか？\n鎧の持ち主が幽霊になって\n往年の甲冑姿で現れたのでは？\nと考えるようになっていた。"
    nvl clear
    story "俺が調べたところ\nこの鎧を作らせた最初の持ち主は\n一度もこの鎧を着用して\n戦場には立っていない…。"
    story "この鎧自体最初から\n実用性よりもデザインを重視した\n装飾用の鎧だったのだ。\nなぜ現代になって\n甲冑姿で現れるようになったのか\n謎は深まるばかりだった。"
    nvl clear
    story "おかしな点はもう一つある。\n　\n夜になると俺の家に現れる動く鎧は\n年代も製造された場所も違う二つの鎧の\nパーツを繋ぎあわせて一つの鎧にしていた。\n　\n鎧の持ち主が鎧に取り憑いたのならば\n果たしてそんなことをするだろうか？"
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
    ger "すまないが日本\nまだだ。まだ耐えてくれ"
    $ jpn.screen='center_1'
    jpn "すいません…"

    stop music fadeout 1
    scene black
    show nvl_textbox
    $ na2.screen='center_1'
    na2 "そして昨日。"
    show bg armor behind nvl_textbox
    with {'master': Dissolve(0.25)} 
    play music "music/echo.ogg"
    story "\n\n\n…鎧が俺の寝室に\n座っているではないか！"
    nvl clear
    story "\n\nこの鎧…、何者なんだ…！！"
    story "最近、眠りが浅く\n小さな物音でも起きてしまう俺に\n気づかれずに侵入するとは…！"
    nvl clear

    scene bg armor2
    show nvl_textbox
    with flashbulb
    show nvl_textbox at shake_4s1 with {'master': Dissolve(0.25)} 
    play sound ["<silence .2>", "sfx/hit34.ogg"]
    $ window_transform = shake_4s1
    story "\n「誰だっ！！」{nw=1}"
    $ window_transform = None
    extend "\n俺が問い詰めると…！"
    nvl clear
    
    scene bg oresama
    show nvl_textbox
    with flash
    camera at sshake
    camera screens at sshake
    play sound "sfx/wa-bam.ogg"
    story "{size=+15}　\n　\n「俺様だっ！！」{/size}"
    nvl clear

    camera
    camera screens
    scene bg classroom1 at pan_to_bottom
    $ audio_crossFade(0.25, "music/11_weisswurst.ogg")
    show germany squint exasperated at pos_transform(xpos=500, yalign=0.0)
    $ ger.screen = 'right_1'
    ger "…という話だ。"

    play sound ["<silence .8>", "sfx/hit34.ogg"]
    show england blush shout at pos_transform(xpos=200, yalign=0.0)
    $ eng.screen = 'center_3long'
    $ window_transform = shake_4s3
    eng "最初から犯人\nお前の兄貴しかいねーだろ！"
    $ window_transform = None

    show germany exasperated
    $ ger.screen = 'right_4'
    ger "いやしかし\n怪奇現象の初日に\n本人に証言を求めた所\n自分ではないと…！"

    show finland suup at pos_transform(xpos=340, yalign=0.0) behind germany
    $ fin.screen = 'center_3'
    fin "それ\n信じちゃったんですか！？"

    show japan worried grimace at pos_transform(xpos=0, yalign=0.0)
    $ jpn.screen = 'left_3'
    jpn "御兄弟仲が良くて\n楽しそうですね。"

    stop music1 fadeout 1



    jump story5