from django.db.backends.base.schema import BaseDatabaseSchemaEditor


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    def create_model(self, model):
        pass

    def delete_model(self, model):
        pass

    def alter_db_table(self, model, old_db_table, new_db_table):
        pass

    def alter_field(self, model, old_field, new_field, strict=False):
        pass

    def remove_field(self, model, field):
        pass

    def add_field(self, model, field):
        pass