import os

os.system("cls")
# inicializando um conjunto vazio
conjunto = set()
print(conjunto)
print("---------------------------")

# exibindo elementos de um set
numeros = [5, 4, 1, 2, 2, 3, 3, 3]
conjunto = set(numeros)
print(numeros)
print(conjunto)
print("---------------------------")


# add - adicionando elementos em um set
numeros = [5, 4, 1, 2, 2, 3, 3, 3]
conjuntos = set()
for num in numeros:
    conjunto.add(num)
print(numeros)
print(conjunto)
print("---------------------------")


# remove - remove um elemento do set -> se o elemento existir
conjunto = {1, 2, 3}
print(conjunto)
conjunto.remove(2)
print(conjunto)
"""
conjunto.remove(4)
print(conjunto)
"""
print("---------------------------")


# discard - remove um elemento do set -> se existr, porem não da erro de compilação
conjunto = {1, 2, 3}
print(conjunto)
conjunto.discard(2)
print(conjunto)
conjunto.discard(4)
print(conjunto)
print("---------------------------")

#clear() - remove todos os elementos de um set



# ======= OPERAÇÕES MATEMÁTICAS COM CONJUNTOS ========
# union - união de dois conjuntos
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a.union(b)
print(c)
print("---------------------------")

# | - união de dois conjuntos - OPERADOR
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a | b
print(c)
print("---------------------------")

# intersection - efetua uma intersecção entre dois conjuntos
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a.intersection(b)
print(c)
print("---------------------------")

# & - efetua uma intersecção entre dois conjuntos - OPERADOR
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a & b
print(c)
print("---------------------------")


# =======================================================
planetas = {"mercurio", "venus", "terra", "marte"}
print(planetas)
# operador de associação in
print("terra" in planetas) # vai retornar True
print("plutao" not in planetas) # vai retornar True
print("---------------------------")

# ============= COMPARAÇÃO DE CONJUNTOS (SETS) =====================
planetas1 = {"terra", "venus", "mercurio", "marte"}
planetas2 = {"terra", "venus", "mercurio", "marte", "saturno"}
print(planetas1 == planetas2)
print(planetas1 != planetas2)
print("---------------------------")


# < - verifica se o conjunto da esquerda está na direita
planetas1 = {"terra", "venus", "mercurio", "marte"}
planetas2 = {"terra", "venus", "mercurio", "marte", "saturno"}
print(planetas1 < planetas2)
print("---------------------------")

# diference ou "-" -> a diferença entre dois conjuntos é um conjunto contendo os elementos da esquerda que não estão no da direita
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
print(planetas1 - planetas2)
print(planetas2 - planetas1)
print(planetas1.difference(planetas2))
print("---------------------------")

# diferença simétrica - esquerda comparado com o da direita e vice-versa
# ^ ou .symmetric_difference
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
print(planetas1 ^ planetas2)
print(planetas1.symmetric_difference(planetas2))
print("---------------------------")


# disjuntos: não possuem nenhum elemento em comum
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
planetas3 = {"jupiter", "urano", "saturno"}
print(planetas1.isdisjoint(planetas2))
print(planetas1.isdisjoint(planetas3))
print("---------------------------")


# |= - faz a união com ordem aleatória
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = {"terra", "jupiter", "urano", "saturno", "marte"}
planetas1 |= planetas2
print(planetas1)
print("---------------------------")

# copiando conjuntos
planetas1 = {"venus", "mercurio", "terra", "netuno", "marte"}
planetas2 = planetas1.copy()
print(planetas1)
print(planetas2)
print("---------------------------")

# pop() - remove um elemento aleatóriamente
planetas = {"venus", "mercurio", "terra", "netuno", "marte"}
print(planetas)
planetas.pop()
print(planetas)
print("---------------------------")


# casting
lista = [1, 2, 3, 3, 3, 4]
conjunto = set(lista)
print(lista)
print(conjunto)
lista2 = list(conjunto)
print(lista)
print(lista2)