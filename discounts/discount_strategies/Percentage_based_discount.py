from discounts.IDiscount import Discount

class Percentage_based_discount(Discount):
    def __init__(self, discount_percentage) :
        self.discount_percentage = discount_percentage

    def calculate_discount(self, order):
        return order.price * self.discount_percentage
