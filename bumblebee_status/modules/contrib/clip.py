"""Short description in RST format

   Show clipboard information
"""

import core.module
import core.widget
import core.input
import clipboard


class Module(core.module.Module):
    def __init__(self, config, theme):
        super().__init__(config, theme, core.widget.Widget(self.full_text))
        core.input.register(
            self, button=core.input.LEFT_MOUSE, cmd='copyq menu')

    def full_text(self, widgets):
        return ";".join(clipboard.paste().split('\n'))
