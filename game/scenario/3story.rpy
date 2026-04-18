
label story3:
    stop music
    scene bg exterior1
    with Dissolve(0.2)
    pause 0.2
    na "{size=+2}第三話　日本の怖い話。{/size}" id story3_1d710f02

    scene bg classroom1

    play music "music/4_aniki2.ogg"
    pause 0.2
    show japan large normal at pos_transform(xpos=450, ypos=-80)
    show nvl_textbox
    with Dissolve(0.25)

    $ _pending_sprite_transform = [("japan large contemplation", jpn_2s1, Dissolve(0.2))]
    story "三番目にお話しさせて頂きます。\n宜しくお願い致します。" id story3_1e299711


    show japan large deepthinking with {'master': Dissolve(0.2)}
    story "\n怖い話というよりは\n不思議な話になるのですが…。" id story3_6fdc4dba
    nvl clear

    show bg tokyo5 behind nvl_textbox
    pause 0.2
    show japan large cocky eyesclosed
    $ audio_crossFade(0.5, "music/01_steadynightbreeze.ogg")
    story "あれはしとしとと雨の降る\n夜の事でした…。" id story3_1beae1ae
    hide japan
    with {'master': Dissolve(0.25)}
    

    story "用事が長引いて\n遅くなってしまった私は、\n家路を急いでおりました。" id story3_d12d6e02
    nvl clear

    scene bg tokyo1
    show nvl_textbox
    show black:
        alpha 0.4
    show window_rain

    story "昼間は活気にあふれた賑やかな道も\n夜になると人通りも少なく\nひっそりとしていて\nまるで別の場所のような錯覚に襲われます。" id story3_b3c8b40e
    nvl clear

    scene bg tokyo3
    show nvl_textbox
    
    story "光源はぼんやりとした街燈と\n遠くに見える住宅の灯りしかありません。\nそれが雨の日ともなると\nさらに弱々しく淡く見えました。" id story3_47f7f7e6
    show bg tokyo4 behind nvl_textbox
    with None

    story "下を見れば\n水たまりの中の\n街燈の光が雨に合わせて\n忙しなく揺れています。" id story3_c7836389
    nvl clear
    
    story "その日は風向きの関係で\n傘を前の方に向けて\n差すことになってしまい\n前の視界が塞がれると同時に\n足元や背後が気になってしまいます。" id story3_630ea9c0
    
    story "長い直線の道路なのに\n今日に限って車すら通りません。" id story3_8813e9c1
    nvl clear

    scene bg tokyo5
    show nvl_textbox
    with None
    story "聞こえるのは雨音だけ…。" id story3_065d04be
    show black behind nvl_textbox
    with None
    play sound "sfx/HORROR - ZOMBIES FEEDING.ogg"
    play sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    story "ぺた、ぺた、ぺた…。" id story3_4f25cc56

    hide black
    show bg tokyo5 behind nvl_textbox
    with None

    story "…雨音だけ、ではない…？" id story3_41b4e617

    story "雨音の合間に自分のものではない\n足音が混じっていました。" id story3_8388265d
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
    story "\nぺた、ぺた、ぺた…。" id story3_f1fe5855
    story "私の靴の音が\n反響しているのかと思いましたが、\n確かに水を吸った履物の音が\n背後から聞こえてきます。" id story3_48f3c4c2
    nvl clear
    
    story "ぺた、ぺたという\n濡れた地面から足が離れる時の音と\nその足が地面について靴の中の水が\n押し出されるぐじゅっ、ぐじゅっという\n不気味な音が静かな路地に交互に響きます。" id story3_b77c6f42
    nvl clear
    
    scene bg tokyo2
    show nvl_textbox
    with None
    story "途中道を２度ほど曲がりましたが、\n足音は同じ距離、同じ間隔で聞こえてくる…。\n　\n…つけてきているわけではないと\n思いたいのですが、如何せん不気味です。" id story3_b7d97d1b
    nvl clear
    
    scene bg legs2
    play sound "sfx/HORROR - ZOMBIES FEEDING.ogg"
    play sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    story "\nぺた、ぺた、ぺた…。" id story3_f1fe5855_1
    show nvl_textbox
    show bg tokyo2 behind nvl_textbox
    with None

    story "何故だか、その音を聞いていると\n背筋にぞくぞくと冷たいものが走ります。\nこんな夜だからでしょうか。" id story3_74d02afc
    nvl clear

    show black behind nvl_textbox:
        alpha 0
    $ _pending_sprite_transform = [("black", unhide_s3)]
    story "何とも言えない息苦しさを感じ\nあまりじろじろ見ては失礼なので\n傘の影からちらりと後ろを見ました。" id story3_dedacf49

    nvl clear
    pause 0.2
    
    scene bg legs
    show nvl_textbox
    with flash
    show black behind nvl_textbox:
        alpha 0
    $ _pending_sprite_transform = [("black", unhide_s3)]
    story "　\n　\n　\n　\n傘の隙間から見えたのは、\nぐっしょりと濡れた着物の裾と\n泥で変色した足袋と草履…。" id story3_b573c2af
    nvl clear

    show black behind nvl_textbox
    show window_rain
    story "\n祭りがある日ではありませんし、\nそのあたりには和装で行う\n習い事教室はなかったはずです。\n　\n男性の和装は珍しいですしね。\nそれに雨に打たれたというよりは\n水の中に落ちたような濡れ方…。\n如何なされたのでしょうか…。" id story3_c082051e
    nvl clear
    hide window_rain
    pause 0.3
    
    scene bg tokyo2
    show nvl_textbox
    with flash
    show black behind nvl_textbox:
        alpha 0
    story "私は、心の中に芽生えた\n小さな恐怖感から逃れるため\n頭の中を考え事でいっぱいにしている間も\nその音は私と同じ速度で、\n五メートルほどの間隔を保ちながら\nついてきます。" id story3_e546a53b
    
    show bg legs2 behind nvl_textbox
    with {'master': None}
    play sound "sfx/HORROR - ZOMBIES FEEDING.ogg"
    play sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    queue sound1 "sfx/OOZE2.WAV"
    story "\nぺた、ぺた、ぺた…。{nw=1}" id story3_584f5ae1
    $ _pending_sprite_transform = [("black", unhide_s3)]
    story "ぺた、ぺた…。" id story3_15a168c3
    nvl clear
    
    
    story "…背後の不気味な音だけ聞いていると\n恐ろしい妄想だけが、\n際限なく膨らんでしまいます。" id story3_72360f0c
    hide black
    show bg tokyo2 behind nvl_textbox
    with {'master': None}
    extend "\n\nかくなる上は、道路を渡る際に\nしっかり相手の方を\n確認させて頂きましょう！\n想像だけで怖がっていては失礼です！\nええ！" id story3_01ea78e5
    nvl clear

    story "そこで私は傘をいつもよりも上の方に構え、\n道路を渡るため、９０度回れ右をし\n前後確認をしました。" id story3_3f703cab
    nvl clear
    
    story "まずは前。…もう少し前。\nそして気を引き締めて後ろ…。" id story3_08f2ebbe
    
    show black behind nvl_textbox with {'master': Dissolve(0.5)}
    pause 0.5

    story "そこで初めて音の発信元である\n「後ろの男性」の全体を見たのです。\nその彼は…" id story3_82cf7bd3
    nvl clear

    play music "music/legend.ogg"
    ### Japan rain scene
    scene bg rainjapan
    show nvl_textbox
    with flash
    show black behind nvl_textbox:
        alpha 0
    story "{cps=10}{color=#E6E8E5}\n\n\n\n\n\n私だったのです。{/color}{/cps}" id story3_25ee3875
    nvl clear
    story "最初、鏡でもあるのかと思いましたが、\n彼は傘もささず、全身ずぶ濡れの和装で、\n大量の水分を吸った布地が、\n背後の街燈の光を鈍く反射させています。" id story3_a43bbb4e
    $ _pending_sprite_transform = [("black", unhide_s3)]
    story "当日私は傘を差しておりましたし、\nなにより洋装でしたから…。" id story3_579c308d
    story "鏡と見まがうほど\n私と瓜二つの方でした。" id story3_da67871a
    nvl clear
    
    scene bg tokyo2

    story "…こういう時は\nどうすべきなのでしょうか。\n皆さんならどうされますか？" id story3_26ef12ea
    nvl clear

    scene bg legs2
    
    
    story "私ときたら情けないことに\nこの摩訶不思議な存在に\nすっかり気が動転してしまい\n鞄の中の折り畳み傘を取り出すと\n\n{color=#E5E5E5}「よろしかったら使って下さい」{/color}{nw=4.0}" id story3_7a854c94
    stop music fadeout 1.0
    
    show bg tokyo4 with None
    
    story "\nと彼に渡すやいなや\n脇目も振らずに駆けだしたのです。" id story3_7bc3a131
    stop music1 fadeout 1.0
    nvl clear



    scene bg japanhouse with None
    show black:
        alpha 0
    story "家に帰ってみると\nよほど動転していたのか\n傘をさしていたというのに\n私もずぶ濡れになっておりました。" id story3_4189d091
    story "はぁ…。\n私にそっくりで、和服を着ていて\n傘を差さずにずぶ濡れで\n背後を等間隔で歩いているだけの方に\n何を恐れる必要があったのか…。" id story3_f0dc5ef0
    nvl clear
    
    
    story "それにすでに彼は\n服のまま海に入ったが如く\n全身濡れておりましたので\n私が手渡した傘が\nお役に立てないばかりか\nお荷物になってしまっていたら\n申し訳なく思います。" id story3_6f8d30d8
    nvl clear
    
    $ _pending_sprite_transform = [("black", unhide_s1)]
    story "その晩、布団に潜り込んだものの\n先ほどの私によく似た方が\n気になってしまい\nなかなか寝付けません。" id story3_531f856d

    show window_rain with {'master': Dissolve(0.2)}
    
    story "眠れないのは仕方ありませんから、\n私は布団の中で彼について\n考えてみることにしました。" id story3_8d9a0842
    nvl clear
    story "たまたま似ているだけなのか。\nはたまたドッペルゲンガーか…。" id story3_eff9618d
    story "\n結果。朝の五時まで眠れず\n酷い目にあいました…。\n考えすぎるのもよくありません…。" id story3_d094b60f
    nvl clear

    scene bg classroom_window
    show nvl_textbox
    play music "music/4_aniki2.ogg"
    show japan large contemplation at pos_transform(xpos=450, ypos=-80)
    story "それで彼について考えうる可能性を\n私なりに五つにまとめてみたのですが…。{nw}" id story3_e8d51713

    show japan large normal with {'master': Dissolve(0.25)}
    extend "\n\n\nまず一つ目。\n私に非常によく似た普通の方。" id story3_1bc6e8d6

    show japan large deepthinking with {'master': Dissolve(0.25)}
    story "これが一番可能性としては\n高いと思うのですが…。" id story3_9b2160b1
    nvl clear
    
    show japan large hmm
    with {'master': Dissolve(0.2)}
    story "もしそうだとすると、\n傘もささず、雨宿りをするでもなく、\n折角の着物を濡らしながら\n私につかず離れず歩いていたのは\n何故なのか気になる所です…。" id story3_1ae36e4a
    story "それはそれで恐怖を感じます…。" id story3_b4c48df3
    nvl clear

    show japan large normal
    with {'master': Dissolve(0.2)}  
    story "そして二つ目の可能性。\n西洋でいうドッペルゲンガーです。" id story3_965b4871
    story "西洋ではドッペルゲンガーのような\n「もう一人の自分」は死や不幸といった\n不浄や不吉なものとして\n扱われる事が多いようですね。" id story3_9262e330
    nvl clear

    show japan large laugh
    with {'master': Dissolve(0.2)}      
    story "しかし私の家の地方によっては\n姿を借りて現れた神様であったり、\n吉兆の知らせであったりするため、\n摩訶不思議ではあるものの、\n怖い物ではありませんね。" id story3_c2356440
    nvl clear

    show japan large deepthinking
    with {'master': Dissolve(0.2)}    
    story "それから三つ目。\n…少々ＳＦ的な要素が\n入るのですが…。" id story3_058ce3ee

    show japan large angry with {'master': Dissolve(0.2)} 
    $ _pending_sprite_transform = [("nvl_textbox", shake_2s7)]
    $ _pending_sound = ("sfx/hit71.ogg", "sound")
    $ _pending_camera_transform = [([shake_2s6], "screens")]
    story "私は、何人もいる…！" id story3_ac56c9bd
    $ _pending_camera_transform = None

    nvl clear

    show japan large normal
    with {'master': Dissolve(0.2)} 
    
    story "考えられる理由としては、\n私という存在に何かあった時や、\n大幅に変わるやもしれない\n事態になった時の換えの品。\nいわゆるストックです…。" id story3_13397d71
    show japan large contemplation
    with {'master': Dissolve(0.2)} 
    story "私たちが知らないだけで、\nもしかしたら私や皆さんにも\n「換え」がいるのかもしれません…。" id story3_ee3186d9
    nvl clear
    
    show japan large normal with {'master': Dissolve(0.2)} 
    story "四つ目。\n　\n　\nブータンさんがプライベートで\n私の家に観光で遊びにいらしていた。" id story3_3f4606cb
    nvl clear
    story "ブータンさんが最近流行りの\n貸し着物で観光を楽しんでいた所、\n急に雨が降ってきたが、\nどこに傘が売っているのか分からず、\n聞くに聞けず、私についてきた…説です。" id story3_ff0e55f4
    nvl clear
    

    story "私とブータンさんは皆さんからも\nよく似ていると言われます。{nw}" id story3_b65cef91
    show japan large distant-look sweat with {'master': Dissolve(0.2)} 
    extend "\n\n暗い夜道で雨も降っていたら、\n私自身が私と認識してしまう事も\nあるかもしれません。" id story3_476a26e5
    story "それにとてもシャイな方ですから\n話しかけられなかった可能性はありますよね。" id story3_098cd4fb
    nvl clear
    
    show japan large normal
    with {'master': Dissolve(0.2)}     
    story "後で直接お話を伺ってみたのですが、\n　\n{color=#F4F4D2}「私ではないが、もし私だとしても\n　気にしないでください」{/color}" id story3_f996fea8
    show japan large worried
    with {'master': Dissolve(0.2)}  
    story "というお答えを頂きました。\nどちらなのでしょうか…。" id story3_18825748
    extend "\nもしあれがブータンさんでしたら\n非常に可哀想な事をしてしまいました…。" id story3_4e53adf5
    nvl clear
    show japan large cocky eyesclosed
    with {'master': Dissolve(0.2)}
    story "そして最後の一つ。\n私としてはこれだけは\n考えたくなかったのですが…" id story3_6bede216
    stop music fadeout 4
    
    show japan large blush sweat embarassed with {'master': Dissolve(0.2)}
    story "如何しても{nw=1}" id story3_3290eab9
    show japan large blush sweat embarassed sideglance with {'master': Dissolve(0.2)}
    extend "\n頭から離れない{nw=1}" id story3_0cb8fff4
    show japan large blush sweat pleasestop with {'master': Dissolve(0.2)}
    extend "\n五つ目の可能性…。" id story3_9587ddf5
    
    show japan large blush yell with {'master': Dissolve(0.2)}

    $ _pending_camera_transform = [([shake_2s8], "screens")]
    $ _pending_sprite_transform = [("japan large closedmouth sweat", pos_transform(xpos=450, ypos=-80), Dissolve(0.2))]
    story "{size=+12}{cps=5}……【老｜お】い。{/cps}{/size}" id story3_e8275d2f
    $ _pending_camera_transform = None

    nvl clear
    camera screens


    scene bg classroom4
    play music "music/joking.ogg"

    show england blush shout3 at pos_transform(xpos=60, yoffset=1.0)
    $ eng.screen='left_3'
    $ _pending_window_transform = (sshake)
    $ _pending_sprite_transform = [("england", [sshake, eng_3s1])]
    $ _pending_sound = ("sfx/hit74_c.ogg", "sound")
    eng "{size=+5}ぐああぁっ！！{/size}" id story3_458c3e33


    show america whatyousay at pos_transform(xpos=200, yoffset=1.0) behind england
    $ ame.screen='center_3'
    $ _pending_window_transform = (shake_3s2)
    $ _pending_sound = ("sfx/ding48.ogg", "sound")
    ame "{size=+2}えっ！！\n君もしかして何か\n自覚症状があるのかい！？{/size}" id story3_a7aff70d

    show japan distant-look sweat at pos_transform(xpos=600, yoffset=1.0)
    $ jpn.screen='right_4long'
    jpn "それが昔は遠くの山まで\nハッキリ見えたものですが、\n山を見る機会自体が減ってしまい\n確認するのも怖くなってしまいました。" id story3_74b6c537
    show japan sweat hm
    $ jpn.screen='right_4long'
    jpn "手前のものばかり見るのが\nいけない事とはわかりつつも…。\nくっ、不甲斐ない…。" id story3_fa383dca


    scene bg classroom1
    show nvl_textbox
    show japan large blush sweat embarassed at pos_transform(xpos=450, ypos=-80)
    with Dissolve(0.25)
    story "あの日は暗く…雨も降っており、\n更に多少距離がありましたので\n\n実はしっかり見たと思ってても\n実はそれほど見てなかったのではないかという\n疑念が払拭出来ないのです…！" id story3_30483c36
    nvl clear

    show japan large blush sweat pleasestop
    with {'master': Dissolve(0.25)} 
    story "それに最近、どうにも変と言いますか。\nリモコンや新聞を変な所に置いていたり、\n縁側でだらだらと飼い犬を撫でるだけで\n休日を過ごしてしまったり\nどうにも、どうにも私自身\n鈍ってるように感じるのです…！" id story3_41fe28b9
    story "昔なら空いた時間があれば\n仕事に趣味に、旅行にと\n飛び回っていたというのに…！" id story3_5bfee16c
    nvl clear

    show japan large blush sweat ughh with {'master': Dissolve(0.25)}
    pause 0.3
    $ _pending_sprite_transform = [("japan", shake_3s3)]
    story "それとガリ○リ君が発売当初は\n齧って食べられていたはずなのに、\n今ではなめてしか食べられない\n私がいるのに気づいた時の絶望感たるや…！" id story3_aa63bc1b
    
    show japan large ah2 at pos_transform(xpos=450, ypos=-80)
    with {'master': Dissolve(0.25)} 
    story "齧るとアイスクリーム頭痛が\n直で脳に来るあの感覚が…\n今の私には耐えられないのです…っ！" id story3_0409e854
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
    eng "老いが原因ではないはずだ！\nきっと俺たちに人みたいな\n老いの症状はないはずだ…！\nああ、ないに違いない！" id story3_dee9a6a1

    show finland worried smiling at pos_transform(xpos=-80, ypos=30) behind england
    $ fin.screen='left_3'
    fin "まるで自分に\n言い聞かせるよう\nじゃないですかぁ！" id story3_7b5844cd

    show bulgaria sweat worried at pos_transform(xpos=550, yoffset=1.0) behind japan
    $ bul.screen='right_3'
    bul "俺も実は結構歳いって…\n大丈夫っすよね。\nうん大丈夫なんだわー！" id story3_277eafee
    
    

    show germany squint at pos_transform(xpos=630, yoffset=1.0) behind bulgaria with Dissolve(0.2)
    show england at stop_offset with {'master':move}
    $ ger.screen='right_4'
    ger "どうも気になる話だな\n俺の方で調査してみよう\n後で詳しい場所と証言を頼む" id story3_ffe4e766

    show japan shocked
    $ jpn.screen='center_1'
    jpn "えっ、はい" id story3_2fa621a2

    scene bg classroom1
    show nvl_textbox
    stop music fadeout 2
    show japan large laugh at pos_transform(xpos=450, ypos=-80)

    story "私の話は以上です。\nご清聴ありがとうございました。\n次の方、お願いいたします。" id story3_e7f27d58
    nvl clear
    hide nvl_textbox
    pause 0.1


    jump story4