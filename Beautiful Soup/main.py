import requests
from bs4 import BeautifulSoup

WEBSITE_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=WEBSITE_URL)
html_text = response.text

soup = BeautifulSoup(html_text, "html.parser")

title = soup.find_all(name="h3", class_="title")

title_text = []
for n in reversed(title):
    m = n.getText().replace(":", ")")
    title_text.append(m)

with open("movies.txt", "w", encoding="utf-8") as file:
    for n in title_text:
        file.write(f"{n}\n")
