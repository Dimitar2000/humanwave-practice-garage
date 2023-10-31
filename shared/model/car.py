from google.cloud import ndb
from shared.system.base.model import BaseModel


class Car(BaseModel):
    """The Car model"""

    name = ndb.StringProperty(required=True)
    owner = ndb.StringProperty()
    price = ndb.FloatProperty()
    garage_id = ndb.IntegerProperty()

    # I dont know what this is used for
    note = ndb.TextProperty(indexed=False)

    @classmethod
    def list(cls, garage_id=None, name=None, owner=None, price=None, limit=20):
        """
        example normal query with filter.

        """
        with cls.ndb_context():
            query = Car.query()
            if garage_id:
                query = query.filter(Car.garage_id == garage_id)
            if name:
                query = query.filter(Car.name == name)
            elif owner:
                query = query.filter(Car.owner == owner)
            elif price:
                query = query.filter(Car.price == price)
            if limit:
                return query.fetch(limit)
            return query.fetch()
