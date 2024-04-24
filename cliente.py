from conta import Conta
from transacao import Transacao


class Cliente:

    def __init__(self, endereco: str) -> None:
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(conta: Conta, transacao: Transacao) -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta) -> None:
        self._contas.append(conta)

    def __repr__(self) -> str:
        return f"Cliente(endereco: {self._endereco}, contas: {self._contas})"

    def __str__(self) -> str:
        return f"Endereço: {self._endereco}\nContas: {self._contas}"
