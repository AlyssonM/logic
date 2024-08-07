from sympy import symbols, Or, Not, And, satisfiable


## Considere o argumento:
# "Se chove, a rua fica molhada. Se a rua não fica molhada, não podemos jogar. Choveu. 
#   Não pudemos jogar. Logo, a rua estava molhada."

# Tarefas:
# * Formule logicamente as premissas e a conclusão.
# * Transforme em FNC.
# * Verifique a conclusão por inferência por resolução.

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
