# > ESTRUTURAS CONDICIONAIS

idade = 18

if idade >= 18:
    print("Voce é maior de idade.")
else:
    print("Voce é menor de idade.")

"""
Imagine que voce queira imprimir aprovado caso o estudante tenha uma media superior a 7,
reprovado caso a media seja inferior a 7. Para isso, voce pode usar a estrutura condicional if-else:

"""
# Exercicio: Calcular a media de um estudante e imprimir aprovado ou reprovado
# media = float(input("Digite a media do estudante: "))

# # Verificar se a media é maior ou igual a 7, o estudante é aprovado
# if media >= 7:
#     print("Voce foi aprovado!")
#     # Se a media for maior ou igual a 5, o estudante fica de recuperação
# elif media >= 5:
#     print("Voce ficou de recuperação!")
#     # Se a media for inferior a 7, o estudante é reprovado
# else:
#     print("voce foi reprovado!")

# Exercicio: Calcular a media e a presenca de um estudante e imprimir aprovado, recuperação ou reprovado
media = 10
presenca = 100

# Verificar se a media é maior ou igual a 7 e a presenca é maior ou igual a 75, o estudante é aprovado
if media >= 7 and presenca >= 75:
    print("Voce foi aprovado!")
# Se a media for maior ou igual a 5 e a presenca for maior ou igual a 75, o estudante fica de recuperação
elif media >= 5 and presenca >= 75:
    print("Voce ficou de recuperação!")
# Se a media for inferior a 5 ou a presenca for inferior a 75, o estudante é reprovado
else:
    print("Voce foi reprovado!")