# Text:
# Texto é uma sequência de caracteres
# A função print() exibe o texto na tela
print("Python")
# A função type() retorna o tipo de dado
print(type("Meu nome é Gustavo")) # class 'str'
print(type("500")) # class 'str'

# Se tentarmos somar um int com um str, teremos um erro
print(5 + "5")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Para evitar esse erro, convertemos o str para int
print(5 + int("5"))  # Resultado: 10

# Podemos fazer o inverso, converter um int para str
print("5" + str(5))  # Resultado: "55" (concatenando strings)

# Podemos usar a função len() para contar o número de caracteres em uma string
print(len("Python"))  # Resultado: 6
print(len("Meu nome é Gustavo"))  # Resultado: 20

# A função help() pode ser usada para obter mais informações sobre uma função
help(print)  # Exibe a documentação da função print
help(len)    # Exibe a documentação da função len


