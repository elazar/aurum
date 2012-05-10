from .. import command

class Pwd(command.Command):

    def do_all(self, params):
        context = self.context
        context_type = context.get_type()
        if context_type == "global":
            print "/",
        else:
            if context_type in ("server", "database", "table", "column"):
                print "/" + context.dsn,
            if context_type in ("database", "table", "column"):
                print "/" + context.database,
            if context_type in ("table", "column"):
                print "/" + context.table,
            if context_type == "column":
                print "/" + context.column,
        print
        return False
