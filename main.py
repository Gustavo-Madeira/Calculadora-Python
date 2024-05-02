class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, n1, n2):
        return n1 + n2
    
    def sub(self, n1, n2):
        return n1 - n2
    
    def mul(self, n1, n2):
        return n1 * n2
    
    def div(self, n1, n2):
        if n2 != 0:
            return n1 / n2
        else:
            print('ERROR: Não existe divisão por 0(zero)')

calcular = Calculadora()

while True:
    print('O que você deseja calcular? 1- Soma / 2- Subtração / 3- Multiplicação / 4- Divisão / 0- Sair')
    opcao = input('Escreva o número do que deseja calcular: ')

    if opcao == '0':
        print('...Saindo...')
        break
    elif opcao == '1':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'A soma é {calcular.soma(n1, n2)}')
    elif opcao == '2':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'A subtração é {calcular.sub(n1, n2)}')
    elif opcao == '3':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'A multiplicação é {calcular.mul(n1, n2)}')
    elif opcao == '4':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        print(f'A divisão é {calcular.div(n1, n2)}')
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
