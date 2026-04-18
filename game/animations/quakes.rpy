


## Prologue #############################################################################
transform shake_0p1:
    linear 0.1 xoffset -21 yoffset -17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0p2:
    xoffset 0 yoffset 0
    block:
        linear 0.1 xoffset -8 yoffset -8
        linear 0.1 xoffset +8 yoffset +8
        repeat 2
    linear 0.1 xoffset 0 yoffset 0

transform shake_0p3:
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset -8 yoffset +8
    linear 0.1 xoffset +8 yoffset -8
    linear 0.1 xoffset 0 yoffset 0

transform shake_0p4:
    linear 0.1 xoffset -21 yoffset -17
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0p5:
    linear 0.1 xoffset -21 yoffset +17
    linear 0.1 xoffset +10 yoffset -10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform humming_tf:
    xoffset 0 yoffset 0
    block:
        parallel:
            ease 0.6 xoffset -150
            ease 0.6 xoffset +150
        parallel:
            ease 0.3 yoffset 0
            ease 0.3 yoffset -15
            ease 0.3 yoffset 0
            ease 0.3 yoffset -15
        repeat


## Meeting #################################################################################

transform shake_0m1:
    linear 0.1 xoffset -22 yoffset -21
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -18 yoffset +19
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset -11 yoffset +8
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m2:
    linear 0.1 xoffset +22 yoffset -22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset -6
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m3:
    linear 0.1 xoffset +15 yoffset -15
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -9 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +4 yoffset -4
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m4:
    linear 0.1 xoffset +21 yoffset -17
    linear 0.1 xoffset -10 yoffset +10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m5:
    linear 0.1 xoffset -21 yoffset +17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m6:
    linear 0.1 xoffset -22 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m7:
    linear 0.1 xoffset +22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m8:
    linear 0.1 xoffset +18 yoffset +18
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m9:
    linear 0.1 xoffset -18 yoffset +18
    linear 0.1 xoffset +9 yoffset -9
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +8 yoffset +8
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m10:
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset -8 yoffset +8
    linear 0.1 xoffset +8 yoffset -8
    linear 0.1 xoffset 0 yoffset 0

transform shake_0m11:
    linear 0.1 xoffset +22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform fin_m1:
    easeout 0.2 yoffset -30
    easein 0.15 yoffset 10
    easeout 0.15 yoffset 0

transform fin_m2:
    easeout 0.3 yoffset -40
    ease 0.2 yoffset 10
    easeout 0.2 yoffset -30
    ease 0.15 yoffset 0

transform fin_m3:
    yoffset 0
    easeout 0.3 yoffset -30
    ease 0.2 yoffset 10
    easeout 0.2 yoffset -20
    ease 0.15 yoffset 0

transform hide_celeb:
    alpha 1.0
    linear 1 alpha 0

## Ch1 ###########################################################################################

transform shake_1s1:
    linear 0.1 xoffset -22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform unhide_s1:
    alpha 0
    linear 1 alpha 1

## Ch2 ###########################################################################################
transform shake_stop:
    ypos 0 xpos 0

transform shake_2s1:
    linear 0.1 xoffset -12 yoffset -12
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -8 yoffset +9
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset -2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s2:
    linear 0.1 xoffset -22 yoffset +22
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset -12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s3:
    linear 0.1 xoffset +22 yoffset +22
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset +12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s4:
    linear 0.1 xoffset -21 yoffset -17
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s5:
    linear 0.1 xoffset -22 yoffset -21
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -18 yoffset +19
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset -11 yoffset +8
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s6:
    linear 0.1 xoffset -22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s7:
    linear 0.1 xoffset -22 yoffset +22
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset +12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0

transform shake_2s8:
    linear 0.1 xoffset +8 yoffset +8
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -4 yoffset -4
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0

transform ame_2s1:
    linear 0.1 xoffset -22 yoffset -21
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -18 yoffset +19
    linear 0.1 xoffset +12 yoffset -12
    linear 0.1 xoffset -11 yoffset +8
    linear 0.1 xoffset 0 yoffset 0

## Ch3 ###########################################################################################

transform shake_3s1:
    block:
        linear 0.07 xoffset -12 yoffset 12
        linear 0.07 xoffset 0 yoffset 0
        repeat 3
    linear 0.07 xoffset 8 yoffset 8
    linear 0.07 xoffset 0 yoffset 0
    linear 0.05 xoffset -8 yoffset 8
    linear 0.05 xoffset 0 yoffset 0
    linear 0.07 xoffset -4 yoffset 4
    linear 0.07 xoffset 0 yoffset 0

transform shake_3s2:
    linear 0.1 xoffset -21 yoffset +17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_3s3:
    linear 0.1 xoffset -8 yoffset -8
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +8 yoffset -8
    linear 0.1 xoffset -4 yoffset -4
    linear 0.1 xoffset +2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0

transform jpn_2s1:
    easein 0.45 yoffset +40
    easeout 0.3 yoffset 0

transform eng_3s1:
    xpos 60 yoffset 1.0
    block:
        linear 0.07 xoffset -12
        linear 0.07 xoffset 0
        repeat 5

transform unhide_s3:
    alpha 0
    time 1
    linear 1 alpha 1

## Ch4 ###########################################################################################

transform shake_4s1:
    linear 0.05 xoffset -42 yoffset -40
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +20 yoffset -20
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +10 yoffset +10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -6 yoffset -6
    linear 0.05 xoffset 0 yoffset 0


transform shake_4s2:
    linear 0.05 xoffset +42 yoffset +40
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -20 yoffset -20
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +10 yoffset -10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -6 yoffset +6
    linear 0.05 xoffset 0 yoffset 0


transform shake_4s3:
    linear 0.1 xoffset -32 yoffset +30
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +6 yoffset +6
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +3 yoffset -3
    linear 0.1 xoffset 0 yoffset 0

## Ch5 ###########################################################################################

transform shake_5s1:
    linear 0.05 xoffset -42 yoffset -40
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +30 yoffset -30
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +10 yoffset +10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset -6 yoffset -6
    linear 0.05 xoffset 0 yoffset 0
    linear 0.05 xoffset +3 yoffset +3
    linear 0.05 xoffset 0 yoffset 0

transform shake_5s2:
    linear 0.1 xoffset -30 yoffset -30
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -6 yoffset -6
    linear 0.1 xoffset 0 yoffset 0

transform shake_5s3:
    linear 0.1 xoffset +20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0

transform shake_5s4:
    linear 0.1 xoffset -22 yoffset -21
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -12 yoffset -12
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -3 yoffset -3
    linear 0.1 xoffset 0 yoffset 0

transform shake_5s5:
    linear 0.1 xoffset -20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -4 yoffset +4
    linear 0.1 xoffset 0 yoffset 0

transform bul_5s:
    xpos 700

transform ame_5s:
    ypos 100

## Ch6 ###########################################################################################

transform shake_6s1:
    linear 0.1 xoffset +20 yoffset +17
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0

transform shake_6s2:
    linear 0.1 xoffset +30 yoffset +27
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0

## Ch7 ###########################################################################################

transform shake_7s1:
    linear 0.1 xoffset +20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s2:
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +15 yoffset -15
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -9 yoffset -9
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +4 yoffset -4
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s3:
    linear 0.1 xoffset +20 yoffset +20
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s4:
    linear 0.1 xoffset -30 yoffset -30
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s5:
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s6:
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -2 yoffset -2
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s7:
    linear 0.1 xoffset -20 yoffset +20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -2 yoffset -2
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s8:
    linear 0.1 xoffset +20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset -5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset +2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0

transform shake_7s9:
    linear 0.1 xoffset +20 yoffset -20
    linear 0.05 xoffset 0 yoffset 0
    linear 0.1 xoffset +20 yoffset -20
    linear 0.1 xoffset -10 yoffset +10
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -5 yoffset +5
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -2 yoffset +2
    linear 0.1 xoffset 0 yoffset 0

transform rom_7s1:
    linear 0.5 alpha 1
    easeout 0.15 yoffset -45
    ease 0.15 yoffset 10
    easeout 0.15 yoffset -35
    ease 0.15 yoffset 5
    easeout 0.15 yoffset -5
    ease 0.15 yoffset 0

transform rom_7s2:
    easeout 0.15 yoffset -30
    easein 0.15 yoffset 5
    easeout 0.15 yoffset -20
    easein 0.15 yoffset 2
    easeout 0.15 yoffset 0


transform bul_7s3:
    xpos -50 ypos -40
    linear 0.1 xoffset 15 yoffset -10
    linear 0.1 xoffset 0 yoffset 0

transform rom_7s3:
    pause 0.2
    "romania med eh" with Dissolve(0.2)
    pause 0.4
    linear 0.1 xoffset -30 yoffset -30
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -20 yoffset -20
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -10 yoffset -10
    linear 0.1 xoffset 0 yoffset 0

transform rom_7s4:
    xpos 310
    linear 0.08 xoffset 0
    linear 0.08 xoffset 7
    linear 0.08 xoffset -7
    linear 0.08 xoffset 7
    linear 0.08 xoffset -7
    linear 0.08 xoffset 7
    linear 0.08 xoffset -7
    linear 0.1 xoffset 0


transform rom_7s5:
    xpos -40, yalign 0.0
    block:
        linear 0.08 xoffset -5
        linear 0.08 xoffset 0
        repeat