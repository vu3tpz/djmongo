from django.db.backends.base.creation import BaseDatabaseCreation

class DatabaseCreation(BaseDatabaseCreation):
    def create_test_db(self, *args, **kwargs):
        pass

    def destroy_test_db(self, *args, **kwargs):
        pass