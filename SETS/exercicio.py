import os

"""
1 - Escreva  uma função que receba uma lista com elementos e retorne a quantidade de elementos únicos (distintos) na lista.

2 - Escreva uma função que receba uma lista por parâmentro e retorne a quantidade de elementos duplicados nessa lista.
"""

# ============== SUBALGORITMOS ===============
lista = [1, 2, 3, 3, 3, 4, 4]
# ----------------- 1 --------------------
def elementos_unicos(lista = list) -> None:
    os.system("cls")
    qtd_elem = set()
    for elem in lista:
        qtd_elem.add(elem)
    print(lista)
    print(qtd_elem)
    print(f"A quantidade de elementos distintos dessa lista é = {len(qtd_elem)}")

# ----------------- 2 --------------------
def elementos_duplicados(lista = list) -> None:
    os.system("cls")



# ============== PROGRAMA PRINCIPAL ===============
print(f"{lista}\n")
print("""====== MENU ======
 1 - Quantidade de elementos unicos na lista
 2 - Quantidade de elementos duplicados na lista
      """)

opcao = int(input("Escolha uma opção: "))
match(opcao):
    case 1:
        elementos_unicos(lista = list)
    case 2:
        elementos_duplicados(lista = list)
    case _:
        print("Opção inválida! Escolha 1 ou 2.")

    