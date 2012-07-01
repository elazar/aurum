from .. import command

from sqlalchemy.engine.url import make_url

class Pwd(command.Command):

    def do_all(self, params):
        context = self.context
        context_type = context.get_type()
        if context_type == "global":
            path = "/"
        else:
            path = ""
            if context_type in ("server", "database", "table", "column"):
                path += "/" + context.dsn
            if context_type in ("database", "table", "column"):
                parsed_dsn = make_url(self.config.dsn[context.dsn])
                database = parsed_dsn.database
                if database == None:
                    path += "/" + context.database
            if context_type in ("table", "column"):
                path += "/" + context.table
            if context_type == "column":
                path += "/" + context.column
        print path
        return False
