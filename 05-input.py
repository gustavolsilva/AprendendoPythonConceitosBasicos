# %%
# Função input(): Função embutida que lê dados do teclado
x = input() # Lê uma linha do teclado
print("O valor de input é " + x) # Exibe o que foi lido

# %%
# Parametros opcionais para o input(). input(prompt,())
x = input(prompt="Digite um número: ")
print("O valor digitado foi: " + x)

# %%
# Podemos pegar de um valor digitado e garantir realmente que ele é um número fazendo uma conversão com a função int()
x = input(prompt="Digite um número: ")
x_num = int(x) # Converte a string digitada para um número inteiro
print(x_num + 10) # Exibe o número digitado mais 10

# Caso eu não fizesse a conversão:
print(x + 10) # Exibe a string digitada mais 10, o que causaria um erro
# TypeError: can only concatenate str (not "int") to str

# Se passarmos valor literal causará um erro
x = input(prompt="Digite um número: ") # supondo que passaremos a string dfasdfasdfas
x_num = int(x) # Converte a string digitada para um número inteiro
print(x_num + 10) # Logo se a string passada for dfasdfasdfas, teremos um erro
# ValueError: invalid literal for int() with base 10: 'dfasdfasdfas'
