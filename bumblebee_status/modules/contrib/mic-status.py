"""Short description in RST format

   Show clipboard information
"""

import subprocess
import core.module
import core.widget
import core.input


class Module(core.module.Module):
    def __init__(self, config, theme):
        super().__init__(config, theme, core.widget.Widget(self.full_text))

    def full_text(self, widgets):
        command = "python3 /tmp/test.py"
        return str(subprocess.getoutput(command))
