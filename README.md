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

### Exemplo de texto utilizado: 
Ontem, eu fui ao parque com minha família. O tempo estava ensolarado e todos se divertiram bastante.
### Análise e Principais Diferenças Observadas:
-	<b>Número Total de Tokens:</b>
O NLTK Default gerou 20 tokens, enquanto ambos o Treebank e o Toktok geraram 19 tokens.
-	<b>Tratamento de Pontuações:</b>
NLTK Default separou a pontuação do texto corretamente, resultando em dois tokens de pontuação: “,” e “.”, já o Treebank e o Toktok consideraram "família." como um único token.
-	<b>Desempenho:</b>
O NLTK Default foi significativamente mais lento (0.020499 segundos), devido ao uso do modelo estatístico Punkt, que realiza cálculos mais complexos durante a tokenização.
Por outro lado, tanto o Treebank quanto o Toktok foram extremamente rápidos (0.000000 segundos), indicando que eles usam métodos mais diretos baseados em regras.
-	<b>Número de Palavras:</b>
O número de palavras (tokens alfanuméricos) foi igual em todos os tokenizadores, com 18 palavras, o que indica que eles lidaram bem com a identificação de palavras sem pontuação.

### Conclusão:
O NLTK Default é mais detalhado na separação de tokens, mas isso vem à custa do desempenho e da quantidade total de tokens, especialmente em textos simples. Ele é mais robusto em situações onde a precisão é mais crítica.
O Treebank e o Toktok foram mais rápidos e apresentaram resultados mais eficientes na tokenização, mas podem se perder na separação de pontuações que o NLTK Default consegue. Eles são ideais para aplicações onde a velocidade é uma prioridade e o texto não apresenta muitos desafios complexos.
