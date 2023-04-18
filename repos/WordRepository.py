import sqlite3
import random

def all_words():
    connection = sqlite3.connect('data/words.db')
    words = connection.execute(f"SELECT CONTENT FROM WORD;").fetchall()
    connection.close()
    return list(map(lambda x: x[0], words))

def all_words_by_len(len: int):
    connection = sqlite3.connect('data/words.db')
    if (len is None):
        words = connection.execute(f"SELECT CONTENT FROM WORD;").fetchall()
    else:
        words = connection.execute(f"SELECT CONTENT, LENGTH(CONTENT) FROM WORD WHERE LENGTH(CONTENT) = {len};").fetchall()
    connection.close()
    return list(map(lambda x: x[0], words))

def all_words_by_pattern(pattern: str):
    pattern = pattern.replace("~", "%")
    connection = sqlite3.connect('data/words.db')
    words = connection.execute(f"SELECT CONTENT FROM WORD WHERE CONTENT LIKE '{pattern}';").fetchall()
    connection.close()
    return list(map(lambda x: x[0], words))

def random_word_by_len(len: int):
    return random.choice(all_words_by_len(len))

def random_word_by_pattern(pattern: str):
    return random.choice(all_words_by_pattern(pattern))
