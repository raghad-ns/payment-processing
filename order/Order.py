
class Order:
    def __init__(self, items, price, payment_method, discount_strategy, currency="ILS"):
        self.payment_method = payment_method
        self.discount_strategy = discount_strategy
        self.price = price
        self.items = items
        self.currency = currency
        self.total_price = price # initially it equals the initial price, without discounts or payment fees
    
    def process_payment(self):
        self.total_price = self.payment_method.process_payment(self)
    
    def apply_discount(self):
        self.total_price -= self.discount_strategy.calculate_discount(self)
