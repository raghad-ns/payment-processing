import unittest
from order.Order import Order
from payment.payment_stratigies.Cryptocurrency_payment import Cryptocurrency_payment
from discounts.discount_strategies.Percentage_based_discount import Percentage_based_discount


class Test(unittest.TestCase):
    def test_discount(self):
        order = Order(['Apple', 'Banana', 'Tomato'], 100, Cryptocurrency_payment(), Percentage_based_discount(0.5))
        order.apply_discount()
        self.assertEqual(int(order.total_price), 50)
    
    def test_payment(self):
        order = Order(['Apple', 'Banana', 'Tomato'], 100, Cryptocurrency_payment(), Percentage_based_discount(0.5))
        order.process_payment()
        self.assertEqual(int(order.total_price), 110)

    def test_payment_with_discount(self):
        order = Order(['Apple', 'Banana', 'Tomato'], 100, Cryptocurrency_payment(), Percentage_based_discount(0.5))
        order.apply_discount()
        order.process_payment()
        self.assertEqual(int(order.total_price), 55)


if __name__ == '__main__':
    unittest.main()