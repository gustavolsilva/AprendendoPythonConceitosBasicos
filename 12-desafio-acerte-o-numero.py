"""
Desafio - Crie um programa que:
- Escolhe um número secreto.
- Pede por um chute do usuário
- Indica se o usuário acertou ou não.
- Se não acertou, dá uma dica dizendo:
    - se o número é mais alto ou mais baixo.
- Repete isso até 3 vezes!
"""
# %%
numero_secreto = 10
descobriu = False

if not descobriu:
    chute_usuario = int(input("Chute um número!\n Seu chute é: "))
    if chute_usuario < numero_secreto:
        print("Chute muito baixo!")
    elif chute_usuario > numero_secreto:
        print("Chute muito alto!")
    else:
        print("Descobriu!")
        descobriu = True
    
if not descobriu:
    chute_usuario = int(input("Chute um número!\n Seu chute é: "))
    if chute_usuario < numero_secreto:
        print("Chute muito baixo!")
    elif chute_usuario > numero_secreto:
        print("Chute muito alto!")
    else:
        print("Descobriu!")
        descobriu = True

if not descobriu:
    chute_usuario = int(input("Chute um número!\n Seu chute é: "))
    if chute_usuario < numero_secreto:
        print("Chute muito baixo!")
    elif chute_usuario > numero_secreto:
        print("Chute muito alto!")
    else:
        print("Descobriu!")
        descobriu = True

if descobriu:
    print("Você ganhou!")
else:
    print(f"Que pena você perdeu! O número era {numero_secreto}.")
    