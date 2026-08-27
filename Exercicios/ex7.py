"""🟢 MUITO FÁCIL — Exercício 22
Crie uma lista com 5 nomes de cidades (direto no código, sem input). 
Imprima: a lista inteira, a primeira cidade, e a última cidade (usando índice negativo).
"""

cidades = ['São Paulo', 'Santos', 'Diadema', 'São Caetano', 'Santo André']
print(cidades)
print(cidades[0])
print(cidades[-1])


"""🟢 FÁCIL — Exercício 23
Peça ao usuário 3 números (um de cada vez, com input), guarde os três numa lista, 
e depois imprima a lista ordenada em ordem crescente.
"""

numeros = []
num1 = int(input('Digite um número: '))
numeros.append(num1)
num2 = int(input('Digite mais um número: '))
numeros.append(num2)
num3 = int(input('Digite mais um número: '))
numeros.append(num3)
numeros.sort()
print(numeros)



"""🟡 MÉDIO — Exercício 24
Peça ao usuário uma frase qualquer. Usando .split(), transforme a frase numa lista de palavras
(separadas por espaço). Informe: quantas palavras a frase tem (len()), qual é a primeira palavra e qual é a última.
"""

frase = input('Digite uma frase aleatória: ')
frase_quebrada = frase.split(' ')
print(frase_quebrada)
print(f"A frase {frase} tem {len(frase_quebrada)} palavras")
print(f"A palavra da primeira posição da nova lista é {frase_quebrada[0]}")
print(f"A palavra da última posição da nova lista é {frase_quebrada[-1]}")


"""🟠 DIFÍCIL — Exercício 25
Você tem a lista fixa tarefas = ['Comprar pão', 'Estudar Python', 'Lavar o carro']. 
Peça ao usuário o nome de uma nova tarefa e adicione na lista. 
Depois, peça ao usuário qual tarefa ele concluiu (ele digita o texto exato) e remova ela da lista. 
Ao final, imprima a lista atualizada, e informe quantas tarefas ainda restam (len()).

(Pense: o que acontece se o usuário digitar uma tarefa que não existe na lista, na hora do .remove()? 
Ainda não precisamos tratar isso formalmente — mas fica a reflexão pra quando virmos tratamento de erros.)
"""

# Adicionar na lista
tarefas = ['comprar pão', 'estudar python', 'lavar o carro']
nova_tarefa = input('Digite uma nova tarefa: ').lower()
tarefas.append(nova_tarefa)
print(tarefas)

# Remover da lista
remover_tarefa = input('Digite a tarefa exata que você já concluiu para que seja removido da sua lista: ').lower()
if remover_tarefa not in tarefas:
    print('Não existe esse item na sua lista, por isso não é possível remover')
else:
    tarefas.remove(remover_tarefa)
    print(tarefas)  
    print(f"Ainda faltam {len(tarefas)} tarefas para você cumprir e finalizar a sua lista")



"""🔴 MUITO DIFÍCIL — Exercício 26
Você tem a lista fixa produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Mouse'] 
(repare que "Mouse" aparece duas vezes, de propósito). Sem usar for (ainda não vimos formalmente):

Informe quantas vezes "Mouse" aparece na lista (.count());
Informe em que posição (índice) ele aparece pela primeira vez (.index());
Remova uma ocorrência de "Mouse" da lista (.remove() remove só a primeira que encontrar — teste esse comportamento);
Depois de remover, informe novamente quantas vezes "Mouse" aparece (deve ter diminuído em 1, não sumido totalmente);
Por fim, transforme a lista final numa única string, separada por vírgula e espaço (", "), usando .join().

(Atenção: o .join() só funciona com listas de string — confirme que todos os itens da sua 
lista final são strings antes de aplicar.)"""

produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Mouse']
print(produtos.count('Mouse'))
print(produtos.index('Mouse'))
produtos.remove('Mouse')
print(produtos)
nova_string = ", ".join(produtos)
print(nova_string)
