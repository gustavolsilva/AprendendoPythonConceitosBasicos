"""
Operadores Booleanos: são usados para combinar expressões condicionais. Eles retornam True ou False.
Os principais operadores booleanos são:
- E (and): retorna True se ambas as expressões forem True
- OU (or): retorna True se pelo menos uma das expressões for True
- NÃO (not): inverte o valor da expressão
"""
# %%
True and True  # Retorna True
True and False  # Retorna False
False and False  # Retorna False

# %%
True or True  # Retorna True
True or False  # Retorna True
False or False  # Retorna False

# %%
True
not True  # Retorna False
not False  # Retorna True

# %%

print("----- INÍCIO -----\n")

estou_com_fome = input("Estou com fome? (Digite s para sim)") == "s"
tenho_comida = input("Tenho comida? (Digite s para sim)") == "s"

if estou_com_fome and not tenho_comida:
    print("Ir ao mercado")
    print("Voltar para casa")
    print("Preparar uma refeição")
    print("Comer a comida")

if estou_com_fome and tenho_comida:
    print("Preparar uma refeição")
    print("Comer a comida")

print("\n----- FIM -----")
