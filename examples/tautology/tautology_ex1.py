from sympy import symbols, And, Or, Not, Implies, Equivalent, simplify
from sympy.logic.boolalg import truth_table
from sympy.logic.inference import satisfiable


# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

# Definindo símbolos
j, g, t, c = symbols('j g t c')

# Criando as expressões das premissas
expr1 = Implies(j, g)
expr2 = Implies(Not(j), t)
expr3 = Implies(g, c)
expr4 = Not(c)

# Criando a expressão combinada das premissas
premises = And(expr1, expr2, expr3, expr4)

# Conclusão esperada
conclusion = t

# Verificando se a conclusão é derivável das premissas
combined_expr = Implies(premises, conclusion)
# Verificando se a expressão combinada é uma tautologia
is_taut = is_tautology(combined_expr, [j, c, t, g])
print(f"A expressão combinada é uma tautologia? {is_taut}")

# Gerando a tabela verdade para a expressão combinada
table = list(truth_table(combined_expr, [j, c, t, g]))
print("Tabela Verdade:")
for row in table:
    print(row)

