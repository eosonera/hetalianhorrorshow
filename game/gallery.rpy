## Gallery ############################################################
##
##
##
##

define gal = Character(None,
    window_background="textbox_gush.png",
    window_xalign=0,
    window_yalign=0,
    what_xpos=162,
    what_ypos=468,
    ctc="ctc_button",
    ctc_position="nestled")

label gallery:

    if persistent.game_finished:
        play music "9_townscape.ogg" fadeout 1
        scene bg exterior6

        show sweden

        gal "スウェーデン。"
        
        
    else:
        stop music fadeout 1
        scene bg exterior6

        gal "クリアーすると解放されます。"
        
    return
