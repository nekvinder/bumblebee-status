import core.input
import core.decorators

import util.store
import util.format

class Widget(util.store.Store, core.input.Object):
    def __init__(self, full_text='', name=None, module=None):
        super(Widget, self).__init__()
        self.__full_text = full_text
        self.module = module
        self.name = name

    def index(self):
        if not self.module: return 0

        idx = 0
        for w in self.module.widgets():
            if w.id == self.id:
                return idx
            idx = idx + 1
        return -1 # not found

    def theme(self, attribute):
        attr = 'theme.{}'.format(attribute)
        if self.module:
            param = util.format.aslist(self.module.parameter(attr))
            if param and len(param) > self.index():
                return param[self.index()]
        return self.get(attr)

    def full_text(self, value=None):
        if value:
            self.__full_text = value
        else:
            if callable(self.__full_text):
                return self.__full_text(self)
        return self.__full_text

    def state(self):
        rv = []
        if self.get('state', None):
            tmp = self.get('state')
            rv = tmp[:] if isinstance(tmp, list) else [tmp]
        if self.module:
            tmp = self.module.state(self)
            rv.extend(tmp if isinstance(tmp, list) else [tmp])
        return rv

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
