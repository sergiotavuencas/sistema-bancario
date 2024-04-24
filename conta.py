from decimal import Decimal

from cliente import Cliente
from historico import Historico


class Conta:
    def __init__(self, numero: int, cliente: Cliente) -> None:
        self._saldo = Decimal('0')
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente: Cliente, numero: int):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor) -> bool:
        saldo = self.saldo

        if valor > 0:
            if valor <= saldo:
                self._saldo -= valor
                return True

        return False

    def depositar(self, valor) -> bool:
        if valor > 0:
            self._saldo += valor
            return True

        return False

    def __repr__(self) -> str:
        return f"Conta(agencia: {self._agencia}, numero: {self._numero}, cliente: {self._cliente}, \
        saldo: {self._saldo})"

    def __str__(self) -> str:
        return f"Agência: {self._agencia}\nNúmero: {self._numero}\nCliente: {self._cliente}\n\
        Saldo: R$ {self._saldo:.2f}"
