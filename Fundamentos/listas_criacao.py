# Listas: Criação e indexação

lista = ['Notebook', 'Mouse', 'Teclado']
print(lista)

lista_numeros = list(range(1,6)) # Aqui eu estou transformando o range em uma lista, ou seja, quando eu printar isso, vai me retornar uma lista com números de 1 a 5 pois o último é exclusivo
print(lista_numeros)
# Eu posso colocar vários tipos de dados dentro de uma lista como: String, Inteiro, float, none, json e etc.

print(lista[0]) # Aqui eu estou pegando o item que está na posição 0 da minha lista
print(lista[len(lista) - 1]) # Aqui eu estou pegando o último item da minha lista

print(lista[-1]) # Aqui eu estou pegando o último item da minha lista
print(lista[-2]) # Aqui eu estou pegando o penúltimo item da minha lista
print(lista[0:3]) # Aqui eu estou pegando da posição 0 a 2 da minha lista, pois o 3 é exclusivo
print(lista[::-1]) # Aqui eu estou invertendo a minha lista
print(lista[:-1]) # Aqui eu estou pegando todos os elementos da minha lista menos o último
