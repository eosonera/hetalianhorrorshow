

label story6:
    stop music
    scene bg exterior5
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第六話　スペインの怖い話{/size}"
    show white screen onlayer bottom

    scene bg classroom1
    play music "music/Fall_In_Love.ogg"
    pause 0.2
    show spain large ahaha at pos_transform(xpos=350, ypos=-40)
    show nvl_textbox
    with Dissolve(0.25)
    story "ほんま、遅れてごめんなぁ。\nなんや俺日向ぼっこしすぎて\n頭から草生えそうな勢いやー。"
    nvl clear

    show spain large sup
    story "ほな、怖い話やんなぁ。\n俺の怖い話は日常に\n食い込んでくるタイプやで～。\n早速話させてもらうでー。"
    nvl clear
    
    show spain large smiling
    story "\nこれはアジアからの観光客が体験した話。\n…仮にワンさんとでもしとこか。\nなんや俺アジア人ゆーと\nワンさんってイメージやねん。\nイタちゃんの映画のせいやんな。"
    show spain large normal
    with {'master': Dissolve(0.2)}
    story "ある夏。ワンさんっちゅー方が\n俺の家に一人旅に来てはったん。"
    nvl clear
    
    story "初めて見るものの数々にワンさんは\n心躍らせとった…。"
    show spain large wahaha
    with {'master': Dissolve(0.2)}
    story "俺の家今めっちゃ\n観光に力入れとるさかい、\nみんな来たってな～。\nほんま最高のバケーション？\nっちゅーやつを体験させたるよ～。"
    
    show spain large fufufu
    with {'master': Dissolve(0.2)}
    play sound "sfx/HAUNTED HOUSE MOAN 4.ogg"
    story "{color=#6F7686}{outlinecolor=#262F3E}{cps=8}…気ぃ抜かんかったらな…。{/color}{/outlinecolor}{/cps}"
    nvl clear

    show spain large concern
    show black:
        alpha 0.0
        pause 1.5
        linear 0.5 alpha 1.0
    show nvl_textbox
    story "\n\nワンさんは俺の家初めて\nやったから知らんかったんや…。\n　\nワンさんを狙とる黒ーい影が\nぎょうさんおるっちゅー事を…。"
    nvl clear

    play music "sfx/New York traffic from a rooftop upper east side.ogg" fadeout 3 fadein 3
    story "\nほんでワンさんが有名観光地を\n散策していた時の話や…。"
    hide spain
    hide black

    show bg postcard behind nvl_textbox
    play sound "sfx/footsteps_stop.ogg"
    story "\n「絵葉書！絵葉書こうて！！」"
    story "と下から声がしたん、\nそこに１０歳くらいの男の子がおってな。\n絵葉書こうて～って叫んでるん。"
    nvl clear
    
    story "まあ可愛らしい！そう思ったワンさんは\n絵葉書を買ったろう思たんやって。"
    story "「いくら？」"
    story "「８ユーロ」"

    show spain large whatintarnation at pos_transform(xpos=350, ypos=-40) behind nvl_textbox
    with {'master': Dissolve(0.2)}
    play music "music/FilmEdge2_Casual_Z234-DayTripping-Kelly.ogg" fadeout 1
    story "{size=+12}【高｜たっか】っ！{/size}"
    nvl clear

    show bg classroom1 behind spain
    show spain large sweat
    story "絵葉書１枚８ユーロて！\n俺の一日の昼飯代やで…！"
    show spain large blush areyoukidding
    with {'master': Dissolve(0.2)}
    story "\nえ…安すぎんとちゃうかって？\nほんまに！？、普通これくらいちゃうん！？\n俺、特別安い方なんかな…。\nそうなん…。"
    show spain large ahaha
    with {'master': Dissolve(0.2)}    
    story "今度上司に直談判してみるわ…。"
    nvl clear
    stop music fadeout 3

    scene bg postcard2
    show nvl_textbox
    story "あ、ほんで、ワンさんも８ユーロは\n高い思うたらしいんやけど、\n可愛い子供が一生懸命はがき売っとる姿に\n応援したなったらしくてな。"
    story "高い思うても言い値で\n買うたることにしたらしいで。\nワンさん金持ちやんな。"
    nvl clear
    story "ワンさんが財布開いた\nその時やった…！"
    show bg white behind nvl_textbox
    with flash
    play sound "sfx/wood_hit_wood_1.ogg"
    play sound1 "sfx/coin01.ogg"
    play music "sfx/Subway station-New York-6 line-51st street-voices-some pa.ogg"
    queue sound1 "sfx/run_wait.ogg"
    show bg white:
        pause 1.5
        "bg runaway" with Dissolve (0.2)
    story "ガキがジャンプしたか思うと\nワンさんの財布に入っとった\n１００ユーロ札ばっかわっしと掴むと\n猛ダッシュしよった！"
    nvl clear

    stop music fadeout 2
    stop sound1 fadeout 1
    scene bg alley
    show nvl_textbox
    with Dissolve(0.2)
    story "ワンさんも追わはったけど\nガキめっちゃすばしっこい！\nががーっちゅー感じで急カーブしよって\nわーっと細い路地に逃げ込みよった！"
    
    
    show spain large cry mouthopen blush at pos_transform(xpos=350, ypos=-40) behind nvl_textbox
    show bg classroom1 behind spain
    story "ワンさんは俺の家のお客様やで！\n貴重なお客様になにしとんの…！！"
    nvl clear

    show spain large concern
    story "…悪ガキもなんとかせんとなぁ…。\n普通に暮らせるくらいなら\n社会保障とかいろいろやっとるさかい\n盗みとかせえへんくてもええのに…。\nその辺、地方役所なにやっとんのかな。\n俺も反省せんとやなぁ。"
    show spain large fufufu bashful
    with {'master': Dissolve(0.2)}
    story "それとも普通に働くの\n馬鹿らしなるくらい稼ぎええんかな…。\n俺よりええ昼飯食ーてたりしてな。"
    nvl clear
    
    show spain large oh
    story "あっ、ごめんなぁ。\n話戻すで！"
    hide spain


    show bg alley behind nvl_textbox
    play music "music/unease.ogg"
    story "ワンさんがいかんかったんは、\nあの物売りを追いかけて\n人通りない路地に入ってもうた事…。"
    story "もうあの物売りはいななってて、\n路地にはワンさんしかおらんかった…。\n意気消沈してもうたワンさんは\n立ち尽くすことしかでけへんかった…。"
    nvl clear
    
    scene bg ripples1 with fade_red
    show ripples vfx
    show nvl_textbox
    play sound "sfx/bang08.ogg"
    story "\nほんならいきなり\nワンさん呼吸ができんくなった！"
    story "なんや！何が起こっとるん！！？"
    hide ripples vfx
    show bg strangle behind nvl_textbox
    story "これは…"
    camera at sshake
    camera screens at sshake
    play sound "sfx/hit43_a.ogg"
    extend "\n最近はやりの首絞め強盗や！"
    nvl clear
    camera
    camera screens
    
    story "その名の通り\n首を絞めとる間にバッグを奪うっちゅー\n獲物がおるから、首絞めるくらいの\n野生返りも甚だしい手口やで！"
    stop music fadeout 1
    
    story "サバンナの方が住みやすいんとちゃうかなぁ…。"

    play sound "sfx/run_wait.ogg"
    play music "music/03_spidersandflies.ogg"
    show bg alley behind nvl_textbox
    story "ワンさんもいきなり首絞められたわけやろ\n対処しきれんくてな…。\nそのままバッグまで奪われてしもたん…。"
    nvl clear

    scene bg luggage
    show nvl_textbox    
    story "ほな、このままうかうかしとったら\nいつ第二第三の首絞めに\nエンカウントするかわからん！\n警察や！思うたワンさんは\n走って警察を探すことにしたんやって。"
    nvl clear
    
    scene bg pedestrian
    show nvl_textbox     
    story "人通りの多いとこまで戻らはったら\nちょうどええ所に警察官がひとり\nぶらぶらしとってな。"
    story "これ幸いや思うて\nその警察官に助けを求めはったん。"
    nvl clear

    scene bg officer
    show nvl_textbox  
    story "「ふーん。え。\n　でパスポートはあるー？」"
    story "こっちは緊急事態やで！\nなんやねんその気の抜けた応対は！"
    story "お、俺かてもうちょっと急ぐで！"
    nvl clear

    story "「ほんで、今日どないすんの？\n　金ないんならホテル泊まれへんやろ。\n　大使館いって帰りーや。ほな！」"
    story "もー警官まったく話聞く気なしや。"
    nvl clear

    scene bg pedestrian2
    show nvl_textbox      
    story "ワンさんは手元の翻訳機で\n\n「パスポートもあるし、\n　幸いクレジットカードは取られてないから\n　ホテルくらいは何とかなる。\n　だけど、あのバッグには大事なものが\n　入っていてどうしても取り返したい」\n　\nって伝えたん。"
    nvl clear
    
    scene bg officer
    show nvl_textbox  
    story "「ほんなら付き合ったるわー」"
    story "今まで「お前ウザいなぁあっち行ったれや」って\nオーラ出しとったんが一変して、\n急に話聞くモードになったらしいん。"
    nvl clear
    stop music fadeout 3
    
    story "そらワンさんも必死やったし、\n本気出してもらわんと困るやんなぁ。"
    play sound "sfx/Footsteps On Concrete 1.ogg"
    story "せやけど、その警官ときたら、\nだらだら歩きながら、状況を聞くわけでもなく、\n犯人探すわけでもなく無駄口ばっかり叩きよる。"
    nvl clear

    story "短時間に二回も被害にあってねんで！\nもっと緊迫感もてや！なんて思うたんかしらんけど\nワンさんはちょいイラついた声で急かしたん。"
    
    show bg road behind nvl_textbox
    play sound "sfx/Footsteps On Concrete 1.ogg"
    play sound1 "sfx/Footsteps On Concrete 2.ogg"
    story "「ごめんなぁ。こういうヤツは組織的やねん。\n　痕跡消すのも、隠れ場もめっちゃ巧妙でな。\n　せやから組織ごと潰さんと解決せぇへんのよ。\n　俺らが組織つぶした時にバックや財布\n　出てくるかもしれへんから被害届出そ」\n\nなんて言ってきたんやって。"
    nvl clear
    story "\nスペインてそんなもんなんやな～\n国が違うから警察もちゃうんやな～なんて\n別に変に思わんかったらしい…。"
    nvl clear

    scene bg walking
    show nvl_textbox
    play sound "sfx/footsteps.ogg"
    play music "music/lullaby_beat_julio_kladniew.ogg"
    story "\n「これから君の国の大使館いこかー。\n　ここから歩いてすぐやでー。\n　被害届出すさかい、ここにサインしてやー。\n　いつもの感じでな」"
    nvl clear
    play sound "sfx/Footsteps On Concrete 1.ogg"
    story "\n\n「アジア人の君はしらんかもしれんけど、\n　ヨーロッパの国によっては\n　誕生日ネームゆうのがあってなー。\n　３６５日分の名前があんねんで。\n\n　君、誕生日いつやの？\n　ヨーロッパ風に名前つけたるよぉ」"
    nvl clear
    play sound1 "sfx/Footsteps On Concrete 2.ogg"
    story "\n\n\n「家族は何人おるのー？\n　嫁おるん？何歳何歳？」"
    nvl clear
    story "最初ワンさん、この警官に\nめっちゃイラついとったんやけど\nだんだん\n\n「この人、自分の緊張といてくれるために\n　わざとのんびり話してるんちゃうかなー？」"
    story "なんて感じるようになったらしん。\nそいつのことを信用しはじめとった。"
    nvl clear

    scene bg casual
    show nvl_textbox
    story "しばらくしてワンさんの国の国旗が\nでかでかと飾ってある建物についたん。\n警察官は大使館やいうんやけど…。"
    story "大使館…にしてはカジュアルすぎんとちゃう？\n普通警備員とかおるんとちゃうの？"
    nvl clear

    scene bg officer
    show nvl_textbox 
    story "「ほな、パスポートとクレジットカードで\n　身元証明するさかい、ちょっと貸したってね」"
    play sound ["<silence 1>","sfx/paper.ogg"]
    story "せやけど早よ助け求めたいワンさんは\n言われるまま渡してもうたん。"
    nvl clear

    stop music fadeout 3

    scene bg casual
    show nvl_textbox
    
    play sound1 "sfx/run_wait.ogg"
    story "\n\nパスポートとクレジットカード受け取った\n警官は素敵な笑顔で大使館？に消えていったそやで…。"
    nvl clear


    play music "music/Fall_In_Love.ogg"
    show spain large concern at pos_transform(xpos=350, ypos=-40) behind nvl_textbox
    story "　\n　\n　\nそれから二度と、\n警官は、戻ってこんかった…。"
    show bg classroom1 behind spain
    show spain large oops
    with {'master': Dissolve(0.2)}
    story "そいつニセ警官やったんな…。"
    nvl clear

    show spain large angry
    story "\nしかも何気ない会話で\n個人情報聞き出しとったんや…。\n恐ろしい男やで…！"
    nvl clear

    show spain large whatintarnation
    story "そもそもそこ大使館やあらへんかってん！！\nその観光客の国の国旗掲げてるだけの\nただのレストランやってん…。\n別の入口からそそくさと逃げたらしいで…。"
    
    show spain large sweat
    with {'master': Dissolve(0.2)}
    story "英語だったらなんとなくわかるやん？\nせやけどスペイン語ってアジアの人には\nなじみ薄いやん…。\nせやから分からんかったんやな…。"
    nvl clear
    
    show spain large fufufu
    story "ほんま旅行する時は、\n簡単な単語でええから重要なものは\nあらかじめ暗記しておくとええかもな～。\n俺も注意して回ってんで！"
    nvl clear
    
    show bg classroom5 behind spain
    show spain large normal
    story "\nワンさんどないなったのって？\nああ。今の話後なー。\n俺のとこ直で文句言いにきはったんやで！\nそれで聞いたのが今のお話やで！"
    show spain large worried
    with {'master': Dissolve(0.2)}
    story "パスポートは再発行に\nめちゃくちゃ時間かかってまうさかい\nワンさんの不幸はもうちょっと続くんやで…。"
    nvl clear

    show spain large smiling
    story "\nもう二度と来てくれんと思たけど\nワンさん暇見つけては\nちょくちょく遊びに来てくれはるん。\nごっつうれしーわぁ。"
    show spain large fufufu bashful
    with {'master': Dissolve(0.2)}
    story "俺の魅力に乾杯…やんな！"
    nvl clear
    
    show spain large worried
    story "\n俺も規制とか見回りとかしてねんけど、\nほんま！ほんまに奴ら\n連携取れすぎやっちゅーねん！"
    show spain large oops
    with {'master': Dissolve(0.2)}
    story "俺が回るとさーっといななってぇ！\n俺が別んとこいくとすすーっと\n戻ってきよる！どないなってんねん！"
    nvl clear

    show spain large blush areyoukidding
    story "幽霊か！奴ら幽霊ちゃうん！？\n行動先読みしすぎやろぉ…。\nううっ…、俺の経済、\n観光のしめる割合でかいんやでぇ…。\nせやからこんな事あったらあかんやん…！"
    show spain large wahaha
    with {'master': Dissolve(0.2)}
    story "ほんなら、俺の話は終わりやで！\n何かええ対策あったら教えたってなー！"
    nvl clear

    scene bg classroom3
    play music "music/19_playful.ogg" fadeout 1

    show bulgaria hmmm at pos_transform(xpos=530, yoffset=1.0)
    $ bul.screen='right_3'
    bul "そういや\n誰の家だったか\n忘れたんすけど…。"

    show bulgaria conniving
    $ bul.screen='right_3'
    bul "女の人が胸べローンって出して\nあっけに取られてる観光客から\nスリを働くって手口が\nあるらしいんだわー。"

    show spain wahaha at pos_transform(xpos=200, yoffset=1.0) behind bulgaria
    $ spa.screen = 'center_3'
    play sound ["<silence .5>", "sfx/ding27.ogg"]
    $ window_transform = shake_6s1
    spa "ほんまに！？\n美人な子やったら\nええやんなぁ！"
    $ window_transform = None
    stop sound

    show england scream at pos_transform(xpos=60, yoffset=1.0)
    $ eng.screen = 'left_3'
    play sound ["<silence .5>", "sfx/hit_s04.ogg"]
    $ window_transform = shake_6s2
    eng "ええやんなじゃ\nねーだろ！！"
    $ window_transform = None
    stop sound
    
    scene bg classroom2

    $ jpn.screen = 'left_4'
    jpn "おほん。\n…まだ７人目は\nいらっしゃらないようですね。"

    $ eng.screen = 'center_3long'
    eng "そうだな。\nスペインより遅いなんて\n忘れてんじゃねぇのか？"

    $ ger.screen = 'right_3'
    ger "それでは六怪談に\nなってしまうな…。\nどうにも収まりが悪い…。"

    $ fin.screen = 'center_3'
    fin "じゃあ僕がもう一話\n話しましょうか！？"

    $ spa.screen = 'right_4'
    spa "あっ\n聞きたい聞きたい！\n俺ふわふわした話\n聞いてないねん。"

    $ fin.screen = 'center_3'
    fin "つ…次こそ\nふわふわしてない話を\nさせてもらいますよ！"

    stop music fadeout 3

    jump story7