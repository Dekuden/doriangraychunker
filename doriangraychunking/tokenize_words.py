import nltk 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

def word_sentence_tokenize(text):
  sentence_tokenizer = PunktSentenceTokenizer(text)
  sentence_tokenized = sentence_tokenizer.tokenize(text)
  word_tokenized = list()

  for tokenized_sentence in sentence_tokenized:
    word_tokenized.append(word_tokenize(tokenized_sentence))
    
  return word_tokenized