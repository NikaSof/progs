from bs4 import BeautifulSoup
from time import sleep
from requests import Session

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}

for count in range(1, 2):
    url = f"https://kanobu.ru/games/popular/?page={count}"
    work = Session()
    r = work.get(url, headers = headers)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all("div", class_="knb-cell")

def array():
    for el in data:
        sleep(2)
        key = el.find("div", class_="BaseElementCard_body__fcrUh")
        name = key.find("a").text
        genre = el.find("div", class_="BaseElementCard_genres__DtPr1").text
        date = el.find("div", class_="BaseElementCard_date__FPfgY").text
        rating = el.find("div", class_="KnbCardMark_label__hg6Pg tv-series-mark KnbCardMark_isGreen__G_FLl").text
        img = el.find("img", class_="knb-card--image").get("src")
        yield name, genre, date, rating, img

array()

----------------------------------------------------------------

import xlsxwriter
from main import array


def writer(parametr):

    book = xlsxwriter.Workbook(r"C:\Users\Veronika\Desktop\Parsing.xlsx")
    page = book.add_worksheet("товар")

    row = 0
    column = 0

    page.set_column("A:A", 30)
    page.set_column("B:B", 30)
    page.set_column("C:C", 25)
    page.set_column("D:D", 10)
    page.set_column("E:E", 50)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column + 4, item[4])
        row += 1

    book.close()


writer(array)
