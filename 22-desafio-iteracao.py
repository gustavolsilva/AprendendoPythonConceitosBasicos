# Desafio - Iteração
# %%
"""
Dado uma sequencia de números, calcule a soma e média dos números
ATENÇÃO: não vale usar a função sum()
"""

sequencia = [10, 20, 30, 40, 50]

soma = 0
for n in sequencia:
    soma += n
media = soma / len(sequencia)
print(f"A soma é: {soma}")
print(f"A média é: {media}")

"""
Dado uma Sequencia de números, calcule o maior valor da sequencia.
ATENÇÃO: não vale usar a função max()
"""
seq = [45, 78, 12, 90, 34]

maior = seq[0]
for n in seq:
    if n > maior:
        maior = n
print(f"O maior valor é: {maior}")


# %%
"""
Dado uma lista de palavras, print todas as palavras com pelo menos 5 caracteres.
"""
palavras = ["maçã", "banana", "laranja", "kiwi", "abacaxi"]
for p in palavras:
    if len(p) >= 5:
        print(p)
# %%
