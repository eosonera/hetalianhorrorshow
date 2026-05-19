
default _pending_window_transform = None
default _pending_sprite_transform = None
default _pending_sound = None
default _pending_camera_transform = None
default _pending_stop_music = None
default _pending_music = None
default _pending_store_set = None

init python:
    def dialogue_callback(event, interact=True, **kwargs):
        if event == "begin":
            if store.window_transform is not None:
                store.window_transform = None
            if getattr(store, '_pending_clear_camera', False):
                renpy.layer_at_list([], layer="master")
                renpy.layer_at_list([], layer="screens")
                store._pending_clear_camera = False

        if event == "slow_done":

            # window transform
            if store._pending_window_transform:
                store.window_transform = store._pending_window_transform
                renpy.restart_interaction()
                store._pending_window_transform = None

            # sprite transform
            if store._pending_sprite_transform:
                for entry in store._pending_sprite_transform:
                    tag = entry[0]
                    at_list = entry[1]
                    transition = entry[2] if len(entry) > 2 else None

                    if not isinstance(at_list, list):
                        at_list = [at_list]

                    renpy.show(tag, at_list=at_list)

                    if transition:
                        renpy.transition(transition)

                renpy.restart_interaction()
                store._pending_sprite_transform = None

            # sound effect
            if store._pending_sound:
                sound, channel = store._pending_sound
                renpy.sound.play(sound, channel=channel)
                store._pending_sound = None

            # camera shake
            if store._pending_camera_transform:
                for transforms, layer in store._pending_camera_transform:
                    renpy.layer_at_list(transforms, layer=layer)
                renpy.restart_interaction()
                store._pending_camera_transform = None
                store._pending_clear_camera = True

            # music
            if store._pending_music:
                filename, fadein, fadeout = store._pending_music
                renpy.music.play(filename, fadein=fadein, fadeout=fadeout)
                store._pending_music = None

            # stop music
            if store._pending_stop_music is not None:
                fadeout = store._pending_stop_music
                renpy.music.stop(fadeout=fadeout)
                store._pending_stop_music = None

            # store variable assignments
            if store._pending_store_set:
                for var, value in store._pending_store_set:
                    setattr(store, var, value)
                renpy.restart_interaction()
                store._pending_store_set = None



## Characters ############################################################


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
    ctc_position="nestled",
    callback=dialogue_callback)

# narrator with normal text outlines
define na2 = Character(None,
    image="na2",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define story = Character(None,
    kind = nvl,
    ctc="ctc_arrow", #ctc_arrow
    ctc_position="nestled",
    callback=dialogue_callback)

define bul = Character("bulgaria",
    image="bulgaria",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define rom = Character("romania",
    image="romania",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define eng = Character("england",
    image="england",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define jpn = Character("japan",
    image="japan",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define ger = Character("germany",
    image="germany",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define fin = Character("finland",
    image="finland",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define ame = Character("america",
    image="america",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define spa = Character("spain",
    image="spain",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

define rus = Character("russia",
    image="russia",
    ctc="ctc_button",
    ctc_position="nestled",
    callback=dialogue_callback)

