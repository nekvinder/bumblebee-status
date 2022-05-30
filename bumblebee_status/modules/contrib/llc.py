"""Short description in RST format

   Show clipboard information
"""

from os import popen
import shelve
import core.module
import core.widget
import core.input

filename = "~.headseti3Config"


class Module(core.module.Module):
    def __init__(self, config, theme):
        super().__init__(config, theme, core.widget.Widget(self.full_text))
        core.input.register(
            self, button=core.input.LEFT_MOUSE, cmd=self.eventHandlersToggle
        )
        core.input.register(
            self, button=core.input.RIGHT_MOUSE, cmd=self.eventHandlersApply
        )

    def full_text(self, widgets):
        return (
            "Headset Lights On!!!!"
            if self.getHeadsetStatus()
            else "Headsets Lights Off"
        )

    def eventHandlersToggle(self, event):
        self.setHeadsetStatus(not self.getHeadsetStatus())
        ToggleValue = 1 if self.getHeadsetStatus() else 0
        popen(f"headsetcontrol -l {ToggleValue}")

    def eventHandlersApply(self, event):
        ToggleValue = 1 if self.getHeadsetStatus() else 0
        popen(f"headsetcontrol -l {ToggleValue}")

    def getHeadsetStatus(self):
        with shelve.open(filename) as db:
            if "lightOn" not in db.keys():
                db["lightOn"] = False
            return db["lightOn"] if db["lightOn"] else False

    def setHeadsetStatus(self, isOn):
        with shelve.open(filename) as db:
            db["lightOn"] = isOn
