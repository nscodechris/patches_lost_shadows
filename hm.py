import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://www.github.com"

# https://www.nordea.se/privat/produkter/aktuella-priser-och-rantor.html
proxy = "http://serviceproxy.se.shb.biz:8130"

page = requests.get(url,
                    proxies={"http": proxy, "https": proxy}, headers=headers)

# print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
fake_dict = {"item": [0], "picture": []}
list_use = []
i = 0
# print(soup)
for item in soup.find_all('img'):
    if item['src'].endswith('png'):
        fake_dict["picture"] = item['src']
        fake_dict["item"] = i
        i += 1
        list_use.append(fake_dict.copy())


table = pd.DataFrame(list_use)
table.to_csv('picture.xlsx')

# def render_imgs(path: str = None) -> str:
#     return f"""<img src="{path}" width="60" > """
#
# table.to_html("table.html", escape=False, formatters=dict(picture=render_imgs))