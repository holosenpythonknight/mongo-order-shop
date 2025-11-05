from traceback import print_tb

from service.OrderService import OrderService

order_service = OrderService()
# order1 = order_service.create({
#     "user": "Ali",
#     "amount": 450,
#     "status": "paid"
# })
# print(order1)
#

# order_service.create_bulk([{
#     "user": "Sara",
#     "amount": 220,
#     "status": "paid"
# }, {
#     "user": "Hossein",
#     "amount": 800,
#     "status": "paid"
# }])

# xxxxxx print(order_repo.read({"user": "Ali"}))
# print(order_service.read_by_user("Ali"))

# result = order_service.read_paid_above_200()
#
# for o in result:
#     print(o)


# print(order_service.accept_transaction("Hossein", 800))

# print(order_service.accept_transaction("Mohammad", 400))

# print(order_service.delete_all_by_user("Mohammad"))

result = order_service.get_report()

for o in result:
    print(o)
