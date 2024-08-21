from abc import ABC,abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate_discount(self, order):
        pass