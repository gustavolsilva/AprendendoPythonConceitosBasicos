"""
while loop: Executa enquanto a condição for verdadeira
"""
# %%

n = 0

while n < 3:
    print(f"O valor de {n}")
    n += 1 # n = n + 1

print("O Loop acabou")

# %%

# Logo a variavel de condição de paradaeração, tem que ser declarada, pois sem ela, gera um loop infinito

while n < 3:
    print(f"O valor de {n}")
    # n = n + 1

print("O Loop acabou") 
# loop infinito
