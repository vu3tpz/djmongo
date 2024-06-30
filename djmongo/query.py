from django.db.models.query import QuerySet as DjangoQuerySet
from .client import get_client


class MongoDBQuerySet(DjangoQuerySet):
    def __init__(self, model=None, query=None, using=None, hints=None):
        super().__init__(model=model, query=query, using=using, hints=hints)
        self.collection = get_client().get_collection(model._meta.db_table)

    def filter(self, **kwargs):
        results = self.collection.find(kwargs)
        return [self.model(**res) for res in results]