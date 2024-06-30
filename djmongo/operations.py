from django.db.backends.base.operations import BaseDatabaseOperations

class DatabaseOperations(BaseDatabaseOperations):
    def quote_name(self, name):
        return name

    def bulk_insert_sql(self, fields, placeholder_rows):
        return "bulk insert not supported by MongoDB"