from db import get_db

shopDB = get_db()
customers = shopDB["customers"]


class CustomerRepository:

    def create(self, obj):
        return customers.insert_one(obj)

    def read(self, filter):
        return customers.find_one(filter)

    def upsert(self, filter, value):
        return customers.update_one(filter, value, upsert=True)
