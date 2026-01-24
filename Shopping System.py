from abc import ABC, abstractmethod
from math import prod

class Product(ABC):
    @abstractmethod

    def get_price(self):
        pass

class PhysicalProduct(Product):
    def __init__(self,price):
        self.__price = price

    def get_price(self,cost):
        self.cost = cost

        price += cost
        print(f"Your Physicle Product price {self.__price}")


class DigitalProduct(Product):
    def __init__(self,price):
        self.__price = price

    def get_price(self,discount):
        self.discount = discount

        price -= discount
        print(f"Your Digital Product price is {self.__price}")

def calculate_total(self,product):
    calculate_total(product)
    

physical_product = PhysicalProduct()
digital_product = DigitalProduct()

physical_product.get_price(900,100)
digital_product.get_price(1200,200)