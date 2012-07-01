from .. import command

from fnmatch import fnmatch

class Ls(command.Command):

    def do_global(self, params):
        dsn = self.config.dsn
        keys = dsn.keys()
        width = len(max(keys, key=len))
        for name in keys:
            print name.ljust(width) + "  " + dsn[name]

    def do_server(self, params):
        databases = self.context.inspector.get_schema_names()
        self._print_filtered(databases, params)

    def do_database(self, params):
        inspector = self.context.inspector
        tables = inspector.get_table_names(self.context.database) + inspector.get_view_names(self.context.database)
        self._print_filtered(tables, params)

    def do_table(self, params):
        columns = [column["name"] for column in self.context.inspector.get_columns(self.context.table, self.context.database)]
        self._print_filtered(columns, params)

    def _print_filtered(self, items, pattern):
        if pattern:
            items = [item for item in items if fnmatch(item, pattern)]
        items.sort()
        for item in items:
            print item
