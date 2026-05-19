################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for a declaring controller icons in Ren'Py. These
## icons automatically change to suit the current controller layout, and can
## be manually changed by the player. The icons can be used in screens to
## clarify which buttons to press.
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## For more information and examples, check out the tools section on my website:
## https://feniksdev.com/tool/controller-and-keyboard-icons/
##
## These icons are slightly modified from:
## https://mrbreakfastsdelight.itch.io/mr-breakfasts-free-prompts
## They are licensed under CC0 1.0 Universal. The GitHub repository can also
## be found here: https://github.com/mr-breakfast/mrbreakfasts_free_prompts
## Leave a comment on the tool page on itch.io if you run into any issues.
##
## Tip: If you'd like to update the icons to suit your own colour scheme (e.g.
## changing out the orange on the d-pad icons to something else), you can just
## edit the colour code directly in a code editor by opening the svg file as if
## it were a text file. The colour you're replacing is #ff8335.
################################################################################
init python:
    ############################################################################
    ## UI IMAGE FUNCTIONS
    ############################################################################
    def controller_icon(name, colors=pad_config.ICON_COLOR_TYPE, layout=None):
        """
        Returns an image of a controller button based on the current layout.

        name: The name of the button. One of:
            a, b, x, y, l1, r1, l2, r2, select, start, up, down, left, right,
            left_stick, right_stick, l3, r3
        colors: The number of colors to use. Default is 2. Valid values are 1,
            2, and 3. 1 is no colour. 2 is full colour. 3 is text colour only.
        layout : str
            If provided, one of "xbox", "playstation", "nintendo", "steam",
            or "generic". If not provided, the persistent layout is used.
        """
        ## The path where the images are. You may update these values (the
        ## pad_config ones - they're used in more than one place) if needed.
        path = pad_config.ICON_FOLDER
        ext = pad_config.ICON_EXTENSION

        if layout is None:
            layout = persistent.controller_layout
        ## Possible controller schemes:
        ## xbox, nintendo, playstation, steam, generic
        name = name.lower()
        ## We reuse the same buttons for the sticks/directions
        if name in ["up", "down", "left", "right"]:
            return "{}/button_dpad_{}.{}".format(path, name, ext)
        elif name == "left_stick":
            return "{}/left_stick.{}".format(path, ext)
        elif name == "right_stick":
            return "{}/right_stick.{}".format(path, ext)
        elif name in ("l3", "r3"):
            return "{}/button_{}.{}".format(path, name, ext)

        if layout == "playstation":
            ## Playstation has its own buttons.
            if name in ["a", "b", "x", "y"]:
                return "{}/button_ps_{}{}.{}".format(path, name, colors, ext)
            elif name in ["l1", "r1", "l2", "r2", "select", "start"]:
                return "{}/button_ps_{}.{}".format(path, name, ext)

        elif layout == "nintendo":
            if name in ["l1", "r1", "l2", "r2", "select", "start"]:
                return "{}/button_switch_{}.{}".format(path, name, ext)

        elif layout == "steam":
            if name in ["l1", "r1", "l2", "r2", "select", "start", "home"]:
                return "{}/button_steam_{}.{}".format(path, name, ext)

        elif layout == "xbox":
            if name in ["a", "b", "x", "y"]:
                return "{}/button_{}{}.{}".format(path, name, colors, ext)

        ## Generic controller.
        if name in ["a", "b", "x", "y"]:
            return "{}/button_{}1.{}".format(path, name, ext)
        elif name in ["l1", "r1", "l2", "r2", "home"]:
            return "{}/button_{}.{}".format(path, name, ext)
        elif name in ["select", "start"]:
            return "{}/button_generic_{}.{}".format(path, name, ext)

        return Null()

    def get_pad_image(name, oversample=1, box_size=None,
            colors=pad_config.ICON_COLOR_TYPE):
        """
        A function which returns a ConditionSwitch which picks the correct
        controller icon image, sized to center the icon at the given DPI.

        Arguments:
        ----------
        name : str
            Passed off to controller_icon to get the correct icon image. See
            above for valid values.
        oversample : float
            Can be used to shrink the image. Passed as the oversample value
            for the image.
        colors : int
            As for controller_icon. Default is 2. 1 is no colour, 2 is full
            colour, and 3 colours only the text or symbol. This applies only
            to the PlayStation and Xbox icons.
        box_size : int
            The size of the "box" containing the icon, so all icons are the
            same size and centered. If None, this uses DEFAULT_ICON_SIZE from
            pad_config and oversample to determine the correct value.

        Other Parameters:
        -----------------
        dpi : int
            The DPI for this image. Default is 150 - feel free to change this
            to a default that makes sense for your project or images. This uses
            DEFAULT_DPI from pad_config.
        """

        dpi = pad_config.DEFAULT_DPI or 96

        if box_size is None:
            box_size = int(-(-pad_config.DEFAULT_ICON_SIZE / float(oversample)))

        def get_box(layout):
            img = controller_icon(name, colors, layout)
            return Fixed(Image(img, dpi=dpi, oversample=oversample,
                align=(0.5, 0.5)), xysize=(box_size, box_size))

        return ConditionSwitch(
            "persistent.controller_layout == 'xbox'", get_box("xbox"),
            "persistent.controller_layout == 'playstation'", get_box("playstation"),
            "persistent.controller_layout == 'nintendo'", get_box("nintendo"),
            "persistent.controller_layout == 'steam'", get_box("steam"),
            "True", get_box("generic")
        )

    def get_button_text(name, include_colors=False):
        """
        Return a text-only name of a button, based on the active controller
        layout. Optionally, include colouring for the text (for PlayStation
        and Xbox only).
        This function expects the following names:
            A, B, X, Y
            L1 - left bumper/shoulder
            R1 - right bumper/shoulder
            L2 - left trigger
            R2 - right trigger
        So, get_button_text("L2") will return "L2" for PlayStation, Steam, and
        generic controller layouts, "LT" for Xbox, and "ZL" for Nintendo.
        """
        from pad_config import XBOX_A_COLOR, XBOX_B_COLOR, XBOX_X_COLOR, XBOX_Y_COLOR
        from pad_config import PS_X_COLOR, PS_O_COLOR, PS_SQUARE_COLOR, PS_TRIANGLE_COLOR

        c1 = ""
        if include_colors:
            c2 = "{/color}"
        else:
            c2 = ""
        if name == "R1":
            if persistent.controller_layout == "nintendo":
                return "R"
            elif persistent.controller_layout == "xbox":
                return "RB"
            else:
                return "R1"
        elif name == "L1":
            if persistent.controller_layout == "nintendo":
                return "L"
            elif persistent.controller_layout == "xbox":
                return "LB"
            else:
                return "L1"
        elif name == "R2":
            if persistent.controller_layout == "nintendo":
                return "ZR"
            elif persistent.controller_layout == "xbox":
                return "RT"
            else:
                return "R2"
        elif name == "L2":
            if persistent.controller_layout == "nintendo":
                return "ZL"
            elif persistent.controller_layout == "xbox":
                return "LT"
            else:
                return "L2"
        elif name == "A":
            if persistent.controller_layout in ("playstation", "ps4"):
                if include_colors:
                    c1 = "{color=" + PS_X_COLOR + "}"
                return c1+"{font=DejaVuSans.ttf}✖{/font}"+c2
            else:
                if include_colors:
                    c1 = "{color=" + XBOX_A_COLOR + "}"
                return c1+"A"+c2
        elif name == "B":
            if persistent.controller_layout in ("playstation", "ps4"):
                if include_colors:
                    c1 = "{color=" + PS_O_COLOR + "}"
                return c1+"{font=DejaVuSans.ttf}○{/font}"+c2
            else:
                if include_colors and persistent.controller_layout == "xbox":
                    c1 = "{color=" + XBOX_B_COLOR + "}"
                return c1+"B"+c2
        elif name == "X":
            if persistent.controller_layout in ("playstation", "ps4"):
                if include_colors:
                    c1 = "{color=" + PS_SQUARE_COLOR + "}"
                return c1+"{font=DejaVuSans.ttf}□{/font}"+c2
            else:
                if include_colors and persistent.controller_layout == "xbox":
                    c1 = "{color=" + XBOX_X_COLOR + "}"
                return c1+"X"+c2
        elif name == "Y":
            if persistent.controller_layout in ("playstation", "ps4"):
                if include_colors:
                    c1 = "{color=" + PS_TRIANGLE_COLOR + "}"
                return c1+"{font=DejaVuSans.ttf}△{/font}"+c2
            else:
                if include_colors and persistent.controller_layout == "xbox":
                    c1 = "{color=" + XBOX_Y_COLOR + "}"
                return c1+"Y"+c2
        return name

    def declare_mkb_icons():
        files = renpy.list_files()

        def get_box(img, oversample, box_size):
            return Fixed(Image(img, dpi=dpi, oversample=oversample,
                align=(0.5, 0.5)), xysize=(box_size, box_size))
        dpi = pad_config.DEFAULT_DPI or 96

        for f in files:
            if f.startswith(pad_config.ICON_FOLDER):
                ## Get the name of the file without the folder or extension
                name = f.split("/")[-1].split(".")[0]
                if not name.startswith("mouse_") and not name.startswith("key_"):
                    ## It's a controller icon
                    continue
                box_size = pad_config.DEFAULT_ICON_SIZE
                oversample = 1.0
                ## Some special cases for extra-big keys
                if name in ("key_enter", "key_tab", "key_shift", "key_ctrl",
                        "key_space", "key_pgup", "key_pgdn"):
                    if name in ("key_tab", "key_enter"):
                        mult = 1.4
                    else:
                        mult = 1.8
                    if name in ("key_enter",):
                        oversample *= 1.4
                    ## Declare a regular sized version
                    renpy.image(name, Fixed(Image(f, dpi=dpi,
                        oversample=oversample, align=(0.5, 0.5)),
                        xysize=(int(box_size*mult), box_size)))
                    ## Declare the 1.6x smaller version
                    oversample = 1.6
                    if name in ("key_enter",):
                        oversample *= 1.4
                    renpy.image(name+"_small", Fixed(Image(f, dpi=dpi,
                        oversample=oversample, align=(0.5, 0.5)),
                        xysize=(int(box_size / oversample * mult), int(box_size / oversample))))
                else:
                    ## Declare a regular sized version
                    renpy.image(name, get_box(f, oversample, box_size))
                    ## Declare the 1.6x smaller version
                    oversample = 1.6
                    renpy.image(name+"_small", get_box(f, oversample, int(box_size / oversample)))

    declare_mkb_icons()

    class FocusTypeDisplayable(renpy.Displayable):
        """
        A special displayable which changes based on the current focus type.
        """
        def __init__(self, mouse_img=None, keyboard_img=None, controller_img=None):
            self.mouse_img = renpy.displayable(mouse_img or Null())
            self.keyboard_img = renpy.displayable(keyboard_img or Null())
            self.controller_img = renpy.displayable(controller_img or Null())
            super(FocusTypeDisplayable, self).__init__()
            ## Register this image to be redrawn when switching between mouse
            ## and keyboard and controller
            pad_config.register_redrawable(self)
        def render(self, width, height, st, at):
            if pad_config.is_using_mouse():
                return self.mouse_img.render(width, height, st, at)
            elif pad_config.is_using_keyboard():
                return self.keyboard_img.render(width, height, st, at)
            elif pad_config.is_using_controller():
                return self.controller_img.render(width, height, st, at)
            return renpy.Render(width, height)


    ############################################################################
    ## ICON-RELATED ACTIONS
    ############################################################################
    # from renpy.display.controller import controllers as renpy_controllers

    class CycleControllerLayout(Action):
        """
        A screen action which cycles through the controller layouts.
        """
        layouts = ["generic", "xbox", "playstation", "nintendo", "steam"]
        def __init__(self, reverse=False):
            self.reverse = reverse
            super(CycleControllerLayout, self).__init__()
        def get_sensitive(self):
            return GamepadExists()
        def __call__(self):
            idx = self.layouts.index(persistent.controller_layout)
            if self.reverse:
                idx -= 1
            else:
                idx += 1
            persistent.controller_layout = self.layouts[idx % len(self.layouts)]
            ## Save this new layout to the controller, if it exists.
            if renpy_controllers:
                for c in renpy_controllers:
                    guid = renpy_controllers[c].get_guid_string()
                    persistent.controller_guid_to_type[guid] = persistent.controller_layout
            renpy.store.pad_config.refresh_redrawables(0, 1, None, force=True)
            renpy.restart_interaction()


    class SetControllerLayout(CycleControllerLayout):
        """
        A screen action which sets the controller layout directly.
        """
        def __init__(self, layout):
            self.layout = layout
            if layout not in self.layouts:
                renpy.error("Invalid controller layout: {}".format(layout))
            super(SetControllerLayout, self).__init__()
        def __call__(self):
            persistent.controller_layout = self.layout
            ## Save this new layout to the controller.
            if renpy_controllers:
                for c in renpy_controllers:
                    guid = renpy_controllers[c].get_guid_string()
                    persistent.controller_guid_to_type[guid] = persistent.controller_layout
            renpy.store.pad_config.refresh_redrawables(0, 1, None, force=True)
            renpy.restart_interaction()

    class MenuReturn(Return):
        """
        A class which manages the return action for the game menu.
        It handles focus and input types.
        """
        def __call__(self):
            if main_menu or renpy.get_screen("game_menu"):
                pad_config.clear_managed_focus("game_menu")
                return super(MenuReturn, self).__call__()
            else:
                renpy.run(ShowMenu("game_menu", can_focus=True))


################################################################################
## UI IMAGES
################################################################################
## Standard size, for remapping or otherwise shrinking down. ConditionSwitch
## allows them to update in real-time if the player changes the controller
## layout.
image pad_left = get_pad_image("left")
image pad_right = get_pad_image("right")
image pad_up = get_pad_image("up")
image pad_down = get_pad_image("down")
image pad_a = get_pad_image("a")
image pad_b = get_pad_image("b")
image pad_x = get_pad_image("x")
image pad_y = get_pad_image("y")
image pad_l1 = get_pad_image("l1")
image pad_r1 = get_pad_image("r1")
image pad_l2 = get_pad_image("l2")
image pad_r2 = get_pad_image("r2")
image pad_select = get_pad_image("select")
image pad_start = get_pad_image("start")
image pad_home = get_pad_image("home")
image pad_left_stick = get_pad_image("left_stick")
image pad_right_stick = get_pad_image("right_stick")
image pad_l3 = get_pad_image("l3")
image pad_r3 = get_pad_image("r3")

## Smaller size, useful for inline UI alongside text for tooltips or buttons.
image pad_left_small = get_pad_image("left", oversample=1.6)
image pad_right_small = get_pad_image("right", oversample=1.6)
image pad_up_small = get_pad_image("up", oversample=1.6)
image pad_down_small = get_pad_image("down", oversample=1.6)
image pad_a_small = get_pad_image("a", oversample=1.6)
image pad_b_small = get_pad_image("b", oversample=1.6)
image pad_x_small = get_pad_image("x", oversample=1.6)
image pad_y_small = get_pad_image("y", oversample=1.6)
image pad_l1_small = get_pad_image("l1", oversample=1.6)
image pad_r1_small = get_pad_image("r1", oversample=1.6)
image pad_l2_small = get_pad_image("l2", oversample=1.6)
image pad_r2_small = get_pad_image("r2", oversample=1.6)
image pad_select_small = get_pad_image("select", oversample=1.6)
image pad_start_small = get_pad_image("start", oversample=1.6)
image pad_home_small = get_pad_image("home", oversample=1.6)
image pad_left_stick_small = get_pad_image("left_stick", oversample=1.6)
image pad_right_stick_small = get_pad_image("right_stick", oversample=1.6)
image pad_l3_small = get_pad_image("l3", oversample=1.6)
image pad_r3_small = get_pad_image("r3", oversample=1.6)

## A special mouse + keyboard icon that changes when the input type
## does without requiring a screen refresh.
image mkb_select = FocusTypeDisplayable("mouse_left", "key_enter")
image mkb_select_small = FocusTypeDisplayable("mouse_left_small", "key_enter_small")

style icon_button:
    #hover_background Frame("gui/frame.png", 5, 5)
    padding (10, 10)
style icon_button_hbox:
    spacing 12
style icon_button_text:
    yalign 0.5
    insensitive_color "#888"

## These are special IconButton displayables, meant to be inherited when using
## the icon_button displayable in screens. The arguments are as follows:
## pad_event : str
##      This should be an event as found in persistent.pad_bindings
##      e.g. "screenshot", "button_select"
##      May also be a custom event as added via add_custom_event
##      This is the event that will be used for gamepads.
## key_event : str or list
##      This is an event or list of events as could be provided as a keysym
##      or similar. So, it can be something like ['K_LCTRL', 'K_RCTRL'] or
##      just "skip". See https://www.renpy.org/doc/html/keymap.html
##      This is the event that will be used for mouse & keyboard.
## caption : str
##      The text to display on the button. If icon_only is True (see below),
##      this is still used for the alt text of the button.
## mkb_icon : str
##      A string name of a declared image to use for the mouse and keyboard
##      icons. This may be a FocusTypeDisplayable as seen below, or a regular
##      key_image. Pad images are declared earlier in this file, and keyboard
##      images are declared automatically if found in pad_config.ICON_FOLDER
##     with the prefix "key_".
## action : Action
##      The action to perform when the appropriate button/key is pressed (or the
##      on-screen button is clicked). Often included in the screen directly
##      but not in the declarations here since they're situation-dependant.
## activate_sound : str
##      If provided, pressing the appropriate button will play this sound.
## kind : IconButton
##      IconButtons can inherit from each other. This is intended to make it
##      easy to create icons with very similar properties while changing a thing
##      or two like the caption or action.
## use_keysym : bool
##      If True, the default, the generated icon button will listen for the
##      provided event(s). If False, the player must physically click the
##      on-screen button.
## icon_only : bool
##      If True, the icon will be displayed without text/no caption. False
##      by default.
## suffix : str
##      A string to append to the icon image. Most often this is "small" to
##      get the smaller icon version.
## keymap_only : bool
##      If True, no icon image will be displayed, but the events will still be
##      listened for and triggered if the correct button is pressed.
##
## You may also pass other keyword arguments to style the button, text, and hbox
## containers. Properties prefixed with "text_" get passed to the caption, and
## properties prefixed with "hbox_" get passed to the hbox. Everything else is
## used by the button.
define icn.back = IconButton("cancel", "game_menu", _("Back"),
    mkb_icon="key_escape", action=Return())
## A version of the back/return button which is set up to work with the
## menu screens.
define icn.menu_return = IconButton(kind=icn.back, action=MenuReturn())
define icn.select = IconButton("button_select",
    ## The key event doesn't use button_select because it would absorb
    ## mouseup events, interfering with using screens with a mouse.
    key_event=['K_RETURN', 'K_KP_ENTER', 'K_SELECT'],
    caption=_("Select"),
    mkb_icon="mkb_select")
define icn.reset = IconButton("extra_menu", ["r", "R"], _("Reset"), "key_r")
define icn.sync = IconButton("extra_menu", ["s", "S"], _("Sync"), "key_s")
define icn.delete = IconButton("save_delete", "save_delete", _("Delete"), "key_delete")
define icn.page_left = IconButton("page_left", ["Q", "q"], _("Previous"), "key_q")
define icn.page_right = IconButton("page_right", ["E", "e"], _("Next"), "key_e")