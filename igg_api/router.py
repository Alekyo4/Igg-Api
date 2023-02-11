from fastapi import APIRouter

from igg_api import calls as c
from igg_api.model import Post

app: APIRouter = APIRouter()

@app.get("/search")
async def search(q: str) -> list[Post]:
    return (await c.search(query=q))
