# open/closed

from abc import ABC, abstractmethod


class Customer(ABC):
    
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_discount_rate(self) -> float:
        pass


class SilverCustomer(Customer):

    def get_discount_rate(self) -> float:
        return 0.2


class GoldCustomer(Customer):

    def get_discount_rate(self) -> float:
        return 0.3


class VipCustomer(Customer):

    def get_discount_rate(self) -> float:
        return 0.4


class Discount:
   def __init__(self, customer: Customer, price):
       self.customer = customer
       self.price = price
   
   def give_discount(self) -> float:
       return self.price * self.customer.get_discount_rate()


if __name__ == "__main__":
    orders = [
       Discount(SilverCustomer('Raj'), 100),
       Discount(GoldCustomer('John'), 100),
       Discount(VipCustomer('Ahmad'), 100),
    ]

    for item in orders:
        print(f'Dicount for {item.customer.name} = {item.give_discount()}')
