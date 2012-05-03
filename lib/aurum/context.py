class Context:
    dsn = None
    database = None
    table = None
    column = None
    engine = None

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
        elif self.table == None:
            return "database"
        elif self.column == None:
            return "table"
        else:
            return "column"
