from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')


text = "Пример текста для токенизации."
tokens = word_tokenize(text, language='russian')

print(tokens)