

label story7:
    scene bg hallway2
    na "第七話最後の怖い話"
    scene bg classroom_window
    play music "Carol_of_the_Bells_ESPN_(Album_Version).ogg"
    show russia 2 large ahahahaha at pos_transform(x=-70, y=-90)
    $ rus.screen = 'center_3'
    rus"大丈夫。\n僕は怖くないよ？"
    with dissolve
    scene bg classroom1

    menu:

        "成り行きに任せる":
            jump donothing

        "俺が止める！！":
            jump stophim


    label stophim:
        #$ menu_flag = False
        play music "11_liarliar.ogg"
        bul "ロ…ロシアさんっ！\nちょっとそれは\nやめるんだわー！"
        scene bg exterior
        pause 5
        scene bg exterior4
        pause 5
        scene bg exterior5
        pause 5
        scene bg exterior6
        pause 5
        scene bg exterior8
        pause 5
        

        $ persistent.game_finished = True
        return

    label donothing:
        #$ menu_flag = True
        scene bg exterior2
        play music "39_USbattlesong.ogg"
        ame "やめるんだロシア！\n君がやめないのなら\n俺が君を止めるまでだ！"
        pause 5
        scene bg exterior4
        pause 5
        
        

        $ persistent.game_finished = True
        return




    