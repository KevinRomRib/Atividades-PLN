# Atividade 01 de Processamento de Linguagem Natural

## Problema:

<p>PP.1.8. Repita o PP.1.7. mas utilizando um texto em inglês ("PP.1.7. Desenvolva um programa em Python que lê um arquivo de entrada, em formato txt, quebra o teto em palavras e contabiliza quantas vezes a palavra ocorre no texto. Como saída o programa gera um gráfico que ilustra o número de vezes que cada palavra ocorreu. Em PNL, como são chamadas as palavras que ocorrem com muita frequência e que podem não agregar muito significado? Para o texto que você analisou (que deve conter no mínimo 2000 palavras) quais seriam essas palavras? Quais as classes dessas palavras?")</p>

## Solução

### Como rodar o projeto?

Criar ambiente virtual (venv):

```sh
python -m venv env
```

Entrar no ambiente criado:

```sh
.\env\Scripts\activate
```

Instalar as dependências

```sh
pip install -r requirements.txt
```

No arquivo "main.py", na linha 4, especificamos o nome do arquivo de texto a ser lido, e em seguida rodamos o arquivo "main.py" para executar o processamento:

```sh
python .\main.py
```
## Respostas das perguntas do problema:

<strong><p>Em PNL, como são chamadas as palavras que ocorrem com muita frequência e que podem não agregar muito significado?</p></strong>
<p><strong>R:</strong> Em Processamento de Linguagem Natural (PLN), as palavras que ocorrem com muita frequência e que geralmente não agregam muito significado ao texto são chamadas de stopwords</p>

<strong><p>Para o texto que você analisou (que deve conter no mínimo 2000 palavras) quais seriam essas palavras? Quais as classes dessas palavras?"</p></strong>
<strong><p>R:</p></strong>
  <p>- the (artigo definido)</p>
  <p>- and (conjunção coordenativa)</p>
  <p>- of (preposição)</p>
  <p>- in (preposição)</p>
  <p>- to (preposição ou infinitivo)</p>
  <p>- a (artigo indefinido)</p>
  <p>- it (pronome)</p>
  <p>- was (verbo auxiliar)</p>
  <p>- with (preposição)</p>
  <p>- on (preposição)</p>
