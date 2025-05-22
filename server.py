from fastapi import FastAPI
from modules import n_random_words

app = FastAPI()

@app.get("/")
async def random_words(n: int = 1):
    return n_random_words(n)
