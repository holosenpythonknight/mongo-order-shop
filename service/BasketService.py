from repository.BasketRepository import BasketRepository

basket_repo = BasketRepository()


class CustomerService:
    def create(self, obj):
        return basket_repo.create(obj)
