from sympy import symbols, Or, Not, And, satisfiable


## Considere o argumento:
# "Se é feriado, então não trabalho. Hoje é feriado. Logo, não estou trabalhando hoje."
# Tarefas:
# * Converta as premissas e a conclusão em cláusulas lógicas.
# * Transforme essas cláusulas em FNC.
# * Prove a conclusão usando a inferência por resolução.

# Definindo as variáveis lógicas
p, q = symbols('p q')

# Premissas e Conclusão em termos lógicos
# p: é feriado
# q: trabalho

premise1 = Or(Not(p), Not(q))  # p -> ~q convertido em FNC: ~p | ~q
premise2 = p  # Hoje é feriado

# Negativa da Conclusão para teste: q (estou trabalhando)
neg_conclusion = q

# Construindo a FNC com todas as premissas e a negação da conclusão
expr = And(premise1, premise2, neg_conclusion)

# Usando satisfiable para verificar se a formulação é insatisfatória
result = satisfiable(expr)

# Saída
print("A fórmula é insatisfatória, ou seja, a conclusão é derivável?", not result)
if not result:
    print("A conclusão 'não estou trabalhando' pode ser logicamente derivada das premissas.")
