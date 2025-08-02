# Text:
# Texto é uma sequência de caracteres. Escrito com "" ou ''
# Se inicamos com aspas duplas, devemos terminar com aspas duplas
# Se iniciamos com aspas simples, devemos terminar com aspas simples
# A função print() exibe o texto na tela
print("Python")
# A função type() retorna o tipo de dado
print(type("Meu nome é Gustavo")) # class 'str'
print(type("500")) # class 'str'
print(type(500))   # class 'int'
print(type('500')) # class 'str'


# Se tentarmos somar um int com um str, teremos um erro
print(5 + "5")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Para evitar esse erro, convertemos o str para int
print(5 + int("5"))  # Resultado: 10

# Podemos fazer o inverso, converter um int para str
print("5" + str(5))  # Resultado: "55" (concatenando strings)
type(int("5"))  # class 'int'

int("Python")  # ValueError: invalid literal for int() with base 10: 'Python'

str(10) # Resultado: '10' (convertendo int para str)

type(str(10))  # class 'str'

# Podemos usar a função len() para contar o número de caracteres em uma string
print(len("Python"))  # Resultado: 6
print(len("Meu nome é Gustavo"))  # Resultado: 20

# A função help() pode ser usada para obter mais informações sobre uma função
help(print)  # Exibe a documentação da função print
help(len)    # Exibe a documentação da função len

"50" + "10" # Resultado: "5010" (concatenando strings)

"Olá " + "Gustavo"  # Resultado: "OláGustavo" (concatenando strings)

"30" + "____" + "???"  # Resultado: "30____???" (concatenando strings)

"Python" * 3  # Resultado: "PythonPythonPython" (repetindo a string 3 vezes)

"abc" - "c"  # TypeError: unsupported operand type(s) for -: 'str' and 'str'

len("Gustavo")  # Resultado: 7 (contando os caracteres da string) - Len = length

len("       ") # Resultado: 7 (contando os espaços em branco)

len(5)  # TypeError: object of type 'int' has no len()

# 99% os programadores procuram no Google: Ex: print function python documentation
