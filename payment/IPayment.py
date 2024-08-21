from abc import ABC,abstractmethod

# Payment interface
class Payment(ABC):
    @abstractmethod
    def process_payment(self, order):
        pass
