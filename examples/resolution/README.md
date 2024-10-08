# Inferência por Resolução e a FNC (Forma Normal Conjuntiva)

A Forma Normal Conjuntiva é uma forma de expressar uma fórmula lógica como uma conjunção (E) de cláusulas, onde cada cláusula é uma disjunção (OU) de literais (variáveis ou suas negações).

## Resolução 

A resolução é uma regra de inferência que permite derivar uma nova cláusula a partir de duas cláusulas que contêm literais complementares. É uma técnica fundamental na lógica proposicional para provar a insatisfabilidade ou realizar inferências.

### Inferência por Resolução
Inferência por resolução envolve usar a regra de resolução repetidamente para simplificar cláusulas e eventualmente provar que uma conclusão específica pode ser derivada a partir das premissas fornecidas.

### Exemplos

#### Exemplo 1: Verificação de Satisfabilidade
Este exemplo verifica se um conjunto de cláusulas em FNC é satisfatível.

```python
from sympy import symbols, Or, Not, And
from sympy.logic.boolalg import satisfiable

# Definindo as variáveis
p, q, r = symbols('p q r')

# Definindo as cláusulas em FNC
clause1 = Or(p, q)
clause2 = Or(Not(p), r)
clause3 = Or(Not(q), Not(r))

# Combinando as cláusulas em uma expressão FNC
expr = And(clause1, clause2, clause3)

# Verificando a satisfabilidade
result = satisfiable(expr)

# Imprimindo os resultados
print("É satisfatível?", bool(result))
if result:
    print("Uma possível atribuição de verdade é:", result)
```

* p, q, r: símbolos lógicos usados nas cláusulas.
* '**clause1**', '**clause2**', '**clause3**': cláusulas na forma normal conjuntiva.
* **satisfiable(expr)**: função que verifica se existe alguma atribuição que satisfaça a fórmula.

#### Exemplo 2: Inferência por Resolução
Este exemplo determina se uma conclusão pode ser logicamente inferida.
```python
from sympy import symbols, Or, Not, And
from sympy.logic.boolalg import satisfiable

# Definindo as variáveis
p, q, r = symbols('p q r')

# Definindo as cláusulas
clause1 = Or(p, q)
clause2 = Or(Not(p), r)
clause3 = Or(Not(q), Not(r))

# Adicionando a negação da conclusão esperada para testar a insatisfabilidade
fnc = And(clause1, clause2, clause3, Not(r))

# Verificando se a inferência é possível
result = not satisfiable(fnc)

# Imprimindo os resultados
print("Pode 'r' ser derivado?", result)
```
* Inclui uma negação da conclusão (**Not(r)**) para aplicar a técnica de prova por contradição.
* '**not satisfiable(fnc)**': se a fórmula com a negação da conclusão é insatisfatível, então a conclusão original pode ser derivada.

#### Exemplo 3: Inferência por Resolução
O argumento lógico considerado é o seguinte:

```
"Se é feriado, então não trabalho. Hoje é feriado. Logo, não estou trabalhando hoje."
```

O objetivo deste exemplo é:

* Converter as premissas e a conclusão do argumento em cláusulas lógicas.
* Transformar essas cláusulas em Forma Normal Conjuntiva (FNC).
* Provar a conclusão usando a inferência por resolução.

O script realiza as seguintes operações:

1. Definição das Variáveis Lógicas:

    * p: representa "é feriado".
    * q: representa "trabalho".

2. Premissas e Conversão em FNC:

    * A implicação "Se é feriado, então não trabalho" é convertida para FNC como ~p | ~q.
    * A afirmação "Hoje é feriado" é diretamente p.

3. Construção da Expressão:

    * As premissas e a negação da conclusão ("estou trabalhando") são combinadas em uma única expressão FNC.

4. Verificação de Satisfabilidade:

    * A função **satisfiable** da sympy é usada para verificar se a formulação combinada é insatisfatível, indicando que a conclusão pode ser logicamente derivada das premissas.

## Como Executar

Execute os arquivos via terminal ou prompt de comando:

```bash
python fnc_ex1.py
python fnc_ex2.py
```

## Saída Esperada
Você receberá confirmações sobre a satisfabilidade das cláusulas ou a validade das inferências, juntamente com as atribuições possíveis para as variáveis, se aplicável.

