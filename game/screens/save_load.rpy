## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 270
define config.thumbnail_height = 180
define file_slot_rows = 50

screen save():
    add "gui/save.png":
        xpos 118
        ypos 150
    use file_slots(_("Save"))

screen load():
    add "gui/load.png":
        xpos 118
        ypos 150
    use file_slots(_("Load"))

screen file_slots(title):
    
    frame:
        xpos 220
        ypos 245
        xsize 460
        ysize 180
        
        vbox:
            spacing 0
            
            viewport:
                mousewheel True draggable True pagekeys True
                scrollbars "vertical"
                
                vbox:
                    spacing 0
                    style_prefix "slot"
                    
                    for i in range(1, file_slot_rows + 1):
                        hbox:
                            spacing 0
                            
                            # Save slot button
                            button:
                                ysize 30
                                action FileAction(i)
                                hovered ShowTransient("save_preview", slot=i)
                                unhovered Hide("save_preview")
                                
                                hbox:
                                    
                                    # Save info
                                    vbox:
                                        
                                        text "[i:02d]. [FileTime(i, format=_('%m/%d %H:%M'), empty=_('--/-- --:--'))]":
                                            style "slot_text"
                                        
                                        text FileSaveName(i):
                                            style "slot_text"
                            
            
            # Close button at bottom
            textbutton _("Return"):
                xalign 1.0
                
                if main_menu:
                    pass
                else:
                    action Return()


screen save_preview(slot):
    if FileLoadable(slot):
        frame:
            xalign 1.0
            yalign 0.0            
            vbox:
                add FileScreenshot(slot):
                    size (config.thumbnail_width, config.thumbnail_height)

## Styles

style slot_text:
    color "#728f9b"
    size 22

