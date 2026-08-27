"""
1 - Antecessor e sucessor.

Leia um número inteiro e imprima:
  - O número
  - Seu antecessor
  - Seu sucessor
"""

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print(f"O número que você escolheu foi {numero} o seu antecessor é {antecessor} e o seu sucessor é {sucessor}")


"""
2 - Média de 3 notas

Leia 3 notas de um aluno e calcule a média delas
"""
nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite mais uma nota: '))
nota3 = float(input('Digite mais uma nota: '))

media = (nota1 + nota2 + nota3) / 3
print(f"A média das suas notas foi de {media:.2f}") # O .2f é para trazer somente duas casas decimais após a vírgula

"""
3 - Manipulação de String

Leia o nome completo de uma pessoa e:
   - Imprima em maiúscula
   - Imprima em minúscula
   - Contar quantas letras tem
   - Extrair e imprimir as 3 primeiras letras
   - Extrair e imprimir as 3 últimas letras
   - substituir espaços por underscore
"""

nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome))
print(nome[0:3])
print(nome[-3:])
print(nome.replace(" ", "_"))
