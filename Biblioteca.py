class ContaBancaria():
    def __init__(self,numero, nome, tipo):
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 0

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def ativarContar(self):
        if self.status == False:
            print(f"A conta {self.numero}, de {self.nome}, Conta Ativada com Sucesso!")
            self.status = True
        else:
            print(f"A conta {self.numero}, de {self.nome}, Não pode ser Ativada, pois já está ativa!")

    def sacarValor(self, valor):
        if self.status == True and self.saldo + self.limite >= valor:
            self.saldo = self.saldo - valor
            print(f"O valor sacado {valor}, foi aceito!")

    def verificarSaldo(self):
        if self.status == True:
            print(f"Seu saldo é de {self.saldo}!")
        else:
            print(f"A sua conta {self.numero}, está inativa!")

    def ajustarLimite(self, novoLimite):
        self.limite += novoLimite     
