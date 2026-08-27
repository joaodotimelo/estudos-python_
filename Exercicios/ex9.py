"""🟢 MUITO FÁCIL — Exercício 32
Crie uma lista com 6 números direto no código. Sem usar for, informe: 
quantos números tem na lista (len()), e se o número 10 está presente nela (in).
"""

numeros = [1, 2, 3, 4, 5, 6]
print(len(numeros))

if 10 in numeros:
    print('O número 10 tem na lista')
else:
    print('Não existe o número 10 na lista')

"""🟢 FÁCIL — Exercício 33
Peça ao usuário uma palavra. Informe se ela é um palíndromo (você já fez isso com string antes) 
— mas dessa vez, ao invés de usar [::-1], use a lista: transforme a palavra numa lista de letras
com list(palavra), inverta com .reverse() (método novo — pesquisa como ele funciona), 
transforme de volta em string com .join(), e compare.
"""

palavra = list(input("Digite uma palavra: "))
palavra_invertida = list(reversed(palavra))
palavra_invertida_str = ", ".join(palavra_invertida)
palavra_str = ", ".join(palavra)

if palavra_str.lower() == palavra_invertida_str.lower():
    print('Sua palavra é uma palíndromo')
else:
    print('Sua palavra não é um palíndromo')



"""🟡 MÉDIO — Exercício 34
Você tem a lista fixa estoque = ['Caneta', 'Caderno', 'Borracha', 'Lápis']. Peça ao usuário o nome de um produto:
Se ele já existir no estoque, informe "Produto já cadastrado" (sem duplicar);
Se não existir, adicione na lista e informe "Produto cadastrado com sucesso".

Ao final (independente do caminho), imprima a lista atualizada.
"""

estoque = ['caneta', 'caderno', 'borracha', 'lápis']
produto = input('Digite um produto: ')

if produto in estoque:
    print(f"Temos esse produto em estoque. {estoque}")
else:
    estoque.append(produto)
    print(f"Não temos esse produto no estoque, mas acabamos de adicionar")
    print(f"Segue o estoque atualizado: {estoque}")



"""🟠 DIFÍCIL — Exercício 35
Você tem duas listas fixas de mesmo tamanho: produtos = ['Notebook', 'Mouse', 'Teclado'] 
e quantidades = [2, 15, 8] (quantidade em estoque de cada, na mesma ordem). 
Peça ao usuário o nome de um produto e a quantidade que ele quer comprar. 
Descubra o índice do produto, compare a quantidade pedida com a quantidade em estoque, 
e informe se a compra pode ser realizada ("Compra autorizada") ou não 
("Estoque insuficiente, disponível: X unidades").
"""

produtos = ['notebook', 'mouse', 'teclado']
print(f"Esses são so produtos que nós temos {produtos}")
quantidades = [2, 15, 8]
produto_solicitado = input('Qual produto você deseja comprar? ')
quantidade_solicitada = int(input('Quantos itens você quer? '))
posicao_produto = produtos.index(produto_solicitado)


if quantidade_solicitada > quantidades[posicao_produto]:
    print(f"Estoque insificiente, disponível: {quantidades[posicao_produto]} unidades.")
else:
    print('Compra autorizada')
    estoque_atual = quantidades[posicao_produto] - quantidade_solicitada
    print(f"A quantidade de estoque do {produto_solicitado} após a compra é de {estoque_atual}")

"""🔴 MUITO DIFÍCIL — Exercício 36
Você tem a lista acessos = ['ana.silva', 'bruno.costa', 'ana.silva', 'carlos.souza', 'bruno.costa', 'ana.silva']
— representando um log de acessos ao sistema (o mesmo usuário pode aparecer várias vezes). Sem usar for:

Informe quantos acessos únicos existem 
(dica: pesquisa a função set() — o que ela faz com itens repetidos numa lista? Depois use len() nesse resultado);
Informe quantas vezes especificamente "ana.silva" acessou o sistema;
Informe se "diana.melo" já acessou o sistema alguma vez."""

lista_acessos = ['ana.silva', 'bruno.costa', 'ana.silva', 'carlos.souza', 'bruno.costa', 'ana.silva']
pessoa = 'diana.melo'

acesso_unicos = set(lista_acessos)
print(f"Existem {len(acesso_unicos)} acessos únicos no sistema")

print(f"A ana acessou {lista_acessos.count('ana.silva')} vezes o sistema")

if pessoa in lista_acessos:
    print('A diana já acessou o sistema')
else:
    print('A diana nunca acessou o sistema')
