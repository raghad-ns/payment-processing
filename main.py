from abc import ABC,abstractmethod
# Assume

# Payment interface
class Payment(ABC):
    @abstractmethod
    def process_payment(self, order):
        pass

# Validation interface
class Validation(ABC):
    @abstractmethod
    def validate_payment(self):
        pass

class Cridit_card_payment(Payment, Validation):
    def process_payment (self, order):
        if (self.validate_payment()):
            return order.price * 1.02
    
    def validate_payment(self):
        # Assuming valid payment
        return True

class Paypal_payment(Payment, Validation):
    def process_payment (self, order):
        if (self.validate_payment()):
            return order.price + 5
    
    def validate_payment(self):
        # Assuming valid payment
        return True

class Cryptocurrency_payment(Payment, Validation):
    def process_payment(self, order):
        if (self.validate_payment()):
            return order.price * 1.1
    
    def validate_payment(self):
        # Assuming valid payment
        return True

class Order:
    def __init__(self, items, price, payment_method):
        self.payment_method = payment_method
        self.price = price
        self.items = items
    def process_payment(self):
        self.total_price = self.payment_method.process_payment(self)

order = Order(['Apple', 'Banana', 'Tomato'], 100, Cryptocurrency_payment())
order.process_payment()
print(order.total_price)