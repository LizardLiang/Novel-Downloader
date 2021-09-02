# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os


def get_novel(page):
    url = "https://www.bg3.co/novel/pagea/moshoulingzhu-gaopo_" + str(page) + ".html"

    res = requests.get(url)

    if res.status_code == 404:
        return False

    soup = BeautifulSoup(res.text, "html.parser")
    lines = soup.select("div.content > p")

    paragraph = ""
    for line in lines:
        paragraph = paragraph + line.text.strip() + "\r\n"

    return paragraph


if __name__ == "__main__":
    res = True
    page = 1
    episode = 1
    content = ""
    topic = "魔獸領主"
    route = os.path.join(os.path.abspath(os.getcwd()), topic)
    os.mkdir(route)
    name = topic + "_"
    while res:
        res = get_novel(page)

        if res:
            content = content + res + "\r\n"

        if (page % 20) == 0 or not res:
            with open(
                os.path.join(route, name + str(episode)), "w", encoding="utf-8"
            ) as f:
                f.write(content)
                f.close()

            episode = episode + 1
            content = ""

        print("Current Page {}".format(page))
        page = page + 1
