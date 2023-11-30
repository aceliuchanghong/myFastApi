from typing import Union
import uvicorn
from fastapi import FastAPI

from test.gpt_util import talkToGpt

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/gpt/{item_id}")
def read_item(item_id: str):
    return talkToGpt("100+" + item_id + "是多少?")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
