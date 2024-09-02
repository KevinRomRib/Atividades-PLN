import matplotlib.pyplot as plt
from collections import Counter

palavras = open('texto2000palavras.txt', 'r').read().lower().split()

contador = Counter(palavras)
palavras_comuns = contador.most_common(10)
lista_palavras, lista_quantidade_palavras = zip(*palavras_comuns)

plt.bar(lista_palavras, lista_quantidade_palavras)
plt.xticks(rotation=45)

for i, quantidade in enumerate(lista_quantidade_palavras):
    plt.text(i, quantidade, str(quantidade), ha='center', va='bottom')

plt.xlabel('Palavras')
plt.ylabel('Contagens')
plt.title('Top 10 Palavras Mais Frequentes')
plt.show()

# Perguntas:

# Em PNL, como são chamadas as palavras que ocorrem com muita frequência e que podem não agregar muito significado?
# R: Em Processamento de Linguagem Natural (PLN), as palavras que ocorrem com muita frequência e que geralmente não agregam muito significado ao texto são chamadas de stopwords

# Para o texto que você analisou (que deve conter no mínimo 2000 palavras) quais seriam essas palavras? Quais as classes dessas palavras?")
# R:
#   the (artigo definido)
#   and (conjunção coordenativa)
#   of (preposição)
#   in (preposição)
#   to (preposição ou infinitivo)
#   a (artigo indefinido)
#   it (pronome)
#   was (verbo auxiliar)
#   with (preposição)
#   on (preposição)
