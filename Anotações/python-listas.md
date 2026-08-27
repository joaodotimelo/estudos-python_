# Python — Listas

## O que é

Uma lista é uma coleção **ordenada** e **mutável** de itens. Pode guardar qualquer tipo de dado — inclusive misturado (`str`, `int`, `float`, `None`, etc.) na mesma lista.

```python
lista = ['Notebook', 'Mouse', 'Teclado']
numeros = [1, 4, 6, 2, 7, 3]
```

---

## Criando lista a partir de `range()`

```python
lista_numeros = list(range(1, 6))
print(lista_numeros)   # [1, 2, 3, 4, 5]
```
Mesma regra do slicing: **o limite final é exclusivo** — `range(1,6)` vai até o `5`, não inclui o `6`.

---

## Indexação e Slicing (igual string)

Listas usam **exatamente a mesma lógica** de índice e slicing que strings.

```python
lista = ['Notebook', 'Mouse', 'Teclado']

lista[0]              # 'Notebook' (primeiro item)
lista[len(lista) - 1]  # 'Teclado' (último item, calculado)
lista[-1]              # 'Teclado' (último item, direto)
lista[-2]              # 'Mouse' (penúltimo)
lista[0:3]             # todos os itens (o 3 é exclusivo)
lista[::-1]            # lista invertida
lista[:-1]             # todos, exceto o último
```

---

## ⚠️ Diferença fundamental com string: Listas são MUTÁVEIS

String é imutável — métodos como `.replace()` retornam uma **nova** string, sem alterar a original (por isso precisávamos reatribuir: `texto = texto.replace(...)`).

**Lista é o oposto: os métodos alteram a lista original diretamente ("in-place"), sem precisar reatribuir.**

```python
frutas = ['Uva', 'Banana']
frutas.append('Abacate')   # já altera 'frutas' direto
print(frutas)               # ['Uva', 'Banana', 'Abacate']
```

**Cuidado:** `frutas = frutas.append(...)` seria um ERRO — `append()` (e a maioria dos métodos de lista) retorna `None`, não a lista. Nunca reatribua o resultado desses métodos.

---

## Métodos de Lista

### Adicionando itens

| Método | Faz o quê |
|---|---|
| `.append(item)` | Adiciona no **final** da lista |
| `.insert(posicao, item)` | Adiciona numa posição específica |

```python
frutas = ['Uva', 'Banana', 'Abacate']
frutas.append("laranja")        # ['Uva', 'Banana', 'Abacate', 'laranja']
frutas.insert(1, 'morango')      # ['Uva', 'morango', 'Banana', 'Abacate', 'laranja']
```

### Removendo itens

| Método | Faz o quê |
|---|---|
| `.remove(item)` | Remove pelo **valor** (o item em si) |
| `.pop(indice)` | Remove pelo **índice**. Sem parâmetro, remove o último |

```python
frutas.remove('laranja')   # remove o item "laranja"
frutas.pop(0)               # remove o item que está no índice 0
frutas.pop()                 # sem parâmetro: remove o último item
```

### Ordenando

```python
numeros = [1, 4, 6, 2, 7, 3]
numeros.sort()                 # ordem crescente: [1, 2, 3, 4, 6, 7]
numeros.sort(reverse=True)      # ordem decrescente: [7, 6, 4, 3, 2, 1]
```

### Buscando e contando

| Método | Faz o quê |
|---|---|
| `.index(item)` | Retorna o **índice** onde o item está |
| `.count(item)` | Retorna **quantas vezes** o item aparece |

```python
numeros.index(2)   # índice onde o número 2 está
numeros.count(1)   # quantas vezes o número 1 aparece
```

---

## Convertendo entre Lista e String

### Lista → String: `.join()`
```python
frutas = ['morango', 'Banana', 'Abacate']
frutas_texto = " e ".join(frutas)
print(frutas_texto)   # "morango e Banana e Abacate"
```
**Atenção:** `.join()` só funciona com lista de **strings**. Se a lista tiver números, dá erro (precisaria converter cada item pra `str` antes).

### String → Lista: `.split()`
```python
frutas1 = "Maça, Banana, Abacaxi"
frutas2 = frutas1.split(', ')
print(frutas2)   # ['Maça', 'Banana', 'Abacaxi']
```
O parâmetro do `.split()` define **onde** a string será "quebrada" em itens da lista.

---

## Concatenando listas

```python
frutas3 = frutas + frutas2   # junta os itens das duas listas numa lista nova
```
Igual à concatenação de string com `+`, mas aqui juntando listas inteiras.

---

## Resumo rápido de sintaxe

```python
lista = [item1, item2, item3]
list(range(a, b))

lista[i]
lista[-1]
lista[a:b]
lista[::-1]

lista.append(item)
lista.insert(posicao, item)
lista.remove(item)
lista.pop(indice)
lista.sort()
lista.sort(reverse=True)
lista.index(item)
lista.count(item)

"separador".join(lista)
string.split("separador")
lista1 + lista2
```
