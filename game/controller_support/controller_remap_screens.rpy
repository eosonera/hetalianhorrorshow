# ################################################################################
# ##
# ## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
# ## v1.0
# ##
# ################################################################################
# ## This file contains code for the screens relating to remapping gamepad
# ## controls. It overrides some of the screens from 00gamepad.rpy so you can
# ## restyle them however you like.
# ##
# ## For more information and examples, see the tools section on my website:
# ## https://feniksdev.com/tool/remapping-controls/
# ## If you use this code in your projects, credit me as Feniks @ feniksdev.com
# ##
# ## Leave a comment on the tool page on itch.io if you run into any issues.
# ################################################################################
# ## SCREENS
# ################################################################################
# ## Modified from 00gamepad.rpy so you can update the styling however you like.
# ## This is the screen that's shown when the GamepadCalibrate() action is called.
# ## It allows the player to select which gamepad they want to calibrate.
# screen _gamepad_select(joysticks):

#     modal True
#     style_prefix "gamepad1"

#     add "#292835"

#     frame:
#         has vbox

#         label _("Select Gamepad to Calibrate")

#         if not joysticks:
#             text _("No Gamepads Available")
#         else:
#             for i, name in joysticks:
#                 textbutton "[i]: [name]" action Return(i) size_group "joysticks":
#                     if i == 0:
#                         default_focus 10

#         null height 20

#         icon_button caption _("Cancel") kind icn.back:
#             action Return("cancel") suffix "small"

# style gamepad1_frame:
#     background "#21212d"
#     padding (50, 50)
#     align (0.5, 0.5)

# style gamepad1_button:
#     #background Frame("gui/menu_game/about.png", 5, 5)
#     padding (15, 15)

# ################################################################################
# ## Modified from 00gamepad.rpy so you can update the styling however you like.
# ## This is the screen that's shown to the player when they are calibrating
# ## their gamepad. It asks them to press or move the various gamepad buttons.
# init python in pad_remap:
#     ## These are the descriptions this screen shows the player to ask them to
#     ## move or press the different gamepad buttons.
#     ## I find the default descriptions for remapping controllers are
#     ## ugly, so you can replace them here.
#     REMAP_DESCRIPTIONS = [
#         ## a
#         _("Press or move the {image=pad_a_small}{alt}a{/alt} button."),
#         ## b
#         _("Press or move the {image=pad_b_small}{alt}b{/alt} button."),
#         ## x
#         _("Press or move the {image=pad_x_small}{alt}x{/alt} button."),
#         ## y
#         _("Press or move the {image=pad_y_small}{alt}y{/alt} button."),
#         ## back
#         _("Press or move the {image=pad_select_small}{alt}select{/alt} button."),
#         ## guide
#         _("Press or move the {image=pad_home_small}{alt}home{/alt} button."),
#         ## start
#         _("Press or move the {image=pad_start_small}{alt}start{/alt} button."),
#         ## leftstick
#         _("Click the {image=pad_l3_small} left stick."),
#         ## rightstick
#         _("Click the {image=pad_r3_small} right stick."),
#         ## leftshoulder
#         _("Press or move the {image=pad_l1_small}{alt}left shoulder{/alt} button."),
#         ## rightshoulder
#         _("Press or move the {image=pad_r1_small}{alt}right shoulder{/alt} button."),
#         ## dpup
#         _("Press or move the {image=pad_up_small} d-pad up."),
#         ## dpdown
#         _("Press or move the {image=pad_down_small} d-pad down."),
#         ## dpleft
#         _("Press or move the {image=pad_left_small} d-pad left."),
#         ## dpright
#         _("Press or move the {image=pad_right_small} d-pad right."),
#         ## leftx
#         _("Move the {image=pad_left_stick_small} left stick to the left or right."),
#         ## lefty
#         _("Move the {image=pad_left_stick_small} left stick up or down."),
#         ## rightx
#         _("Move the {image=pad_right_stick_small} right stick to the left or right."),
#         ## righty
#         _("Move the {image=pad_right_stick_small} right stick up or down."),
#         ## lefttrigger
#         _("Press or move the {image=pad_l2_small}{alt}left trigger{/alt} button."),
#         ## righttrigger
#         _("Press or move the {image=pad_r2_small}{alt}right trigger{/alt} button."),
#     ]
# ################################################################################
# ## name - The name of the gamepad the player is updating
# ## control - The control the player is updating
# ## kind - The variant on the control the player is updating (e.g. it'll say
# ##      "Press or move the 'a' button" - control is 'a' and kind is 'button').
# ## mappings - A dictionary used by Ren'Py to know how to map the gamepad
# ##      controls to the game controls. You won't adjust this.
# ## i - The current index of the control the player is updating
# ## total - The total number of controls the player will update
# ################################################################################
# screen _gamepad_control(name, control, kind, mappings, back, i, total):

#     modal True
#     style_group "calibrate"

#     add "#292835"

#     hbox:
#         align (0.5, 0.5) spacing 80
#         frame:
#             has vbox
#             align (0.5, 0.5)

#             label _("Calibrating [name]\n([i]/[total])") xalign 0.5:
#                 text_text_align 0.5

#             null height 20

#             ####################################################
#             ## This is the default display text for calibration
#             # text _("Press or move the '[control!s]' [kind].")
#             ####################################################
#             ## This uses the descriptions from earlier instead.
#             text pad_remap.REMAP_DESCRIPTIONS[i-1] xalign 0.5
#             ####################################################

#             null height 20

#             hbox:
#                 xalign 0.5 spacing 10

#                 if len(mappings) >= 4:
#                     textbutton _("Cancel {image=pad_x_small}{alt}X{/alt}"):
#                         action Return("cancel")

#                 if len(mappings) >= 3:
#                     textbutton _("Skip {image=pad_a_small}{alt}A{/alt}") action Return("skip")

#                 if back and len(mappings) >= 3:
#                     textbutton _("Back {image=pad_b_small}{alt}B{/alt}") action Return(back)

#         ########################################################################
#         ## This is a personal touch; show which buttons have been calibrated
#         ## so far.
#         vbox:
#             spacing 50
#             hbox:
#                 spacing 550 xalign 0.5
#                 vbox:
#                     add 'pad_l2' alpha (1.0 if i > 20 else 0.2)
#                     add 'pad_l1' alpha (1.0 if i > 10 else 0.2)
#                 vbox:
#                     add 'pad_r2' alpha (1.0 if i > 21 else 0.2)
#                     add 'pad_r1' alpha (1.0 if i > 11 else 0.2)
#             hbox:
#                 spacing 50
#                 add Image("{}/button_dpad.{}".format(pad_config.ICON_FOLDER,
#                         pad_config.ICON_EXTENSION), dpi=400):
#                     alpha (1.0 if i > 15 else 0.2)
#                 vbox:
#                     yalign 0.5
#                     hbox:
#                         add 'pad_select' alpha (1.0 if i > 5 else 0.2)
#                         null width 75
#                         add 'pad_start' alpha (1.0 if i > 7 else 0.2)
#                     null height 30
#                     add 'pad_home' xalign 0.5 alpha (1.0 if i > 6 else 0.2)
#                     null height 0
#                     hbox:
#                         xalign 0.5 spacing 140
#                         vbox:
#                             add 'pad_l3' alpha (1.0 if i > 8 else 0.2)
#                             add 'pad_left_stick'  alpha (1.0 if i > 17 else 0.2)
#                         vbox:
#                             add 'pad_r3' alpha (1.0 if i > 9 else 0.2)
#                             add 'pad_right_stick' alpha (1.0 if i > 19 else 0.2)
#                 vbox:
#                     if persistent.controller_layout == "nintendo":
#                         add "pad_x" xalign 0.5 alpha (1.0 if i > 3 else 0.2)
#                         hbox:
#                             add "pad_y" alpha (1.0 if i > 4 else 0.2)
#                             null width 75
#                             add "pad_a"  alpha (1.0 if i > 1 else 0.2)
#                         add "pad_b" xalign 0.5 alpha (1.0 if i > 2 else 0.2)
#                     else:
#                         add "pad_y" xalign 0.5  alpha (1.0 if i > 4 else 0.2)
#                         hbox:
#                             add "pad_x" alpha (1.0 if i > 3 else 0.2)
#                             null width 75
#                             add "pad_b" alpha (1.0 if i > 2 else 0.2)
#                         add "pad_a" xalign 0.5 alpha (1.0 if i > 1 else 0.2)
#         ########################################################################

#     ## This is required; do not remove. Keep it at the bottom of the screen.
#     ## If the listener doesn't catch it, we want to ignore it
#     key pad_remap.ALL_EVENTS action NullAction()
#     ## Provided by Ren'Py to get the events
#     add _gamepad.EventWatcher(mappings)
#     ## Allow a shortcut for cancelling
#     key "pad_x_press" action If(len(mappings) >= 4, Return("cancel"))

# style calibrate_frame:
#     align (0.5, 0.5)
#     padding (50, 50)
#     xsize 700
#     background "#21212d"
# style calibrate_hbox:
#     spacing 25
# style calibrate_vbox:
#     spacing 25
# style calibrate_button_text:
#     color "#FFF"
#     size gui.text_size
# style calibrate_text:
#     color "#FFF"
#     size gui.text_size


# ################################################################################
# ## SCREENS
# ################################################################################
# ## A small screen which is shown on top of the controller remap screen to
# ## prompt the player to press a button for remapping. Can be restyled however
# ## you like, but keep the arguments and general actions the same.
# screen listen_remap(title, which_key, remapper):
#     modal True
#     dismiss action NullAction()
#     ###################################################
#     ## Free to modify below here
#     add "#0008"
#     frame:
#         background "#21212d" padding (50, 50) align (0.5, 0.5)
#         text _("Press the button you want to remap to [title!t].")
#     ## Keep the rest below here as-is
#     ###################################################
#     add pad_remap.RemapKey(which_key, remapper)
#     on 'hide' action Function(pad_config.manage_focus)

# ## A screen for remapping gamepad bindings. You may restyle this however
# ## you like. You should keep the underlay and vp_yadj arguments as-is.
# default remapper = pad_remap.ControllerRemap()
# screen controller_remap(underlay=False, vp_yadj=None):
#     tag menu

#     ####################################################################
#     ## Keep these so the listen_remap screen can be displayed on top of
#     ## this one.
#     sensitive not underlay
#     default yadj = vp_yadj or ui.adjustment()
#     ## And keep this so it can do the remapping
#     ####################################################################

#     add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

#     ## default_focus is a bit finicky here due to the remapping screen
#     ## being shown on top of this one, so the on show/replace actions
#     ## ensure it's set up when it's initially shown.
#     if not underlay:
#         on 'show' action If(not pad_config.is_using_mouse(), SetFocus("controller_remap", "calibrate"))
#         on 'replace' action If(not pad_config.is_using_mouse(), SetFocus("controller_remap", "calibrate"))

#     use game_menu(_("Controls"), can_focus=False, show_footer=False)

#     vbox:
#         xpos 400 ypos 120
#         side 'c r':
#             controller_viewport:
#                 xysize (900, 820)
#                 mousewheel True
#                 vscroll_style 'center'
#                 shortcuts True
#                 id 'controller_remap_viewport'
#                 yadjustment yadj
#                 has vbox
#                 style_prefix "controller_remap"
#                 spacing 10
#                 ## Some extra options here
#                 textbutton _("Calibrate Gamepad Buttons"):
#                     style_prefix 'remap_extra' id 'calibrate'
#                     action GamepadCalibrate()
#                 textbutton _("Change Icon Set"):
#                     style_prefix 'remap_extra'
#                     action CycleControllerLayout()
#                 for title, act, p in pad_remap.REMAPPABLE_EVENTS:
#                     hbox:
#                         spacing 20
#                         label title
#                         $ pad_images = pad_remap.get_images(act, remapper.get_current_bindings())
#                         grid 3 1:
#                             spacing 10
#                             for i, img in enumerate(pad_images):
#                                 imagebutton:
#                                     xysize (80, 80)
#                                     id "{}_{}".format(act, i)
#                                     background "#292835"
#                                     idle Transform(img[0], xysize=(80, 80))
#                                     hover_foreground "#f003"
#                                     action [Function(remapper.remove_button, img[1], act),
#                                         If((act not in pad_remap.REQUIRED_EVENTS
#                                                 or len(pad_images) > 1), None,
#                                         Function(renpy.call_in_new_context,
#                                             "listen_for_remap", title, act, yadj,
#                                             remapper))]
#                             for i in range(3 - len(pad_images)):
#                                 textbutton _("+{#remap new controller button}"):
#                                     yalign 0.5 xysize (80, 80)
#                                     id "{}_{}".format(act, i+len(pad_images))
#                                     text_align (0.5, 0.5)
#                                     background "#292835" text_hover_color "#21212d"
#                                     hover_background "#ff8335"
#                                     action Function(renpy.call_in_new_context,
#                                         "listen_for_remap", title, act, yadj,
#                                         remapper)
#             vbar value YScrollValue("controller_remap_viewport") keyboard_focus False

#     $ missing_events = remapper.get_missing_events_text()
#     if missing_events:
#         vbox:
#             yalign 0.5 xanchor 1.0 xpos 0.97 xsize 420
#             label _("Warning: Control set is not currently valid")
#             text _("The following events are missing:")
#             for mis_ev in missing_events:
#                 text "[mis_ev]" xalign 0.5

#     use key_footer():
#         ## This button resets the controller bindings to the default.
#         icon_button kind icn.reset caption _("Reset to Defaults"):
#             action CConfirm(_("Are you sure you want to reset the controller bindings to the default?"),
#                 Function(pad_remap.reset_to_default, remapper))
#             suffix "small"
#         icon_button kind icn.back action ShowMenu("help") suffix "small"
#         icon_button kind icn.select suffix "small"

#     ## Once this screen is hidden, we don't want to remember where the cursor
#     ## was. We also need to finalize the keymap, if it's valid.
#     on 'hide' action [Function(pad_config.clear_managed_focus, "controller_remap"),
#         Function(remapper.finalize_keymap)]
#     on 'replace' action [Function(pad_config.clear_managed_focus, "controller_remap"),
#         Function(remapper.finalize_keymap)]

# style remap_extra_button:
#     #hover_background Frame("gui/frame.png", 5, 5)
#     padding (15, 15)
#     xalign 1.0
# style controller_remap_label:
#     size_group 'ctrl_title' ysize 80
# style controller_remap_label_text:
#     yalign 0.5 xalign 1.0 text_align 1.0