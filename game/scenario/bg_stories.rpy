## Prologue ################################################################

image sun1_rroom1 = At("sunlight2", tr_sunlight1((-200, 0), (-200, 0), (-200, 0), 0.25, 1, 1, 1, 1, 1, 1))
image sun2_rroom1 = At("sunlight2", tr_sunlight2((-200, 32), (-200, 33), (-200, 35), 0.25, 1, 1, 1, 1, 1, 1))

image bg romania_room = Fixed(
    pan_to_top("romania_room"),
    spin_sun1("sun1_rroom1"),
    spin_sun2_1("sun2_rroom1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
)

image sun1_rroom3 = At("sunlight2", tr_sunlight1((428, 85), (430, 85), (430, 86), 0.15, 0.71, 0.92, 0.76, 0.76, 1, 1))
image sun2_rroom3 = At("sunlight2", tr_sunlight2((371, 29), (371, 29), (373, 32), 0.15, 0.32, 0.44, 0.8, 0.6, 1, 1))

image bg romania_room3= Fixed(
    pan_to_top("romania_room3"),
    spin_sun1("sun1_rroom3"),
    spin_sun2_1("sun2_rroom3"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_classroom("orange"),
    tr_yellow_classroom("yellow"),
)

image sun1_rroom2 = At("sunlight2", tr_sunlight1((509, 65), (509, 67), (509, 66), 0.25, 0.47, 0.58, 1, 1, 1, 1))

image bg romania_room2= Fixed(
    pan_to_top("romania_room2"),
    spin_sun1("sun1_rroom2"),
    spin_sun2_1("sun2_rroom1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
)



## Meeting ################################################################

transform tr_sun_eng(time1, cen1, cen2, cen3):
    alpha 0.0 additive_blend xzoom 0.15 yzoom 0.24 xycenter cen1
    time time1
    block:
        linear 4.5 alpha 0.15 additive_blend xzoom 1 yzoom 1 xycenter cen2
        linear 3 alpha 0.0 additive_blend xzoom 1 yzoom 1 xycenter cen3
        pause 10.8 alpha 0.0 additive_blend xzoom 0.15 yzoom 0.24 xycenter cen1
        repeat 

transform spin_sun_eng1:
    rotate 1
    time 1.9
    block:
        linear 6.7 rotate -35 #8.6
        linear 5.85 rotate -58 #14.45

transform spin_sun_eng2:
    rotate 1
    time 2.35
    block:
        linear 6.7 rotate -35 #8.6
        linear 5.85 rotate -58 #14.45

image sun1_engdoodles = At("sunlight2", tr_sun_eng(1.9, (19, 20), (21, 22), (21, 22)))
image sun2_engdoodles = At("sunlight2", tr_sun_eng(2.35, (-3, 6), (-3, 6), (-5, 3)))

image bg engdoodles= Fixed(
    blackboard("engdoodles"),
    spin_sun_eng1("sun1_engdoodles"),
    spin_sun_eng2("sun2_engdoodles"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_eng_yellow("yellow"),
    tr_eng_lightblue("lightblue"),
    tr_eng_blue("upperhalf")
)




## Ch 1 ################################################################

image bg forest1= Fixed(
    pan_forest4("forest1"),
    spin_sun1("sun1_forest2"),
    spin_sun2("sun2_forest2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)


image sun1_forest2 = At("sunlight2", tr_sunlight1((22, 146), (17, 140), (14, 140), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_forest2 = At("sunlight2", tr_sunlight2((22, 137), (20, 137), (19, 138), 0.25, 0.15, 0.24, 0.8, 0.6, 1, 1))
transform pan_forest2:
    yalign 1.0 xalign 0
    easein 5 yalign 0.0


image bg forest2= Fixed(
    pan_forest2("forest2"),
    spin_sun1("sun1_forest2"),
    spin_sun2("sun2_forest2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)

transform pan_forest3:
    yalign 1.0 xalign 0.0
    easein 25 xoffset -223
    block:
        linear 25 xoffset 0
        linear 25 xoffset -223
        repeat


image bg forest3= Fixed(
    pan_forest3("forest3"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)

image sun1_forest4 = At("sunlight2", tr_sunlight1((761, 63), (757, 64), (757, 61), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_forest4 = At("sunlight2", tr_sunlight2((836, 1), (836, 3), (837, 5), 0.25, 0.15, 0.24, 0.8, 0.6, 1, 1))

transform pan_forest4:
    yalign 0.0 xalign 0
    easein 1.6 yoffset -70


image bg forest4= Fixed(
    pan_forest4("forest4"),
    spin_sun1("sun1_forest4"),
    spin_sun2("sun2_forest4"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)


image bg night= Fixed(
    pan_to_top("night"),
    spin_sun1("sun1_forest2"),
    spin_sun2("sun2_forest2"),  
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)


image bg stars= Fixed(
    pan_forest3("stars"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)


transform pan_snowy2:
    ypos -270 xalign 0
    easein 1.6 ypos 0


image bg snowy2= Fixed(
    pan_snowy2("snowy2"),
    spin_sun1("sun1_forest2"),
    spin_sun2("sun2_forest2"),  
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)

transform pan_snowy:
    yalign 0 xalign 0
    easein 1.6 yoffset -210


image bg snowy= Fixed(
    pan_snowy("snowy"),
    spin_sun1("sun1_forest2"),
    spin_sun2("sun2_forest2"),  
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_yellow_ext("yellow"),

)

transform pan_water:
    yalign 0 xalign 0
    linear 30 yoffset -404

image bg water1 = WrapTiled("water1", speed_x=0, speed_y=-10, init_x=0.0, init_y=0)

image bg water= Fixed(
    #pan_water("water"),
    "bg water1"
)

image bg ripples1 = WrapTiled("ripples1", speed_x=0, speed_y=-50, init_x=0.0, init_y=0)
image ripples vfx= Fixed(
    "dust2_0",
    "dust0_0",
    "dust1_0",

)


image swe_anim= Fixed(
    swe1_transform("swe1"),
    swe2_transform("swe2"),
    swe3_transform("swe3"),

)


transform pan_home:
    yalign 0 xalign 0
    linear 1.6 yoffset -70

image bg home= Fixed(
    pan_home("home"),
    spin_sun1("sun1_forest2"),
    spin_sun2("sun2_forest2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),

)


## Ch2 ################################################################

image bg tech= Fixed(
    pan_to_top("tech"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)


image bg tech2= Fixed(
    pan_to_top("tech2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)

image bg tech3= Fixed(
    pan_to_top("tech3"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)

transform tr_yellow_a:
    align(0.5,0.5) alpha 0.0 xzoom 1 yzoom 1
    time 0.95
    linear 4.4 xzoom 1.3 yzoom 1.2 alpha 0.25 additive_blend
    linear 4.4 xzoom 1 yzoom 1 alpha 0.0 additive_blend

transform tech3_tr:
    align(0.53, 0.93) zoom 2.0
    linear 9.65 align(1.0, 0.0) zoom 1.0

image alien_anim= Fixed(
    tech3_tr("tech3"),
    "dust2_1",
    "dust0_0",
    "dust1_0",
    tr_yellow_a("yellow"),
)

transform tr_blue_a:
    align(0.5,0.5) alpha 0.0 xzoom 1 yzoom 1
    time 0.35
    linear 4.4 xzoom 1.3 yzoom 1.2 alpha 0.15 additive_blend
    linear 4.4 xzoom 1 yzoom 1 alpha 0.0 additive_blend

transform tr_orange_a:
    align(0.5,0.5) alpha 0.0
    time 10.5
    linear 4.4 alpha 0.25 additive_blend
    linear 4.4 alpha 0.0 additive_blend

image ufo_anim= Fixed(
    ufo1_pos("ufo1"),
    ufo2_pos("ufo2"),
    "snow_alien",
    ufo4_pos("ufo4"),
    "dust2_1",
    "dust0_0",
    "dust1_0",
    ufo3_pos("ufo3"),
    tr_blue_a("blue"),
    tr_orange_a("orange"),
)

## Ch 3 ################################################################

image bg tokyo1= Fixed(
    pan_to_top("tokyo1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)


image bg tokyo2= Fixed(
    ("tokyo2"),
    "surface3_0",
    "rain1_0",
    "rain2_0",
    "rain3_0",
    "rain4_0"
)

image bg tokyo3= Fixed(
    ("tokyo3"),
    "surface1_0",
    "surface2_0",
    "rain1_0",
    "rain2_0",
    "rain3_0",
    "rain4_0"
)

image bg tokyo4= Fixed(
    ("tokyo4"),
    "surface4_0",
    "rain1_0",
    "rain2_0",
    "rain3_0",
    "rain4_0"
)


transform pan_tokyo5:
    ypos -270 xalign 0
    linear 8.3 yalign 0.0

image bg tokyo5= Fixed(
    pan_tokyo5("tokyo5"),
    "rain1_0",
    "rain2_0",
    "rain3_0",
    "rain4_0"
)

image legs1 = Fixed(
    ("legs"),
    ("surface6_0"))


image bg legs= Fixed(
    pan_legs("legs1"),
    "rain1_0",
    "rain2_0",
    "rain3_0",
    "rain5_0"
)


transform pan_legs:
    ypos -130 xalign 0
    linear 8.3 yalign 0.0



image bg legs2= Fixed(
    pan_legs("legs2"),
    "surface5_0",
    "rain1_0",
    "rain2_0",
    "rain3_0",
    "rain5_0"
)

transform pan_japanhouse:
    ypos 0 xalign 0
    linear 5 ypos -140

transform tr_light(time1):
    alpha 0.0 xycenter(425,380) xzoom 0.1 yzoom 0.1 additive_blend
    time time1
    block:
        linear 4.5 xzoom 0.15 yzoom 0.1 alpha 0.15 additive_blend
        linear 3 xzoom 0.2 yzoom 0.5 alpha 0.0 additive_blend
        linear 15.7 xzoom 0.1 yzoom 0.1 xycenter(425,380) alpha 0.0 additive_blend
        repeat

image light1_japan = At("light", tr_light(time1=0.01))
image light2_japan = At("light", tr_light(time1=8.5))

transform spin_lightjapan1:
    rotate 1
    time 0.01
    block:
        linear 4.5 rotate -30
        linear 3 rotate -58
        pause 15.7 rotate 1
        repeat

transform spin_lightjapan2:
    rotate 1
    time 8.5
    block:
        linear 4.5 rotate -30
        linear 3 rotate -58
        pause 15.7 rotate 1
        repeat

image japanhouse1 = Fixed(
    ("japanhouse"),
    spin_lightjapan1("light1_japan"),
    spin_lightjapan2("light2_japan"))

image bg japanhouse = Fixed(
    pan_japanhouse("japanhouse1"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_yellow_ext("yellow"),
)


transform pan_rainjapan:
    ypos 0 xpos 0
    linear 8.3 xpos -190
    block:
        linear 7.2 xpos -170
        linear 7.2 xpos -190
        repeat

image bg rainjapan= Fixed(
    pan_rainjapan("rainjapan"),
    "rain3_0",
    tr_rainjpn1("rainjapan1"),
    tr_rainjpn2("rainjapan2"),
    "bigrain1_0",
    "bigrain2_0",
    "rain5_0",
)


## Ch 4 ################################################################

transform tr_wrapfog:
    alpha 0.53 additive_blend

image fog_ger1 = WrapTiled("images/vfx/mist.png", speed_x=-42)
image fog_ger2 = WrapTiled("images/vfx/mist.png", speed_x=-21, speed_y=4, init_x=0.0, init_y=200.0)

transform tr_armor0:
    xpos -26 ypos -4
    linear 21 xpos -282 ypos -35
    block:
        linear 21 ypos -4
        linear 21 ypos -35
        repeat

image bg armor0= Fixed(
    tr_armor0("armor0"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
    tr_wrapfog("fog_ger1"),
    tr_wrapfog("fog_ger2")    
)

transform tr_blue_armor:
    alpha 0
    block:
        linear 4.5 alpha 0.25 xzoom 1.3 yzoom 1.2 additive_blend
        linear 4.5 alpha 0.0 xzoom 1.0 yzoom 1.0 additive_blend
        time 32
        repeat

transform tr_armor1:
    ypos 0
    block:
        linear 21 ypos -120
        linear 21 ypos 0
        repeat

image bg armor= Fixed(
    tr_armor1("armor"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_blue_armor("blue"),
    tr_orange2("orange"),
    tr_orange3("orange"),
    tr_wrapfog("fog_ger1"),
)

transform tr_armor2:
    linear 21 ypos -70
    block:
        linear 21 ypos 0
        linear 21 ypos -70
        repeat

image bg armor2= Fixed(
    tr_armor2("armor2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_armor("blue"),
    tr_orange2("orange"),
    tr_orange3("orange"),
    tr_wrapfog("fog_ger1")
)


image bg oresama= Fixed(
    ("oresama"),
)


## Ch 6 ################################################################

transform tr_runaway:
    xpos -140
    linear 11.5 xpos 0

transform tr_runaway1:
    align (0.5, 0.5)
    parallel:
        xoffset -60
        linear 11.5 xoffset 0
    parallel:
        zoom 1 alpha 0.6
        linear 1 zoom 2 alpha 0
        repeat 3

transform tr_runaway2:
    align (0.5, 0.5) alpha 0
    time 1
    parallel:
        xoffset -60
        linear 11.5 xoffset 0
    parallel:
        zoom 1 alpha 0.6
        linear 1 zoom 2 alpha 0
        repeat 2


image bg runaway= Fixed(
    tr_runaway("runaway"),
    tr_runaway1("runaway"),
    tr_runaway2("runaway"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)




transform pan_alley:
    yalign 1.0
    linear 11.5 yoffset 200

image sun1_alley = At("sunlight2", tr_sunlight1((46, 2), (47, 1), (48, 3), 0.25, 0.15, 0.24, 1, 1, 1, 1))
image sun2_alley = At("sunlight2", tr_sunlight2((62, -7), (78, -3), (83, -5), 0.25, 0.15, 0.24, 0.8, 0.6, 1, 1))

image bg alley= Fixed(
    pan_alley("alley"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)

transform pan_casual:
    yalign 0.0
    linear 6 yoffset -80

image bg casual= Fixed(
    pan_casual("casual"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)



image bg luggage= Fixed(
    pan_officer("luggage"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)

transform pan_officer:
    yalign 1.0
    linear 6 yoffset 70

image bg officer= Fixed(
    pan_officer("officer"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)

transform pan_pedestrian:
    xpos -270
    linear 11.5 xpos 0

image bg pedestrian= Fixed(
    pan_pedestrian("pedestrian"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)

transform pan_pedestrian2:
    ypos 0
    linear 23.5 yoffset -200

image bg pedestrian2= Fixed(
    pan_pedestrian2("pedestrian2"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)

transform pan_postcard:
    xpos 0
    block:
        linear 11.5 xoffset -220
        linear 11.5 xoffset 0
        repeat
    

image bg postcard= Fixed(
    pan_postcard("postcard"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)

transform pan_postcard2:
    ypos 0
    linear 23.5 yoffset -300

image bg postcard2= Fixed(
    pan_postcard2("postcard2"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)

transform pan_road:
    yalign 1.0
    linear 11.5 yoffset 67

image bg road= Fixed(
    pan_road("road"),
    spin_sun1("sun1_alley"),
    spin_sun2("sun2_alley"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)


image bg strangle= Fixed(
    tr_strangle1("strangle"),
    tr_strangle2("strangle2"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_orange_ext("orange"),
    tr_blue_ext("blue"),
)

transform pan_walking:
    xpos -1700
    linear 75 xpos 0


transform tr_sun_w(time1, cen1, cen2, cen3, xzoom2, yzoom2):
    alpha 0.0 xzoom 0.15 yzoom 0.24 xycenter cen1 additive_blend
    time time1
    block:
        linear 6.7 alpha 0.25 xzoom 1 yzoom 1 xycenter cen2 additive_blend
        linear 5.85 alpha 0.0 xzoom xzoom2 yzoom yzoom2 xycenter cen3 additive_blend
        pause 76.9 alpha 0.0 xzoom 0.15 yzoom 0.24 xycenter cen1 additive_blend
        repeat 

image sun1_walking = At("sunlight2", tr_sun_w(1.9, (46, 2), (47, 1), (48, 3), 1, 1))
image sun2_walking = At("sunlight2", tr_sun_w(8.9, (62, -7), (78, -3), (83, -5), 1, 1))
image sun3_walking = At("sunlight2", tr_sun_w(26.4, (62, -7), (78, -3), (83, -5), 0.8, 0.6))

transform sun1_walkingspin:
    rotate 1
    time 1.9
    block:
        linear 6.7 rotate -35 #8.6
        linear 5.85 rotate -58 #14.45
        pause 10.8 rotate 1
        repeat

transform sun2_walkingspin:
    rotate 1
    time 8.9
    block:
        linear 6.7 rotate -35 #8.6
        linear 5.85 rotate -58 #14.45
        pause 10.8 rotate 1
        repeat

transform sun3_walkingspin:
    rotate 1
    time 26.4
    block:
        linear 6.7 rotate -35 #8.6
        linear 5.85 rotate -58 #14.45
        pause 10.8 rotate 1
        repeat

transform tr_blue_w1:
    align(0.5,0.5) alpha 0.0 xzoom 1 yzoom 1
    block:
        time 1.85
        linear 4.4 xzoom 1.3 yzoom 1.2 alpha 0.25 additive_blend
        linear 4.4 xzoom 1 yzoom 1 alpha 0.0 additive_blend
        time 52.82
        repeat

transform tr_blue_w2:
    align(0.5,0.5) alpha 0.0 xzoom 1 yzoom 1
    time 36.75
    linear 4.4 xzoom 1.3 yzoom 1.2 alpha 0.25 additive_blend
    linear 4.4 xzoom 1 yzoom 1 alpha 0.0 additive_blend
    
transform tr_orange_w1:
    align(0.5,0.5) alpha 0.0 xzoom 1 yzoom 1
    block:
        time 13.35
        linear 4.4 alpha 0.25 additive_blend
        linear 4.4 alpha 0.0 additive_blend
        time 64.2
        repeat

transform tr_orange_w2:
    align(0.5,0.5) alpha 0.0 xzoom 1 yzoom 1
    time 23.65
    linear 4.4 alpha 0.25 additive_blend
    linear 4.4 alpha 0.0 additive_blend

image bg walking= Fixed(
    pan_walking("walking"),
    sun1_walkingspin("sun1_walking"),
    sun2_walkingspin("sun2_walking"),
    sun3_walkingspin("sun3_walking"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_blue_w1("blue"),
    tr_blue_w2("blue"),
    tr_orange_w1("orange"),
    tr_orange_w2("orange"),
)



## Ch 7 ################################################################

image aura1 = WrapTiled("images/vfx/aura1.png", speed_x=0, speed_y=-300)
transform tr_aura1:
    alpha 0.4 additive_blend
image aura2 = WrapTiled("images/vfx/aura2.png", speed_x=0, speed_y=-200)
transform tr_aura2:
    alpha 0.5 additive_blend

image bg aura1= Fixed(
    ("classroom_window"),
    tr_aura2("aura2"),
    tr_aura1("aura1"),

)

image bg aura2= Fixed(
    ("classroom1"),
    tr_aura2("aura2"),
    tr_aura1("aura1"),
)

image aura3 = WrapTiled("images/vfx/aura3.png", speed_x=0, speed_y=-300)
image aura4 = WrapTiled("images/vfx/aura4.png", speed_x=0, speed_y=-200)

image bg aura3= Fixed(
    ("classroom1"),
    tr_aura2("aura3"),
    tr_aura1("aura4"),
)

image sparkle_radiate = Fixed(
    "sparkle2_0",
    "sparkle5_0",
    "sparklebig_0",
)

image sparkle_up = Fixed(
    "sparklebig2_0",
    "sparklebig3_0",
    "sparklebig4_0",
)

## Bad end

transform tr_yellowbul:
    align(0.5,0.5) alpha 0.0
    block:
        time 1
        linear 4.2 alpha 0.2 additive_blend
        linear 4.2 alpha 0.0 additive_blend
        repeat

transform pan_bul0:
    yalign 1.0
    linear 9.4 yalign 0.0

image bg bul0= Fixed(
    pan_bul0("bul0"),
    "dust0_0",
    "dust1_0",
    tr_yellowbul("yellow"),
)

transform pan_bul1:
    xpos -87 ypos -314
    linear 9.4 xpos -177 ypos -33

transform pan_bulrussia1:
    pos(-63,-206) xzoom 1.1 yzoom 1.1 rotate 0 rotate_pad False
    linear 9.4 pos(-123,-56) xzoom 1.2 yzoom 1.1 rotate 5 rotate_pad False

image bg bul1= Fixed(
    pan_bul1("bul1"),
    pan_bulrussia1("bulrussia"),
    "dust0_0",
    "dust1_0",
    tr_yellowbul("yellow"),
)

transform pan_bul2:
    xpos -122 ypos -11
    block:
        linear 10 xpos -100 ypos -64
        linear 10 xpos -122 ypos -11
        repeat

transform pan_bulrussia2:
    pos(-70,-35) xzoom 1.1 yzoom 1.1 rotate -1 rotate_pad False
    block:
        linear 10 pos(-49,-122) xzoom 1.2 yzoom 1.1 rotate 3 rotate_pad False
        linear 10 pos(-70,-35) xzoom 1.1 yzoom 1.1 rotate -1 rotate_pad False
        repeat

transform pan_bulshadow2:
    pos(-281, -581)
    block:
        linear 10 pos(-227, -237)
        linear 10 pos(-281, -581)
        repeat

transform tr_yellowbul2:
    align(0.5,0.5) alpha 0.0
    block:
        time 1
        linear 4.2 alpha 0.2 additive_blend
        linear 4.2 alpha 0.0 additive_blend
        time 11.6
        repeat

transform tr_orangebul:
    align(0.5,0.5) alpha 0.0
    block:
        time 11.2
        linear 4.2 alpha 0.35 additive_blend
        linear 4.2 alpha 0.0 additive_blend
        time 3.4
        repeat

image bulvfx= Fixed(
    pan_bulrussia2("bulrussia"),
    pan_bulshadow2("bulshadow"),
    "dust2_0",
    "dust0_0",
    "dust1_0",
    tr_yellowbul2("yellow"),
    tr_orangebul("orange"),
)

image bgbul 2 = "bul2"
image bgbul 3 = "bul3"
image bgbul 4 = "bul4"
image bgbul 5 = "bul5"

image staffroll = "gui/staffroll.png"