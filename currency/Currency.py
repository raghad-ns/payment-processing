CURENCIES = {
    "USD": 3.73,
    "EUR": 4.15,
    "ILS": 1.00,
    "JOD": 5.26,
    "EGP": 0.076 
}

# This class is responsible for currency conversion only
class Currency:
    @classmethod
    def convert_currency(self, order):
        order.total_price /= CURENCIES[order.currency]