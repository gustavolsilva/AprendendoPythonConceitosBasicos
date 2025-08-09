# Formatação de Texto
# Olhando uma solução do Desafio da aula passada

# Pega inputs do usuário
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

# Faz conversões de idade
idade_futuro = int(idade) + 5
idade_futuro_str = str(idade_futuro)

# Exibe resultados do código
print("Olá, " + nome + "!")
print("Seu nome tem " + str(len(nome)) + " letras.")
print("Daqui a 5 anos, você terá " + idade_futuro_str + " anos.")

# Vamos falar agora sobre F-Strings: f é sobre formatado
print(f"Olá, {nome}!")
print(f"Seu nome tem {len(nome)} letras.")
print(f"Daqui a 5 anos, você terá {idade_futuro} anos.")

# É possivel formatar os números para serem exibidos como float com duas casas decimais
# Usando o mesmo exemplo, no caso da quantidade de letras
print(f"Seu nome tem {len(nome):.2f} letras.") # Exibirá, se colocar o nome de "João", 4.00

# Uma outra forma para Números inteiros, se eu quiser mostrar com 3 digitos: :03d
print(f"Seu nome tem {len(nome):03d} letras.") # Exibirá, se colocar o nome de "João", 004

# Caso precisemos dar um Enter, usamos o caracter \n
nome = input("Qual o seu nome?\nDigite aqui: ")

# Existe o r"" que significa raw
print(r"Isso é uma string raw: \n não será interpretado") 

