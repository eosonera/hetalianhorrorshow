## Exterior ################################################################


image sun1_exterior = At("sunlight2", tr_sun_ext(0.25, (509, -100), (509, -100), (509, -100)))
image sun2_exterior = At("sunlight2", tr_sun_ext(9.6, (509, -100), (509, -100), (509, -100)))
image sun3_exterior = At("sunlight2", tr_sun_ext(12.7, (509, 65), (509, 67), (509, 66)))


transform pan_exterior:
    yalign 1.0
    easein 7 yalign 0.0

image bg exterior= Fixed(
    pan_exterior("exterior"),
    sun1_exteriorspin("sun1_exterior"),
    sun2_exteriorspin("sun2_exterior"),
    sun3_exteriorspin("sun3_exterior"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
)


transform tr_yellow_ext:
    align(0.5,0.5) alpha 0.0 xzoom 1 yzoom 1
    block:
        time 1.85
        linear 4.4 xzoom 1.3 yzoom 1.2 alpha 0.25 additive_blend
        linear 4.4 xzoom 1 yzoom 1 alpha 0.0 additive_blend
        time 1.05
        repeat

transform tr_orange_ext:
    align(0.5,0.5) alpha 0.0
    block:
        time 13.35
        linear 4.4 alpha 0.25 additive_blend
        linear 4.4 alpha 0.0 additive_blend
        time 12
        repeat


image sun1_exterior1 = At("sunlight2", tr_sunlight1((653,12), (657,0), (648,1), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_exterior1 = At("sunlight2", tr_sunlight2((653,12), (657,0), (648,1), 0.25, 0.15, 0.24, 1, 1, 1, 1))


image bg exterior1= Fixed(
    pan_to_top("exterior1"),
    spin_sun1("sun1_exterior1"),
    spin_sun2("sun2_exterior1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)


image bg exterior2= Fixed(
    pan_to_top("exterior2"),
    spin_sun1("sun1_exterior1"),
    spin_sun2("sun2_exterior1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)


image bg exterior3= Fixed(
    pan_to_bottom("exterior3"),
    spin_sun1("sun1_exterior1"),
    spin_sun2("sun2_exterior1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)

transform tr_blue_ext:
    align(0.5,0.5) alpha 0.0 xzoom 1 yzoom 1
    block:
        time 1.85
        linear 4.4 xzoom 1.3 yzoom 1.2 alpha 0.25 additive_blend
        linear 4.4 xzoom 1 yzoom 1 alpha 0.0 additive_blend
        time 1.05
        repeat

transform pan_exterior4:
    yalign 1.0 xalign 0
    easein 20 yoffset 270

image sun1_exterior4 = At("sunlight2", tr_sunlight1((46, 2), (47, 1), (48, 3), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_exterior4 = At("sunlight2", tr_sunlight2((62, -7), (78, -3), (83, -5), 0.25, 0.15, 0.24, 1, 1, 1, 1))

image bg exterior4= Fixed(
    pan_exterior4("exterior4"),
    spin_sun1("sun1_exterior4"),
    spin_sun2("sun2_exterior4"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_classroom("orange"),
    tr_blue_ext("blue"),
)


image bg exterior5= Fixed(
    pan_to_top("exterior5"),
    spin_sun1("sun1_exterior1"),
    spin_sun2("sun2_exterior1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)


image bg exterior6= Fixed(
    pan_to_top("exterior6"),
    spin_sun1("sun1_exterior1"),
    spin_sun2("sun2_exterior1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)


image bg exterior7= Fixed(
    pan_to_top("exterior7"),
    spin_sun1("sun1_exterior1"),
    spin_sun2("sun2_exterior1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)


image bg exterior8= Fixed(
    pan_to_top("exterior8"),
    spin_sun1("sun1_exterior1"),
    spin_sun2("sun2_exterior1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),

)

image bg exterior9= Fixed(
    pan_to_top("exterior9"),
    spin_sun1("sun1_exterior1"),
    spin_sun2("sun2_exterior1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)



## Hallway ################################################################


image bg hallway= Fixed(
    pan_to_top("hallway"),
    spin_sun1("sun1_rroom1"),
    spin_sun2_1("sun2_rroom1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
)

image sun1_hallway2 = At("sunlight2", tr_sunlight1((684, 17), (684, 17), (684, 18), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_hallway2 = At("sunlight2", tr_sunlight2((684, 17), (684, 17), (684, 18), 0.25, 0.15, 0.24, 0.8, 0.6, 1, 1))

image bg hallway2= Fixed(
    pan_to_bottom("hallway2"),
    spin_sun1("sun1_hallway2"),
    spin_sun2("sun2_hallway2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
)



## Classroom ################################################################


image sun1_classroom1 = At("sunlight2", tr_sunlight1((22, 146), (17, 140), (14, 140), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_classroom1 = At("sunlight2", tr_sunlight2((22, 137), (20, 137), (19, 138), 0.25, 0.15, 0.24, 1, 1, 1, 1))

image bg classroom1= Fixed(
    pan_to_bottom("classroom1"),
    spin_sun1("sun1_classroom1"),
    spin_sun2("sun2_classroom1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",

)

image sun1_classroom2 = At("sunlight2", tr_sunlight1((684, -100), (684, -100), (684, -100), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_classroom2 = At("sunlight2", tr_sunlight2((684, -120), (684, -120), (684, -120), 0.25, 0.15, 0.24, 1, 1, 1, 1))

image bg classroom2= Fixed(
    pan_to_bottom1("classroom2"),
    spin_sun1("sun1_classroom2"),
    spin_sun2("sun2_classroom2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",

)


transform tr_orange_classroom:
    align(0.5,0.5) alpha 0.0
    block:
        time 3.35
        linear 1.75 alpha 0.2 additive_blend
        linear 1.75 alpha 0.0 additive_blend
        time 16.55
        repeat

transform tr_yellow_classroom:
    align(0.5,0.5) alpha 0.0
    block:
        time 14.2
        linear 1.75 alpha 0.15 additive_blend
        linear 1.75 alpha 0.0 additive_blend
        time 5.7 #total 23.35
        repeat


image sun1_classroom3 = At("sunlight2", tr_sunlight1((189, 167), (188, 171), (187, 169), 0.15, 0.71, 0.92, 0.76, 0.76, 1, 1))
image sun2_classroom3 = At("sunlight2", tr_sunlight2((344, 206), (338, 205), (337, 203), 0.15, 0.32, 0.44, 0.8, 0.6, 1, 1))

image bg classroom3= Fixed(
    pan_to_top("classroom3"),
    spin_sun1("sun1_classroom3"),
    spin_sun2_1("sun2_classroom3"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_classroom("orange"),
    tr_yellow_classroom("yellow"),

)

transform pan_classroom4:
    ypos 0 xalign 0
    linear 1.6 yoffset -70

image sun1_classroom4 = At("sunlight2", tr_sunlight1((46, 2), (47, 1), (48, 3), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_classroom4 = At("sunlight2", tr_sunlight2((62, -7), (78, -3), (83, -5), 0.25, 0.15, 0.24, 1, 1, 1, 1))

image bg classroom4= Fixed(
    pan_classroom4("classroom4"),
    spin_sun1("sun1_classroom4"),
    spin_sun2("sun2_classroom4"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)

image sun1_classroom_door2 = At("sunlight2", tr_sunlight1((0, -55), (0, -149), (0, -130), 0.15, 0.71, 0.92, 0.76, 0.76, 1, 1))
image sun2_classroom_door2 = At("sunlight2", tr_sunlight2((-158, 71), (-33, 99), (-66, 65), 0.15, 0.71, 0.92, 0.76, 0.76, 1.4, 1.3))

transform tr_red_door:
    align(0.5,0.5) alpha 0.0
    block:
        time 17.2
        linear 1.75 alpha 0.15 additive_blend
        linear 1.75 alpha 0.0 additive_blend
        time 2.7 #total 23.35
        repeat

image bg classroom_door2= Fixed(
    pan_to_top("classroom4"),
    spin_sun1("sun1_classroom_door2"),
    spin_sun2("sun2_classroom_door2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_classroom("orange"),
    tr_yellow_classroom("yellow"),
    tr_red_door("red")

)


image sun1_classroom5 = At("sunlight2", tr_sunlight1((699, 105), (699, 105), (697, 106), 0.15, 0.71, 0.92, 0.76, 0.76, 1, 1))
image sun2_classroom5 = At("sunlight2", tr_sunlight2((789, 74), (790, 67), (791, 67), 0.15, 0.32, 0.44, 0.8, 0.6, 1, 1))

image bg classroom5= Fixed(
    pan_to_top("classroom5"),
    spin_sun1("sun1_classroom5"),
    spin_sun2_1("sun2_classroom5"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_classroom("orange"),
    tr_yellow_classroom("yellow"),

)


image sun1_classroom_door = At("sunlight2", tr_sunlight1((133, -55), (279, -149), (255, -130), 0.15, 0.71, 0.92, 0.76, 0.76, 1, 1))
image sun2_classroom_door = At("sunlight2", tr_sunlight2((-158, 71), (-33, 99), (-66, 65), 0.15, 0.71, 0.92, 0.76, 0.76, 1.4, 1.3))

image bg classroom_door= Fixed(
    pan_to_top("classroom_door"),
    spin_sun1("sun1_classroom_door"),
    spin_sun2("sun2_classroom_door"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_classroom("orange"),
    tr_yellow_classroom("yellow"),
    tr_red_door("red")

)



image sun1_classroom_window = At("sunlight2", tr_sunlight1((269, 2), (192, 3), (227, -4), 0.25, 0.71, 0.92, 0.76, 0.76, 1, 1))
image sun2_classroom_window = At("sunlight2", tr_sunlight2((311, -3), (313, 1), (313, -1), 0.25, 0.32, 0.44, 0.8, 0.6, 1, 1))

image bg classroom_window= Fixed(
    pan_to_top("classroom_window"),
    spin_sun1("sun1_classroom_window"),
    spin_sun2_1("sun2_classroom_window"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_classroom("orange"),
    tr_yellow_classroom("yellow"),

)


image sun1_bulletin_board = At("sunlight2", tr_sunlight1((892, 32), (894, 36), (894, 34), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_bulletin_board = At("sunlight2", tr_sunlight2((916, 74), (910, 86), (912, 108), 0.25, 0.15, 0.24, 0.8, 0.6, 1, 1))

image bg bulletin_board = Fixed(
    ("bulletin_board"),
    spin_sun1("sun1_bulletin_board"),
    spin_sun2("sun2_bulletin_board"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
)


