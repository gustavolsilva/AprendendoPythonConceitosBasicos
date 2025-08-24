"""
For Loop: Repetição de ações em n número de vezes
"""

# %%
# for variavel in range(n):
for n in range(10):
    print(f"O valor de n é: {n}")

# %%
# Não necessariamente preciso usar a variavel do loop
for n in range(5):
    print("Olá!")

# %%
# Existe uma convenção de que a variável de loop deve ser chamada de _
for _ in range(5):
    print("Olá!")

# %%
# Olhando o Desafio do Acerte o numero, agora sabendo for loop

numero_secreto = 10
descobriu = False

for n in range(3):
    if not descobriu:
        chute = int(input("Descubra o número: \nSeu chute: "))
        if chute < numero_secreto:
            print("Chute muito baixo!")
        elif chute > numero_secreto:
            print("Chute muito alto!")
        else:
            print("Descobriu!")
            descobriu = True

if descobriu:
    print("Parabéns, você ganhou!")
else:
    print(f"Que pena, você perdeu! O número secreto era {numero_secreto}.")