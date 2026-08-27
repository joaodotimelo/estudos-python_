"""🟢 MUITO FÁCIL — Exercício 17
Peça dois números ao usuário. Informe qual dos dois é o maior (ou se são iguais).
"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))

if num1 == num2:
    print('Os dois números são iguais')
elif num1 > num2:
    print(f"O {num1} é maior que {num2}")
else:
    print(f"O {num2} é maior que {num1}")

"""🟢 FÁCIL — Exercício 18
Peça uma palavra ao usuário. Informe se ela começa com vogal (a, e, i, o, u — maiúscula ou minúscula).
"""


palavra = input("Digite uma palavra: ")

if palavra[0].lower() == 'a' or palavra[0].lower() == 'e' or palavra[0].lower() == 'i' or palavra[0].lower() == 'o' or palavra[0].lower() == 'u':
    print('Sua palavra começa com vogal')
else:
    print('Sua palavra começa com consoante')

if palavra[0].isupper():
    print('Sua palavra começa com letra maiúscula!')
else:
    print('Sua palavra começa com letra minúscula!')



"""🟡 MÉDIO — Exercício 19
Peça ao usuário um valor em reais e informe quantas notas de R$50, R$20, R$10 e R$5 seriam 
necessárias para formar esse valor, usando o menor número de notas possível.
"""

valor = int(input('Digite um valor em reais: '))

notas_50 = valor // 50
valor = valor % 50

notas_20 = valor // 20
valor = valor % 20

notas_10 = valor // 10
valor = valor % 10

notas_5 = valor // 5
valor = valor % 5

print(f"""
Notas de R$50: {notas_50}
Notas de R$20: {notas_20}
Notas de R$10: {notas_10}
Notas de R$5: {notas_5}
Valor que sobrou (não formou nota inteira): R${valor}
""")



"""🟠 DIFÍCIL — Exercício 20
Peça ao usuário uma placa de carro (formato antigo: "ABC1234", 3 letras + 4 números, sem espaço). 
Valide se o formato está correto, checando: os 3 primeiros caracteres são letras 
(.isalpha()), os 4 últimos são números (.isdigit()), e o tamanho total é exatamente 7. 
Informe qual regra falhou, se houver.
"""

placa = input('Digite a placa de uma carro no formato antigo: ')

if placa[0:3].isalpha() and placa[-4:].isdigit() and len(placa) == 7:
    print('A placa do seu carro é valida')
else:
    if not placa[0:3].isalpha():
        print('A placa do carro é inválida! Os 3 primeiros dígitos da placa devem ser obrigatóriamente letras.')
    if not placa[-4:].isdigit():
        print('A placa do carro é inválida! Os 4 últimos dígitos da placa devem ser obrigatóriamente números.')
    if len(placa) != 7:
        print('A placa do carro é inválida! A placa precisa ter obrigatóriamente 7 dígitos.')



"""🔴 MUITO DIFÍCIL — Exercício 21
Peça ao usuário o salário bruto e o número de dependentes. 
Calcule o desconto de INSS de forma progressiva (regras simplificadas):

Até R$1.500 → 7,5%
De R$1.500,01 até R$3.000 → 9%
Acima de R$3.000 → 12%

Além disso, para cada dependente, desconte um adicional fixo de R$50 do salário líquido. 
Mostre salário bruto, desconto de INSS (valor e %), desconto de dependentes, e salário líquido final — 
tudo formatado com 2 casas decimais.
"""

salario = float(input('Digite seu salário: '))
dependentes = int(input('Informe quantos dependentes você tem: '))

valor_dependente = 50

if salario <= 1500:
    desconto_inss = salario * 0.075
    desconto_fixo = 7.5
elif salario > 1500 and salario <= 3000:
    desconto_inss = salario * 0.09
    desconto_fixo = 9
elif salario > 3000:
    desconto_inss = salario * 0.12
    desconto_fixo = 12

print(f"""
Salário Bruto: R${salario:.2f}
Desconto INSS: O valor em reais é R${desconto_inss:.2f} e em porcentagem é {desconto_fixo}%
Desconto Dependentes: R${dependentes * valor_dependente:.2f}
Salário Final: {salario - desconto_inss - (dependentes * valor_dependente):.2f}
""")
