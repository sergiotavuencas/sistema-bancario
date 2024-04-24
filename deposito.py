from decimal import Decimal

from conta import Conta


class Deposito:
    def __init__(self, valor: Decimal) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
