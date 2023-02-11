from bs4 import BeautifulSoup
from aiohttp import ClientSession
from fastapi import HTTPException

BASE_URL: str = "https://igg-games.com/"

async def scraping(router: list[str] = [], params: dict = {}) -> BeautifulSoup:
    async with ClientSession() as ses:
        async with ses.get( BASE_URL + "/".join(router), params=params ) as res:
            if res.status != 200:
                raise HTTPException(503, detail="Connectionless service")

            return BeautifulSoup((await res.text()), "html.parser")
