from repository.OrderRepository import OrderRepository

order_repo = OrderRepository()


class OrderService:
    def create(self, obj):
        return order_repo.create(obj)

    def create_bulk(self, lst):
        return order_repo.create_bulk(lst)

    def read_by_user(self, user):
        return order_repo.read({"user": user})

    def read_paid_above_200(self):
        return order_repo.read_all({"amount": {"$gte": 200}, "status": "paid"},
                                   {"_id": 0, "user": 1, "amount": 1})

    def accept_order(self, user, amount):
        return order_repo.upsert({
            "user": user, "amount": amount
        }, {
            "$set": {"accepted": True, "status": "paid"}
        })

    def delete_all_by_user(self, user):
        return order_repo.delete_all({"user": user})

    def get_report(self):
        return order_repo.aggregate(
            {"$match": {"status": "paid"}},
            {"$group": {"_id": "$user", "total": {"$sum": "$amount"}}},
            {"$sort": {"total": -1}},
            {"$limit": 5}
        )
