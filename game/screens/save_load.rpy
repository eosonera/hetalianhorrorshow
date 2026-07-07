## Load and Save screens #######################################################
##
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

## Save game names based on BadMustard's code: https://www.badmustard.itch.io/renpy-save-game-names

if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("touch")):
    default persistent.saveName = True
    default persistent.savePreview = True
else:
    default persistent.saveName = False
    default persistent.savePreview = False

screen save():
    if gamemenu_open:
        modal False
    else:
        modal True
    add "gui/menu_game/save.png":
        xpos 118
        ypos 150
    use file_slots("Save")

screen load():
    if gamemenu_open:
        modal False
    else:
        modal True

    add "gui/menu_game/load.png":
        xpos 118
        ypos 150
    use file_slots("Load")

screen file_slots(title):
    if gamemenu_open:
        modal False
    else:
        modal True

    on "show" action [Function(invalidate_preview_cache), Function(build_slot_cache)]
    
    button:
        if main_menu:
            action Hide("load")
        else:
            action Return()
        background None
        xysize (900, 600)
        focus_mask None

    add "gui/scrollbar/scrollbar.png":
        xpos 702
        ypos 241

    frame:

        controller_viewport:
            style_prefix "slot"
            mousewheel True draggable renpy.variant("touch") pagekeys True
            scrollbars "vertical"
            id "saveload_viewport" vscroll_style "nudge"
            scroll_delay (0.2, 0.2)
            extra_scroll dict(up=-100, down=100)
            trap_focus ("up", "down", "left", "right")
            xpos 213
            ypos 243
            xsize 508
            ysize 178

            vbox:
                spacing 0

                $ is_load = bool(renpy.get_screen("load"))
                $ use_save_name = (renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("touch"))) and persistent.saveName
                $ show_save_preview = (renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("touch"))) and persistent.savePreview

                for slot in range(1, file_slot_rows + 1):

                    $ d = _slot_data_cache.get(slot, {
                        "time": "--/-- --:--",
                        "name": 27*'-',
                        "newest": False,
                        "loadable": False,
                    })

                    button:
                        ysize 25
                        xsize 460
                        hovered (ShowTransient("dynamic_preview", what=_preview_cache.get(slot)) if show_save_preview else None)
                        unhovered (Hide("dynamic_preview") if show_save_preview else None)
                        if is_load:
                            hover_background Solid("#c4e9ff80")
                        else:
                            hover_background Solid("#baffe480")
                        

                        if renpy.get_screen("save") and use_save_name:
                            action [Function(SetSaveName, slot), Show("savegameName", slot=slot, accept=FileSave(slot))]
                        elif renpy.get_screen("load") and FileLoadable(slot):
                            action Show("confirm",
                            message=renpy.translate_string("{slot:02d}番をロードします").format(slot=slot),
                            yes_action=FileLoad(slot, confirm=False), no_action=Hide("confirm"))

                        else:
                            action [
                                Function(SetSaveName, slot),
                                FileSave(slot),
                                Function(invalidate_preview_cache, slot),
                                Function(build_slot_cache),
                            ]


                        hbox:
                            if d["newest"]:
                                frame:
                                    xsize 32
                                    yoffset -6
                                    add "gui/button/check_0.png":
                                        at check_hover
                                        yalign 1
                            else:
                                null width 32
                                
                            null width 2

                            text "[slot:02d].":
                                if is_load:
                                    style "slot_load_text"
                                else:
                                    style "slot_save_text"
                            
                            null width 7

                            $ file_time = d["time"]
                            text "[file_time]":
                                if is_load:
                                    style "slot_load_text"
                                else:
                                    style "slot_save_text"

                            null width 25
                            
                            $ slot_name = d["name"]
                            text "[slot_name]":
                                if is_load:
                                    style "slot_load_text"
                                else:
                                    style "slot_save_text"
                                    
        vbar value YScrollValue("saveload_viewport") style 'slot_vscrollbar' keyboard_focus False:
            xpos 696
            ypos 243
                            



define memo_text_size = 16




screen savegameName(slot, accept=NullAction()):
    modal True
    zorder 200
    style_prefix "confirm_input"

    on "show" action Function(
        Namer,
        get_last_textline() if FileLoadable(slot) else (store.save_name or get_last_textline())
    )

    add "gui/menu_game/confirm_input.png":
        xpos 206
        ypos 192
    add "gui/menu_game/input.png":
        xpos 334
        ypos 290
        
    frame:
        xpos 290
        xsize 318
        ypos 260
        label _("[slot]番にセーブします"):
            style "confirm_input_prompt"
            xalign 0.5
            

    hbox:
        xpos 307
        ypos 315  
        spacing 11
        textbutton _("OK"):
            action [accept, Function(invalidate_preview_cache, slot), Function(build_slot_cache), Hide("savegameName")]
            keyboard_focus False

        textbutton _("キャンセル"):
            action Hide("savegameName")
            keyboard_focus False

    frame:
        xpos 292
        ypos 289
        ysize 28
        xsize 40
        text _("メモ"):
            color "#000"
            size memo_text_size
            yalign 0.5
            xalign 1.0
    
    viewport:
        id "save_name_vp"
        xpos 338
        ypos 291
        xsize 258
        ysize 28
        scrollbars "horizontal"
        draggable False
        mousewheel "horizontal"
        input:
            id "save_name_input"
            default (get_last_textline() if FileLoadable(slot) else (store.save_name or get_last_textline()))
            changed scroll_input_with_caret
            length 27
            yalign 1.0
            xalign 0.0
            xsize None
            color "#000"
            




## Styles

style confirm_input_button is confirm_button
style confirm_input_button_text is confirm_button_text
style confirm_input_button:
    background "gui/button/confirm_button_0.png"
    hover_background "gui/button/confirm_button_1.png"
    keyboard_focus False

style confirm_input_prompt_text is confirm_prompt_text
style confirm_input_prompt_text:
    color "#000"
    size 16


screen dynamic_preview(what):
    add what

style slot_save_text:
    size 16
    color "#fff"
    outlines [(1.2, "#597a87", 0, 0)]
    hover_color "#a6cfc1"
    hover_outlines [(1.2, "#fff", 0, 0)]

style slot_load_text:
    size 16
    color "#fff"
    outlines [(1.2, "#5b728e", 0, 0)]
    hover_color "#b8b8ff"
    hover_outlines [(1.2, "#fff", 0, 0)]

style slot_vscrollbar:
    xsize 25
    ysize 105
    yoffset 40
    thumb_offset 15
    thumb "gui/scrollbar/scrollbar_thumb.png"


define config.thumbnail_width = 270
define config.thumbnail_height = 180
define file_slot_rows = 50
define chars_in_savename = 13

## Python

init python:
    import string

    # Save game names

    # Get last textline and clean
    def get_last_textline():
        cleaned = renpy.filter_text_tags(store._last_raw_what, allow=[])
        cleaned = cleaned.strip()
        cleaned = "".join(ch for ch in cleaned if ch.isprintable())
        cleaned = cleaned[:chars_in_savename]
        return cleaned

    # Set save name
    def SetSaveName(slot):
        Namer(FileSaveName(slot))
    def Namer(name):
        if name:
            store.save_name = name
        else:
            store.save_name = get_last_textline()

init python:
    # Caret scroll
    def scroll_input_with_caret(new_text=None):
        if new_text is not None:
            Namer(new_text)
        scroll_to_caret()

    def scroll_to_caret():
        input_disp = renpy.get_widget("savegameName", "save_name_input")
        viewport_disp = renpy.get_widget("savegameName", "save_name_vp")

        if not input_disp or not viewport_disp:
            return

        caret_pos = getattr(input_disp, 'caret_pos', 0)
        avg_char_width = 12
        caret_px = caret_pos * avg_char_width
        vp_width = viewport_disp.width
        current_scroll = viewport_disp.xadjustment.value

        if caret_px < current_scroll:
            viewport_disp.xadjustment.value = max(0, caret_px - 10)
        elif caret_px > current_scroll + vp_width - avg_char_width:
            viewport_disp.xadjustment.value = caret_px - vp_width + avg_char_width + 10

init python:
    # Save preview
    _preview_cache = {}

    def get_save_preview(slot):
        if slot not in _preview_cache:
            if FileLoadable(slot):
                _preview_cache[slot] = TrackCursor(FileScreenshot(slot))
            else:
                _preview_cache[slot] = None
        return _preview_cache[slot]

    def invalidate_preview_cache(slot=None):
        if slot is None:
            _preview_cache.clear()
        else:
            _preview_cache.pop(slot, None)

    _slot_data_cache = {}

    def build_slot_cache():
        _slot_data_cache.clear()
        _preview_cache.clear()
        for slot in range(1, file_slot_rows + 1):
            loadable = FileLoadable(slot)
            _slot_data_cache[slot] = {
                "time":     FileTime(slot, format=_("%m/%d  %H:%M"), empty="--/--  --:--") or "--/-- --:--",
                "name":     FileJson(slot, key="_save_name", empty=27*'-'),
                "newest":   FileNewest(slot),
                "loadable": loadable,
            }
            if loadable:
                _preview_cache[slot] = TrackCursor(FileScreenshot(slot))
            else:
                _preview_cache[slot] = None



init python:

    class TrackCursor(renpy.Displayable):
        def __init__(self, child):
            super(TrackCursor, self).__init__()
            self.child = renpy.displayable(child)
            self.x = None
            self.y = None
            self._last_redraw = 0

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x, self.y + 20))
            return rv

        def event(self, ev, x, y, st):
            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                # Redraw screenshot every 60 fps
                if st - self._last_redraw > 0.016:
                    self._last_redraw = st
                    renpy.redraw(self, 0)


