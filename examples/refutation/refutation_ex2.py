from sympy import symbols, Implies, Not, And
from sympy.logic.boolalg import truth_table

# Função para verificar se é uma refutação
def is_refutation(expr, symbols):
    table = list(truth_table(expr, symbols))
    return not any(row[1] for row in table)  # Nenhuma linha deve tornar a expressão verdadeira

## Verifique se há contradição no conjunto de fórmulas:
# 1. Se o estudante tem boas notas em matemática (p), então ele passará no vestibular (q).
# 2. Se o estudante passar no vestibular (q), então ele será admitido na universidade (r).
# 3. Se o estudante é admitido na universidade (r), então ele não precisará de bolsa de estudos (¬s).
# 4. O estudante tem boas notas em matemática (p) e necessita de bolsa de estudos (s).

# Definição dos símbolos
p, q, r, s = symbols('p q r s')

# Definição das premissas
premise1 = Implies(p, q)
premise2 = Implies(q, r)
premise3 = Implies(r, Not(s))
premise4 = And(p, s) 

# Combinando todas as premissas, e checando a contradição
expr = And(premise1, premise2, premise3, premise4)

# Imprimindo a expressão
print(f"Expressão: {expr}")

# Verificando se é uma refutação
is_refut = is_refutation(expr, [p, q, r, s])
print(f"A fórmula é uma refutação válida (contradição)? {is_refut}")

# Gerando a tabela verdade para a expressão combinada
table = list(truth_table(expr, [p, q, r, s]))
print("Tabela Verdade:")
for row in table:
    print(row)
