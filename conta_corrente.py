from decimal import Decimal

from cliente import Cliente
from conta import Conta
from saque import Saque


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite=Decimal("500"), limite_saques=3) -> None:
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor) -> bool:
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if not valor > self._limite and not numero_saques >= self._limite_saques:
            super().sacar(valor)
            return True

        return False

    def __repr__(self) -> str:
        return f"ContaCorrente(agencia: {self._agencia}, numero: {self._numero}, cliente: {self._cliente},\
        limite: {self._limite}, limite_saques: {self._limite_saques}, saldo: {self._saldo})"

    def __str__(self) -> str:
        return f"Agência: {self._agencia}\nNúmero: {self._numero}Cliente: {self._cliente}\nSaldo: {self._saldo})"
