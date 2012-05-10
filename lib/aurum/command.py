import types

class Command:
    def __init__(self, config, context):
        self.config = config
        self.context = context

    def _unsupported(self, params):
        if (type(getattr(self, 'do_all')) == types.MethodType):
            return self.do_all(params)
        class_name = self.__class__.__name__
        module_name = class_name.lower()
        print "aurum: Class aurum.commands.%s.%s does not support context %s" % (module_name, class_name, self.context.get_type())
        return True

    def do_global(self, params):
        return self._unsupported(params)

    def do_server(self, params):
        return self._unsupported(params)

    def do_database(self, params):
        return self._unsupported(params)

    def do_table(self, params):
        return self._unsupported(params)

    def do_column(self, params):
        return self._unsupported(params)
