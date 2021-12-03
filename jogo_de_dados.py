"""
Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir) e permitir que o usuário rode o script quantas vezes quiser.

Habilidades praticas a aplicar:

Tratamento de exceções
Condicionais If/Else
Input de dados
Geração de valores
Print

"""
import random

continuar = 'c'

while (continuar == 'c'):
    valor = input("Digite um valor inteiro entre 1 - 6: ")
    if (valor.isdigit()):
        valor = int(valor)
        valorAleatorio = random.randint(1,6)
        if valorAleatorio == valor:
            print(f'Parabéns vc acertou! seu número {valor}, número sorteado foi {valorAleatorio}')
        else:
            print(f'Que pena vc não acertou! seu número {valor} número sorteado {valorAleatorio}')   
    else:
        print(f'O valor digitado {valor} não é valido!') 

    continuar = input('Digite "c" para continuar ou "s" para sair: ')      


        