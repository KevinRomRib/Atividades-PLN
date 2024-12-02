# atv03pln

## Problema:

<p>PP.4.4. Ilustre uma aplicação simples de chatbot que utilize o modelo pré-treinado word2vec.
Seu modelo deve fazer uso dos componetes fornecidos no repositório do professor da
disciplina e deve possuir todas as componentes básicas da pipeline de pré-processamento. O
Chatbot deve ser utilizado para responder perguntas relacionadas ao uso de determinada
aplicação (ex. Como gero um relatório? Como faço o upload de dados, etc.).</p>

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

Rodar o Chatbot

```sh
python .\app.py
```

Após rodar o Chatbot é só fazer as requisições POST em localhost:5000/chat com o a objeto "mensagem" no body e sua pergunta, por exemplo:
```sh
{
    "mensagem": como gerar um relatório?
}
```
