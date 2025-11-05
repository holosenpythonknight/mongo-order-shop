from db import get_db

shopDB = get_db()
baskets = shopDB["baskets"]


class BasketRepository:

    def create(self, obj):
        return baskets.insert_one(obj)

    def read(self, filter):
        return baskets.find_one(filter)

    def upsert(self, filter, value):
        return baskets.update_one(filter, value, upsert=True)
