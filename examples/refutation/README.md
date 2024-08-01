# Verificação de Refutação com SymPy

Este exemplo demonstra como usar a biblioteca SymPy para verificar a validade de uma refutação lógica.

## O que é uma Refutação?

Refutação é o processo de demonstrar que uma determinada proposição é falsa ao mostrar que ela leva a uma contradição. Em lógica proposicional, uma proposição é uma contradição se é falsa em todas as interpretações possíveis.

## Descrição do Script

O script a seguir usa a biblioteca SymPy para verificar se a expressão $\( \neg (P \land \neg P) \)$ é uma tautologia. Isso significa que estamos verificando se a negação de uma contradição é sempre verdadeira.

### Passos do Script

1. **Importar Bibliotecas**: Importa as funções necessárias da biblioteca SymPy.
2. **Definir Símbolos**: Cria o símbolo \(P\) que será usado para representar a proposição lógica.
3. **Criar a Expressão**: Define a expressão lógica a ser verificada.
4. **Verificar Validade**: Usa SymPy para verificar se a expressão é uma tautologia.
5. **Imprimir Resultado**: Imprime o resultado da verificação.

### Código do Script
1. Importar Bibliotecas:
```python
from sympy import symbols, And, Not
from sympy.logic.boolalg import truth_table
```
2. Definir Símbolos:
```python
# Definindo símbolos
P = symbols('P')
```
3. Criar a Expressão:
```python
# Criando a expressão
expr = Not(And(P, Not(P)))
```
Esta linha cria a expressão lógica ¬(𝑃∧¬𝑃), que é a negação de uma contradição. A expressão 𝑃∧¬𝑃 é sempre falsa, então sua negação deve ser sempre verdadeira.


4. Verificar Validade:
```python
# Função para verificar se é uma tautologia
def is_tautology(expr, symbols):
    table = list(truth_table(expr, symbols))
    return all(row[1] for row in table)

# Verificando se a expressão é uma tautologia (refutação)
is_taut = is_tautology(expr, [P])
print(f"A expressão {expr} é uma tautologia? {is_taut}")
```

Esta parte do código verifica se a expressão é uma tautologia, ou seja, se é verdadeira para todas as combinações de valores de verdade de 𝑃.

## Como Executar

1. Certifique-se de que o Python está instalado em seu computador.
2. Instale a biblioteca SymPy (caso não tenha feito anteriormente):
```bash
pip install sympy
```

3. Execute o script (o terminal deve estar direcionado para a pasta ./logic/examples/refutation/):
```bash
python refutation_ex1.py
```
Você verá a saída indicando se a expressão é uma tautologia.
