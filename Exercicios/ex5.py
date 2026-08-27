"""🟢 MUITO FÁCIL — Exercício 12
Peça ao usuário o ano de nascimento. Calcule e informe a idade da pessoa 
(considerando o ano atual como 2026), usando f-string.
"""

data_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2026

print(f"Você tem {ano_atual - data_nascimento} anos.")



"""🟢 FÁCIL — Exercício 13
Peça ao usuário uma frase. Usando métodos de string, informe: quantas vezes a letra "a" aparece na frase 
(contando maiúscula e minúscula como iguais).
"""

frase = input('Digite uma frase: ').lower()
print(frase.count('a'))


"""🟡 MÉDIO — Exercício 14
Peça ao usuário o nome de um produto e o preço. Se o preço for maior que R$50, 
aplique 10% de desconto automaticamente; caso contrário, mantenha o preço original. 
Ao final, mostre com f-string: nome do produto, preço original e preço final (com 2 casas decimais).
"""

produto = input('Digite o nome de um produto: ')
preco = float(input('Digite o preço desse produto: '))

if preco > 50:
    valor_atual = preco - preco * 0.10
    print(f"{produto}: preço original R${preco:.2f}, com desconto de 10% o valor final é R${valor_atual:.2f}")
else:
    print(f"{produto}: preço original R${preco:.2f}, sem desconto (valor final igual ao original: R${preco:.2f})")



"""🟠 DIFÍCIL — Exercício 15
Peça ao usuário um nome de usuário (para cadastro). Valide se ele atende a estas regras, informando qual(is) 
regra(s) foi(ram) violada(s) se inválido:

Tem entre 5 e 15 caracteres;
Não contém espaços;
É composto só por letras e números (.isalnum()).

"""

cadastro_usuario = input('Digite o usuário que você quer cadastrar: ').strip()

if len(cadastro_usuario) >= 5 and len(cadastro_usuario) <= 15 and cadastro_usuario.find(" ") == -1 and cadastro_usuario.isalnum():
    print(f"Usuário {cadastro_usuario} cadastrado com sucesso!")
else:
    if len(cadastro_usuario) < 5 or len(cadastro_usuario) > 15:
        print('Seu usuário não pode ser cadastrado pois não tem a quantidade de caracteres válidos!')
    if cadastro_usuario.find(" ") != -1:
        print('Seu usuário não pode ser cadastrado pois tem espaços.')
    if cadastro_usuario.isalnum() == False:
        print('Para que seja cadastrado o usuário, pode ter apenas letras e números')


"""
🔴 MUITO DIFÍCIL — Exercício 16
Peça ao usuário três notas (float) e a frequência (percentual, ex: 85). 
As regras de aprovação de uma escola são:

Média das notas maior ou igual a 7 e frequência maior ou igual a 75% → "Aprovado"
Média entre 5 e 6.99 e frequência maior ou igual a 75% → "Recuperação"
Frequência menor que 75% (independente da média) → "Reprovado por falta"
Média menor que 5 e frequência ok → "Reprovado por nota"
"""

# --- Primeira tentativa (com checagem redundante de frequência dentro do else) ---

nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite mais uma nota: '))
nota3 = float(input('Digite mais uma nota: '))
frequencia = int(input("Qual foi a sua frequência de comparecimento percentual nas aulas? "))
media = (nota1 + nota2 + nota3) / 3

if frequencia < 75:
    print('Reprovado por falta')
else:
    if media >= 7 and frequencia >= 75:
        print('Aprovado')
    if (media >= 5 and media < 7) and frequencia >= 75:
        print('Recuperação')
    if media < 5 and frequencia >= 75:
        print('Reprovado por nota')


# --- Código mais limpo e menos redundante ---

nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite mais uma nota: '))
nota3 = float(input('Digite mais uma nota: '))
frequencia = int(input("Qual foi a sua frequência de comparecimento percentual nas aulas? "))
media = (nota1 + nota2 + nota3) / 3

if frequencia < 75:
    print('Reprovado por falta')
else:
    if media >= 7:
        print('Aprovado')
    if media >= 5 and media < 7:
        print('Recuperação')
    if media < 5:
        print('Reprovado por nota')

"""Aqui eu removi o 'and frequencia >= 75' pois a primeira validação automaticamente 
   valida se é maior ou não, pois:

   O primeiro 'if' (frequencia < 75) já filtra e "sai" do fluxo (imprime 'Reprovado por 
   falta' e não entra no else). Ou seja, para qualquer código chegar até o bloco 'else', 
   significa que a condição 'frequencia < 75' foi FALSA — e o oposto lógico disso é 
   'frequencia >= 75'.

   Por isso, dentro do else, não preciso checar 'frequencia >= 75' de novo: essa condição 
   já é garantidamente verdadeira só por eu estar ali dentro. Checar de novo não mudaria 
   o resultado, só repetiria uma verificação que o próprio fluxo do if/else já fez por mim.
"""
