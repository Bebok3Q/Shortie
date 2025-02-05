from pydantic import BaseModel


class URLModel(BaseModel):
    id: int
    original_url: str
    short_code: str
    click_count: int
    created_at: str
    expires_at: str