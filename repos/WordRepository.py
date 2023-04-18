import sqlite3
import random

def all_words():
    try:
        connection = sqlite3.connect('data/words.db')
        words = connection.execute(f"SELECT CONTENT FROM WORD;").fetchall()
        connection.close()
        return list(map(lambda x: x[0], words))
    except:
        return []

    

def all_words_by_len(len: int):
    try:
        connection = sqlite3.connect('data/words.db')
        if (len is None):
            words = connection.execute(f"SELECT CONTENT FROM WORD;").fetchall()
        else:
            words = connection.execute(f"SELECT CONTENT, LENGTH(CONTENT) FROM WORD WHERE LENGTH(CONTENT) = {len};").fetchall()
        connection.close()
        return list(map(lambda x: x[0], words))
    except:
        return []
    

def all_words_by_pattern(pattern: str):
    try:
        pattern = pattern.replace("~", "%")
        connection = sqlite3.connect('data/words.db')
        words = connection.execute(f"SELECT CONTENT FROM WORD WHERE CONTENT LIKE '{pattern}';").fetchall()
        connection.close()
        return list(map(lambda x: x[0], words))
    except:
        return []

def random_word_by_len(len: int):
    result = all_words_by_len(len)
    return "" if not result else random.choice(result)

def random_word_by_pattern(pattern: str):
    result = all_words_by_pattern(pattern)
    return "" if not result else random.choice(result)
