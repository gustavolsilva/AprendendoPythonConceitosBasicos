"""
Palavras chaves para controle de loops: break e continue
"""
# %%
# break: Interrompe o loop

n = 0

while n < 10:
    print(f"O valor de n é: {n}")
    n += 1
    if n == 5:
        break

print("O loop acabou")
# %%

# continue: próxima interação venha antes

for n in range(-5, 6):
    print(n)
    if n == 0:
        continue
    resultado = 1 / n
    print(f"O resultado é {resultado}")

print("O loop acabou")
# %%
# While - True

while True: # Loop infinito
    entrada = input('Digite qualquer coisa ("q" para sair): ')
    print(f"O valor digitado foi: {entrada}")
    if entrada == "q":
        break

print("Programa finalizado")

# %%

while True:
    opt = input("Escolha uma opção (1, 2) | 'q' para sair: ")
    if opt == "q":
        break
    elif opt != "1" and opt != "2":
        print("Opção invalida")
        continue
    print(f"Você escolheu a opção {opt}")

print("Programa finalizado")
