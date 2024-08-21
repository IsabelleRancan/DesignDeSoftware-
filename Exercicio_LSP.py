from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        return f"Processed {amount} using Credit Card {self.card_number}"
    
class PixProcessor(PaymentProcessor):
    def __init__(self, chave):
        self.chave = chave 

    def process_payment(self, amount):
        return f"Pagamento PIX valor {amount} para chave {self.chave}"
    
#Exemplo de uso 
def pagar(metodo: PaymentProcessor):
    metodo.process_payment()
    
cc = CreditCardProcessor(card_number="123456789")
pix = PixProcessor(chave="123.456.789-00")

print(pagar(cc))
print(pagar(pix))