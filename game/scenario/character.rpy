## Characters ############################################################


#define fadeWithText = { "master" : Dissolve(1.0) }

define name_map = {
    "bulgaria": ("ブルガリア"),
    "romania": ("ルーマニア"),
    "england": ("イギリス"),
    "japan": ("日本"),
    "germany": ("ドイツ"),
    "finland": ("フィンランド"),
    "america": ("アメリカ"),
    "spain": ("スペイン"),
    "russia": ("ロシア"),
}

# narrator with blue text outlines
define na = Character(None,
    screen='narrator',
    what_color="#763931",
    what_outlines=[( 0.9, "#D1EBED", 0, 0 )],
    ctc="ctc_button",
    ctc_position="nestled",)

# narrator with normal text outlines
define na2 = Character(None,
    image="na2",
    ctc="ctc_button",
    ctc_position="nestled")

define story = Character(None,
    kind = nvl,
    ctc="ctc_button", #ctc_arrow
    ctc_position="nestled",)

define bul = Character("bulgaria",
    image="bulgaria",
    ctc="ctc_button",
    ctc_position="nestled")

define rom = Character("romania",
    image="romania",
    ctc="ctc_button",
    ctc_position="nestled")

define eng = Character("england",
    image="england",
    ctc="ctc_button",
    ctc_position="nestled")

define jpn = Character("japan",
    image="japan",
    ctc="ctc_button",
    ctc_position="nestled")

define ger = Character("germany",
    image="germany",
    ctc="ctc_button",
    ctc_position="nestled")

define fin = Character("finland",
    image="finland",
    ctc="ctc_button",
    ctc_position="nestled")

define ame = Character("america",
    image="america",
    ctc="ctc_button",
    ctc_position="nestled")

define spa = Character("spain",
    image="spain",
    ctc="ctc_button",
    ctc_position="nestled")

define rus = Character("russia",
    image="russia",
    ctc="ctc_button",
    ctc_position="nestled")