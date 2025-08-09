"""
Desafio - Crie um programa que:
- Pede pelo seu nome e idade
- Dá oi para você
- Conta quantas letras seu nome possui
- Fala quantos anos você terá daqui a 5 anos
"""
# %%
nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))
print("Oi, " + nome + "!")
print("Seu nome tem " + str(len(nome)) + " letras")
print("Daqui a 5 anos você terá " + str(idade + 5) + " anos.")