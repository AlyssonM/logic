from sympy import symbols, Or, Not, And
from sympy.logic.inference import satisfiable

## Usando a inferência por resolução, determine se a conclusão 'r' pode ser derivada a partir das premissas anteriores.
# 1. p ∨ q
# 2. ¬p ∨ r
# 3. q ∨ ¬r

# Definindo os símbolos
p, q, r = symbols('p q r')

# Definindo as cláusulas
clause1 = Or(p, q)
clause2 = Or(Not(p), r)
clause3 = Or(Not(q), Not(r))

# Tentando derivar r usando resolução
# Adicionamos a negação da conclusão para verificar a refutação
expr = And(clause1, clause2, clause3, Not(r))

# Verificando se o conjunto é insatisfatível (o que implicaria que r pode ser derivado)
result = not satisfiable(expr)

# Saída
print("Pode 'r' ser derivado?", result)
