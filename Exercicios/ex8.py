"""🟢 MUITO FÁCIL — Exercício 27
Crie uma lista com 4 números direto no código. Sem usar for, informe: o maior valor da lista 
(dica: existe uma função pronta pra isso, parecida com len() — pesquisa max()), o menor valor (min()), 
e a soma de todos (sum()).
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
print(max(numeros))
print(min(numeros))
print(sum(numeros))


"""🟢 FÁCIL — Exercício 28
Peça ao usuário um nome completo. Usando .split(), separe em lista de partes do nome.
Informe: o primeiro nome, o último sobrenome, e quantos "nomes" (palavras) a pessoa tem ao todo.
"""

nome_completo = input('Digite seu nome completo: ')

nome_quebrado = nome_completo.split(' ')
print(f"O seu primeiro nome é {nome_quebrado[0]}.")
print(f"O seu último nome é {nome_quebrado[-1]}")
print(f"Ao total seu nome tem {len(nome_quebrado)} palavras.")


"""🟡 MÉDIO — Exercício 29
Você tem a lista fixa carrinho = ['Notebook', 'Mouse', 'Teclado'] e a lista de preços precos = [3000, 80, 150] 
(na mesma ordem dos produtos). Peça ao usuário o nome de um produto que está no carrinho, descubra o índice dele 
(.index()), e usando esse mesmo índice na lista precos, informe o preço correspondente.

(Pense: por que as duas listas precisam estar na "mesma ordem" pra essa lógica funcionar? 
O que aconteceria se elas estivessem desalinhadas?)
"""

produtos = ['Notebook', 'Mouse', 'Teclado']
precos = [3000, 80, 150]

produto_lista = input('Digite um produto que está no seu carrinho: ')
posicao_produto = produtos.index(produto_lista)

print(f"O valor do {produto_lista} que está no seu carrinho é R${precos[posicao_produto]}.")



"""🟠 DIFÍCIL — Exercício 30
Peça ao usuário 5 números, um de cada vez, guardando numa lista. 
Sem usar for, calcule e informe a média desses números (dica: você já sabe somar tudo com sum(), 
e já sabe a quantidade com len()).
"""

lista_numeros = []

num1 = int(input('Digite um número: '))
lista_numeros.append(num1)
num2 = int(input('Digite mais um número: '))
lista_numeros.append(num2)
num3 = int(input('Digite mais um número: '))
lista_numeros.append(num3)
num4 = int(input('Digite mais um número: '))
lista_numeros.append(num4)
num5 = int(input('Digite mais um número: '))
lista_numeros.append(num5)

# Aqui eu poderia printar o resultado direto, mas eu preferi armazenar em uma variável para resutilizar depois hipotéticamente
media_lista = float(sum(lista_numeros) / len(lista_numeros))
print(media_lista)



"""🔴 MUITO DIFÍCIL — Exercício 31
Você tem duas listas fixas: funcionarios_sistema = ['ana', 'bruno', 'carlos', 'diana'] (quem tem acesso ao sistema)
e funcionarios_ativos_rh = ['ana', 'carlos', 'eduarda'] (quem está ativo no RH). Sem usar for:
Descubra e informe se "bruno" está na lista de acesso ao sistema, mas não está ativo no RH — 
isso seria uma "exceção crítica" (lembra do exercício de raciocínio que fizemos, sobre auditoria de acessos? 
Agora dá pra fazer com código de verdade);
Faça o mesmo teste pra "diana".

(Dica: você já sabe usar in e not in — o exercício 25 usou isso. Aqui você vai combinar isso com and.)
"""

funcionarios_sistema = ['ana', 'bruno', 'carlos', 'diana']
funcionarios_ativos_rh = ['ana', 'carlos', 'eduarda']
nome_a_procurar1 = "bruno"
nome_a_procurar2 = "diana"

if nome_a_procurar1 in funcionarios_sistema and nome_a_procurar1 not in funcionarios_ativos_rh:
    print('Por favor desativar o usuário do sistema, pois o mesmo tem acesso ao sistema mas está demitido no RH')
elif nome_a_procurar1 not in funcionarios_sistema:
    print('O usuário não está ativo no Sistema')
else:
    print('O usuário está ativo o RH')

if nome_a_procurar2 in funcionarios_sistema and nome_a_procurar2 not in funcionarios_ativos_rh:
    print('Por favor desativar o usuário do sistema, pois o mesmo tem acesso ao sistema mas está demitido no RH')
elif nome_a_procurar2 not in funcionarios_sistema:
    print('O usuário não está ativo no Sistema')
else:
    print('O usuário está ativo o RH')
