from repository.CustomerRepository import CustomerRepository

customer_repo = CustomerRepository()


class CustomerService:

    def create_bulk(self, lst):
       return customer_repo.create_bulk(lst)
        
    def create(self, obj):
        return customer_repo.create(obj)


