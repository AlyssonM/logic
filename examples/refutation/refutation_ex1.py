from sympy import symbols, And, Not
from sympy.logic.boolalg import truth_table


# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

# Definindo símbolos
P = symbols('P')

# Criando a expressão
expr = Not(And(P, Not(P)))

# Verificando se a expressão é uma tautologia (refutação)
is_taut = is_tautology(expr, [P])
print(f"A expressão {expr} é uma tautologia? {is_taut}")
