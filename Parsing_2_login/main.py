from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}

work = Session()

work.get("https://quotes.toscrape.com/", headers = headers)

work.get("https://quotes.toscrape.com/login", headers = headers)

response = work.get("https://quotes.toscrape.com/login", headers = headers)
soup = BeautifulSoup(response.text, "html.parser")
token = soup.find("form").find("input").get("value")

data = {"csrf_token" : token, "username": "noname", "password": "password"}

result = work.post("https://quotes.toscrape.com/login", headers = headers, data = data, allow_redirects=True)

print(result.text)
