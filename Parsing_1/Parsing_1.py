import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}


def download(url):
    resp = requests.get(url, stream = True)
    r = open("C:\\Users\\Nika\\Desktop\\image\\" + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()


def get_url():

    for count in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        r = requests.get(url, headers = headers)
        html = BeautifulSoup(r.text, 'html.parser')
        data = html.find_all("div", class_="col-lg-4 col-md-6 mb-4")

        for el in data:
            card_url = "https://scrapingclub.com/" + el.find("a").get("href")
            yield card_url


def array():

    for card_url in get_url():
        sleep(1)
        r = requests.get(card_url, headers=headers)
        html = BeautifulSoup(r.text, 'html.parser')
        data = html.find("div", class_ = "card mt-4 my-4")
        name = data.find("h3", class_ = "card-title").text
        price = data.find("h4").text
        text = data.find("p", class_ = "card-text").text
        url_img = "https://scrapingclub.com" + data.find("img", class_ = "card-img-top img-fluid").get("src")
        download(url_img)
        print (name, price, text, url_img)

array()