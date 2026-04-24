# Variaveis em Python

# 1. Variaveis

idade = 21 # Atribuindo o valor 21 à variável idade

print(idade)

nome ='Vinicius' # Atribuindo o valor 'Vinicius' à variável nome
print(nome)


"""
Tipos de variáveis em Python:
- int: números inteiros ou seja sem casas decimais, como 1, 2, 3, etc.
- float: números com casas decimais, como 3.14, 2.5, etc.
- str: texto, como 'Olá', 'Python', etc.
- bool: valores booleanos, que podem ser True (verdadeiro) ou False (falso).

"""

idade = 21
altura = 1.60
nome = 'Vinicius Feitosa'
estudando_python = True

print(type(idade)) # Saída: <class 'int'>
print(type(altura)) # Saída: <class 'float'>
print(type(nome)) # Saída: <class 'str'>
print(type(estudando_python)) # Saída: <class 'bool'>

# Obtendo dados do usuário e armazenando em variáveis

linguagem = input('Qual é a linguagem de programacao que voce esta aprendendo? ') # Solicita ao usuário que informe a linguagem de programação que está aprendendo
print('A linguagem de programacao que voce esta aprendendo é:', linguagem) # Exibe a linguagem de programação informada pelo usuário