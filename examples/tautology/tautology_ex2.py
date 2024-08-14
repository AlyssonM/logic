from sympy import symbols, And, Or, Not, Implies, Equivalent, simplify
from sympy.logic.boolalg import truth_table
from sympy.logic.inference import satisfiable


# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

# Definindo símbolos
p , q = symbols('p q')

# Criando as expressões das premissas
expr1 = Implies(p, q)
expr2 = p

# Criando a expressão combinada das premissas
premises = And(expr1, expr2)

# Conclusão esperada
conclusion = q

# Verificando se a conclusão é derivável das premissas
combined_expr = Implies(premises, conclusion)
# Verificando se a expressão combinada é uma tautologia
is_taut = is_tautology(combined_expr, [p, q])
print(f"A expressão combinada é uma tautologia? {is_taut}")

# Gerando a tabela verdade para a expressão combinada
table = list(truth_table(combined_expr, [p, q]))
print("Tabela Verdade:")
for row in table:
    print(row)


