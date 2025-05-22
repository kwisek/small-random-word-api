import random
import nltk
from nltk.corpus import words

try:
    english_words = words.words()
except LookupError:
    nltk.download('words')
    english_words = words.words()


def n_random_words(n: int) -> list[str]:
    if n > len(english_words):
        raise ValueError("Requested more words than are available")
    if n < 1:
        raise ValueError("Requested less than 1 word")
    return random.sample(english_words, n)
