from bs4 import BeautifulSoup
from time import sleep
from requests import Session

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
for count in range(1, 4):
    url = f"https://kanobu.ru/games/popular/?page={count}"

    work = Session()
    r = work.get(url, headers = headers)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all("div", class_="knb-cell")

    for el in data:
        sleep(3)
        key = el.find("div", class_="BaseElementCard_body__fcrUh")
        name = key.find("a").text
        genre = el.find("div", class_="BaseElementCard_genres__DtPr1").text
        date = el.find("div", class_="BaseElementCard_date__FPfgY").text
        rating = el.find("div", class_="KnbCardMark_label__hg6Pg tv-series-mark KnbCardMark_isGreen__G_FLl").text
        img = el.find("img", class_="knb-card--image").get("src")
        print(name + "\n" + genre + "\n" + "Дата выхода: " + date + "\n" + "Рейтинг: " + rating + "\n" + img + "\n")
