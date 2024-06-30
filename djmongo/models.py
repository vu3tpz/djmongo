from django.db.models import Model
from .client import get_client


class MongoDBModel(Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        collection = get_client().get_collection(self._meta.db_table)
        data = self.__dict__.copy()
        if '_id' in data:
            collection.replace_one({'_id': data['_id']}, data)
        else:
            collection.insert_one(data)
        super().save(*args, **kwargs)