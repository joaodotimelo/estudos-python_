# Python — Revisão Completa (Fundamentos, Operadores, Strings + Exercícios 1-21)

---

# PARTE 1 — TEORIA

## 1.1 Tipos de Dados

| Tipo | Representa | Exemplo |
|---|---|---|
| `int` | Números inteiros | `idade = 25` |
| `float` | Números decimais | `altura = 1.75` |
| `str` | Texto | `nome = "João"` |
| `bool` | Verdadeiro/Falso | `ativo = True` |
| `None` | Ausência de valor | `resultado = None` |

### Função `type()`
Retorna o tipo de um dado — usada pra depurar, validar entrada de `input()`, checar retorno de função, ou dado vindo de API/arquivo/banco.
```python
print(type(25))     # <class 'int'>
print(type("oi"))    # <class 'str'>
```

### Conversão de tipos (Type Casting)
```python
int("10")       # texto → inteiro
float("3.14")    # texto → decimal
str(25)          # número → texto

idade = int(input("Idade: "))     # input() sempre retorna str — converter na captura
```

### Concatenação com `+`
Só funciona entre strings — número precisa virar `str()` antes.
```python
"Idade: " + str(25)
```

### Quebra de linha `\n`
```python
print("Linha 1\nLinha 2")
```

---

## 1.2 Operadores Aritméticos

| Operador | Nome | Exemplo | Resultado |
|---|---|---|---|
| `+` | Soma | `5 + 2` | `7` |
| `-` | Subtração | `5 - 2` | `3` |
| `*` | Multiplicação | `5 * 2` | `10` |
| `/` | Divisão | `5 / 2` | `2.5` (sempre `float`) |
| `//` | Divisão inteira (piso) | `5 // 2` | `2` |
| `%` | Módulo (resto) | `5 % 2` | `1` |
| `**` | Potenciação | `5 ** 2` | `25` |

**Atenção:** `//` arredonda pra baixo (floor), não "trunca" — com negativos, `-7 // 2` dá `-4`, não `-3`.
`%` é muito usado pra par/ímpar (`n % 2 == 0`) e pra "quebrar" valores em partes (exercício das notas de dinheiro).

## 1.3 Operadores Relacionais

| Operador | Significado |
|---|---|
| `==` | Igual a (comparação) |
| `!=` | Diferente de |
| `>` `<` `>=` `<=` | Maior, menor, maior/igual, menor/igual |

**⚠️ Nunca confundir `=` (atribuição) com `==` (comparação).**

## 1.4 Operadores Lógicos

| Operador | Regra |
|---|---|
| `and` | Todas as condições precisam ser `True` |
| `or` | Pelo menos uma precisa ser `True` |
| `not` | Inverte uma única condição |

```python
if (idade >= 18 or acompanhado) and tem_ingresso:
```
**Regra de ouro:** sempre que misturar `and`/`or`, usar parênteses explícitos — a precedência padrão (`and` antes de `or`) pode gerar bugs silenciosos.

---

## 1.5 Strings — Indexação e Slicing

- Índice positivo começa em `0`; índice negativo começa em `-1`.
- **O índice final do slice é sempre EXCLUSIVO.**

```python
nome = "João"
nome[0]        # 'J'
nome[-1]       # 'o' (último)
nome[0:2]      # 'Jo' (índices 0 e 1, o 2 fica de fora)
nome[:3]       # do início até o índice 3 (exclusivo)
nome[2:]       # do índice 2 até o final
nome[:]        # string inteira
nome[:-1]      # tudo, exceto o último caractere
nome[0:4:2]    # de 2 em 2
nome[::-1]     # inverte a string inteira
```

**Regra de ouro (últimos/primeiros N caracteres):**
```python
string[-N:]    # ÚLTIMOS N caracteres
string[:-N]    # TUDO exceto os últimos N caracteres  (não confundir a posição do -N!)
```

`len(string)` retorna quantidade de caracteres (conta a partir de 1). `len(string) - 1` dá o índice do último caractere.

## 1.6 F-string
```python
f"Meu nome é {nome} e tenho {idade} anos"
f"{valor:.2f}"     # formata com 2 casas decimais
```

## 1.7 Métodos de String

| Método | Faz o quê |
|---|---|
| `.upper()` / `.lower()` | Maiúsculo / minúsculo |
| `.strip()` / `.lstrip()` / `.rstrip()` | Remove espaços (fim+início / só esquerda / só direita) |
| `.replace(antigo, novo)` | Substitui texto (retorna NOVA string, original não muda) |
| `.replace(antigo, novo, qtd)` | Substitui só as N primeiras ocorrências |
| `.find(procurado)` | Retorna índice da 1ª ocorrência, ou `-1` se não achar |
| `.find(procurado, inicio, fim)` | Busca num intervalo específico |
| `.count(procurado)` | Conta quantas vezes aparece |
| `.isdigit()` | `True` se só números |
| `.isalpha()` | `True` se só letras |
| `.isalnum()` | `True` se só letras e/ou números |
| `.isupper()` / `.islower()` | `True` se está em maiúsculo / minúsculo |

**Importante:** métodos de validação (`isdigit`, `isalpha`, etc.) retornam `bool` de verdade — não precisa comparar com `== True`/`== False`, usa direto no `if` (ou com `not`).

---

# PARTE 2 — PONTOS DE ATENÇÃO (erros que já caí e como reconhecer)

| Armadilha | Exemplo errado | Correção |
|---|---|---|
| `=` vs `==` | `if idade = 18` | `if idade == 18` |
| `len()` é função, não método | `senha.len()` | `len(senha)` |
| Comparar bool com `== True/False` | `if ativo == True` | `if ativo:` |
| `.find()` retorna número, não bool | `if texto.find(" ")` | `if texto.find(" ") != -1` |
| Slicing últimos N caracteres invertido | `nome[:-3]` | `nome[-3:]` |
| Maiúscula/minúscula na comparação | `if letra == 'a'` | `if letra.lower() == 'a'` |
| `and`/`or` sem parênteses | `if a >= 18 and b or c` | `if (a >= 18 and b) or c` |
| Condições que se sobrepõem — ordem importa | isósceles antes de equilátero | testar o caso **mais restritivo primeiro** |
| Checagem redundante dentro de `else` | repetir `and freq >= 75` dentro do `else` que já garante isso | confiar na estrutura do `if/else` |
| `for` tentando percorrer um número | `for x in valor_dependente` (int) | usar multiplicação direta, `for` é pra percorrer coleções |
| Código duplicado esquecido | copiar/colar sem apagar versão antiga | sempre reler o arquivo inteiro antes de considerar pronto |

**Regra de ouro geral sobre `if/elif/else`:** perguntar sempre — *"essas condições podem ser verdadeiras ao mesmo tempo?"* Se sim, a ordem importa (mais restritiva primeiro). Se as faixas são naturalmente exclusivas (como faixas de salário/nota), a ordem não importa.

---

# PARTE 3 — EXERCÍCIOS 1 A 21 (enunciado + solução final)

### Exercício 1 — Soma de dois números (tipos e conversão)
```python
numero = int(input('Digite um número: '))
numero2 = int(input('Digite mais um número: '))
soma = f"A soma dos dois números é {numero + numero2}"
print(soma)
```

### Exercício 2 — Maior de idade + CNH (relacionais/lógicos)
```python
idade = int(input('Digite sua idade: '))
possui_cnh = True

if idade >= 18 and possui_cnh:
    print(f"A sua idade é {idade} e você pode dirigir")
else:
    print(f"A sua idade é {idade} e você não pode dirigir pois é menor de idade")
```

### Exercício 3 — Par ou ímpar (módulo)
```python
numerox = int(input('Digite um número: '))
if numerox % 2 == 0:
    print(f"O número {numerox} é par")
else:
    print(f"O número {numerox} é ímpar")
```

### Exercício 4 — Slicing básico
```python
frase = "Auditoria de Sistemas"
print(frase[0:9])     # Auditoria
print(frase[13:21])   # Sistemas
print(frase[::-1])    # invertida
```

### Exercício 5 — F-string + cálculo
```python
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
idade_futura = idade + 5
print(f"O {nome} tem {idade} anos e daqui a 5 anos terá {idade_futura} anos.")
```

### Exercício 6 — Desconto de produto
```python
preco_produto = float(input('Digite o preço do produto: '))
desconto = int(input('Digite o valor do desconto: '))
desconto_valor = (desconto / 100) * preco_produto
valor_final = preco_produto - desconto_valor
print(f"O valor final do seu produto já com o desconto aplicado é de R${valor_final:.2f}")
```

### Exercício 7 — CPF via slicing
```python
cpf = "532.553.838-11"
slice1 = cpf[0:3]
slice2 = cpf[4:7]
slice3 = cpf[8:11]
slice4 = cpf[12:]
slice_concatenado = slice1 + slice2 + slice3 + slice4
print(slice_concatenado)
```

### Exercício 8 — Triângulo (validação + classificação)
**Ponto de atenção que caiu aqui:** ordem das condições — equilátero precisa ser testado ANTES de isósceles.
```python
lado1 = int(input('Digite o lado do triângulo: '))
lado2 = int(input('Digite o lado do triângulo: '))
lado3 = int(input('Digite o lado do triângulo: '))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if (lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3):
        print('Seu triângulo é escaleno')
    elif (lado1 == lado2) and (lado1 == lado3):
        print('Seu triângulo é equilátero')
    else:
        print('Seu triângulo é Isósceles')
else:
    print('Esses lados não formam um triângulo válido')
```

### Exercício 9 — E-mail (strip, lower, find)
```python
email = input('Digite seu email: ').strip().lower()
print(email.find("@"))
```

### Exercício 10 — Validação de CPF (replace + isdigit)
**Ponto de atenção:** medir o tamanho DEPOIS de limpar a pontuação, não antes.
```python
cpf_completo = input("Digite seu CPF: ")
cpf_limpo = cpf_completo.replace(".", "").replace("-", "")

if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')
```

### Exercício 11 — Validação de senha (múltiplas regras)
```python
senha = input('Digite uma senha: ').strip().lower()
tamanho_senha = len(senha)
posicao_espaco = senha.find(" ")
tem_numero = any(caractere.isdigit() for caractere in senha)

if tamanho_senha >= 8 and tem_numero and posicao_espaco == -1:
    print('A sua senha é válida')
else:
    print('A sua senha é inválida')
    if tamanho_senha < 8:
        print('Sua senha deve ter no mínimo 8 caracteres.')
    if posicao_espaco != -1:
        print('Sua senha não pode ter espaços')
    if not tem_numero:
        print('Sua senha precisa ter pelo menos 1 número')
```

### Exercício 12 — Idade a partir do ano de nascimento
```python
data_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = 2026
print(f"Você tem {ano_atual - data_nascimento} anos.")
```

### Exercício 13 — Contar ocorrências de letra
```python
frase = input('Digite uma frase: ').lower()
print(frase.count('a'))
```

### Exercício 14 — Desconto condicional com formatação
```python
produto = input('Digite o nome de um produto: ')
preco = float(input('Digite o preço desse produto: '))

if preco > 50:
    valor_atual = preco - preco * 0.10
    print(f"{produto}: preço original R${preco:.2f}, com desconto de 10% o valor final é R${valor_atual:.2f}")
else:
    print(f"{produto}: preço original R${preco:.2f}, sem desconto (valor final igual ao original: R${preco:.2f})")
```

### Exercício 15 — Validação de nome de usuário
```python
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
```

### Exercício 16 — Aprovação escolar (média + frequência)
**Ponto de atenção:** frequência baixa "vence" qualquer nota — por isso é checada primeiro, e depois, dentro do `else`, não precisa reconfirmar frequência (já é garantida).
```python
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
```

### Exercício 17 — Maior de dois números
```python
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))

if num1 == num2:
    print('Os dois números são iguais')
elif num1 > num2:
    print(f"O {num1} é maior que {num2}")
else:
    print(f"O {num2} é maior que {num1}")
```

### Exercício 18 — Vogal + maiúscula/minúscula
```python
palavra = input("Digite uma palavra: ")

if palavra[0].lower() == 'a' or palavra[0].lower() == 'e' or palavra[0].lower() == 'i' or palavra[0].lower() == 'o' or palavra[0].lower() == 'u':
    print('Sua palavra começa com vogal')
else:
    print('Sua palavra começa com consoante')

if palavra[0].isupper():
    print('Sua palavra começa com letra maiúscula!')
else:
    print('Sua palavra começa com letra minúscula!')
```

### Exercício 19 — Troco em notas (// e % em sequência)
**Conceito-chave:** o resto de uma divisão vira a entrada da próxima — mesma variável sendo reatribuída várias vezes (semente do `while`).
```python
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
```

### Exercício 20 — Validação de placa
**Ponto de atenção:** `[-4:]` pega os últimos 4 caracteres (não `[:4:-1]`).
```python
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
```

### Exercício 21 — INSS progressivo + dependentes
**Ponto de atenção:** calcular dentro do `if/elif`, mas imprimir uma única vez fora — evita repetição de código.
```python
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
```

---

# PARTE 4 — O QUE VEM DEPOIS

Próximo assunto natural na trilha: **loops (`for` e `while`)** — você já sentiu a necessidade deles em pelo menos 2 momentos (exercício 19, com a repetição manual de `//`/`%`; e ao tentar usar `for` num número no exercício do INSS). Loops vão te permitir automatizar exatamente esse tipo de repetição.
