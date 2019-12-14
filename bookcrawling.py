from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

book_title=[]
book_rating=[]
book_price=[]


for page_end in range(1, 4246):
    url = 'https://series.naver.com/ebook/categoryProductList.nhn?categoryTypeCode=all&page=' + str(page_end)
    page=urlopen(url)
    soup=BeautifulSoup(page,"html.parser")
    book_title.extend([soup.find_all('div','cont')[n].h3.a.string for n in range(0,25)])
    book_rating.extend([soup.find_all('em','score_num')[n].string for n in range(0,25)])
    book_price.extend([soup.find_all('p','price')[n].strong.string.replace(",","").replace("무료","0") for n in range(0,25)])


data=pd.DataFrame({'title':book_title,'rating':book_rating,'price':book_price})
data
data.to_csv("all_total_bookcrawling.csv")