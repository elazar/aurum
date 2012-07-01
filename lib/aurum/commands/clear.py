from .. import command

import os

class Clear(command.Command):

    def do_all(self, params):
        if os.name == "posix":
            os.system("clear")
        elif os.name in ("nt", "dos", "ce"):
            os.system("cls")
        else:
            print "\n" * 100
