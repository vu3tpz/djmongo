from django.db.backends.base.introspection import BaseDatabaseIntrospection, TableInfo


class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_table_list(self, cursor):
        # Use cursor directly to list collection names
        collection_names = cursor.list_collection_names()
        return [TableInfo(name, 't') for name in collection_names]

    def get_table_description(self, cursor, table_name):
        return []

    def get_relations(self, cursor, table_name):
        return {}

    def get_indexes(self, cursor, table_name):
        return {}