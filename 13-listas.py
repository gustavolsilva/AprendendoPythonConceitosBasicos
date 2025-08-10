"""
Listas: são uma sequencia de elementos de qualquer tipo.
Para definir uma lista basta usar colchetes [].
"""
lista = [1, 2, 3] # Uma lista com 3 elementos int
type(lista) # Retorna <class 'list'>

lista_variavel = [1, 1.0, True, "Python"] # Lista valida com diversos elementos de diferentes tipos

# Uma lista pode conter outras listas dentro
lista_misturada = [0, 1.1, "PYTHON", True, [1,2]] 
lista_misturada # Retorna [0, 1.1, "PYTHON", True, [1, 2]]

# Quando pensamos em lista, geralmente é uma estrutura que traga algo relevante
alunos = ["João", "Maria", "Pedro", "Ana"] # Lista de alunos
vendas = [100, 200, 300, 400] # Lista de vendas

# Para trabalhar com os elementos da lista, usamos a indexação
lista_misturada[0]  # Retorna 0
alunos[0]  # Retorna "João"
# Lembre-se, a indexação em listas começa em zero

# Se quisermos pegar o último elemento de uma lista pode ser:
alunos[len(alunos) - 1] # Retorna "Ana"
# que o Python permite resumir para:
alunos[-1]  # Retorna "Ana"

# No caso de uma lista dentro de lista, para pegarmos o elemento basta colocar o colchetes a mais
lista_misturada[-1][1]  # Retorna 2

# Caso você peça um índice fora da lista
lista_misturada[10]  # Retorna IndexError: list index out of range
