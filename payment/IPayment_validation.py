from abc import ABC,abstractmethod

# Validation interface
class Validation(ABC):
    @abstractmethod
    def validate_payment(self):
        pass
