from .. import command, context

from sqlalchemy import create_engine
from sqlalchemy.engine import reflection, url
from sqlalchemy.engine.url import make_url

class Cd(command.Command):

    sep = "/"

    def do_all(self, params):
        if len(params) == 0:
            segments = [self.sep]
        else:
            segments = params.split(self.sep)

        # Handle absolute paths
        if (segments[0] == ""):
            segments.pop(0)

        # Handle relative paths
        else:
            segments = filter(None, [
                self.context.dsn,
                self.context.database,
                self.context.table,
                self.context.column
                ] + segments)

        try:

            # Handle the DSN
            dsn = segments.pop(0)
            if dsn not in self.config.dsn:
                print "aurum: DSN not found: " + dsn + "..."
                return
            self.context.dsn = dsn
            self.context.engine = create_engine(self.config.dsn[dsn])
            inspector = reflection.Inspector.from_engine(self.context.engine)

            # Handle the database
            parsed_dsn = make_url(self.config.dsn[dsn])
            database = parsed_dsn.database
            if database == None:
                databases = inspector.get_schema_names()
                database = segments.pop(0)
                if database not in databases:
                    print "aurum: Database not found in DSN " + dsn + ": " + database + "..."
                    return
            self.context.database = database

            # Handle the table
            table = segments.pop(0)
            tables = inspector.get_table_names(database)
            if table not in tables:
                print "aurum: Table not found in database " + database + ": " + table + "..."
                return
            self.context.table = table

            # Handle the column
            column = segments.pop(0)
            columns = [column.name for column in inspector.get_columns(table, database)]
            if column not in columns:
                print "aurum: Column not found in table " + table + ": " + column + "..."
                return
            self.context.column = column

        except IndexError:
            pass
