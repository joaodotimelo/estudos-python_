# Métodos de Listas:

frutas1 = "Maça, Banana, Abacaxi"
frutas = ['Uva', 'Banana', 'Abacate']
print(frutas)

numeros = [1, 4, 6, 2, 7, 3]


frutas.append("laranja") # Aqui eu estou adicionando um item no final da minha lista
print(frutas)

frutas.insert(1,'morango') # Aqui eu estou adicionando um item na posição que eu quero, nesse caso eu coloquei posição 1. Parêmtros que eu preciso passar: Posição que eu quero adicionar meu item e depois o item que eu quero adicionar
print(frutas)

frutas.remove('laranja') # Aqui eu removo o item que eu passar como parâmetro
print(frutas)

frutas.pop(0) # Aqui eu removo o item pelo índice, ou seja, ele vai remover o item que estiver localizado no índice que eu passei. Se eu não passar nenhum parâmetro para o pop ele remove o último por padrão
print(frutas)

numeros.sort() # Aqui ele ordena minha lista em ordem crescente
print(numeros)

numeros.sort(reverse=True) # Aqui ele ordena minha lista em ordem decrescente
print(numeros)

print(numeros.index(2)) # Aqui ele me retorna o índice que está posicionado esse item que eu passei como parâmetro

print(numeros.count(1)) # Aqui ele me retorna a quantidade de itens que eu passei como parâmetro que existem na lista

frutas_texto = " e ".join(frutas) # Aqui eu estou convertendo minha lista em uma string. Eu passei o "e" como o separador da minha string
# Obs: O join é usado para uma lista de strings se eu colocar um número por exemplo ele vai me retornar um erro.

frutas2 = frutas1.split(', ') # Aqui eu estou convertendo minha string em uma lista e passando onde ela deve seprarar, que nesse caso é na vírgula, então toda vírgula vai ser uma separação e vai criar uma item na minha lista
print(frutas2[0])

frutas3 = frutas + frutas2 # Aqui eu estou concatenando as listas
print(frutas3)
