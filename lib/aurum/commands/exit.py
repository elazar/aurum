from .. import command

import sys

class Exit(command.Command):

    def do_all(self, params):
        sys.exit(0)
