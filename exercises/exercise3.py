from sympy import symbols, Implies, Not, And
from sympy.logic.boolalg import truth_table

# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

## Verifique se a fórmula 's' deriva do conjunto de fórmulas:
# 1.Se eu estudar (p), então eu passarei no exame (q).
# 2. Se eu passar no exame (q), então eu conseguirei um emprego (r).
# 3. Se eu conseguir um emprego (r), então eu terei sucesso (s).
# 4. Eu estudo (p) e tenho tempo livre (t).

# Defina os símbolos ex.:
# p, q, r = symbols('p q r')

## TODO
premise1 = False
premise2 = False
premise3 = False
premise4 = False
conclusion = True

# Verificando se a conclusão segue das premissas
# (Premise1 and Premise2) => Conclusion should be a tautology
expr = Implies(And(premise1, premise2, premise3,premise4), conclusion)

# Imprimindo a expressão
print(f"Expressão: {expr}")

# Verificando se é uma tautologia
#TODO: Adicione a lista de símbolos a serem usados na verificação dentro de []
is_valid = is_tautology(expr, [])
print(f"A fórmula é válida? {is_valid}")

# Gerando a tabela verdade para a expressão combinada
#TODO: Adicione a lista de símbolos a serem usados na tabela verdade dentro de []
table = list(truth_table(expr, []))
print("Tabela Verdade:")
for row in table:
    print(row)
