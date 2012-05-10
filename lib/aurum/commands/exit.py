from .. import command

class Exit(command.Command):

    def do_all(self, params):
        return True
