from abc import ABC,abstractmethod
from Logger import Logger
from discounts.discount_strategies.Percentage_based_discount import Percentage_based_discount
from payment.payment_stratigies.Cryptocurrency_payment import Cryptocurrency_payment
from payment.payment_stratigies.Paypal_payment import Paypal_payment 


class Order:
    def __init__(self, items, price, payment_method, discount_strategy):
        self.payment_method = payment_method
        self.discount_strategy = discount_strategy
        self.price = price
        self.items = items
        self.total_price = price # initially it equals the initial price, without discounts or payment fees
    
    def process_payment(self):
        self.total_price = self.payment_method.process_payment(self)
    
    def apply_discount(self):
        self.total_price -= self.discount_strategy.calculate_discount(self)

order = Order(['Apple', 'Banana', 'Tomato'], 100, Cryptocurrency_payment(), Percentage_based_discount(0.5))
order.apply_discount()
order.process_payment()
order = Order(['Apple', 'Banana', 'Tomato'], 100, Paypal_payment(), Percentage_based_discount(0.5))
order.process_payment()
print(order.total_price)