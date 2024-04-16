
from decimal import Decimal
from datetime import datetime

titulo = '> Sistema Bancário <'
menu = '''
Operações disponíveis:

    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Sair
    
Informe a operação desejada: '''
movimentacoes = f'   Data    | {'Hora'.center(8, ' ')} | {'Operação'.center(6, ' ')} | {'Valor'.center(10, ' ')}'

saldo = 0
extrato = []
quantidade_saques = 0
LIMITE_QUANTIDADE_SAQUES = 3
LIMITE_SAQUE = Decimal('500')

while True:
    print(titulo.center(100, '-') + '\n' * 1)
    operacao = int(input(menu))
    operacao_selecionada = ''
    print('\n')
    
    if operacao == 1:
        print('> Depósito <'.center(100, '-') + '\n' * 1)
        valor = Decimal(input('Por favor, informe o valor a ser depositado: '))
        
        if valor > 0:
            saldo += valor
            operacao_selecionada = 'DEPÓSITO'
            print(f'\nDepósito de R$ {str(f'{valor:.2f}').replace('.', ',')} realizado com sucesso!\n')
        
        else:
            print('\nOperação cancelada! Por favor informe um valor positivo.\n')
    
    elif operacao == 2:
        print('> Saque <'.center(100, '-') + '\n' * 1)
        print(f'ATENÇÃO! Existe o limite de 3 saques por dia.\n')
        valor = Decimal(input('Por favor, informe o valor a ser sacado (máx: R$ 500,00): '))
        
        if valor > saldo:
            print('\nOperação cancelada! Saldo insuficiente.\n')
            
        elif valor > LIMITE_SAQUE:
            print('\nOperação cancelada! Excedeu o limite.\n')
        
        elif quantidade_saques >= LIMITE_QUANTIDADE_SAQUES:
            print('\nOperação cancelada! Excedeu o limite de saques por dia (máx: 3).\n')
        
        elif valor > 0 :
            saldo -= valor
            operacao_selecionada = 'SAQUE'
            quantidade_saques += 1
            print(f'\nSaque de R$ {str(f'{valor:.2f}').replace('.', ',')} realizado com sucesso!\n')
    
    elif operacao == 3:
        print('> Extrato <'.center(100, '-') + '\n' * 1)
        print(f'\nSaldo: R${saldo:.2f}\n')
        
        if len(extrato) == 0:
            print('\nNão há operações registradas\n')
        else:
            print(f'\nMovimentações realizadas:\n\n{movimentacoes}\n')
            for operacao in extrato:
                print(operacao)
            print('\n')
    
    elif operacao == 4:
        print('Saindo... \n\n')
        break
    
    else:
        print('Operação não existente!\nPor favor, informe apenas uma das operações informadas acima.\n')
    
    if len(operacao_selecionada) > 0:
        data_hora = datetime.now()
        dh_formatada = data_hora.strftime("%d/%m/%Y - %H:%M:%S")
        valor_formatado = f'R$ {valor:.2f}'
        extrato.append(f'{dh_formatada} - {operacao_selecionada.center(8, ' ')} - {valor_formatado.replace('.', ',')}')
