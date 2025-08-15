""" 
Slicing

Slicing é uma técnica utilizada para acessar partes de sequências, como listas, tuplas e strings, 
permitindo extrair sub-conjuntos de dados de forma eficiente.

"""
# %%
pessoas = ["João", "Paulo", "Clara", "Maria"]
pessoas[1]
# %%

pessoas[1:3]  # Acessa do índice 1 até o índice 2 (exclusivo)
# %%
pessoas[3:4] # Acessa o índice 3 Ele vai até o índice 4, não o incluindo
# %%
len(pessoas) # Retorna o comprimento da lista
# %%
# logo

pessoas[0:len(pessoas)]  # Acessa do índice 0 até o final da lista
# %%

# ou
pessoas[1:] # Acessa do índice 1 até o final da lista

# %%
pessoas[:3] # Acessa do início da lista até o índice 2 (exclusivo)

# %%
pessoas[:] # Acessa toda a lista

# %%
# Também funciona para str, já que tem comportamento de arrays (listas)
nome = "Gustavo"
nome[1:]
# %%
nome[:-1] # Acessa do início da string até o penúltimo caractere (exclusivo)
# %%
nome[2:5] # Acessa do índice 2 até o índice 4 (exclusivo)
# %%
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros[1:len(numeros):2]
# %%
numeros[1:len(numeros):3]

# %%
numeros[1::2]

# %%
numeros[::2]  # Acessa todos os elementos com passo 2, começando do início
# %%

numeros[::1] # Acessa todos os elementos com passo 1, começando do início

# %%
numeros[::-1] # Inverte a lista

# %%
numeros[::-2] # Inverte a lista e pega todos os elementos com passo 2
