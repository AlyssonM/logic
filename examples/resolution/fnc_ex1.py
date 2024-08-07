from sympy import symbols, Or, Not, And, satisfiable
from sympy.logic.boolalg import truth_table

## Verifique se o conjunto de cláusulas na FNC a seguir é satisfatível.
# 1. p ∨ q
# 2. ¬p ∨ r
# 3. q ∨ ¬r

# Definindo símbolos
p, q, r = symbols('p q r')

# Definindo as cláusulas
clause1 = Or(p, q)
clause2 = Or(Not(p), r)
clause3 = Or(Not(q), Not(r))

# Combinando as cláusulas na FNC
expr = And(clause1, clause2, clause3)

# Verificando se o conjunto de cláusulas é satisfatível
result = satisfiable(expr)

# Saída
print("É satisfatível?", bool(result))
if result:
    print("Uma possível atribuição de verdade é:", result)

# Gerando a tabela verdade para a expressão combinada    
table = list(truth_table(fnc, [p, q, r]))
print("Tabela Verdade:")
for row in table:
    print(f"{row[0]}: {'Verdadeiro' if row[1] else 'Falso'}")
