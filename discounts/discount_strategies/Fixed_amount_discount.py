from discounts.IDiscount import Discount

class Fixed_amount_discount(Discount):
    def __init__(self, discount_amount) :
        self.discount_amount = discount_amount

    def calculate_discount(self, order):
        return self.discount_amount
