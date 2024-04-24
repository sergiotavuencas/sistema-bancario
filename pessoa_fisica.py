from datetime import date

from cliente import Cliente


class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __repr__(self) -> str:
        return f"PessoaFisica(cpf: {self._cpf}, nome: {self._nome}, data_nascimento: {self._data_nascimento},\
         endereco: {self._endereco}, contas: {self._contas})"

    def __str__(self) -> str:
        return f"CPF: {self._cpf}\nNome: {self._nome}\nData de Nascimento: {self._data_nascimento}\n\
        Endereço: {self._endereco}"
