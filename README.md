## Small dockerized API for generating random words
I needed a small, simple API that would return random words based on given criteria - either by length or pattern. This repository contains such an application that uses FastAPI and SQLite.

### Dictonary source
[https://github.com/dwyl/english-words](https://github.com/dwyl/english-words)

If you want to change it, put your raw dictionary in `src/data/source.txt` (one word per line) and refill the db by running `fill.py`.

### Quickstart
Clone this repository with `git clone https://github.com/kwisek/small-random-word-api.git`

Build the container with `docker build -t <name> .`

Start the container with `docker run -d -p <ports> <name>`

### API
[]()  | []() | []() | []()
--- | --- | --- | ---
Method | Endpoint | Return type | Description
**GET** | /all | string[] | Returns all stored words as an array of strings. Might take a while.

#### Responses:
- `200`
- `404`

#### Example:
🡆 `curl -X GET http://127.0.0.1:8000/all`

🡄 `["word1", "word2", ...]`

---

[]()  | []() | []() | []()
--- | --- | --- | ---
Method | Endpoint | Return type | Description
**GET** | /word | string[] | Returns all words matching provided criteria. Requires either `len` or `pattern` to be provided.

#### Query parameters:
- `len` length of a word.
- `pattern` case-sensitive pattern of a word. Wildcards: `~` for zero, one or multiple characters, `_` for one character.

#### Responses:
- `200`
- `400` 
- `404`

#### Example:
🡆 `curl -X GET http://127.0.0.1:8000/word?pattern=f~o_e_t`

🡄 `[
    "floreat",
    "florent",
    "foment",
    "forecovert",
    "forest",
    "fouett",
    "fovent",
    "fowent"
]`

---

[]()  | []() | []() | []()
--- | --- | --- | ---
Method | Endpoint | Return type | Description
**GET** | /word/random | string | Returns a random word. Requires either `len` or `pattern` to be provided.

#### Query parameters:
- `len` length of a word.
- `pattern` case-sensitive pattern of a word. Wildcards: `~` for zero, one or multiple characters, `_` for one character.

#### Responses:
- `200`
- `400` 
- `404`

#### Example:
🡆 `curl -X GET http://127.0.0.1:8000/word/random?len=5`

🡄 `"smile"`
