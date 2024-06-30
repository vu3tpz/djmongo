from django.db.backends.base.base import BaseDatabaseWrapper
from .client import get_client, MongoDBClient
from .creation import DatabaseCreation
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor
from .features import DatabaseFeatures
from .database import Database


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'mongodb'
    display_name = 'MongoDB'

    # Add required attributes for Django database backend
    data_types = {}
    data_type_check_constraints = {}
    operators = {}
    pattern_ops = {}
    reversed_data_types = {}
    client_class = MongoDBClient  # Define the client class
    features_class = DatabaseFeatures
    creation_class = DatabaseCreation
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations
    schema_editor_class = DatabaseSchemaEditor
    Database = Database  # Reference the Database class

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = self.client_class(self)
        self.ops = self.ops_class(self)
        self.creation = self.creation_class(self)
        self.introspection = self.introspection_class(self)
        self.schema_editor = self.schema_editor_class(self)
        self.features = self.features_class(self)

    def get_connection_params(self):
        # This method should return a dictionary of connection parameters
        return {
            'host': self.settings_dict.get('HOST', 'localhost'),
            'port': self.settings_dict.get('PORT', 27017),
            'name': self.settings_dict.get('NAME', ''),
            'user': self.settings_dict.get('USER', ''),
            'password': self.settings_dict.get('PASSWORD', ''),
            'options': self.settings_dict.get('OPTIONS', {}),
        }

    def get_new_connection(self, conn_params):
        return get_client()

    def create_cursor(self, name=None):
        return self.connection.db

    def init_connection_state(self):
        pass

    def close(self):
        self.client.close()

    def _rollback(self):
        pass

    def _set_autocommit(self, autocommit):
        pass

    def _start_transaction_under_autocommit(self):
        pass

    def _commit(self):
        pass