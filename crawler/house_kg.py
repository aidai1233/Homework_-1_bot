import httpx
from parsel import Selector


MAIN_URL = "https://www.house.kg/snyat"


def get_page():
    response = httpx.get(MAIN_URL, timeout=10)
    print("Status code", response.status_code)
    return response.text


def get_page_title(page):
    selector = Selector(text=page)
    title = selector.css("title::text").get()
    return title


def get_links(page):
    selector = Selector(text=page)
    links = selector.css("div.left-side a::attr(href)").getall()
    return list(map(lambda x: "https://www.house.kg" + x, links))


if __name__ == "__main__":
    page = get_page()
    links = get_links(page)
    print(links)
