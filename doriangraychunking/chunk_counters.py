from collections import Counter

# function that pulls chunks out of chunked sentence and finds the most common chunks
def np_chunk_counter(chunked_sentences):
    chunks = list()
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
            chunks.append(tuple(subtree))

    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    # return 30 most frequent chunks
    return chunk_counter.most_common(30)

from collections import Counter

# function that pulls chunks out of chunked sentence and finds the most common chunks
def vp_chunk_counter(chunked_sentences):
    chunks = list()

    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'VP'):
            chunks.append(tuple(subtree))

    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    # return 30 most frequent chunks
    return chunk_counter.most_common(30)
