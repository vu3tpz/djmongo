from django.db.utils import (
    DatabaseError, IntegrityError, DataError, OperationalError,
    InternalError, ProgrammingError, NotSupportedError, InterfaceError
)

class MongoDBError(Exception):
    pass

class MongoDBDatabaseError(DatabaseError):
    pass

class MongoDBIntegrityError(IntegrityError):
    pass

class MongoDBDataError(DataError):
    pass

class MongoDBOperationalError(OperationalError):
    pass

class MongoDBInternalError(InternalError):
    pass

class MongoDBProgrammingError(ProgrammingError):
    pass

class MongoDBNotSupportedError(NotSupportedError):
    pass

class MongoDBInterfaceError(InterfaceError):
    pass