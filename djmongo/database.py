from .exceptions import (
    MongoDBError, MongoDBDatabaseError, MongoDBIntegrityError, MongoDBDataError,
    MongoDBOperationalError, MongoDBInternalError, MongoDBProgrammingError,
    MongoDBNotSupportedError, MongoDBInterfaceError
)

class Database:
    Error = MongoDBError
    DatabaseError = MongoDBDatabaseError
    IntegrityError = MongoDBIntegrityError
    DataError = MongoDBDataError
    OperationalError = MongoDBOperationalError
    InternalError = MongoDBInternalError
    ProgrammingError = MongoDBProgrammingError
    NotSupportedError = MongoDBNotSupportedError
    InterfaceError = MongoDBInterfaceError