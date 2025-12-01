

label story6:
    stop music
    scene bg exterior5
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第六話　スペインの怖い話{/size}" id story6_5501afc1
    show white screen onlayer bottom

    scene bg classroom1
    play music "music/Fall_In_Love.ogg"
    pause 0.2
    show spain large ahaha at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    with Dissolve(0.25)
    story "ほんま、遅れてごめんなぁ。\nなんや俺日向ぼっこしすぎて\n頭から草生えそうな勢いやー。" id story6_00b6f1e5
    nvl clear

    show spain large sup
    story "ほな、怖い話やんなぁ。\n俺の怖い話は日常に\n食い込んでくるタイプやで～。\n早速話させてもらうでー。" id story6_4530b679
    nvl clear
    
    show spain large smiling
    story "\nこれはアジアからの観光客が体験した話。\n…仮にワンさんとでもしとこか。\nなんや俺アジア人ゆーと\nワンさんってイメージやねん。\nイタちゃんの映画のせいやんな。" id story6_d84df516
    show spain large normal with {'master': Dissolve(0.2)}
    story "ある夏。ワンさんっちゅー方が\n俺の家に一人旅に来てはったん。" id story6_6882a1ea
    nvl clear
    
    story "初めて見るものの数々にワンさんは\n心躍らせとった…。" id story6_c923b31b
    show spain large wahaha with {'master': Dissolve(0.2)}
    story "俺の家今めっちゃ\n観光に力入れとるさかい、\nみんな来たってな～。\nほんま最高のバケーション？\nっちゅーやつを体験させたるよ～。" id story6_187d7f46
    
    show spain large fufufu with {'master': Dissolve(0.2)}
    play sound "sfx/HAUNTED HOUSE MOAN 4.ogg"
    story "{color=#808080}{cps=8}…気ぃ抜かんかったらな…。{/cps}{/color}" id story6_e8db0297
    nvl clear
    stop sound

    show spain large concern
    show nvl_textbox
    story "\n\nワンさんは俺の家初めて\nやったから知らんかったんや…。\n　\nワンさんを狙とる黒ーい影が\nぎょうさんおるっちゅー事を…。{nw}" id story6_88afc890
    show black with {'master': Dissolve(0.8)}
    stop music fadeout 3
    extend ""
    nvl clear

    play music "sfx/New York traffic from a rooftop upper east side.ogg"
    story "\nほんでワンさんが有名観光地を\n散策していた時の話や…。" id story6_6766d617
    hide spain
    hide black

    show bg postcard behind nvl_textbox
    play sound "sfx/footsteps_stop.ogg"
    story "\n「絵葉書！絵葉書こうて！！」" id story6_fb88e71b
    story "と下から声がしたん、\nそこに１０歳くらいの男の子がおってな。\n絵葉書こうて～って叫んでるん。" id story6_27cf66bf
    nvl clear
    
    story "まあ可愛らしい！そう思ったワンさんは\n絵葉書を買ったろう思たんやって。" id story6_445852eb
    story "「いくら？」" id story6_5eadaa5d
    story "「８ユーロ」" id story6_e15138bc
    stop music fadeout 3

    show spain large whatintarnation at pos_transform(xpos=350, ypos=-40) behind nvl_textbox
    with {'master': Dissolve(0.2)}
    play music "music/FilmEdge2_Casual_Z234-DayTripping-Kelly.ogg" fadeout 1
    story "{size=+12}【高｜たっか】っ！{/size}" id story6_917d478a
    nvl clear

    show bg classroom1 behind spain
    show spain large sweat
    story "絵葉書１枚８ユーロて！\n俺の一日の昼飯代やで…！" id story6_38b5b283

    show spain large blush areyoukidding
    with {'master': Dissolve(0.2)}
    story "\nえ…安すぎんとちゃうかって？\nほんまに！？、普通これくらいちゃうん！？\n俺、特別安い方なんかな…。\nそうなん…。" id story6_6429e0ff
    
    show spain large ahaha
    with {'master': Dissolve(0.2)}    
    story "今度上司に直談判してみるわ…。" id story6_5ecbbcbb
    nvl clear
    stop music fadeout 3

    scene bg postcard2
    show nvl_textbox
    story "あ、ほんで、ワンさんも８ユーロは\n高い思うたらしいんやけど、\n可愛い子供が一生懸命はがき売っとる姿に\n応援したなったらしくてな。" id story6_70baa050
    story "高い思うても言い値で\n買うたることにしたらしいで。\nワンさん金持ちやんな。" id story6_6b658eb9
    nvl clear
    story "ワンさんが財布開いた\nその時やった…！" id story6_94b3a7cf
    show bg white behind nvl_textbox
    with flash
    play sound "sfx/wood_hit_wood_1.ogg"
    play sound1 "sfx/coin01.ogg"
    play music "sfx/Subway station-New York-6 line-51st street-voices-some pa.ogg"
    story "ガキがジャンプしたか思うと\nワンさんの財布に入っとった\n１００ユーロ札ばっかわっしと掴むと\n猛ダッシュしよった！{nw}" id story6_9cde0fcb
    show bg runaway behind nvl_textbox with {'master': Dissolve(0.2)}
    play sound2 "sfx/run_wait.ogg"
    extend ""
    nvl clear

    stop music fadeout 2
    stop sound1 fadeout 1
    scene bg alley
    show nvl_textbox
    with Dissolve(0.2)
    story "ワンさんも追わはったけど\nガキめっちゃすばしっこい！\nががーっちゅー感じで急カーブしよって\nわーっと細い路地に逃げ込みよった！" id story6_8aeedff0
    
    
    show spain large cry mouthopen blush at pos_transform(xpos=350, ypos=-40) behind nvl_textbox
    show bg classroom1 behind spain
    story "ワンさんは俺の家のお客様やで！\n貴重なお客様になにしとんの…！！" id story6_5c411f77
    nvl clear

    show spain large concern
    story "…悪ガキもなんとかせんとなぁ…。\n普通に暮らせるくらいなら\n社会保障とかいろいろやっとるさかい\n盗みとかせえへんくてもええのに…。\nその辺、地方役所なにやっとんのかな。\n俺も反省せんとやなぁ。" id story6_d0372bdd
    show spain large fufufu bashful with {'master': Dissolve(0.2)}
    story "それとも普通に働くの\n馬鹿らしなるくらい稼ぎええんかな…。\n俺よりええ昼飯食ーてたりしてな。" id story6_44aa1f7b
    nvl clear
    
    show spain large oh
    story "あっ、ごめんなぁ。\n話戻すで！" id story6_4ffdcd16
    hide spain


    show bg alley behind nvl_textbox
    play music "music/unease.ogg"
    story "ワンさんがいかんかったんは、\nあの物売りを追いかけて\n人通りない路地に入ってもうた事…。" id story6_b90c161c
    story "もうあの物売りはいななってて、\n路地にはワンさんしかおらんかった…。\n意気消沈してもうたワンさんは\n立ち尽くすことしかでけへんかった…。" id story6_f10b6330
    nvl clear
    
    scene bg ripples1 with fade_red
    show ripples vfx
    show nvl_textbox
    play sound "sfx/bang08.ogg"
    story "\nほんならいきなり\nワンさん呼吸ができんくなった！" id story6_d3af068b
    story "なんや！何が起こっとるん！！？" id story6_01c97113
    hide ripples vfx
    show bg strangle behind nvl_textbox
    story "これは…" id story6_88fecc5f

    
    extend "\n最近はやりの首絞め強盗や！{nw}" id story6_996b431a
    play sound "sfx/hit43_a.ogg"
    camera at sshake
    camera screens at sshake
    extend ""
    nvl clear
    camera
    camera screens
    
    story "その名の通り\n首を絞めとる間にバッグを奪うっちゅー\n獲物がおるから、首絞めるくらいの\n野生返りも甚だしい手口やで！{nw}" id story6_0fa348b6
    stop music fadeout 1
    story "サバンナの方が住みやすいんとちゃうかなぁ…。" id story6_89f62fd0

    play sound "sfx/run_wait.ogg"
    play music "music/03_spidersandflies.ogg"
    show bg alley behind nvl_textbox
    story "ワンさんもいきなり首絞められたわけやろ\n対処しきれんくてな…。\nそのままバッグまで奪われてしもたん…。" id story6_ec6a28ce
    nvl clear

    scene bg luggage
    show nvl_textbox    
    story "ほな、このままうかうかしとったら\nいつ第二第三の首絞めに\nエンカウントするかわからん！\n警察や！思うたワンさんは\n走って警察を探すことにしたんやって。" id story6_c1b6aa94
    nvl clear
    
    scene bg pedestrian
    show nvl_textbox     
    story "人通りの多いとこまで戻らはったら\nちょうどええ所に警察官がひとり\nぶらぶらしとってな。" id story6_15534434
    story "これ幸いや思うて\nその警察官に助けを求めはったん。" id story6_0151faa2
    nvl clear

    scene bg officer
    show nvl_textbox  
    story "{color=#FFE5F7}「ふーん。え。\n　でパスポートはあるー？」{/color}" id story6_6ff65f7e
    story "こっちは緊急事態やで！\nなんやねんその気の抜けた応対は！" id story6_1ec35c69
    story "お、俺かてもうちょっと急ぐで！" id story6_80daeb48
    nvl clear

    story "{color=#FFE5F7}「ほんで、今日どないすんの？\n　金ないんならホテル泊まれへんやろ。\n　大使館いって帰りーや。ほな！」{/color}" id story6_f7788c46
    story "もー警官まったく話聞く気なしや。" id story6_7633cc15
    nvl clear

    scene bg pedestrian2
    show nvl_textbox      
    story "ワンさんは手元の翻訳機で\n\n{color=#D9DED3}「{/color}{color=#FFB5B5}パスポートもある{/color}{color=#D9DED3}し、\n　幸い{/color}{color=#FFB5B5}クレジットカードは取られてない{/color}{color=#D9DED3}から\n　ホテルくらいは何とかなる。\n　だけど、あの{/color}{color=#FFB5B5}バッグには大事なもの{/color}{color=#D9DED3}が\n　入っていてどうしても取り返したい」{/color}\n　\nって伝えたん。" id story6_8f19ed5d
    nvl clear
    
    scene bg officer
    show nvl_textbox  
    story "そんならその警官\n\n{color=#FFE5F7}「ほんなら付き合ったるわー」{/color}" id story6_66ebc9e4
    story "今まで「お前ウザいなぁあっち行ったれや」って\nオーラ出しとったんが一変して、\n急に話聞くモードになったらしいん。" id story6_c83b6365
    nvl clear
    stop music fadeout 3
    
    story "そらワンさんも必死やったし、\n本気出してもらわんと困るやんなぁ。" id story6_8409643a
    play sound "sfx/Footsteps On Concrete 1.ogg"
    story "せやけど、その警官ときたら、\nだらだら歩きながら、状況を聞くわけでもなく、\n犯人探すわけでもなく無駄口ばっかり叩きよる。" id story6_1d899206
    nvl clear

    story "短時間に二回も被害にあってねんで！\nもっと緊迫感もてや！なんて思うたんかしらんけど\nワンさんはちょいイラついた声で急かしたん。" id story6_a7e65f28
    
    show bg road behind nvl_textbox
    play sound "sfx/Footsteps On Concrete 1.ogg"
    play sound1 "sfx/Footsteps On Concrete 2.ogg"
    story "{color=#FFE5F7}「ごめんなぁ。こういうヤツは組織的やねん。\n　痕跡消すのも、隠れ場もめっちゃ巧妙でな。\n　せやから組織ごと潰さんと解決せぇへんのよ。\n　俺らが組織つぶした時にバックや財布\n　出てくるかもしれへんから被害届出そ」{/color}\n\nなんて言ってきたんやって。" id story6_c7c76c50
    nvl clear
    story "\nスペインてそんなもんなんやな～\n国が違うから警察もちゃうんやな～なんて\n別に変に思わんかったらしい…。" id story6_e2a5a836
    nvl clear

    scene bg walking
    show nvl_textbox
    play sound "sfx/footsteps.ogg"
    play music "music/lullaby_beat_julio_kladniew.ogg"
    story "\n「これから君の国の大使館いこかー。\n　ここから歩いてすぐやでー。\n　被害届出すさかい、ここにサインしてやー。\n　いつもの感じでな」" id story6_352e9c46
    nvl clear
    play sound "sfx/Footsteps On Concrete 1.ogg"
    story "\n\n「アジア人の君はしらんかもしれんけど、\n　ヨーロッパの国によっては\n　誕生日ネームゆうのがあってなー。\n　３６５日分の名前があんねんで。\n\n　君、誕生日いつやの？\n　ヨーロッパ風に名前つけたるよぉ」" id story6_c4c738ae
    nvl clear
    play sound1 "sfx/Footsteps On Concrete 2.ogg"
    story "\n\n\n「家族は何人おるのー？\n　嫁おるん？何歳何歳？」" id story6_77595613
    nvl clear
    story "最初ワンさん、この警官に\nめっちゃイラついとったんやけど\nだんだん\n\n{color=#FFEBD6}「この人、自分の緊張といてくれるために\n　わざとのんびり話してるんちゃうかなー？」{/color}" id story6_62a950ed
    story "なんて感じるようになったらしん。\nそいつのことを信用しはじめとった。" id story6_ea7e0697
    nvl clear

    scene bg casual
    show nvl_textbox
    story "しばらくしてワンさんの国の国旗が\nでかでかと飾ってある建物についたん。\n警察官は大使館やいうんやけど…。" id story6_761939fb
    story "大使館…にしてはカジュアルすぎんとちゃう？\n普通警備員とかおるんとちゃうの？" id story6_ae91938a
    nvl clear

    scene bg officer
    show nvl_textbox 
    story "「ほな、パスポートとクレジットカードで\n　身元証明するさかい、ちょっと貸したってね」" id story6_50c30390
    
    story "せやけど早よ助け求めたいワンさんは\n言われるまま渡してもうたん。{nw}" id story6_1a357a72
    stop music fadeout 3
    play sound "sfx/paper.ogg"
    extend ""
    nvl clear

    scene bg casual
    show nvl_textbox
    
    play sound1 "sfx/run_wait.ogg"
    story "\n\nパスポートとクレジットカード受け取った\n警官は素敵な笑顔で大使館？に消えていったそやで…。" id story6_1bc5adcb
    nvl clear


    play music "music/Fall_In_Love.ogg"
    show spain large concern at pos_transform(xpos=350, ypos=-40) behind nvl_textbox
    story "　\n　\n　\nそれから二度と、\n警官は、戻ってこんかった…。" id story6_125083fb
    show bg classroom1 behind spain
    show spain large oops
    with {'master': Dissolve(0.2)}
    story "そいつニセ警官やったんな…。" id story6_42d10041
    nvl clear

    show spain large angry
    story "\nしかも何気ない会話で\n個人情報聞き出しとったんや…。\n恐ろしい男やで…！" id story6_68ac2194
    nvl clear

    show spain large whatintarnation
    story "そもそもそこ大使館やあらへんかってん！！\nその観光客の国の国旗掲げてるだけの\nただのレストランやってん…。\n別の入口からそそくさと逃げたらしいで…。" id story6_03ddfe38
    
    show spain large sweat
    with {'master': Dissolve(0.2)}
    story "英語だったらなんとなくわかるやん？\nせやけどスペイン語ってアジアの人には\nなじみ薄いやん…。\nせやから分からんかったんやな…。" id story6_e0469c28
    nvl clear
    
    show spain large fufufu
    story "ほんま旅行する時は、\n簡単な単語でええから重要なものは\nあらかじめ暗記しておくとええかもな～。\n俺も注意して回ってんで！" id story6_52696de2
    nvl clear
    
    show bg classroom5 behind spain
    show spain large normal
    story "\nワンさんどないなったのって？\nああ。今の話後なー。\n俺のとこ直で文句言いにきはったんやで！\nそれで聞いたのが今のお話やで！" id story6_0cc5279f
    show spain large worried
    with {'master': Dissolve(0.2)}
    story "パスポートは再発行に\nめちゃくちゃ時間かかってまうさかい\nワンさんの不幸はもうちょっと続くんやで…。" id story6_24e648b9
    nvl clear

    show spain large smiling
    story "\nもう二度と来てくれんと思たけど\nワンさん暇見つけては\nちょくちょく遊びに来てくれはるん。\nごっつうれしーわぁ。" id story6_c1eab80a
    show spain large fufufu bashful
    with {'master': Dissolve(0.2)}
    story "俺の魅力に乾杯…やんな！" id story6_f6aed5a5
    nvl clear
    
    show spain large worried
    story "\n俺も規制とか見回りとかしてねんけど、\nほんま！ほんまに奴ら\n連携取れすぎやっちゅーねん！" id story6_c5ca20fe
    show spain large oops
    with {'master': Dissolve(0.2)}
    story "俺が回るとさーっといななってぇ！\n俺が別んとこいくとすすーっと\n戻ってきよる！どないなってんねん！" id story6_b51b2cfb
    nvl clear

    show spain large blush areyoukidding
    story "幽霊か！奴ら幽霊ちゃうん！？\n行動先読みしすぎやろぉ…。\nううっ…、俺の経済、\n観光のしめる割合でかいんやでぇ…。\nせやからこんな事あったらあかんやん…！" id story6_8087b875
    show spain large wahaha
    with {'master': Dissolve(0.2)}
    story "ほんなら、俺の話は終わりやで！\n何かええ対策あったら教えたってなー！" id story6_04f17cd8
    nvl clear

    scene bg classroom3
    play music "music/19_playful.ogg" fadeout 1

    show bulgaria hmmm at pos_transform(xpos=530, yoffset=1.0)
    $ bul.screen='right_3'
    bul "そういや\n誰の家だったか\n忘れたんすけど…。" id story6_44173c7d

    show bulgaria conniving
    $ bul.screen='right_3'
    bul "女の人が胸べローンって出して\nあっけに取られてる観光客から\nスリを働くって手口が\nあるらしいんだわー。" id story6_a5138f04

    show spain wahaha at pos_transform(xpos=200, yoffset=1.0) behind bulgaria
    $ spa.screen = 'center_3'
    spa "ほんまに！？\n美人な子やったら\nええやんなぁ！{nw}" id story6_f9d9ea8c

    play sound "sfx/ding27.ogg"
    $ window_transform = shake_6s1
    $ _skip_appear_effect = True
    extend ""
    $ _skip_appear_effect = False
    $ window_transform = None
    stop sound

    show england scream at pos_transform(xpos=60, yoffset=1.0)
    $ eng.screen = 'left_3'
    eng "ええやんなじゃ\nねーだろ！！{nw}" id story6_ecd792a2

    play sound "sfx/hit_s04.ogg"
    $ window_transform = shake_6s2
    $ _skip_appear_effect = True
    extend ""
    $ _skip_appear_effect = False
    $ window_transform = None
    stop sound
    
    scene bg classroom2

    $ jpn.screen = 'left_4'
    jpn "おほん。\n…まだ７人目は\nいらっしゃらないようですね。" id story6_e4df78e9

    $ eng.screen = 'center_3long'
    eng "そうだな。\nスペインより遅いなんて\n忘れてんじゃねぇのか？" id story6_03eb83da

    $ ger.screen = 'right_3'
    ger "それでは六怪談に\nなってしまうな…。\nどうにも収まりが悪い…。" id story6_b5b64313

    $ fin.screen = 'center_3'
    fin "じゃあ僕がもう一話\n話しましょうか！？" id story6_f6d57b06

    $ spa.screen = 'right_4'
    spa "あっ\n聞きたい聞きたい！\n俺ふわふわした話\n聞いてないねん。" id story6_643300bf

    $ fin.screen = 'center_3'
    fin "つ…次こそ\nふわふわしてない話を\nさせてもらいますよ！" id story6_01fff8b4

    stop music fadeout 3

    jump story7