from sympy import symbols, Implies, And, Or, Not
from sympy.logic.boolalg import truth_table

# Função para verificar se uma combinação de premissas leva a uma situação impossível (refutação)
def is_refutation(expr, symbols):
    return not any(row[1] for row in truth_table(expr, symbols))


## Considere as seguintes premissas sobre uma empresa de tecnologia que está lançando um novo produto:
# P1. Se o produto é inovador ou a publicidade é eficaz, então o produto será bem recebido.
# P2. Se o produto for bem recebido, então a empresa verá um aumento na lealdade do cliente.
# P3. O produto não é inovador e a publicidade não foi eficaz.
# ∴ : A Empresa viu um aumento na lealdade

# TODO:Defina os símbolos ex.:
# p, q = symbols('p q')

# Definição das premissas lógicas
premise1 = False
premise2 = False         
premise3 = False
conclusion = True

# Combinando todas as premissas para verificar a contradição
expr = Implies(And(premise1, premise2, premise3), conclusion)

# Avaliando a refutação
#TODO: Adicione a lista de símbolos a serem usados na verificação dentro de []
is_refut = is_refutation(expr, [])

# Imprimindo resultados
print(f"A conclusão é uma contradição? {is_refut}")

# Gerando e exibindo a tabela verdade para a combinação de premissas
#TODO: Adicione a lista de símbolos a serem usados na verificação dentro de []
table = list(truth_table(expr, []))
print("Tabela Verdade:")
for row in table:
    print(f"{row[0]}: {'Verdadeiro' if row[1] else 'Falso'}")
