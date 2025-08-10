"""
Listas e tuplas aceitam indexação, pois são Sequências.
As Strings são Sequências de caracteres.
"""
# %%
nome = "Gustavo"
nome[0]  # 'G'
nome[3]  # 't'
nome[-1]  # 'o'

# %%
lista = [1,2,3]
lista

# %%
# Consigo fazer uma conversão para uma tupla
tuple(lista)

# %%
# Também posso retornar a conversão com a função list
list(tuple(lista))

# %%
# Com a função str funciona um pouco diferente
str(lista)
# Transforma em uma representação de strings

# %%
# e se eu passar a minha variavel nome para uma list cada letra se torna elemento da lista.

list(nome) # ['G', 'u', 's', 't', 'a', 'v', 'o']
# %%
# Uma str vazia pode ser criada
s = ""
len(s) # 0
s[0] # IndexError: string index out of range

# No caso de list

l = []
len(l) # 0
l[0] # IndexError: list index out of range

# No caso de tuple

t = ()
len(t) # 0
t[0] # IndexError: tuple index out of range

# %%

# Outra forma para criação dos elementos acima:
s = str() # ''
l = list() # []
t = tuple() # ()

# %%
# Sequencias vazias são Bool = False, se tiver qualquer elemento é True
bool(s) # False
bool(l) # False
bool(t) # False

s = " "
l = [0]
t = (0,)
bool(s) # True
bool(l) # True
bool(t) # True

# %%

# Para confirmação de sequencia em Python, basta fazer:
seq = [1,2,3]

if seq:
    print("Sequência não está vazia")
else:
    print("Sequência está vazia")

# %%
