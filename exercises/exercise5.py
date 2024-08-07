from sympy import symbols, Or, Not, And, satisfiable


## Considere o argumento:
# "Se um software é testado, então ele é confiável. Se não é confiável, então não deve ser lançado. 
#   O software foi testado. Logo, deve ser lançado."

# Tarefas:
# * Traduza as premissas e a conclusão para símbolos lógicos.
# * Coloque as premissas e a negação da conclusão em FNC.
# * Determine se a conclusão pode ser logicamente derivada.

# TODO: Defina os símbolos ex.:
# p, q = symbols('p q')

# TODO: Definindo as cláusulas:
premise1 = False
premise2 = False

# TODO: Negativa da Conclusão para teste:
neg_conclusion = False

# TODO: Construindo a expressão com todas as premissas e a negação da conclusão
expr = False

# Usando satisfiable para verificar se a formulação é insatisfatória
result = satisfiable(expr)

# Saída
print("A fórmula é insatisfatória, ou seja, a conclusão é derivável?", not result)
if not result:
    print("A conclusão 'não estou trabalhando' pode ser logicamente derivada das premissas.")
