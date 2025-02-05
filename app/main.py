from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Shortie")


class URLModel(BaseModel):
    id: int
    original_url: str
    short_code: str
    click_count: int
    created_at: str
    expires_at: str


urls = {
    0: URLModel(id=0, original_url="https://www.google.pl/", short_code="some short code", click_count=12, created_at="05.02.2024", expires_at="expires date"),
    1: URLModel(id=1, original_url="https://www.youtube.com/", short_code="shorter youtube", click_count=5, created_at="06.02.2024", expires_at="expires date")
}

@app.get('/')
def index() ->dict[str, dict[int, URLModel]]:
    return {"URLs": urls}