from abc import ABC, abstractmethod

#abstract class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Paid Rs. {amount} using Credit Card")


class PayPal(PaymentMethod):

    def pay(self, amount):
        print(f"Paid Rs. {amount} using PayPal")


# Objects
card = CreditCard()
paypal = PayPal()

card.pay(5000)
paypal.pay(3000)