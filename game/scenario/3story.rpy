
label story3:
    stop music
    scene bg exterior1
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第三話　日本の怖い話。{/size}"

    scene bg classroom1

    play music "music/4_aniki2.ogg"
    pause 0.2
    show japan large normal:
        xpos 450 ypos -80
        pause 0.6
        "japan large contemplation"
        easein 0.45 yoffset +35
        easein 0.3 yoffset 0
    show nvl_textbox
    with Dissolve(0.25)
    story "三番目にお話しさせて頂きます。\n宜しくお願い致します。"

    show japan large deepthinking
    with {'master': Dissolve(0.25)}
    story "\n怖い話というよりは\n不思議な話になるのですが…。"
    nvl clear

    show japan large deepthinking
    show bg tokyo5 behind nvl_textbox
    $ audio_crossFade(0.5, "music/01_steadynightbreeze.ogg")
    story "あれはしとしとと雨の降る\n夜の事でした…。"
    hide japan
    with {'master': Dissolve(0.25)}
    

    story "用事が長引いて\n遅くなってしまった私は、\n家路を急いでおりました。"
    nvl clear

    scene bg tokyo1
    show nvl_textbox
    show black:
        alpha 0.4
    show window_rain

    story "昼間は活気にあふれた賑やかな道も\n夜になると人通りも少なく\nひっそりとしていて\nまるで別の場所のような錯覚に襲われます。"
    nvl clear

    scene bg tokyo3
    show nvl_textbox
    
    story "光源はぼんやりとした街燈と\n遠くに見える住宅の灯りしかありません。\nそれが雨の日ともなると\nさらに弱々しく淡く見えました。"
    show bg tokyo4 behind nvl_textbox
    with None

    story "下を見れば\n水たまりの中の\n街燈の光が雨に合わせて\n忙しなく揺れています。"
    nvl clear
    
    story "その日は風向きの関係で\n傘を前の方に向けて\n差すことになってしまい\n前の視界が塞がれると同時に\n足元や背後が気になってしまいます。"
    
    story "長い直線の道路なのに\n今日に限って車すら通りません。"
    nvl clear

    scene bg tokyo5
    show nvl_textbox
    with None
    story "聞こえるのは雨音だけ…。"
    show black behind nvl_textbox
    with None
    play sound "sfx/HORROR - ZOMBIES FEEDING.ogg"
    play sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    story "ぺた、ぺた、ぺた…。"

    hide black
    show bg tokyo5 behind nvl_textbox
    with None

    story "…雨音だけ、ではない…？"

    story "雨音の合間に自分のものではない\n足音が混じっていました。"
    nvl clear

    scene bg legs2
    show nvl_textbox
    play sound ["<silence .3>","sfx/HORROR - ZOMBIES FEEDING.ogg"]
    play sound1 ["<silence .3>","sfx/OOZE2.WAV"]
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    story "\nぺた、ぺた、ぺた…。"
    story "私の靴の音が\n反響しているのかと思いましたが、\n確かに水を吸った履物の音が\n背後から聞こえてきます。"
    nvl clear
    
    story "ぺた、ぺたという\n濡れた地面から足が離れる時の音と\nその足が地面について靴の中の水が\n押し出されるぐじゅっ、ぐじゅっという\n不気味な音が静かな路地に交互に響きます。"
    nvl clear
    
    scene bg tokyo2
    show nvl_textbox
    with None
    story "途中道を２度ほど曲がりましたが、\n足音は同じ距離、同じ間隔で聞こえてくる…。\n　\n…つけてきているわけではないと\n思いたいのですが、如何せん不気味です。"
    nvl clear
    
    scene bg legs2
    play sound "sfx/HORROR - ZOMBIES FEEDING.ogg"
    play sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    story "\nぺた、ぺた、ぺた…。"
    show nvl_textbox
    show bg tokyo2 behind nvl_textbox
    with None

    story "何故だか、その音を聞いていると\n背筋にぞくぞくと冷たいものが走ります。\nこんな夜だからでしょうか。"
    nvl clear

    scene black
    show nvl_textbox

    story "何とも言えない息苦しさを感じ\nあまりじろじろ見ては失礼なので\n傘の影からちらりと後ろを見ました。"
    nvl clear
    
    scene bg legs
    show nvl_textbox
    #show black behind nvl_textbox
    with flash
    story "　\n　\n　\n　\n傘の隙間から見えたのは、\nぐっしょりと濡れた着物の裾と\n泥で変色した足袋と草履…。"
    nvl clear

    show black behind nvl_textbox
    show window_rain
    story "\n祭りがある日ではありませんし、\nそのあたりには和装で行う\n習い事教室はなかったはずです。\n　\n男性の和装は珍しいですしね。\nそれに雨に打たれたというよりは\n水の中に落ちたような濡れ方…。\n如何なされたのでしょうか…。"
    nvl clear
    
    scene bg tokyo2
    show nvl_textbox
    with flash
    story "私は、心の中に芽生えた\n小さな恐怖感から逃れるため\n頭の中を考え事でいっぱいにしている間も\nその音は私と同じ速度で、\n五メートルほどの間隔を保ちながら\nついてきます。"
    
    show bg legs2 behind nvl_textbox
    with {'master': None}
    play sound "sfx/HORROR - ZOMBIES FEEDING.ogg"
    play sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    story "\nぺた、ぺた、ぺた…。{nw=3.0}"
    show black behind nvl_textbox
    with {'master': None}
    story "ぺた、ぺた…。"
    nvl clear
    
    
    story "…背後の不気味な音だけ聞いていると\n恐ろしい妄想だけが、\n際限なく膨らんでしまいます。"
    hide black
    show bg tokyo2 behind nvl_textbox
    with {'master': None}
    extend "\n\nかくなる上は、道路を渡る際に\nしっかり相手の方を\n確認させて頂きましょう！\n想像だけで怖がっていては失礼です！\nええ！"
    nvl clear

    story "そこで私は傘をいつもよりも上の方に構え、\n道路を渡るため、９０度回れ右をし\n前後確認をしました。"
    nvl clear
    
    story "まずは前。…もう少し前。\nそして気を引き締めて後ろ…。"
    
    show black behind nvl_textbox

    story "そこで初めて音の発信元である\n「後ろの男性」の全体を見たのです。\nその彼は…"
    nvl clear

    play music "music/legend.ogg"
    ### Japan rain scene
    scene bg rainjapan
    show nvl_textbox
    with flash
    story "{cps=5}\n\n\n\n\n\n私だったのです。{/cps}"
    nvl clear
    story "最初、鏡でもあるのかと思いましたが、\n彼は傘もささず、全身ずぶ濡れの和装で、\n大量の水分を吸った布地が、\n背後の街燈の光を鈍く反射させています。"
    
    show black behind nvl_textbox:
        alpha 0.0
        pause 1.0
        linear 0.5 alpha 1.0
    with {'master': Dissolve(0.25)}
    story "当日私は傘を差しておりましたし、\nなにより洋装でしたから…。"
    story "鏡と見まがうほど\n私と瓜二つの方でした。"
    nvl clear
    
    scene bg tokyo2

    story "…こういう時は\nどうすべきなのでしょうか。\n皆さんならどうされますか？"
    nvl clear

    scene bg legs2
    
    
    story "私ときたら情けないことに\nこの摩訶不思議な存在に\nすっかり気が動転してしまい\n鞄の中の折り畳み傘を取り出すと\n\n「よろしかったら使って下さい」{nw=4.0}"
    stop music fadeout 1.0
    
    show bg tokyo4
    
    story "\nと彼に渡すやいなや\n脇目も振らずに駆けだしたのです。"
    stop music1 fadeout 1.0
    nvl clear



    scene bg japanhouse
    story "家に帰ってみると\nよほど動転していたのか\n傘をさしていたというのに\n私もずぶ濡れになっておりました。"
    story "はぁ…。\n私にそっくりで、和服を着ていて\n傘を差さずにずぶ濡れで\n背後を等間隔で歩いているだけの方に\n何を恐れる必要があったのか…。"
    nvl clear
    
    
    story "それにすでに彼は\n服のまま海に入ったが如く\n全身濡れておりましたので\n私が手渡した傘が\nお役に立てないばかりか\nお荷物になってしまっていたら\n申し訳なく思います。"
    nvl clear
    
    show black
    story "その晩、布団に潜り込んだものの\n先ほどの私によく似た方が\n気になってしまい\nなかなか寝付けません。"

    show window_rain
    with {'master': Dissolve(0.25)}
    
    story "眠れないのは仕方ありませんから、\n私は布団の中で彼について\n考えてみることにしました。"
    nvl clear
    story "たまたま似ているだけなのか。\nはたまたドッペルゲンガーか…。"
    story "\n結果。朝の五時まで眠れず\n酷い目にあいました…。\n考えすぎるのもよくありません…。"
    nvl clear

    scene bg classroom_window
    show nvl_textbox
    play music "music/4_aniki2.ogg"
    show japan large contemplation:
        xpos 450 ypos -80
        pause 1.2
        "japan large normal" with Dissolve(0.2)
    story "それで彼について考えうる可能性を\n私なりに五つにまとめてみたのですが…。\n\n\nまず一つ目。\n私に非常によく似た普通の方。"
    show japan large deepthinking with {'master': Dissolve(0.25)}
    story "これが一番可能性としては\n高いと思うのですが…。"
    nvl clear
    
    show japan large hmm
    with {'master': Dissolve(0.2)}
    story "もしそうだとすると、\n傘もささず、雨宿りをするでもなく、\n折角の着物を濡らしながら\n私につかず離れず歩いていたのは\n何故なのか気になる所です…。"
    story "それはそれで恐怖を感じます…。"
    nvl clear

    show japan large normal
    with {'master': Dissolve(0.2)}  
    story "そして二つ目の可能性。\n西洋でいうドッペルゲンガーです。"
    story "西洋ではドッペルゲンガーのような\n「もう一人の自分」は死や不幸といった\n不浄や不吉なものとして\n扱われる事が多いようですね。"
    nvl clear

    show japan large laugh
    with {'master': Dissolve(0.2)}      
    story "しかし私の家の地方によっては\n姿を借りて現れた神様であったり、\n吉兆の知らせであったりするため、\n摩訶不思議ではあるものの、\n怖い物ではありませんね。"
    nvl clear

    show japan large deepthinking
    with {'master': Dissolve(0.2)}    
    story "それから三つ目。\n…少々ＳＦ的な要素が\n入るのですが…。"
    show japan large angry
    with {'master': Dissolve(0.2)} 
    play sound ["<silence .2>", "sfx/hit71.ogg"]
    show nvl_textbox at shake_2s7
    camera screens at shake_2s6
    story "私は、何人もいる…！"
    nvl clear

    show japan large normal
    with {'master': Dissolve(0.2)} 
    story "考えられる理由としては、\n私という存在に何かあった時や、\n大幅に変わるやもしれない\n事態になった時の換えの品。\nいわゆるストックです…。"
    show japan large contemplation
    with {'master': Dissolve(0.2)} 
    story "私たちが知らないだけで、\nもしかしたら私や皆さんにも\n「換え」がいるのかもしれません…。"
    nvl clear
    
    show japan large normal
    with {'master': Dissolve(0.2)} 
    story "四つ目。\n　\n　\nブータンさんがプライベートで\n私の家に観光で遊びにいらしていた。"
    nvl clear
    story "ブータンさんが最近流行りの\n貸し着物で観光を楽しんでいた所、\n急に雨が降ってきたが、\nどこに傘が売っているのか分からず、\n聞くに聞けず、私についてきた…説です。"
    nvl clear
    
    show japan:
        pause 0.8
        "japan large distant-look sweat" with Dissolve(0.2)
    story "私とブータンさんは皆さんからも\nよく似ていると言われます。\n\n暗い夜道で雨も降っていたら、\n私自身が私と認識してしまう事も\nあるかもしれません。"
    story "それにとてもシャイな方ですから\n話しかけられなかった可能性はありますよね。"
    nvl clear
    
    show japan large normal
    with {'master': Dissolve(0.2)}     
    story "後で直接お話を伺ってみたのですが、\n　\n{color=#D8D7BE}「私ではないが、もし私だとしても\n　気にしないでください」{/color}"
    show japan large worried
    with {'master': Dissolve(0.2)}  
    story "というお答えを頂きました。\nどちらなのでしょうか…。"
    extend "\nもしあれがブータンさんでしたら\n非常に可哀想な事をしてしまいました…。"
    nvl clear
    show japan large cocky eyesclosed
    with {'master': Dissolve(0.2)}
    story "そして最後の一つ。\n私としてはこれだけは\n考えたくなかったのですが…"
    stop music fadeout 4
    
    show japan large blush sweat embarassed with {'master': Dissolve(0.2)}
    story "如何しても{nw=1}"
    show japan large blush sweat embarassed sideglance with {'master': Dissolve(0.2)}
    extend "\n頭から離れない{nw=1}"
    show japan large blush sweat pleasestop with {'master': Dissolve(0.2)}
    extend "\n五つ目の可能性…。"
    camera screens at shake_2s8
    show japan large blush yell with {'master': Dissolve(0.2)}:
        pause 1.2
        "japan large closedmouth sweat" with Dissolve(0.2)
    story "{size=+12}{cps=5}……【老｜お】い。{/cps}{/size}"
    nvl clear
    camera screens

    scene bg classroom4
    play music "music/joking.ogg"
    show england blush shout3 at pos_transform(xpos=60, yoffset=1.0)
    show england blush shout3 at sshake with {'master': Dissolve(0.2)}:
        xpos 60 yoffset 1.0
        block:
            linear 0.07 xoffset -12
            linear 0.07 xoffset 0
            repeat 5

    $ eng.screen='left_3'
    play sound ["<silence .1>", "sfx/hit74_c.ogg"]
    $ window_transform = sshake
    eng "{size=+5}ぐああぁっ！！{/size}"
    $ window_transform = None

    show america whatyousay at pos_transform(xpos=200, yoffset=1.0) behind england
    play sound ["<silence 1>", "sfx/ding48.ogg"]
    $ ame.screen='center_3'
    $ window_transform = shake_3s2
    ame "{size=+2}えっ！！\n君もしかして何か\n自覚症状があるのかい！？{/size}"
    $ window_transform = None

    show japan distant-look sweat at pos_transform(xpos=600, yoffset=1.0)
    $ jpn.screen='right_4long'
    jpn "それが昔は遠くの山まで\nハッキリ見えたものですが、\n山を見る機会自体が減ってしまい\n確認するのも怖くなってしまいました。"
    show japan sweat hm
    $ jpn.screen='right_4long'
    jpn "手前のものばかり見るのが\nいけない事とはわかりつつも…。\nくっ、不甲斐ない…。"


    scene bg classroom1
    show nvl_textbox
    show japan large blush sweat embarassed at pos_transform(xpos=450, ypos=-80)
    with Dissolve(0.25)
    story "あの日は暗く…雨も降っており、\n更に多少距離がありましたので\n\n実はしっかり見たと思ってても\n実はそれほど見てなかったのではないかという\n疑念が払拭出来ないのです…！"
    nvl clear

    show japan large blush sweat pleasestop
    with {'master': Dissolve(0.25)} 
    story "それに最近、どうにも変と言いますか。\nリモコンや新聞を変な所に置いていたり、\n縁側でだらだらと飼い犬を撫でるだけで\n休日を過ごしてしまったり\nどうにも、どうにも私自身\n鈍ってるように感じるのです…！"
    story "昔なら空いた時間があれば\n仕事に趣味に、旅行にと\n飛び回っていたというのに…！"
    nvl clear

    show japan large blush sweat ughh at shake_3s3
    with {'master': Dissolve(0.25)}
    pause 0.3
    story "それとガリ○リ君が発売当初は\n齧って食べられていたはずなのに、\n今ではなめてしか食べられない\n私がいるのに気づいた時の絶望感たるや…！"
    show japan large ah2 at pos_transform(xpos=450, ypos=-80)
    with {'master': Dissolve(0.25)} 
    story "齧るとアイスクリーム頭痛が\n直で脳に来るあの感覚が…\n今の私には耐えられないのです…っ！"
    nvl clear

    scene bg classroom4
    show japan sweat hm at pos_transform(xpos=420, yoffset=1.0)
    show england blush shout2 behind japan:
        xpos 140 yoffset 1.0
        time 0.5
        block:
            linear 0.07 xoffset -5
            linear 0.07 xoffset 5
            repeat

    
    $ eng.screen='left_4'
    eng "老いが原因ではないはずだ！\nきっと俺たちに人みたいな\n老いの症状はないはずだ…！\nああ、ないに違いない！"

    show finland worried smiling at pos_transform(xpos=-80, ypos=30) behind england
    $ fin.screen='left_3'
    fin "まるで自分に\n言い聞かせるよう\nじゃないですかぁ！"

    show bulgaria sweat worried at pos_transform(xpos=550, yoffset=1.0) behind japan
    $ bul.screen='right_3'
    bul "俺も実は結構歳いって…\n大丈夫っすよね。\nうん大丈夫なんだわー！"
    
    

    show germany squint at pos_transform(xpos=630, yoffset=1.0) behind bulgaria with Dissolve(0.2)
    show england at stop_offset with {'master':move}
    $ ger.screen='right_4'
    ger "どうも気になる話だな\n俺の方で調査してみよう\n後で詳しい場所と証言を頼む"

    show japan shocked
    $ jpn.screen='center_1'
    jpn "えっ、はい"

    scene bg classroom1
    show nvl_textbox
    stop music fadeout 2
    show japan large laugh at pos_transform(xpos=450, ypos=-80)

    story "私の話は以上です。\nご清聴ありがとうございました。\n次の方、お願いいたします。"
    nvl clear
    hide nvl_textbox
    pause 0.1


    jump story4