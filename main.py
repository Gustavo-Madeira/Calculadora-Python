class Calculadora:
    def __init__(self):
        pass
    def soma(self, n1, n2):
        return n1 + n2
    def subtrair(self, n1, n2):
        return n1 - n2
    def multi(self, n1, n2):
        return n1 * n2
    def div(self, n1, n2):
        if n2 != 0:
            return n1 / n2
        else:
            return 'ERRO: Não existe divisão por zero'

calcular = Calculadora()
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digete o 2° número: '))

print(f'Soma = {calcular.soma(n1, n2)}\nSubtração = {calcular.subtrair(n1, n2)} \nMultiplicação = {calcular.multi(n1, n2)} \nDivisão = {calcular.div(n1, n2)}')
