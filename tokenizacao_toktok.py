import time
from nltk.tokenize import ToktokTokenizer

toktok_tokenizer = ToktokTokenizer()

text = "Ontem, eu fui ao parque com minha família. O tempo estava ensolarado e todos se divertiram bastante."

start_time = time.time()
tokens = toktok_tokenizer.tokenize(text)
end_time = time.time()
total_tokens = len(tokens)

print(f"Toktok Tokens:\n {tokens}\n - Tempo: {end_time - start_time:.6f} segundos\n - Quantificação: {total_tokens}")
