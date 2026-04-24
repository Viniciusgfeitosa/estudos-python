# CONVERSÃO DE TIPOS

idade = '21' # A variável idade é do tipo string (str)
numero1 = '10' # A variável numero1 é do tipo string (str)
numero2 = '20' # A variável numero2 é do tipo string (str)

print(numero1 + numero2) # Saída: '1020' vai ter uma (concatenação de strings)

print(idade, type(idade)) # Saída: '21' <class 'str'>

idade_inteira = int(idade) # Convertendo a variável idade para o tipo inteiro (int)
print(idade_inteira, type(idade_inteira)) # Saída: 21 <class 'int'>

# int() - converte um valor para o tipo inteiro (int)
# float() - converte um valor para o tipo float (número com casas decimais)
# str() - converte um valor para o tipo string (str)
# bool() - converte um valor para o tipo booleano (True ou False)

altura = int(input('Informe a sua altura: ')) # Solicita ao usuário que informe a sua altura, mas o valor é do tipo string (str)
print(altura, type(altura)) # Saída: '' <class 'str'>a