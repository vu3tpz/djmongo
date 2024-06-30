from pymongo import MongoClient
from django.conf import settings

class MongoDBClient:
    def __init__(self, *args):
        db_settings = settings.DATABASES['default']
        self.client = MongoClient(
            host=db_settings.get('HOST', 'localhost'),
            port=db_settings.get('PORT', 27017),
            username=db_settings.get('USER'),
            password=db_settings.get('PASSWORD'),
            authSource=db_settings.get('OPTIONS', {}).get('authSource', 'admin'),
            authMechanism=db_settings.get('OPTIONS', {}).get('authMechanism', 'SCRAM-SHA-1')
        )
        self.db = self.client[db_settings['NAME']]

    def get_collection(self, name):
        return self.db[name]
    
    def close(self):
        self.client.close()
    
_client_instance = None

def get_client():
    global _client_instance
    if not _client_instance:
        _client_instance = MongoDBClient()
    return _client_instance