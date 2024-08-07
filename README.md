# Lógica Proposicional com SymPy

Este repositório contém exemplos e exercícios sobre introdução à lógica proposicional utilizando a biblioteca SymPy.

## Estrutura do Repositório

- **examples**: Exemplos de inferências, refutações e tautologias.
  - **inferences**: Exemplos de inferências clássicas.
    - `modus_ponens.py`
    - `modus_tollens.py`
    - `hypothetical_syllogism.py`
    - ...

  - **refutation**: Exemplos de refutações.
    - `refutation_ex1.py`
    - `refutation_ex2.py`
    - ...

  - **tautology**: Exemplos de tautologias.
    - `tautology_ex1.py`
    - `tautology_ex2.py`
    - ...

  - **resolution**: Exemplos de inferência por resolução e FNC.
    - `fnc_ex1.py`
    - `fnc_ex2.py`
    - `fnc_ex3.py`

- **exercises**: Exercícios de diferentes níveis de dificuldade.
    - `exercise1.py`
    - `exercise2.py`
    - ...


## Como Usar

1. No terminal (prompt de comando), direcione o caminho para o diretório de interesse utilizando o comando _cd_. Clone o repositório utilizando o comando git clone. Para usar os comandos git é necessário ter o [Git](https://git-scm.com/downloads) instalado:
```bash
   git clone https://github.com/AlyssonM/logic.git
   cd logic
```
ou faça o download da pasta em Code -> Download ZIP, descompacte o arquivo em um diretório. Abra um terminal na pasta descompactada ('logic'). 

2. Instale as dependências:
```bash
    pip install -r requirements.txt
```

3. Explore os exemplos e exercícios:
```bash
    cd examples/inferences
    python modus_ponens.py
```
A execução de programas Python é realizada com o comando python _nomeArquivo.py_

## Para Contribuição com o repositório

1. Crie uma nova branch:
```bash
    git checkout -b minha-branch
```

2. Faça suas alterações e commit:
```bash
    git commit -am 'Adicionando novo exemplo de inferência'
```

3. Envie suas alterações:
```bash
    git push origin minha-branch
```

4. Crie um pull request.


## Referências

* [Documentação do SymPy](https://docs.sympy.org/latest/reference/public/logic/index.html#logic)
* [PEREIRA, S. do L. Lógica Proposicional. 2010](https://www.ime.usp.br/~slago/IA-logicaProposicional.pdf>)

