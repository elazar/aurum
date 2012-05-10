from .. import command

class Ls(command.Command):

    def do_global(self, params):
        dsn = self.config.dsn
        keys = dsn.keys()
        width = len(max(keys, key=len))
        for name in keys:
            print name.ljust(width) + "  " + dsn[name]
