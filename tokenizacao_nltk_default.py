import time
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

text = "Ontem, eu fui ao parque com minha família. O tempo estava ensolarado e todos se divertiram bastante."

start_time = time.time()
tokens = word_tokenize(text)
end_time = time.time()
total_tokens = len(tokens)

print(f"NLTK Default Tokens:\n {tokens} - Tempo: {end_time - start_time:.6f} segundos\n - Quantificação: {total_tokens}")
