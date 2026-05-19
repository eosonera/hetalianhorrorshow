################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0.1
##
################################################################################
## This file contains code for declaring custom events and allowing players to
## remap gamepad controls. It includes the backend for handling remapping, but
## not the screens, which are in controller_remap_screens.rpy. The first half
## of this code is intended to be modified if you'd like to change the keymap
## or add your own events. The second half is backend, and you generally won't
## need to change anything there.
##
## For more information and examples, check out the tools section on my website:
## https://feniksdev.com/tool/remapping-controls/
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################
################################################################################
## REMAPPING FUNCTIONS
################################################################################
init python in pad_remap:
    ############################################################################
    ## CUSTOM EVENTS
    ############################################################################
    ## You'll add custom events by calling the add_custom_event function (or you
    ## could add your event to all the necessary lists, but the function is
    ## made to simplify this). Several custom events are provided, with more
    ## commented out as an example.
    add_custom_event(
        ## The name of the event, which will be used on your buttons. You are
        ## in charge of actually handling these events in your game, e.g. by
        ## using `key` or `keysym` in your screens. They can be remapped as
        ## with other events if you mark it as remappable=True
        ##
        ## You must then use the method pad_config.get_event("your_event_name") to get
        ## the correct event name e.g. `key pad_config.get_event("cancel")`
        ## Note that `key "cancel"` will not work as it is a custom event.
        event_name="cancel",
        ## This title is used in the remapping screen, to explain to the player
        ## what action they are remapping to a new key.
        title=_("Cancel/Return{#pad_remap}"),
        ## The keysyms is a list of what buttons will trigger this event. These
        ## should be strings like "pad_x_press" as seen in DEFAULT_BINDINGS.
        keysyms=["pad_b_press"],
        ## The category is one of "in-game", "menu", "situational", or "always".
        ## See the function signature below for explanations on each.
        category="menu",
        ## Besides the usual categories this event is compatible with, it can
        ## also be used for the same button as game_menu as they often do the
        ## same thing.
        extra_compatibility=["game_menu"],
        ## This event is required to have a button mapped to it - the plan is
        ## that some screens will only allow confirm/cancel to be done through
        ## key events.
        required=True,
        ## Holding down this button (B) should not repeatedly trigger the event.
        repeatable=False,
        ## This event can be remapped by the player.
        remappable=True,
        ## This indicates where it should appear in the REMAPPABLE_EVENTS list
        ## on the remapping screen. We want this to appear below button_select,
        ## which has priority 10.
        priority=11,
        )

    ## These next two are used for custom page left/right actions.
    add_custom_event("page_left", _("Page Left{#pad_remap}"),
        ["pad_leftshoulder_press"], "menu", required=True, remappable=True,
        priority=61)
    add_custom_event("page_right", _("Page Right{#pad_remap}"),
        ["pad_rightshoulder_press"], "menu", required=True, remappable=True,
        priority=62)

    ## This is a custom event for opening the history screen. See the quick
    ## menu in dialogue_screens.rpy for the shortcut.
    add_custom_event("history", _("Open History{#pad_remap}"),
        ["pad_lefttrigger_pos"], "in-game", required=False, remappable=True,
        priority=51)
    ## This is a custom event for extra menu actions, like syncing save data
    ## or resetting preferences to the defaults.
    add_custom_event("extra_menu", _("Sync Save Data/Reset to Default"),
        ["pad_y_press"], "menu", required=True, remappable=True,
        priority=115)
    ## This is a custom event for viewport scrolling shortcuts. It is not
    ## remappable. It is used in 01_controller_vp.rpy to jump the viewport
    ## scrolling to the top or bottom.
    add_custom_event("scroll_shortcut", _("Scroll Shortcut{#pad_remap}"),
        ["pad_rightshoulder_press"], "situational", required=False, remappable=False)
    ## And here's an example of a pad event for opening an inventory screen:
    # add_custom_event("inventory", _("Open Inventory{#pad_remap}"),
    #     ["pad_start_press"], "in-game", required=False, remappable=True)

    ## Here are some non-remappable events for input; these are here if you
    ## need to modify them.
    add_custom_event("input_shift", _("Shift{#pad_remap}"),
        ["pad_lefttrigger_pos"], "situational", required=False, remappable=False)
    add_custom_event("input_page", _("Switch Input Page{#pad_remap}"),
        ["pad_leftstick_press"], "situational", required=False, remappable=False)
    add_custom_event("input_space", _("Spacebar{#pad_remap}"),
        ["pad_y_press"], "situational", required=False, remappable=False,
        repeatable=True)

################################################################################
## BACKEND
################################################################################
## For the most part, you won't have to worry about anything below this.
################################################################################
init -100 python in pad_remap:

    from store import config, persistent, Text, VBox, Null

    def add_custom_event(event_name, title, keysyms, category,
            compatible_categories=None, extra_compatibility=None,
            required=False, repeatable=False, remappable=False,
            priority=999):
        """
        A helper function to add a new event to the custom events list.

        Arguments:
        ----------
        event_name : str
            The name of the event to add to the custom events list. This should
            be in snake_case e.g. "cancel"
        title : str
            The human-readable name of this event. If this event is remappable,
            this will be displayed in the remap screen e.g. _("Cancel/Return")
            You may want to add a translation tag so you know this is for
            the gamepad remapping, e.g. _("Cancel/Return{#pad_remap}")
        keysyms : list of str
            A list of keysyms that will trigger this event. These should be
            strings like "pad_x_press" as seen in DEFAULT_BINDINGS.
            e.g. ["pad_x_press", "pad_y_press"]
        category : str
            The category this event belongs to. The categories are as follows:
                in-game - events that only occur in-game and won't conflict with
                    menu events, such as rollback or skip.
                menu - events that only occur in menus and won't conflict with
                    in-game events, such as cancel or page_left.
                situational - events that only occur in specific situations and
                    won't conflict with in-game or menu events, such as input
                    events or save deletion.
                always - events that can be used anywhere and would conflict
                    with any other button, such as game_menu or button_select.
        compatible_categories : list of str, optional
            If provided, this should be a list of categories that this event is
            compatible with - that is, this event could be mapped to the same
            button as other buttons in the provided categories and not cause
            problems. If not provided, the default, this will be automatically
            filled with typical compatible categories (e.g. in-game events are
            compatible with situational and menu events, but not "always"
            events). For most events, this can safely be handled automatically
            if the category is correct. If set to False, no automatic
            compatibility will be added.
        extra_compatibility : list of str, optional
            If provided, this should be a list of events that this event is
            compatible with. This can be used to fine-tune compatibility
            alongside compatible_categories.
        required : bool, optional
            If True, this event is required to have a button mapped to it, and
            the game will not save a remapped control set which does not have
            a button mapped to this event. Default is False.
            Set this to True if there would be no other way to perform a
            required action in the game if this event is not mapped. Some things
            are not required e.g. it's fine if the player does not have a button
            mapped to rollback if they don't want to use rollback, but it may be
            impossible to navigate a preferences screen if page_left isn't
            mapped.
        repeatable : bool, optional
            If True, this event should repeat when the button is held down.
            Default is False. Some actions, like rollback, should execute
            multiple times while the rollback button is held down. Most events
            should occur only once per button press, so repeatable is False.
        remappable : bool, optional
            If True, this event will show up in the remapping screen and can be
            remapped by the player. Default is False. Ensure you have the other
            properties set (title, category, compatibility, remappable,
            repeatable) correctly if the player can remap this to ensure they
            can't remap themselves into a corner or have conflicts.
        priority : int
            If provided, this indicates where the event should appear in the
            remappable events list. Lower priorities appear before higher ones.
            See REMAPPABLE_EVENTS for the existing priority numbers, so you can
            specify where your custom event should go. If not provided, the
            event will appear at the end of the list.
        """
        if event_name in CUSTOM_EVENTS:
            ## Add the keysyms to the list
            CUSTOM_EVENTS[event_name].extend(keysyms)
            ## Ensure there are no duplicates
            CUSTOM_EVENTS[event_name] = list(set(CUSTOM_EVENTS[event_name]))
        else:
            CUSTOM_EVENTS[event_name] = keysyms

        ## Add the event to the remappable events list if it's remappable
        if remappable:
            REMAPPABLE_EVENTS.append((title, event_name, priority))
            ## Sort remappable events by priority
            REMAPPABLE_EVENTS.sort(key=lambda x: x[2])

        ## Add the event to the event categories
        if category not in EVENT_CATEGORIES:
            raise ValueError("Category " + category + " is not a valid category.")
        if event_name not in EVENT_CATEGORIES[category]:
            EVENT_CATEGORIES[category].append(event_name)

        ## Add the event to the event compatibility list
        if compatible_categories is None:
            if category == "in-game":
                EVENT_COMPATIBILITY[event_name] = EVENT_CATEGORIES["menu"] + EVENT_CATEGORIES["situational"]
            elif category == "menu":
                EVENT_COMPATIBILITY[event_name] = EVENT_CATEGORIES["in-game"] + EVENT_CATEGORIES["situational"]
            elif category == "situational":
                EVENT_COMPATIBILITY[event_name] = EVENT_CATEGORIES["in-game"] + EVENT_CATEGORIES["menu"]
            else:
                EVENT_COMPATIBILITY[event_name] = [ ]
        elif compatible_categories:
            EVENT_COMPATIBILITY[event_name] = [ ]
            for cat in compatible_categories:
                EVENT_COMPATIBILITY[event_name].extend(EVENT_CATEGORIES[cat])
        else:
            EVENT_COMPATIBILITY[event_name] = [ ]

        if extra_compatibility is not None:
            EVENT_COMPATIBILITY[event_name].extend(extra_compatibility)

        ## Now we have to add this event as compatible with all the other events
        ## it's compatible with.
        for other_event in EVENT_COMPATIBILITY[event_name]:
            if other_event not in EVENT_COMPATIBILITY:
                EVENT_COMPATIBILITY[other_event] = [ ]
            if event_name not in EVENT_COMPATIBILITY[other_event]:
                EVENT_COMPATIBILITY[other_event].append(event_name)

        ## Add the event to the required events list if it's required
        if required:
            REQUIRED_EVENTS.append(event_name)

        ## Add the event to the repeatable events list if it's repeatable
        if repeatable:
            REPEAT_ACTIONS.add(event_name)

        ## Add it to the persistent bindings if it's not already there
        if event_name not in persistent.pad_bindings:
            persistent.pad_bindings[event_name] = keysyms


    CUSTOM_EVENTS = {
        ## This is filled automatically by add_custom_event
    }

    ## A list of events that can be remapped by the player. Not all events
    ## are remappable - these plugins expect certain input_ events to be as
    ## provided for the virtual keyboard, for example.
    ## You can add custom events here if you want the player to be able to
    ## remap them, but you can also omit them so they're constant.
    ## The entries in this list are pairs of (human-readable name, event name,
    ## priority). The event name corresponds to the name used for CUSTOM_EVENTS
    ## and the  officially provided ones in https://www.renpy.org/doc/html/keymap.html
    ## The priority is provided here so you can indicate where your custom
    ## events should appear in this list. Lower numbers appear first.
    REMAPPABLE_EVENTS = [
        (_("Confirm{#pad_remap}"), "button_select", 10),

        ## Feniks note: You can add back the button_alternate event if you
        ## have buttons with alternate actions.
        # (_("Alternate Action{#pad_remap}"), "button_alternate", 20),
        ####

        (_("Advance dialogue{#pad_remap}"), "dismiss", 30),
        (_("Toggle Auto-Advance{#pad_remap}"), "toggle_afm", 40),
        (_("Game Menu{#pad_remap}"), "game_menu", 50),
        (_("Skip{#pad_remap}"), "toggle_skip", 60),

        (_("Rollback{#pad_remap}"), "rollback", 70),
        (_("Roll-Forward{#pad_remap}"), "rollforward", 80),
        (_("Hide UI{#pad_remap}"), "hide_windows", 90),
        (_("Screenshot{#pad_remap}"), "screenshot", 100),

        ## For logistical reasons, these are not remappable.
        ## They're left here in case you wanted to add that compatibility.
        # ("Navigate Left", "focus_left", 100),
        # ("Navigate Right", "focus_right", 100),
        # ("Navigate Up", "focus_up", 100),
        # ("Navigate Down", "focus_down", 100),

        (_("Delete Saves{#pad_remap}"), "save_delete", 110),
        (_("Accessibility{#pad_remap}"), "accessibility", 120),
        (_("Self-Voicing{#pad_remap}"), "self_voicing", 130),
        (_("Fast Skip{#pad_remap}"), "fast_skip", 140),
        (_("Quit{#pad_remap}"), "quit", 150),

    ]

    ## Sort events into categories so we know when to remove an event from
    ## a button when the player remaps it to avoid conflicts.
    ## ADD YOUR CUSTOM EVENTS TO THIS LIST! *Even if it is not remappable*.
    ## These are generalizations which attempt to prevent the player from
    ## remapping buttons in a way that means some can't be used.
    EVENT_CATEGORIES = {
        ## Events that only occur in-game, and thus won't conflict with
        ## some other events that can only be used in menus.
        "in-game" : [
            "rollback", "toggle_afm", "hide_windows", "rollforward",
            "skip", "stop_skipping", "toggle_skip", "fast_skip",
            "dismiss",
        ],
        ## Events that only occur in menus, and thus won't conflict with
        ## events that can only be used in-game.
        "menu" : [
            ## This one is useful for custom events, like "cancel" or paging
            ## shortcuts.
        ],
        ## Events which are situational, and won't conflict with menu or in-game
        ## buttons. "save_delete" only occurs on the save/load screens, and
        ## input events only occur during input sections.
        "situational" : [
            "input_backspace", "input_enter", "input_left", "input_right",
            "save_delete",
        ],
        ## Events which can be used anywhere, and would conflict with any other
        ## button.
        "always" : [
            "game_menu", "focus_left", "focus_right", "focus_up", "focus_down",
            "button_select", "button_alternate", "dismiss",
            "bar_left", "bar_right", "bar_up", "bar_down",
            "bar_activate", "bar_deactivate",
            "viewport_leftarrow", "viewport_rightarrow",
            "viewport_uparrow", "viewport_downarrow",
            "screenshot", "quit", "accessibility", "self_voicing",
            "drag_activate", "drag_deactivate",
        ],
    }

    ## The categories above are used to simplify the list below, which details
    ## compatible events for each possible event.
    EVENT_COMPATIBILITY = {
        ## In-game events
        ## What this says is that the rollback button can be mapped to the
        ## same button as an event in the "menu" category or an event in the
        ## "situational" category. e.g. L1 can be mapped to rollback, page_left,
        ## and input_left, since these functionalities won't conflict.
        ##
        ## For the most part, you can follow the same pattern for custom actions
        ## as other events in the same category.
        'rollback' : EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],
        'toggle_afm' : EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],
        'hide_windows' : EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],
        'rollforward' : EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],
        'skip' : EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],
        'stop_skipping' : EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],
        'toggle_skip' : EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],
        'fast_skip' : EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],
        ## dismiss is a case where multiple events are almost always mapped to
        ## it - e.g. usually the A button will select a button and activate bars
        ## - but sometimes the dismiss button may be remapped individually.
        'dismiss' : [ 'button_alternate', 'button_select', 'bar_activate', 'bar_deactivate', 'drag_activate', 'drag_deactivate'] + EVENT_CATEGORIES['menu'] + EVENT_CATEGORIES['situational'],

        ## Menu events
        ## These are added by add_custom_event. Typically they are compatible with
        ## EVENT_CATEGORIES['in-game'] + EVENT_CATEGORIES['situational']

        ## Situational events
        'input_backspace' : EVENT_CATEGORIES['in-game'] + EVENT_CATEGORIES['menu'],
        'input_enter' : EVENT_CATEGORIES['in-game'] + EVENT_CATEGORIES['menu'],
        'input_left' : EVENT_CATEGORIES['in-game'] + EVENT_CATEGORIES['menu'],
        'input_right' : EVENT_CATEGORIES['in-game'] + EVENT_CATEGORIES['menu'],
        'save_delete' : EVENT_CATEGORIES['in-game'] + EVENT_CATEGORIES['menu'],

        ## Always available events
        ## NOTE: This one is up to your coding - in a typical setup, the
        ## alternate button action is infrequent enough that it shouldn't
        ## conflict with input or save delete
        'button_alternate' : [ 'bar_activate', 'bar_deactivate', "dismiss", "drag_activate", "drag_deactivate" ] + EVENT_CATEGORIES['situational'],
        'screenshot' :  [ ],
        'game_menu' : [ ],
        'quit' : [ ],
        'accessibility' : [ ],
        'self_voicing' : [ ],
        'focus_left' : ["bar_left", "viewport_leftarrow" ],
        'focus_right' : [ "bar_right", "viewport_rightarrow" ],
        'focus_up' : [ "bar_up", "viewport_uparrow" ],
        'focus_down' : [ "bar_down", "viewport_downarrow" ],
        'button_select' : [ "bar_activate", "bar_deactivate", "dismiss", "drag_activate", "drag_deactivate" ],
        'drag_activate' : [ "bar_activate", "bar_deactivate", "dismiss", "button_select", "drag_deactivate" ],
        'drag_deactivate' : [ "bar_activate", "bar_deactivate", "dismiss", "button_select", "drag_activate" ],
        "bar_left" : [ "focus_left", "viewport_leftarrow" ],
        "bar_right" : [ "focus_right", "viewport_rightarrow" ],
        "bar_up" : [ "focus_up", "viewport_uparrow" ],
        "bar_down" : [ "focus_down", "viewport_downarrow" ],
        "viewport_leftarrow" : [ "focus_left", "bar_left" ],
        "viewport_rightarrow" : [ "focus_right", "bar_right" ],
        "viewport_uparrow" : [ "focus_up", "bar_up" ],
        "viewport_downarrow" : [ "focus_down", "bar_down" ],
        "bar_activate" : [ "button_select", "bar_deactivate", "dismiss", "button_alternate", 'drag_activate', 'drag_deactivate' ],
        "bar_deactivate" : [ "button_select", "bar_activate", "dismiss", "button_alternate", 'drag_activate', 'drag_deactivate' ],
    }

    ## Events which absolutely *must* have a button assigned to them.
    REQUIRED_EVENTS = [
        "button_select", "dismiss",
        "focus_left", "focus_right", "focus_up", "focus_down",
        "bar_left", "bar_right", "bar_up", "bar_down",
        "game_menu", "drag_activate", "drag_deactivate",
    ]


    ## The default bindings for the gamepad controls. This should NOT include
    ## your custom events; see above for how to add those. This needs to be a
    ## default Ren'Py-friendly button-to-event-list dictionary.
    ## I've modified it from the engine defaults to add things such as
    ## keys for accessibility, screenshots, and fast skipping.
    ## For reference:
    ## pad_BUTTON_press - the button was pressed/pushed down
    ## repeat_pad_BUTTON_press - the button is being held down for an extended
    ##      period. Any actions here will fire multiple times while the button
    ##      is held down.
    ## pad_BUTTON_release - the button was released/lifted up. By default, these
    ##      are not used for key bindings. They can be useful for "shortcuts",
    ##      and are included for clarity.
    ## pad_BUTTON_pos - the button is being held down. This is used for triggers
    ##      and sticks, where the button can be in a "partially pressed" state.
    ## pad_BUTTON_zero - the button is not being held down. This is used for
    ##      triggers and sticks, where the button can be in a "partially pressed"
    ##      state.
    ## pad_BUTTON_neg - the button is being held down in the opposite direction.
    ##      This is used for sticks, where the stick can be pushed left/right
    ##      and up/down, with zero being the resting state in the middle.
    DEFAULT_BINDINGS = {
        ## SHOULDER BUTTONS
        ## LEFT SHOULDER (L1)
        "pad_leftshoulder_press" : ["rollback", "input_left"],
        "repeat_pad_leftshoulder_press" : ["rollback", "input_left"],
        "pad_leftshoulder_release" : [],

        ## RIGHT SHOULDER (R1)
        "pad_rightshoulder_press" : ["rollforward", "input_right"],
        "repeat_pad_rightshoulder_press" : ["rollforward", "input_right"],
        "pad_rightshoulder_release" : [],

        ## TRIGGERS
        ## LEFT TRIGGER (L2)
        "pad_lefttrigger_pos" : [], # Used for the custom history log event
        "repeat_pad_lefttrigger_pos" : [],
        "pad_lefttrigger_zero" : [],

        ## RIGHT TRIGGER (R2)
        "pad_righttrigger_pos" : ["toggle_skip", "input_enter"],
        "repeat_pad_righttrigger_pos" : [],
        "pad_righttrigger_zero" : [],

        ## BUTTONS
        ## A BUTTON
        "pad_a_press" : ["dismiss", "button_select", "bar_activate", "bar_deactivate", "drag_activate", "drag_deactivate"],
        "repeat_pad_a_press" : [],
        "pad_a_release" : [],

        ## B BUTTON
        "pad_b_press" : [], # Used for the custom cancel event
        "repeat_pad_b_press" : [],
        "pad_b_release" : [],

        ## X BUTTON
        "pad_x_press" : ["hide_windows", "save_delete", "input_backspace"],
        "repeat_pad_x_press" : ["input_backspace"],
        "pad_x_release" : [],

        ## Y BUTTON
        "pad_y_press" : ["toggle_afm"],
        "repeat_pad_y_press" : [],
        "pad_y_release" : [],

        ## D-PAD
        ## LEFT
        "pad_dpleft_press" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
        "repeat_pad_dpleft_press" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
        "pad_dpleft_release" : [],

        ## RIGHT
        "pad_dpright_press" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "repeat_pad_dpright_press" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "pad_dpright_release" : [],

        ## UP
        "pad_dpup_press" : ["focus_up", "bar_up", "viewport_uparrow"],
        "repeat_pad_dpup_press" : ["focus_up", "bar_up", "viewport_uparrow"],
        "pad_dpup_release" : [],

        ## DOWN
        "pad_dpdown_press" : ["focus_down", "bar_down", "viewport_downarrow"],
        "repeat_pad_dpdown_press" : ["focus_down", "bar_down", "viewport_downarrow"],
        "pad_dpdown_release" : [],

        ## STICKS
        ## LEFT STICK
        "pad_leftstick_press" : ["accessibility"],
        "repeat_pad_leftstick_press" : [],
        "pad_leftstick_release" : [],

        "pad_leftx_pos" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "repeat_pad_leftx_pos" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "pad_leftx_neg" : ["focus_left", "bar_left", "viewport_leftarrow"],
        "repeat_pad_leftx_neg" : ["focus_left", "bar_left", "viewport_leftarrow"],
        "pad_lefty_pos" : ["focus_down", "bar_down", "viewport_downarrow"],
        "repeat_pad_lefty_pos" : ["focus_down", "bar_down", "viewport_downarrow"],
        "pad_lefty_neg" : ["focus_up", "bar_up", "viewport_uparrow"],
        "repeat_pad_lefty_neg" : ["focus_up", "bar_up", "viewport_uparrow"],

        ## RIGHT STICK
        "pad_rightstick_press" : ["fast_skip"],
        "repeat_pad_rightstick_press" : [],
        "pad_rightstick_release" : [],

        "pad_rightx_pos" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "repeat_pad_rightx_pos" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "pad_rightx_neg" : ["focus_left", "bar_left", "viewport_leftarrow"],
        "repeat_pad_rightx_neg" : ["focus_left", "bar_left", "viewport_leftarrow"],
        "pad_righty_pos" : ["focus_down", "bar_down", "viewport_downarrow"],
        "repeat_pad_righty_pos" : ["focus_down", "bar_down", "viewport_downarrow"],
        "pad_righty_neg" : ["focus_up", "bar_up", "viewport_uparrow"],
        "repeat_pad_righty_neg" : ["focus_up", "bar_up", "viewport_uparrow"],

        ## SELECT
        "pad_back_press" : ["screenshot"],
        "repeat_pad_back_press" : [],
        "pad_back_release" : [],

        ## HOME
        "pad_guide_press" : [],
        "repeat_pad_guide_press" : [],
        "pad_guide_release" : [],

        ## START
        "pad_start_press" : ["game_menu"],
        "repeat_pad_start_press" : [],
        "pad_start_release" : [],
    }


    ############################################################################
    ## Lists you may need to add to for custom events, but usually don't.
    ############################################################################
    ## Actions which should reoccur when the button is held down.
    ## Add to this set if you have custom actions that should repeat!
    ## Not everything does - e.g. you don't want to repeat a screenshot. But
    ## if I hold down bar_left I want it to keep moving the bar rather than
    ## needing to press and release a bunch.
    REPEAT_ACTIONS = set([
        "focus_left", "focus_right", "focus_up", "focus_down",
        "rollback", "rollforward", "input_left", "input_right",
        "input_backspace", "bar_right", "bar_left", "bar_up", "bar_down",
        "viewport_rightarrow", "viewport_leftarrow", "viewport_uparrow",
        "viewport_downarrow",
    ])

    ## Actions which are carried along if this event is remapped (e.g. if the
    ## button_select button is remapped, then bar_activate and bar_deactivate
    ## should also be remapped to the new button for button_select).
    ## For most purposes, this list is fine as-is and won't need to be modified.
    COMBO_ACTIONS = {
        "button_select" : ["bar_activate", "bar_deactivate", "drag_activate", "drag_deactivate"],
        "focus_left" : [ "focus_left", "bar_left", "viewport_leftarrow" ],
        "focus_right" : [ "focus_right", "bar_right", "viewport_rightarrow" ],
        "focus_up" : [ "focus_up", "bar_up", "viewport_uparrow" ],
        "focus_down" : [ "focus_down", "bar_down", "viewport_downarrow" ],
        ## Add more, if relevant.
    }


## A mapping of GUID to which layout to use. Used to remember the player's
## preferred button layout for a given controller, so when they plug it in again
## it'll use the right icons.
default persistent.controller_guid_to_type = dict()
## The current layout.
default persistent.controller_layout = "generic"

init -50 python in pad_remap:
    from renpy.store import Null

    def get_official_bindings():
        """
        Return the persistent bindings, with the custom keysyms filtered
        out, in keysym : [action] format. Suitable to set
        config.pad_bindings to.
        out, in keysym : [action] format. Suitable to set
        config.pad_bindings to.
        """
        pers = persistent.pad_bindings
        new_bindings = dict()
        for action, keysyms in pers.items():
            if action in CUSTOM_EVENTS:
                continue
            if persistent.hold_to_skip and action == "toggle_skip":
                ## Special case; add the press/release keysyms for
                ## skipping instead
                toggle_replacement(keysyms, new_bindings,
                    "skip", "stop_skipping", replace_press=True)
                continue
            elif action == "drag_deactivate" and persistent.hold_to_drag:
                ## Special case; button select comes with press/release
                ## variants for dragging.
                toggle_replacement(keysyms, new_bindings,
                    "drag_activate", "drag_deactivate", replace_press=False)
                continue
            for keysym in keysyms:
                if keysym not in new_bindings:
                    new_bindings[keysym] = [action]
                else:
                    new_bindings[keysym].append(action)
        return new_bindings

    def toggle_replacement(keysyms, new_bindings, press, release, replace_press=True):
        """
        A function which handles replacing a toggle keysym with its on/off
        counterparts attached to the press/release events.
        """
        for keysym in keysyms:
            if keysym.startswith("repeat"):
                continue
            if keysym.endswith("_press"):
                pressed = keysym
                released = keysym.replace("_press", "_release")
            elif keysym.endswith("_pos"):
                pressed = keysym
                released = keysym.replace("_pos", "_zero")
            else:
                continue
            if replace_press:
                if pressed not in new_bindings:
                    new_bindings[pressed] = [press]
                else:
                    new_bindings[pressed].append(press)
            if released not in new_bindings:
                new_bindings[released] = [release]
            else:
                new_bindings[released].append(release)

    def generate_persistent_bindings():
        """
        Generate the persistent bindings from the current bindings and
        custom ones. This dictionary is in action : [keysym] format, like
        the regular keymap.
        """
        new_bindings = dict()
        for keysym, actions in config.pad_bindings.items():
            for action in actions:
                if action not in new_bindings:
                    new_bindings[action] = [keysym]
                else:
                    new_bindings[action].append(keysym)
        for action, keysyms in CUSTOM_EVENTS.items():
            if action not in new_bindings:
                new_bindings[action] = keysyms.copy()
            else:
                new_bindings[action].extend(keysyms)
        return new_bindings

    def update_keymap():
        """Update the keymap."""
        config.pad_bindings = get_official_bindings()
        renpy.display.behavior.clear_keymap_cache()

    def check_for_custom_updates():
        """
        Check if there are any new custom keysyms to add to the persistent
        pad remapping.
        """
        for action, keysyms in CUSTOM_EVENTS.items():
            if action not in persistent.pad_bindings:
                persistent.pad_bindings[action] = keysyms

    def find_events(keysym):
        """
        Find all the events associated with a keysym.
        """
        events = []
        for action, keysyms in persistent.pad_bindings.items():
            if keysym in keysyms:
                events.append(action)
        return events

    def get_images(keysym, the_dict=None):
        """
        Get the images for the keysym.
        """
        if the_dict is None:
            the_dict = persistent.pad_bindings
        ## Get the buttons
        buttons = the_dict.get(keysym, [])
        if not buttons:
            return []
        seen_images = set()
        images = [ ]

        def add_img(img, images, og_btn):
            if img not in seen_images:
                seen_images.add(img)
                images.append((img, og_btn))

        for btn in buttons:
            og_btn = btn
            if btn.startswith("repeat_"):
                btn = btn.replace("repeat_", "")
            if btn.endswith("_press"):
                btn = btn.replace("_press", "")
            if btn.startswith("pad_dp"):
                btn = btn.replace("pad_dp", "pad_")

            if "leftstick" in btn:
                add_img("pad_l3", images, og_btn)
                continue
            if "rightstick" in btn:
                add_img("pad_r3", images, og_btn)
                continue
            if btn.endswith("back"):
                add_img("pad_select", images, og_btn)
                continue
            if btn.endswith("guide"):
                add_img("pad_home", images, og_btn)
                continue
            if btn.startswith("pad_leftshoulder"):
                add_img("pad_l1", images, og_btn)
                continue
            if btn.startswith("pad_rightshoulder"):
                add_img("pad_r1", images, og_btn)
                continue

            if not (btn.endswith("pos") or btn.endswith("zero") or btn.endswith("neg")):
                add_img(btn, images, og_btn)
                continue

            if btn.startswith("pad_rightx") or btn.startswith("pad_righty"):
                add_img("pad_right_stick", images, og_btn)
                continue
            if btn.startswith("pad_leftx") or btn.startswith("pad_lefty"):
                add_img("pad_left_stick", images, og_btn)
                continue
            if btn.startswith("pad_righttrigger"):
                add_img("pad_r2", images, og_btn)
                continue
            if btn.startswith("pad_lefttrigger"):
                add_img("pad_l2", images, og_btn)
                continue

        ## Get rid of duplicates and sort alphabetically
        return sorted(set(images), key=lambda x : x[0])

    def reset_to_default(remapper=None):
        """
        Reset the keymap to the default.
        """
        config.pad_bindings = get_keymap_copy(DEFAULT_BINDINGS)
        persistent.pad_bindings = generate_persistent_bindings()
        ## Ensure this remembers the player's changes
        config.pad_bindings = get_official_bindings()
        if remapper:
            remapper.temporary_bindings = None
            remapper.missing_events = None
            remapper.last_valid_bindings = get_keymap_copy(persistent.pad_bindings)
        renpy.store.pad_config.refresh_redrawables(0, 1, None, force=True)

    def get_keymap_copy(keymap):
        """
        Return a deep copy of the provided keymap.
        """
        new_keymap = dict()
        for k, v in keymap.items():
            new_keymap[k] = v.copy()
        return new_keymap

    class ControllerRemap():
        """
        A class which tracks information on controller mappings and handles
        remapping. Exists primarily to manage persistent.pad_bindings,
        config.pad_bindings, and the CUSTOM_EVENTS dictionary.
        """
        def __init__(self):
            self.temporary_bindings = None
            self.missing_events = None
            self.last_valid_bindings = get_keymap_copy(persistent.pad_bindings)
            self.name_lookup = {k[1] : k[0] for k in REMAPPABLE_EVENTS}

        def check_for_conflicts(self, keysym, action):
            """
            After adding a keysym to an action, check if any of the other events
            the keysym activates are in conflict with the action.
            """
            which_bindings = persistent.pad_bindings
            if self.temporary_bindings:
                which_bindings = self.temporary_bindings
            ## Get all the events associated with the keysym
            events = find_events(keysym)
            ## Get all the events that are compatible with the action
            compat = EVENT_COMPATIBILITY.get(action, [])
            ## Check if any of the events are in conflict
            for event in events:
                if event not in compat and event != action:
                    if keysym in which_bindings[event]:
                        self.remove_button(keysym, event)

        def add_button(self, keysym, action):
            """
            Add a button to the persistent bindings.
            e.g. add "pad_x_press" to "toggle_afm".
            """
            if not self.last_valid_bindings:
                self.last_valid_bindings = get_keymap_copy(persistent.pad_bindings)
            which_bindings = persistent.pad_bindings
            if self.temporary_bindings:
                which_bindings = self.temporary_bindings

            if action not in which_bindings:
                which_bindings[action] = [keysym]
            else:
                which_bindings[action].append(keysym)

            if action in COMBO_ACTIONS:
                ## Combo has more actions like "bar_activate"
                for combo in COMBO_ACTIONS[action]:
                    self.add_button(keysym, combo)

            if action in REPEAT_ACTIONS:
                repeat_keysym = "repeat_" + keysym
                if repeat_keysym not in which_bindings[action]:
                    which_bindings[action].append(repeat_keysym)

            self.check_for_conflicts(keysym, action)
            self.update_config()

        def remove_button(self, keysym, action=None):
            """
            Remove a button from the persistent bindings.
            """
            if not self.last_valid_bindings:
                self.last_valid_bindings = get_keymap_copy(persistent.pad_bindings)
            which_bindings = persistent.pad_bindings
            if self.temporary_bindings:
                which_bindings = self.temporary_bindings

            if action is not None and action not in which_bindings:
                return
            if action is None:
                ## Need to find actions with this keysym
                for action, keysyms in which_bindings.items():
                    if keysym in keysyms:
                        self.remove_button(keysym, action)
                return

            if keysym in which_bindings[action]:
                which_bindings[action].remove(keysym)

            if "repeat_" + keysym in which_bindings[action]:
                which_bindings[action].remove("repeat_" + keysym)

            if action in COMBO_ACTIONS:
                for combo in COMBO_ACTIONS[action]:
                    if combo in which_bindings:
                        self.remove_button(keysym, combo)
            self.update_config()

        def get_missing_events_text(self):
            """Return a pretty version of the missing text."""
            if not self.missing_events:
                return ""
            names = [ ]
            for event in self.missing_events:
                if self.name_lookup.get(event, None):
                    names.append(renpy.translate_string(self.name_lookup[event]))
            return names

        def missing_required_events(self):
            """
            Check if the current keymap is valid. For most purposes, this means
            making sure there's a button for "dismiss" and for "button_select",
            and for any other required events as specified.
            """
            missing_events = [ ]
            which_bindings = persistent.pad_bindings
            if self.temporary_bindings:
                which_bindings = self.temporary_bindings

            for event in REQUIRED_EVENTS:
                if not which_bindings.get(event):
                    missing_events.append(event)
            if missing_events:
                self.missing_events = missing_events
                return missing_events

            ## This is a valid keymap
            self.missing_events = None
            if self.temporary_bindings:
                persistent.pad_bindings = get_keymap_copy(self.temporary_bindings)
                self.temporary_bindings = None

            self.last_valid_bindings = get_keymap_copy(persistent.pad_bindings)
            ## Refresh icons
            renpy.store.pad_config.refresh_redrawables(0, 1, None, force=True)
            return False

        def get_current_bindings(self):
            """Get the bindings the player is currently modifying."""
            if self.temporary_bindings:
                return self.temporary_bindings
            else:
                return persistent.pad_bindings

        def update_config(self):
            """
            Update config with the new bindings if they are valid.
            """
            if self.missing_required_events():
                if not self.temporary_bindings:
                    self.temporary_bindings = persistent.pad_bindings
                    persistent.pad_bindings = get_keymap_copy(self.last_valid_bindings)
                renpy.restart_interaction()
                return
            config.pad_bindings = get_official_bindings()
            renpy.restart_interaction()

        def finalize_keymap(self):
            """
            Update the keymaps if it's valid.
            """
            if self.temporary_bindings:
                ## It is not valid
                self.temporary_bindings = None
                self.missing_events = None
                return
            else:
                ## It is valid
                config.pad_bindings = get_official_bindings()
                renpy.display.behavior.clear_keymap_cache()


    class RemapKey(Null):
        """
        A displayable that listens for a controller key press and adds it to
        the keymap.
        """
        ## You may add more keysyms here if you would like to pay attention to
        ## more events. Note that you will run into issues/need to handle
        ## release/zero events yourself, as the press/pos events will always
        ## be captured first.
        ## The dpad/sticks are not included as I've chosen to not allow
        ## remapping of those to avoid players remapping away their ability
        ## to focus buttons.
        POSSIBLE_KEYS = [
            "pad_x_press", "pad_y_press", "pad_a_press", "pad_b_press",
            "pad_leftshoulder_press", "pad_rightshoulder_press",
            "pad_lefttrigger_pos", "pad_righttrigger_pos",
            "pad_start_press", "pad_back_press", "pad_guide_press",
            "pad_rightstick_press", "pad_leftstick_press",
        ]
        def __init__(self, which_key, remapper):
            self.which_key = which_key
            self.remapper = remapper
            super(RemapKey, self).__init__()
        def event(self, ev, x, y, st):
            for possible_event in self.POSSIBLE_KEYS:
                ## i.e. check for pad_x_press etc
                if renpy.map_event(ev, possible_event):
                    ## Add the button to a ControllerRemap instance.
                    self.remapper.add_button(possible_event, self.which_key)
                    return True


    ## A list of all possible gamepad events, for iterating over to identify
    ## key presses.
    ALL_EVENTS = [
        ## SHOULDER BUTTONS
        ## LEFT SHOULDER
        "pad_leftshoulder_press",
        "pad_leftshoulder_release",
        "repeat_pad_leftshoulder_press",

        ## RIGHT SHOULDER
        "pad_rightshoulder_press",
        "pad_rightshoulder_release",
        "repeat_pad_rightshoulder_press",

        ## TRIGGERS
        ## LEFT TRIGGER
        "pad_lefttrigger_pos",
        "pad_lefttrigger_zero",
        "repeat_pad_lefttrigger_pos",

        ## RIGHT TRIGGER
        "pad_righttrigger_pos",
        "pad_righttrigger_zero",
        "repeat_pad_righttrigger_pos",

        ## BUTTONS
        ## A BUTTON
        "pad_a_press",
        "pad_a_release",
        "repeat_pad_a_press",

        ## B BUTTON
        "pad_b_press",
        "pad_b_release",
        "repeat_pad_b_press",

        ## X BUTTON
        "pad_x_press",
        "pad_x_release",
        "repeat_pad_x_press",

        ## Y BUTTON
        "pad_y_press",
        "pad_y_release",
        "repeat_pad_y_press",

        ## D-PAD
        ## LEFT
        "pad_dpleft_press",
        "pad_dpleft_release",
        "repeat_pad_dpleft_press",

        ## RIGHT
        "pad_dpright_press",
        "pad_dpright_release",
        "repeat_pad_dpright_press",

        ## UP
        "pad_dpup_press",
        "pad_dpup_release",
        "repeat_pad_dpup_press",

        ## DOWN
        "pad_dpdown_press",
        "pad_dpdown_release",
        "repeat_pad_dpdown_press",

        ## STICKS
        ## LEFT STICK
        "pad_leftstick_press",
        "pad_leftstick_release",
        "repeat_pad_leftstick_press",

        "pad_leftx_pos",
        "repeat_pad_leftx_pos",
        "pad_leftx_neg",
        "repeat_pad_leftx_neg",
        "pad_lefty_pos",
        "repeat_pad_lefty_pos",
        "pad_lefty_neg",
        "repeat_pad_lefty_neg",

        ## RIGHT STICK
        "pad_rightstick_press",
        "pad_rightstick_release",
        "repeat_pad_rightstick_press",

        "pad_rightx_pos",
        "repeat_pad_rightx_pos",
        "pad_rightx_neg",
        "repeat_pad_rightx_neg",
        "pad_righty_pos",
        "repeat_pad_righty_pos",
        "pad_righty_neg",
        "repeat_pad_righty_neg",

        ## SELECT/BACK
        "pad_back_press",
        "pad_back_release",
        "repeat_pad_back_press",

        ## HOME
        "pad_guide_press",
        "pad_guide_release",
        "repeat_pad_guide_press",

        ## START
        "pad_start_press",
        "pad_start_release",
        "repeat_pad_start_press",
    ]


    class ControllerEventDebug(Null):
        """
        A special displayable which shows which gamepad events are occurring.
        For debugging purposes.
        """
        def event(self, ev, x, y, st):
            for gp_event in ALL_EVENTS:
                if renpy.map_event(ev, gp_event):
                    self.last_events.append(gp_event)
                    if len(self.last_events) > 10:
                        self.last_events.pop(0)
                    print("Event:", gp_event)
                    renpy.redraw(self, 0)


## A label which is called in a new context to enable remapping of controller
## events.
label listen_for_remap(title, which_key, yadj, remapper):
    show screen controller_remap(underlay=True, vp_yadj=yadj)
    call screen listen_remap(title, which_key, remapper)
    return


################################################################################
## Remapping setup
################################################################################
init 10 python:
    ## Set these to the default, once only.
    if not persistent.controllers_set_up:
        persistent.controllers_set_up = True
        config.pad_bindings = pad_remap.get_keymap_copy(pad_remap.DEFAULT_BINDINGS)
        persistent.pad_bindings = pad_remap.generate_persistent_bindings()
    elif persistent.pad_bindings is None:
        persistent.pad_bindings = pad_remap.generate_persistent_bindings()

    pad_remap.check_for_custom_updates()

    ## Ensure this remembers the player's changes
    config.pad_bindings = pad_remap.get_official_bindings()

    ## Add enter to the drag activate/deactivate
    if 'keydown_K_RETURN' not in config.keymap["drag_activate"]:
        config.keymap["drag_activate"].append('keydown_K_RETURN')
    if 'keydown_K_KP_ENTER' not in config.keymap["drag_activate"]:
        config.keymap["drag_activate"].append('keydown_K_KP_ENTER')
    if 'keyup_K_RETURN' not in config.keymap["drag_deactivate"]:
        config.keymap["drag_deactivate"].append('keyup_K_RETURN')
    if 'keyup_K_KP_ENTER' not in config.keymap["drag_deactivate"]:
        config.keymap["drag_deactivate"].append('keyup_K_KP_ENTER')


## None the first time the game is run, so we can set up the defaults.
default persistent.controllers_set_up = None
## The current bindings for the gamepad. Persistent, so we can update it
## as the player remaps the controller.
default -600 persistent.pad_bindings = dict()
## Whether skipping only happens when the button is held down, or you can
## press it to toggle skip on/off.
default persistent.hold_to_skip = False
## Whether drags only happen when the button is held down, or you can
## press it to toggle dragging on/off.
default persistent.hold_to_drag = True
