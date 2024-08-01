# Verificação de Tautologia com SymPy

Este exemplo demonstra como usar a biblioteca SymPy para verificar se uma expressão lógica é uma tautologia, bem como verificar sua satisfatibilidade.

## O que é uma Tautologia?

Uma tautologia é uma fórmula ou expressão lógica que é verdadeira em todas as possíveis interpretações. Em outras palavras, uma tautologia é sempre verdadeira, independentemente dos valores de verdade de suas sub-expressões.

## Descrição do Script

O script a seguir usa a biblioteca SymPy para verificar se a expressão combinada $\( (\text{premise1} \land \text{premise2}) \rightarrow \text{conclusion} \)$ é uma tautologia e também verifica sua satisfatibilidade.

### Passos do Script

1. **Importar Bibliotecas**: Importa as funções necessárias da biblioteca SymPy.
2. **Definir Símbolos**: Cria os símbolos \(p\) e \(q\) que serão usados para representar as proposições lógicas.
3. **Criar as Expressões das Premissas**: Define as premissas e a conclusão da inferência.
4. **Verificar Validade**: Usa SymPy para verificar se a expressão combinada é uma tautologia.
5. **Gerar Tabela Verdade**: Gera e imprime a tabela verdade para a expressão lógica combinada.
6. **Verificar Satisfatibilidade**: Verifica se a expressão combinada é satisfatível.

### Código do Script
1. Importar Bibliotecas:
```python
from sympy import symbols, And, Or, Not, Implies, Equivalent, simplify
from sympy.logic.boolalg import truth_table
from sympy.logic.inference import satisfiable
```
Essas linhas importam as funções necessárias da biblioteca SymPy para trabalhar com lógica proposicional.

2. Definir Símbolos:
```python
# Definindo símbolos
p, q = symbols('p q')
```
Aqui, definimos 𝑝 e 𝑞 como símbolos que representam proposições lógicas.

3. Criar as Expressões das Premissas:
```python
# Criando as expressões das premissas
expr1 = Implies(p, q)
expr2 = p
```
Estas linhas criam as premissas da inferência lógica. Premissa 1 é "Se 𝑝 então 𝑞" e Premissa 2 é 𝑝.

4. Criar a Expressão Combinada e Conclusão:
```python
# Criando a expressão combinada das premissas
premises = And(expr1, expr2)

# Conclusão esperada
conclusion = q

# Verificando se a conclusão é derivável das premissas
combined_expr = Implies(premises, conclusion)
```
Estas linhas combinam as premissas e definem a conclusão esperada, criando uma expressão que verifica se a conclusão é derivável das premissas.

5. Verificar Validade (Tautologia):
```python
# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

# Verificando se a expressão combinada é uma tautologia
is_taut = is_tautology(combined_expr, [p, q])
print(f"A expressão combinada é uma tautologia? {is_taut}")
```
Esta parte do código verifica se a expressão combinada é uma tautologia, ou seja, se é verdadeira para todas as combinações de valores de verdade de 𝑝 e 𝑞.

6. Gerar Tabela Verdade:
```python
# Gerando a tabela verdade para a expressão combinada
table = list(truth_table(combined_expr, [p, q]))
print("Tabela Verdade:")
for row in table:
    print(row)
```
Essas linhas geram e imprimem a tabela verdade para a expressão combinada, mostrando todas as combinações possíveis de valores de verdade e o resultado da expressão para cada combinação.

7. Verificar Satisfatibilidade:
```python
# Verificando satisfiabilidade
is_satisfiable = satisfiable(combined_expr)
print(f"A expressão {combined_expr} é satisfatível? {is_satisfiable}")
```
Esta parte do código verifica se a expressão é satisfatível, ou seja, se existe pelo menos uma combinação de valores de verdade que torna a expressão verdadeira.

## Como Executar

1. Certifique-se de que o Python está instalado em seu computador.
2. Instale a biblioteca SymPy (caso não tenha feito anteriormente):
```bash
pip install sympy
```

3. Execute o script (o terminal deve estar direcionado para a pasta ./logic/examples/tautology/):
```bash
python tautology_ex2.py
```
Você verá a saída indicando se a expressão é uma tautologia, a tabela verdade correspondente e a satisfatibilidade da expressão.
