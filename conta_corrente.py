class ContaCorrente: 

    def __init__(self, numero : int, saldo : float):
        self.__numero = numero
        self.__saldo = saldo

    #property -- getter - pra exibir os atributos privados
    @property
    def numero(self):
        return self.__numero
        
    @property
    def saldo(self):
        return self.__saldo

    def depositar (self, valor : float): 
        if (valor > 0):
            self.__saldo = self.__saldo + valor 

    def sacar(self, valor : float):
        if (self.__saldo >= valor):
            self.__saldo = self.__saldo - valor 
        
#Utilizando a classe (Cliente)
                
c1 = ContaCorrente(1212, 100.00) #instanciação do objeto 
c2 = ContaCorrente(5050, 120.00) #instanciação do objeto 

print("Conta C1:", c1.numero, "Saldo:", c1.saldo)
