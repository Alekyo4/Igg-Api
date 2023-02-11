from datetime import datetime as dt
from pydantic import AnyHttpUrl, BaseModel

class Post(BaseModel):
    id: str
    title: str
    posted_by: str
    date: dt
    genre: list[str]
    description: str
    image: AnyHttpUrl
