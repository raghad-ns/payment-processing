
from Logger import Logger
from payment.IPayment import Payment
from payment.IPayment_validation import Validation

class Paypal_payment(Payment, Validation):
    def process_payment (self, order):
        if (self.validate_payment()):
            logger = Logger()
            # print(logger) # This will print the logger instance
            logger.log("payment proceeded by paypal!")
            return order.total_price + 5
    
    def validate_payment(self):
        # Assuming valid payment
        return True
