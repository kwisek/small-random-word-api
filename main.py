from fastapi import FastAPI, Response, status
from repos import WordRepository

app = FastAPI()


@app.get("/all")
async def all_words(response: Response):
    result = WordRepository.all_words()
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
    return 

@app.get("/word/random")
async def word_random(response: Response, len: int | None = None, pattern: str | None = None):
    result = ""
    if len:
        result = WordRepository.random_word_by_len(len)
    if pattern:
        result = WordRepository.random_word_by_pattern(pattern)
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
    return result

@app.get("/word")
async def word_random(response: Response, len: int | None = None, pattern: str | None = None):
    result = []
    if len:
        result = WordRepository.all_words_by_len(len)
    if pattern:
        result = WordRepository.all_words_by_pattern(pattern)
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
    return result