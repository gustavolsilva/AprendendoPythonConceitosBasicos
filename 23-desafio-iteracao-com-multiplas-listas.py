"""
Dados duas listas, print todos os valores que aparecerem dupliclados
"""
# %%
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
duplicados = []
for i in lista1:
    if i in lista2:
        duplicados.append(i)
print("Valores duplicados:", duplicados)
# %%

"""
Dado duas listas, printe uma mensagem dizendo se existe algumelemento em comum
entre elas ou não
"""

if len(duplicados) > 0:
    print("Existem elementos em comum.")
else:
    print("Não existem elementos em comum.")

# %%
