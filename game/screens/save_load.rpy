## Load and Save screens #######################################################
##
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

## Save game names based on BadMustard's code: https://www.badmustard.itch.io/renpy-save-game-names

screen save():
    modal True
    add "gui/menu_game/save.png":
        xpos 118
        ypos 150
    use file_slots("Save")

screen load():
    modal True
    add "gui/menu_game/load.png":
        xpos 118
        ypos 150
    use file_slots("Load")

screen file_slots(title):
    modal True
    
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

        viewport:
            style_prefix "slot"
            mousewheel True draggable True pagekeys True
            scrollbars "vertical"
            xpos 213
            ypos 243
            xsize 508
            ysize 178

            vbox:
                spacing 0

                for slot in range(1, file_slot_rows + 1):

                    button:
                        ysize 25
                        xsize 490
                        hovered ShowTransient("dynamic_preview", what=get_save_preview(slot))
                        unhovered Hide("dynamic_preview")
                        if renpy.get_screen("load"):
                            hover_background Solid("#c4e9ff80")
                        else:
                            hover_background Solid("#baffe480")
                        

                        if renpy.get_screen("save") and persistent.saveName:
                            action [Function(SetSaveName, slot), Show("savegameName", slot=slot, accept=FileSave(slot))]
                        elif renpy.get_screen("load") and FileLoadable(slot):
                            action Show("confirm", message=_("[slot:02d]番をロードします").replace("[slot:02d]", f"{slot:02d}"), yes_action=FileLoad(slot, confirm=False), no_action=Hide("confirm"))

                        else:
                            action [Function(SetSaveName, slot), FileAction(slot)]

                        hbox:
                            if FileNewest(slot):
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
                                if renpy.get_screen("load"):
                                    style "slot_load_text"
                                else:
                                    style "slot_save_text"
                            
                            null width 7

                            $ file_time = FileTime(slot, format=_("%m/%d  %H:%M"), empty="--/--  --:--") or "--/-- --:--"
                            text "[file_time]":
                                if renpy.get_screen("load"):
                                    style "slot_load_text"
                                else:
                                    style "slot_save_text"

                            null width 25
                            
                            text FileJson(slot, key="_save_name", empty=27*'-'):
                                if renpy.get_screen("load"):
                                    style "slot_load_text"
                                else:
                                    style "slot_save_text"
                            



define memo_text_size = 16

translate english python:
    memo_text_size = 12


screen savegameName(slot, accept=NullAction()):
    modal True
    zorder 200
    style_prefix "confirm_input"


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
        draggable True
        mousewheel "horizontal"
        input:
            id "save_name_input"
            default store.save_name or get_last_textline()
            changed scroll_input_with_caret
            length 27
            yalign 1.0
            xalign 0.0
            xsize None
            color "#000"

    timer 0.05 repeat True action Function(scroll_input_with_caret)

    hbox:
        xpos 307
        ypos 315  
        spacing 11
        textbutton _("OK"):
            action [accept, Hide("savegameName")]

        textbutton _("キャンセル"):
            action Hide("savegameName")


## Styles

style confirm_input_button is confirm_button
style confirm_input_button_text is confirm_button_text
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

## Python

init python:
    import string

    def get_last_textline():
        cleaned = renpy.filter_text_tags(store._last_raw_what, allow=[])
        cleaned = cleaned.strip()
        cleaned = "".join(ch for ch in cleaned if ch.isprintable())
        cleaned = cleaned[:13]
        return cleaned


    def get_save_preview(slot):
        if FileLoadable(slot):
            preview = FileScreenshot(slot)
            return TrackCursor(preview)
        else:
            return None

    def SetSaveName(slot):
        Namer(FileSaveName(slot))
    def Namer(name):
        if name:
            store.save_name = name
        else:
            store.save_name = get_last_textline()

init python:
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

    class TrackCursor(renpy.Displayable):
        def __init__(self, child):
            super(TrackCursor, self).__init__()
            self.child = renpy.displayable(child)
            self.x = None
            self.y = None

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
                renpy.redraw(self, 0)


