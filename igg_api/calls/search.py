from slugify import slugify
from bs4.element import Tag

from igg_api.model import Post
from igg_api.utils import scraping

async def call(**kwargs) -> None:
    res: BeautifulSoup = await scraping(params={
        "q": kwargs["query"]
        })
    data: list[Post] = []

    for post in res.select(".post"):
        title: str = post.select_one(".uk-article-title").text
        meta: list[Tag] = post.select(".uk-article-meta > a")
        # 0 = posted_by | 1 >= genres

        title = title.split("Free")[0].strip()

        data.append(Post(
            id = slugify(title),
            title = title,
            description = post.select_one(".uk-margin-medium-top").text.strip("\n"),
            posted_by = meta[0].text,
            date = post.select_one(".uk-article-meta > time")["datetime"],
            genre = [x.text for x in meta[1:]],
            image = post.select_one(".attachment-post-thumbnail")["src"]
            ))

    return data
