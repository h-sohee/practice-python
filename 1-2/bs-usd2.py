from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.section_calculator > div.calculator > div.inner > div.input > div#sInput "
                        "> select#select_from > option:nth-child(3)")

print("usd/krw =", price.attrs["value"])

