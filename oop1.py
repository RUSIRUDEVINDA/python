from abc import ABC, abstractmethod

class Payment(ABC):
  @abstractmethod
  def pay(self, amount):
    pass

class CreditCardPayment(Payment):
  def __init__(self, balance):
    self.__balance = balance
    
  def pay(self,amount):
    if amount <= self.__balance:
     self.__balance -= amount
     print(f"transsaction successfull your remaining credit card balance is {self.__balance}")
    else:
     print("Insufficiant account balance in your credit card")
     
class PaypalPayment(Payment):
  def __init__(self, balance):
      self.__balance = balance
    
  def pay(self,amount):
    if amount <= self.__balance:
     self.__balance -= amount
     print(f"transsaction successfull your remaining Pyapal balance is {self.__balance}")
    else:
     print("Insufficiant account balance in your Paypal account")

def process_payment(payment_method, amount):
    payment_method.pay(amount)


c1 = CreditCardPayment(1000)
c2 = PaypalPayment(500)

process_payment(c1, 300)
process_payment(c2, 200)
process_payment(c2, 400)

