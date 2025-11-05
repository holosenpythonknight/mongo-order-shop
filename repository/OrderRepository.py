from db import get_db

shopDB = get_db()
orders = shopDB["orders"]


class OrderRepository:

    def create(self, obj):
        return orders.insert_one(obj)

    def create_bulk(self, lst):
        return orders.insert_many(lst)

    def read(self, filter):
        return orders.find_one(filter)

    def read_all(self, filter, map):
        return orders.find(filter, map)

    def upsert(self, filter, value):
        return orders.update_one(filter, value, upsert=True)

    def delete_all(self, filter):
        return orders.delete_many(filter)

    def aggregate(self, filter, group, sort, limit):
        return orders.aggregate([filter, group, sort, limit])
