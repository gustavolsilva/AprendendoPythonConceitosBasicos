"""
Desafio - crie um programa que:
- Pede por um nome de usuário e uma senha.
- Se ambos forem corretos, exibe uma mensagem de sucesso.
- Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
quando o usuário está incorreto, e quando a senha está incorreta
- O usuário/senha "corretos" podem ser definidos como variáveis dentro do próprio código
"""
# %%
# Minha Solucao
# Definindo usuário e senha corretos
usuario_correto = "Gustavo"
senha_correta = "minha senha"

usuario = input("Digite o nome de usuário: ") == usuario_correto
senha = input("Digite a senha: ") == senha_correta

if usuario and senha:
    print(f"Login bem-sucedido!")
if not usuario:
    print(f"Usuário não cadastrado.")
if not senha:
    print("Senha incorreta.")

# %%
# Solucao do Instrutor com apenas Operadores de comparação
usuario_correto = "Pedro"
senha_correta = "senha secreta"

usuario = input("Nome de usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto:
    if senha == senha_correta:
        print(f"Acesso liberado, seja bem-vindo {usuario}!")
    else:
        print(f"Senha incorreta para usuário {usuario}.")
else:
    print(f"Usuário {usuario} não cadastrado no sistema.")

# Solucao do Instrutor com os Operadores de comparação e Operadores Booleanos

usuario_correto = "Pedro"
senha_correta = "senha secreta"

usuario = input("Nome de usuário: ")
usuario_esta_correto = usuario == usuario_correto
senha_esta_correta = input("Senha: ") == senha_correta

if usuario_esta_correto and senha_esta_correta:
    print(f"Acesso liberado, seja bem-vindo {usuario}!")
if usuario_esta_correto and not senha_esta_correta:
    print(f"Senha incorreta para usuário {usuario}.")
if not usuario_esta_correto:
    print(f"Usuário {usuario} não cadastrado no sistema.")
