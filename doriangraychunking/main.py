import re
import nltk
from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

text = open("dorian_gray.txt").read().lower()

# sentence and word tokenize text

word_tokenized_text = word_sentence_tokenize(text)
print(word_tokenized_text,)
# store and print word tokenized sentence

single_word_tokenized_sentence = word_tokenized_text[100]
print(single_word_tokenized_sentence)

pos_tagged_text = []

for word_tokenized_sentence in word_tokenized_text:
  pos_tagged_text.append(pos_tag(word_tokenized_sentence))

single_pos_sentence = pos_tagged_text[100]
print(single_pos_sentence)
# noun phrase chunk grammar

np_chunk_grammar = "NP:{<DT>?<JJ>*<NN>}"
# noun phrase RegexpParser object

np_chunk_parser = RegexpParser(np_chunk_grammar)

#verb phrase chunk grammar

vp_chunk_grammar = "VB:{<DT>?<JJ>*<NN><VB.*><RB.?>?}"

#verb phrase RegexpParser object

vp_chunk_parser = RegexpParser(vp_chunk_grammar)

np_chunked_text = []
vp_chunked_text = []

for pos_tagged_sentence in pos_tagged_text:
  np_chunked_text.append(np_chunk_parser.parse(pos_tagged_sentence))
  vp_chunked_text.append(vp_chunk_parser.parse(pos_tagged_sentence))



with open("output.txt", "a") as f:
    most_common_np_chunks = np_chunk_counter(np_chunked_text)
    print(most_common_np_chunks,file=f)


    most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
    print(vp_chunk_counter,file=f)













#for i in most_common_np_chunks:
#    if isinstance(i, nltk.tree.Tree):
#        if a.label() == "NP":
#            print(i)
#            print(" ".join([lf[0] for lf in i.leaves()]))
#            print()
#for i in most_common_vp_chunks:
#    if isinstance(i, nltk.tree.Tree):
#        if i.label() == "VB":
#            print(i)
#            print(" ".join([lf[0] for lf in i.leaves()]))
#            print()