import textwrap
import pandas as pd
from decimal import Decimal
from datetime import datetime


def menu():
    titulo = '> Sistema Bancário <'
    menu = f'''
    {titulo.center(100, '-')}
    
    Operações disponíveis:

        [1] - Depósito
        [2] - Saque
        [3] - Extrato
        [4] - Novo Usuário
        [5] - Nova Conta
        [6] - Listar Contas
        [7] - Sair

    Informe a operação desejada: '''

    return input(textwrap.dedent(f'\n{menu}'))


def depositar(saldo: Decimal, valor: Decimal, extrato: list, /):
    if valor > 0:
        saldo += valor
        print(f'\nDepósito de R$ {str(f'{valor:.2f}').replace('.', ',')} realizado com sucesso!\n')
        extrato = registrar_movimento('DEPÓSITO', valor, extrato)

        return {'saldo': saldo, 'extrato': extrato}

    else:
        print('\nOperação cancelada! Por favor informe um valor positivo.\n')


def sacar(*, saldo: Decimal, valor: Decimal, extrato: list, limite: Decimal, quantidade_saques: int,
          limite_saques: int):
    if valor > saldo:
        print('\nOperação cancelada! Saldo insuficiente.\n')

    elif valor > limite:
        print('\nOperação cancelada! Excedeu o limite.\n')

    elif quantidade_saques >= limite_saques:
        print('\nOperação cancelada! Excedeu o limite de saques por dia.\n')

    elif valor > 0:
        saldo -= valor
        quantidade_saques += 1
        print(f'\nSaque de R$ {str(f'{valor:.2f}').replace('.', ',')} realizado com sucesso!')
        extrato = registrar_movimento('SAQUE', valor, extrato)

        return {'saldo': saldo, 'extrato': extrato, 'quantidade_saques': quantidade_saques}

    else:
        print('\nOperação cancelada! Por favor informe um valor positivo.\n')


def exibir_extrato(saldo: Decimal, /, *, extrato: list):
    if saldo <= Decimal(0):
        print('\nNão foram realizadas movimentações\n')
    else:
        print(f'\nSaldo: R${saldo:.2f}\n')
        print(f'\nMovimentações realizadas:\n')

        datas_horas = []
        operacoes = []
        valores = []

        for movimentacao in extrato:
            datas_horas.append(movimentacao['data_hora'])
            operacoes.append(movimentacao['operacao'])
            valores.append(movimentacao['valor'])

        data = {
            'Data - Hora': datas_horas,
            'Operação': operacoes,
            'valor': valores
        }

        df = pd.DataFrame(data)

        print(df)


def filtrar_usuario(cpf: str, usuarios: list) -> tuple | None:
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario

    return None


def criar_usuario(usuarios: list):
    endereco = {'logradouro': '', 'nº': '', 'bairro': '', 'cidade': '', 'estado': ''}

    while True:
        correto = ''

        nome_completo = input('Nome completo (obrigatório): ')
        data_nascimento = input('Data de nascimento (dia/mês/ano): ')
        cpf = input('CPF (obrigatório): ')

        for key in endereco.keys():
            field = f'{key.capitalize()}: ' if key != 'estado' else f'Sigla do {key.capitalize()}: '
            valor = input(field)
            endereco[key] = valor

        if len(nome_completo) > 0 and len(cpf) > 0:
            while True:
                dados = f'''
                    Nome Completo: {nome_completo}
                    Data de Nascimento: {data_nascimento}
                    CPF: {cpf}
                    Endereço: {endereco['logradouro']}, {endereco['nº']} - {endereco['bairro']} - {endereco['cidade']}/{endereco['estado']}
                '''
                correto = input(f'{dados}\nOs dados estão corretos? (S-Sim | N-Não): ')

                if correto.upper() == 'S' or correto.upper() == 'N':
                    break

        else:
            print('\nNome e CPF são campos obrigatórios!\n\n')

        if correto.upper() == 'S':
            usuario = {
                'nome': nome_completo,
                'data_nascimento': data_nascimento,
                'cpf': cpf,
                'endereco': f'{endereco['logradouro']}, {endereco['nº']} - {endereco['bairro']} - {endereco['cidade']}/{endereco['estado']}'
            }

            if filtrar_usuario(cpf, usuarios) is None:
                usuarios.append(usuario)
                print('\nUsuário criado com sucesso!')
                break

            else:
                print('\nOperação cancelada! usuário já está cadastrado.')
                break


def criar_conta(agencia: str, numero_conta: str, usuarios: list):
    cpf = input('Informe seu CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario is None:
        print('Operação cancelada! cpf não encontrado, crie um usuário.')
        return None

    else:
        print(f'''
        \nConta criada com sucesso!

        Agência: {agencia}
        Nº da conta: {numero_conta}
        Nome: {usuario['nome']}
        CPF: {usuario['cpf']}
        ''')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}


def listar_contas(contas: list):
    if len(contas) > 0:
        agencias = []
        numeros_contas = []
        nomes = []
        cpfs = []

        for conta in contas:
            agencias.append(conta['agencia'])
            numeros_contas.append(conta['numero_conta'])
            nomes.append(conta['usuario']['nome'])
            cpfs.append(conta['usuario']['cpf'])

        data = {
            'Agência': agencias,
            'Nº da Conta': numeros_contas,
            'Nome': nomes,
            'CPF': cpfs
        }

        df = pd.DataFrame(data)

        print(df)

    else:
        print('Não existem contas registradas.')


def registrar_movimento(operacao: str, valor: Decimal, extrato: list) -> list:
    data_hora = datetime.now()
    dh_formatada = data_hora.strftime("%d/%m/%Y - %H:%M:%S")
    valor_formatado = f'R$ {valor:.2f}'
    movimentacao = {'data_hora': dh_formatada, 'operacao': operacao, 'valor': valor_formatado}
    extrato.append(movimentacao)

    return extrato


def main():
    LIMITE_SAQUE = Decimal('500')
    LIMITE_QUANTIDADE_SAQUES = 3
    AGENCIA = '0001'

    saldo = Decimal(0)
    quantidade_saques = 0

    extrato = []
    usuarios = []
    contas = []

    while True:
        operacao = menu()
        print('\n')

        if int(operacao) == 1:
            print('> Depósito <'.center(100, '-') + '\n' * 1)
            valor = Decimal(input('Por favor, informe o valor a ser depositado: '))
            resultado = depositar(saldo, valor, extrato)

            if type(resultado) is dict:
                saldo = resultado['saldo']
                extrato = resultado['extrato']

        elif int(operacao) == 2:
            print('> Saque <'.center(100, '-') + '\n' * 1)
            print(f'ATENÇÃO! Existe o limite de {LIMITE_QUANTIDADE_SAQUES} saques por dia.\n')
            valor = Decimal(input(f'Por favor, informe o valor a ser sacado (máx: R$ {LIMITE_SAQUE:.0f},00): '))

            resultado = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_SAQUE,
                quantidade_saques=quantidade_saques,
                limite_saques=LIMITE_QUANTIDADE_SAQUES
            )

            if type(resultado) is dict:
                saldo = resultado['saldo']
                extrato = resultado['extrato']
                quantidade_saques = resultado['quantidade_saques']

        elif int(operacao) == 3:
            print('> Extrato <'.center(100, '-') + '\n' * 1)
            exibir_extrato(saldo, extrato=extrato)

        elif int(operacao) == 4:
            print('> Novo Usuário <'.center(100, '-') + '\n' * 1)
            criar_usuario(usuarios)

        elif int(operacao) == 5:
            print('> Nova Conta <'.center(100, '-') + '\n' * 1)
            conta = criar_conta(AGENCIA, numero_conta=str(len(contas) + 1), usuarios=usuarios)

            if conta is not None:
                contas.append(conta)

        elif int(operacao) == 6:
            print('> Listar Contas <'.center(100, '-') + '\n' * 1)
            listar_contas(contas)

        elif int(operacao) == 7:
            print('Encerrando... \n\n')
            break

        else:
            print('Operação não existente!\nPor favor, digite uma das operações informadas acima.\n')


if __name__ == "__main__":
    main()
