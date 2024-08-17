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
            return order.total_price * 1.02
    
    def validate_payment(self):
        # Assuming valid payment
        return True

class Paypal_payment(Payment, Validation):
    def process_payment (self, order):
        if (self.validate_payment()):
            return order.total_price + 5
    
    def validate_payment(self):
        # Assuming valid payment
        return True

class Cryptocurrency_payment(Payment, Validation):
    def process_payment(self, order):
        if (self.validate_payment()):
            return order.total_price * 1.1
    
    def validate_payment(self):
        # Assuming valid payment
        return True

# Discount interface
class Discount(ABC):
    @abstractmethod
    def calculate_discount(self, order):
        pass

class Percentage_based_discount(Discount):
    def __init__(self, discount_percentage) :
        self.discount_percentage = discount_percentage

    def calculate_discount(self, order):
        return order.price * self.discount_percentage

class Fixed_amount_discount(Discount):
    def __init__(self, discount_amount) :
        self.discount_amount = discount_amount

    def calculate_discount(self, order):
        return self.discount_amount
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
print(order.total_price)