"""Short description in RST format

   Show clipboard information
"""

import core.module
import core.widget
import clipboard


class Module(core.module.Module):
    def __init__(self, config, theme):
        super().__init__(config, theme, core.widget.Widget(self.full_text))

    def full_text(self, widgets):
        return "Clip:" + ";".join(clipboard.paste().split('\n'))
