# %%
alunos = ["Ana", "Bruno", "Carlos"]
alunos

# %%
alunos[0] = "Marcos"
alunos

# %%
alunos[1] = 0.0
alunos

# %%
del alunos[0]
alunos

# %%
x = 2
x = 3

""" Mutabilidade, portanto, em listas são maneiras de modificar os elementos
de forma controlada através dos índices.
"""

"""
Com isso entendido, vamos ao conceito de Tuplas.
Tuplas são estruturas de dados semelhantes às listas, mas com uma diferença fundamental: 
são imutáveis. Isso significa que, uma vez criadas, não podemos alterar seus elementos, 
adicionar novos elementos ou remover elementos existentes.
"""
# %%
valores = [1,2,3]
valores = (1,2,3)
type(valores)

#Já se eu tentar modificar uma posição da tupla
valores[0] = 100 # TypeError: 'tuple' object does not support item assignment

# As operações de leitura do índice da tupla, faço normalmente

valores[1] # 2
valores[-1] # 3

"""
Qual o sentido de termos uma estrutura de dados imutável como a tupla?
Previne alterações acidentais nos dados por parte de desenvolvedores.
Por outro lado, tuplas são bastante utilizadas para trazerem tipos de estrutura de dados 
mais complexos, como registros ou coordenadas, onde a imutabilidade é desejável.
"""

