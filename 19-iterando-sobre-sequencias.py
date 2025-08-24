"""
Vimos For - loop iterando com o range. Contudo, ele funciona bem
com qualquer tipo de sequencia
"""

# %%

valores = [10, 20, 30]

for valor in valores:
    print(f"O valor é: {valor}")

# %%
valores = [10, 20, 30, 3, -2, 17]

for valor in valores:
    print(f"O valor é: {valor}")

print("Acabou o Loop")
# %%

nome = "Gustavo"

for caractere in nome:
    print(f"O caractere é: {caractere}")

print("Acabou o Loop")

# %%
clientes = [("Ana", "1234567890", "ana@email.com"), ("João", "0987654321", "joao@email.com")]

for cliente in clientes:
    nome = cliente[0]
    cpf = cliente[1]
    email = cliente[2]
    print(f"Nome: {nome}\nCPF: {cpf}\nEmail: {email}\n\n")

# %%

# Dentro de listas, o Python ignora espaços em branco. Abaixo, outra maneira de organizar a lista
clientes = [
    ("Ana", "1234567890", "ana@email.com"), 
    ("João", "0987654321", "joao@email.com")
]

# %%

# Outra maneira alternativa, quando o tamanho dos elmentos da lista são fixos é colocar as variaveis antes conforme o exemplo abaixo

for cliente in clientes:
    nome, cpf, email = cliente
    print(f"Nome: {nome}\nCPF: {cpf}\nEmail: {email}\n\n")

print("Acabou o Loop")

# %%

z = (10, 20)
x, y = z
print(x, y)
# %%

