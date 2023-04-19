# Run if you want to refill word database

import sqlite3
import re

with open("source.txt", "r") as data:

    max_len = 0
    for line in data.readlines():
        max_len = len(line) if len(line) > max_len else max_len

    connection = sqlite3.connect('words.db')
    connection.execute("DROP TABLE WORD;")
    connection.execute(f"CREATE TABLE WORD (CONTENT CHAR({max_len}) PRIMARY KEY NOT NULL);")

    data.seek(0)
    for line in data.readlines():
        word = re.sub(r'[^a-zA-Z]', '', line)
        if len(word) >= 2:
            connection.execute(f"INSERT INTO WORD(CONTENT) VALUES('{word}');")

    connection.commit()
    connection.close()