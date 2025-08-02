# Variaveis, de forma simples: São nomes específicos para vincular valores para poder acessá-los posteriormente.

# Exemplo: Area de um Circulo
# Formula: A = π * r²

print(3.14 * 5**2)  # Cálculo direto - Resultado: 78.5

# Isso deixa o código sem clareza e dificíl de entender.
# Vamos usar variáveis para tornar o código mais claro.
pi = 3.14  # Atribuindo o valor de pi a uma variável
raio = 5  # Atribuindo o valor do raio a uma variável
raio_ao_quadrado = raio ** 2  # Calculando o raio ao quadrado
print(pi * raio_ao_quadrado)  # Usando as variáveis para calcular a área do círculo - Resultado: 78.5

# Regras para nomes de variaveis:
# 1. Somente letras, números e o caractere de sublinhado(underscore) (_).
# 2. Não pode começar com número.
# 3. Não pode conter espaços.
# 4. Não pode ser uma palavra reservada do Python (como 'if', 'for', 'while', etc.).
# 5. Nomes de variáveis são sensíveis a maiúsculas e minúsculas (por exemplo, 'raio' e 'Raio' são diferentes).

# Exemplos de nomes válidos de variáveis:
nome = "João"
idade = 30
altura_em_metros = 1.75

# Exemplos de nomes inválidos de variáveis:
# 1nome = "Maria"  # Começa com número
# idade-anos = 25  # Contém um hífen
# nome completo = "Ana"  # Contém espaço
# if = "teste"  # Palavra reservada do Python

# Existe um "bug" que faz você atribuir um valor a uma função, o que não é recomendado.
# Exemplo:

print("oi") # Isso é uma função, mas não é uma variável.

print = 2 # Atribuindo um valor à função print, o que não é recomendado.

print("Ola")    # Isso causará um erro, pois agora 'print' não é mais uma função, mas sim uma variável com valor 2.
# Para evitar isso, é melhor usar nomes de variáveis que não sejam iguais a funções ou palavras reservadas do Python.
# Por exemplo, use 'mensagem' em vez de 'print'.
mensagem = "Olá, mundo!"
print(mensagem)  # Isso funcionará corretamente, pois 'mensagem' é uma variável
# e não interfere na função 'print'.
