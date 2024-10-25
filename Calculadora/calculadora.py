from time import sleep
from math import sqrt

print('Bem-Vindo á calculadora Simples!')

print('-=' * 20)
print('''Selecione o tipo de operação desejada:
[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
[ 5 ] Potencia
[ 6 ] Resto da divisão
[ 7 ] Raiz quadrada''')

print('=-' * 20)

while True:
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('-' * 30)
        resultado = num1 + num2
        sleep(1)
        print(f'O resultado de {num1} + {num2} é de: {resultado}')
    elif opcao == 2:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('-' * 30)
        resultado = num1 - num2
        sleep(1)
        print(f'O resultado de {num1} - {num2} é de: {resultado} ')
    elif opcao == 3:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('-' * 30)
        resultado = num1 * num2
        sleep(1)
        print(f'O resultado de {num1} * {num2} é de: {resultado}')
    elif opcao == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        print('-' * 30)
        resultado = num1 / num2
        sleep(1)
        print(f'O resultado de {num1} / {num2} é de: {resultado}')
    elif opcao == 5:
        num1 = float(input('Digite o segundo número: '))
        num2 = float(input('Elevado a quanto: '))
        print('-' * 30)
        resultado = num1 ** num2
        sleep(1)
        print(f'O resultado de {num1} ** {num2} é de: {resultado}')
    elif opcao == 6:
        num1 = float(input('Digite o segundo número: '))
        num2 = float(input('Digite o segundo número: '))
        print('-' * 30)
        resultado = num1 % num2
        sleep(1)
        print(f'O resultado de {num1} % {num2} é de: {resultado}')
    elif opcao == 7:
        num1 = float(input('Digite um número para calcular a raiz quadrada: '))
        print('-' * 30)
        resultado = sqrt(num1)
        sleep(1)
        print(f'A raiz de {num1} é {resultado}!')
    else:
        print('Operação Inválida. Tente novamente!')
    sleep(1)
    print('-' * 30)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responnda apenas S ou N. ')
    if resp == 'N':
        break
    print('-' * 30)

print('=-' * 20)
print('Obrigado, Volte sempre!')
print('=-' * 20)
