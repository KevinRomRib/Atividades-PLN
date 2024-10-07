# atv02pln

## Problema:

<p>PP.2.5 Fazer o estudo comparativo de saída e desempenho dos tokens de palavras do nltk default, Treebank e Toktok. Utilize dados de uma review de P.2.3. No seu estudo, descreva, baseando-se nas saídas dos tokenizadores, quais as principais diferenças observadas quantificando os resultados com exemplos de textos simples.</p>

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

Rodar os respectivos tokenizadores

```sh
python .\tokenizacao_nltk_default.py
python .\tokenizacao_treebank.py
python .\tokenizacao_toktok.py
```