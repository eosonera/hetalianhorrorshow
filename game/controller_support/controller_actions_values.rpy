################################################################################
##
## Controller Support Expansion for Ren'Py by Feniks (feniksdev.itch.io / feniksdev.com)
## v1.0
##
################################################################################
## This file contains code for several screen actions and values used throughout
## the controller support expansion. See the tools section on my website
## for more details: https://feniksdev.com/tool/screen-actions-and-values/
##
## If you use this code in your projects, credit me as Feniks @ feniksdev.com
##
## Leave a comment on the tool page on itch.io if you run into any issues.
################################################################################

################################################################################
## SCREEN ACTIONS AND VALUES
################################################################################
init python:

    class SetFocus(Action):
        """
        A convenience action for screens which calls renpy.set_focus. Arguments
        are as for renpy.set_focus.
        """
        def __init__(self, screen, id, layer="screens"):
            self.screen = screen
            self.id = id
            self.layer = layer
        def get_sensitive(self):
            ## Only sensitive if this isn't already the currently
            ## focused displayable
            focused = renpy.display.focus.get_focused()
            disp = renpy.get_displayable(self.screen, self.id, self.layer)
            return focused is not disp
        def __call__(self):
            renpy.set_focus(self.screen, self.id, self.layer)


    class SetStickInversion(SetField):
        """
        A convenience action with better alt text for setting the
        inverted state of the sticks.
        """
        def __init__(self, stick, axis, value):
            field = "{}_stick_invert_{}".format(stick, axis)
            self.stick = stick
            self.axis = axis
            super(SetStickInversion, self).__init__(persistent, field, value)
            self.alt = self.get_tooltip()
        def get_tooltip(self):
            if self.value:
                return _("Invert the %s stick on the %s axis") % (self.stick, self.axis)
            else:
                return _("Do not invert the %s stick on the %s axis") % (self.stick, self.axis)


    class ToggleStickInversion(ToggleField):
        """
        A convenience action with better alt text for toggling the
        inverted state of the sticks.
        """
        def __init__(self, stick, axis):
            field = "{}_stick_invert_{}".format(stick, axis)
            self.stick = stick
            self.axis = axis
            super(ToggleStickInversion, self).__init__(persistent, field)
            self.alt = self.get_tooltip()
        def get_tooltip(self):
            return _("Toggle the inversion of the %s stick on the %s axis") % (self.stick, self.axis)


    class StickDeadzoneAdjustment(BarValue):
        """
        A convenience class for the bar value of the stick deadzones.
        """
        def __init__(self, stick="left"):
            self.stick = stick
            super(StickDeadzoneAdjustment, self).__init__()
            self.alt = _("Deadzone for the %s stick") % self.stick
        def get_adjustment(self):
            return ui.adjustment(
                value=self.adjust_deadzone(0, True)-pad_config.MINIMUM_DEADZONE,
                range=pad_config.MAXIMUM_DEADZONE-pad_config.MINIMUM_DEADZONE,
                step=1024, adjustable=True, changed=self.adjust_deadzone)
        def get_tooltip(self):
            return _("Adjust the deadzone for the %s stick. The deadzone is the area where the stick is considered to be at rest.") % self.stick
        def adjust_deadzone(self, value, return_value=False):
            if not renpy_controllers:
                return (pad_config.DEFAULT_DEADZONE if return_value else None)
            stick = self.stick
            ## Grab the first key and get the guid
            id = next(iter(renpy_controllers))
            key = renpy_controllers.get(id)
            if key is None:
                return (pad_config.DEFAULT_DEADZONE if return_value else None)
            key = key.get_guid_string()
            if stick == "left":
                if return_value:
                    return persistent.left_stick_dead_zone.get(key, pad_config.DEFAULT_DEADZONE)
                persistent.left_stick_dead_zone[key] = value + pad_config.MINIMUM_DEADZONE
            else:
                if return_value:
                    return persistent.right_stick_dead_zone.get(key, pad_config.DEFAULT_DEADZONE)
                persistent.right_stick_dead_zone[key] = value + pad_config.MINIMUM_DEADZONE


    class StickSensitivityAdjustment(BarValue):
        """
        A convenience class for the bar value of the stick sensitivities.
        """
        def __init__(self, stick="left"):
            self.stick = stick
            super(StickSensitivityAdjustment, self).__init__()
            self.alt = _("Sensitivity for the %s stick") % self.stick
        def get_adjustment(self):
            return ui.adjustment(
                value=self.get_sensitivity_number(getattr(persistent,
                self.stick + "_stick_sensitivity")), range=10, step=1,
                adjustable=True, changed=self.adjust_sensitivity)
        def get_tooltip(self):
            return _("Adjust the sensitivity of the %s stick. High sensitivity moves faster.") % self.stick
        def adjust_sensitivity(self, value):
            field = "{}_stick_sensitivity".format(self.stick)
            if value == 5:
                setattr(persistent, field, pad_config.DEFAULT_SENSITIVITY)
            elif value == 0:
                setattr(persistent, field, pad_config.MINIMUM_SENSITIVITY)
            elif value == 10:
                setattr(persistent, field, pad_config.MAXIMUM_SENSITIVITY)
            elif value < 5:
                setattr(persistent, field, pad_config.DEFAULT_SENSITIVITY - (pad_config.DEFAULT_SENSITIVITY - pad_config.MINIMUM_SENSITIVITY) * (5 - value) / 5)
            else:
                setattr(persistent, field, pad_config.DEFAULT_SENSITIVITY + (pad_config.MAXIMUM_SENSITIVITY - pad_config.DEFAULT_SENSITIVITY) * (value - 5) / 5)
        def get_sensitivity_number(self, value):
            if value == pad_config.DEFAULT_SENSITIVITY:
                return 5
            elif value == pad_config.MINIMUM_SENSITIVITY:
                return 0
            elif value == pad_config.MAXIMUM_SENSITIVITY:
                return 10
            elif value < pad_config.DEFAULT_SENSITIVITY:
                return 5 - (5 - value) * 5 / (pad_config.DEFAULT_SENSITIVITY - pad_config.MINIMUM_SENSITIVITY)
            else:
                return 5 + (value - pad_config.DEFAULT_SENSITIVITY) * 5 / (pad_config.MAXIMUM_SENSITIVITY - pad_config.DEFAULT_SENSITIVITY)



## Defined despite changing, as it should always begin as False.
define pad_is_calibrating = False
