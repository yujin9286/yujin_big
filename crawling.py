from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd


word_date=[]
word_title=[]
word_view=[]
word_category=[]
word_content=[]


url="https://terms.naver.com/"
link=urlopen(url)
soup=BeautifulSoup(link,"html.parser")


word_content.extend([soup.find_all('p','desc __ellipsis')[n].string for n in range(0,50)])
word_category.extend([soup.find_all('span','info book')[n].a.string for n in range(0,50)])
word_title.extend([soup.find_all('strong','title')[n].a.strong.string for n in range(4,54)])
word_view.extend([soup.find_all('em','count')[n].string for n in range(4,54)])
data=pd.DataFrame({'date':datetime.today().strftime('%Y-%m-%d'),'title':word_title,'view':word_view,'category':word_category,'content':word_content})

data.to_csv("crawling.csv")