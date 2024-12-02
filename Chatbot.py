import re
import numpy as np
from numpy import dot
from numpy.linalg import norm
from gensim.models import word2vec
from nltk.tokenize import word_tokenize

# Definindo o corpus de exemplo
faq_corpus = {
    "como gerar um relatório": "Para gerar um relatório, acesse a aba 'Relatórios' e escolha o tipo de relatório desejado.",
    "como fazer upload de dados": "Para fazer upload, vá até a aba 'Dados', clique em 'Upload' e selecione o arquivo.",
    "como redefinir minha senha": "Você pode redefinir sua senha clicando em 'Esqueci minha senha' na tela de login.",
    "como acessar o suporte": "Entre em contato com o suporte através da aba 'Ajuda' no menu principal."
}

# Função para pré-processar texto
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^A-Za-zÀ-Ýà-ý ]', '', text)
    return word_tokenize(text)

# Preparando o corpus para treinar o modelo Word2Vec
tokenized_corpus = [preprocess_text(question) for question in faq_corpus.keys()]

# Configurando e treinando o modelo Word2Vec (Baseado no arquivo word_to_vec_model do repositório do professor)
feature_size = 5
window_context = 2
min_word_count = 1
sample = 1e-3

w2vec_model = word2vec.Word2Vec(
    tokenized_corpus, vector_size=feature_size,
    window=window_context, min_count=min_word_count,
    sample=sample, epochs=50
)

# Função para calcular similaridade de cosseno
def cosine_similarity(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# Função para obter o vetor médio de uma frase
def get_sentence_vector(sentence, model):
    words = preprocess_text(sentence)
    vectors = [model.wv[word] for word in words if word in model.wv]
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

def chatbot(question):
    question_vector = get_sentence_vector(question, w2vec_model)
    best_match = None
    highest_similarity = -1

    for stored_question, answer in faq_corpus.items():
        stored_vector = get_sentence_vector(stored_question, w2vec_model)
        similarity = cosine_similarity(question_vector, stored_vector)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = answer

    if highest_similarity > 0.5:
        return best_match
    else:
        return "Desculpe, não entendi sua pergunta."
