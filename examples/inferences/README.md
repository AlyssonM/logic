# Verificação de Inferência Lógica com SymPy

Estes exemplos demonstram como usar a biblioteca SymPy para verificar a validade de inferências lógicas, como Modus Ponens, Modus Totens, Silogismo Hipotético, etc..

## Modus Ponens

Modus Ponens é uma forma de inferência lógica que pode ser expressa da seguinte maneira:

1. Se \(P\) então \(Q\). (\(P \rightarrow Q\))
2. \(P\) é verdadeiro.
3. Portanto, \(Q\) deve ser verdadeiro.

## Descrição do Script

O script a seguir usa a biblioteca SymPy para verificar se a inferência Modus Ponens é válida.

### Passos do Script

1. **Importar Bibliotecas**: Importa as funções necessárias da biblioteca SymPy.
2. **Definir Símbolos**: Cria os símbolos \(P\) e \(Q\) que serão usados para representar as proposições lógicas.
3. **Criar Premissas e Conclusão**: Define as premissas e a conclusão da inferência.
4. **Verificar Validade**: Usa SymPy para verificar se a conclusão segue logicamente das premissas.
5. **Gerar Tabela Verdade**: Gera e imprime a tabela verdade para a expressão lógica combinada.

### Código do Script (modus_ponens.py)

1. Importar Bibliotecas:
```python
from sympy import symbols, And, Implies, Not, Or
from sympy.logic.boolalg import truth_table
```
Essas linhas importam as funções necessárias da biblioteca SymPy para trabalhar com lógica proposicional

2. Definir Símbolos:
```python
# Definindo símbolos
P, Q = symbols('P Q')
```
Aqui, definimos P e Q como símbolos que representam proposições lógicas.

3. Criar Premissas e Conclusão:
```python
# Criando as premissas e a conclusão
# (P -> Q, P) => Q
premise1 = Implies(P, Q)
premise2 = P
conclusion = Q
```
Estas linhas criam as premissas e a conclusão da inferência lógica. Premissa 1 é "Se 𝑃 então 𝑄", Premissa 2 é 𝑃, e a Conclusão é 𝑄.

4. Verificar Validade:
```python
# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

# Usando SymPy para verificar se a conclusão segue das premissas
# (Premise1 and Premise2) => Conclusion should be a tautology
expr = Implies(And(premise1, premise2), conclusion)
is_valid = is_tautology(expr, [P, Q])
print(f"Modus Ponens é válido? {is_valid}")
```

Esta parte do código cria uma expressão que verifica se a combinação das premissas implica na conclusão. A função _is\_tautology_ verifica se essa expressão é verdadeira para todas as combinações de valores de verdade de 𝑃 e 𝑄.

5. Gerar Tabela Verdade:
```python
# Gerando a tabela verdade para a expressão combinada
table = list(truth_table(expr, [P, Q]))
print("Tabela Verdade:")
for row in table:
    print(row)
```
Essas linhas geram e imprimem a tabela verdade para a expressão combinada, mostrando todas as combinações possíveis de valores de verdade e o resultado da expressão para cada combinação.

## Como Executar

1. Certifique-se de que o Python está instalado em seu computador.
2. Instale a biblioteca SymPy (caso não tenha feito anteriormente):
```bash
pip install sympy
```

3. Execute o script (o terminal deve estar direcionado para a pasta ./logic/examples/inference/):
```bash
python exercise1.py
```
Você verá a saída indicando se Modus Ponens é válido e a tabela verdade correspondente.

