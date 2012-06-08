class Context:
    dsn = None
    database = None
    table = None
    column = None
    engine = None
    inspector = None

    def get_identifier(self):
        return next(identifier for identifier in (
            self.column,
            self.table,
            self.database,
            self.dsn
            ) if identifier)

    def get_type(self):
        if self.dsn == None:
            return "global"
        if self.database == None:
            return "server"
        if self.table == None:
            return "database"
        if self.column == None:
            return "table"
        return "column"
