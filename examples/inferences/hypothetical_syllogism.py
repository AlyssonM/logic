from sympy import symbols, And, Not, Implies
from sympy.logic.boolalg import truth_table

# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

# Definindo símbolos
P, Q, R = symbols('P Q R')

# Criando as premissas e a conclusão
# (P -> Q, Q -> R) => P -> R
premise1 = Implies(P, Q)
premise2 = Implies(Q, R)
conclusion = Implies(P, R)

# Usando SymPy para verificar se a conclusão segue das premissas
# (Premise1 and Premise2) => Conclusion should be a tautology
expr = Implies(And(premise1, premise2), conclusion)
print(expr)
is_valid = is_tautology(expr, [P, Q, R])
print(f"Silogismo Hipotético é válido? {is_valid}")

# Gerando a tabela verdade para a expressão combinada
table = list(truth_table(expr, [P, Q]))
print("Tabela Verdade:")
for row in table:
    print(row)