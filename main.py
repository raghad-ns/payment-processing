def cridit_card_payment (order):
    return order.price * 1.02

def paypal_payment (order):
    return order.price + 5

def cryptocurrency_payment(order):
    return order.price * 1.1

class Order:
    def __init__(self, items, price, payment_method):
        self.payment_method = payment_method
        self.price = price
        self.items = items
    def process_payment(self):
        self.total_price = self.payment_method(self)

order = Order(['Apple', 'Banana', 'Tomato'], 100, cryptocurrency_payment)
order.process_payment()
print(order.total_price)