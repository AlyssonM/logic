from sympy import symbols, Implies, Not, And
from sympy.logic.boolalg import truth_table

# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

# Definindo os símbolos
P, Q = symbols('P Q')

# Criando as premissas e a conclusão (Substitua True pelas expressões adequadas)
# (P -> Q, P)-> Q
## TODO
premise1 = 1
premise2 = 1
conclusion = 1

# Verificando se a conclusão segue das premissas
# (Premise1 and Premise2) => Conclusion should be a tautology
expr = Implies(And(premise1, premise2), conclusion)

# Imprimindo a expressão
print(f"Expressão: {expr}")

# Verificando se é uma tautologia
is_valid = is_tautology(expr, [P, Q])
print(f"A fórmula é válida? {is_valid}")

# Gerando a tabela verdade para a expressão combinada
table = list(truth_table(expr, [P, Q]))
print("Tabela Verdade:")
for row in table:
    print(row)
