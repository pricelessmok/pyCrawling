from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/usr/local/Cellar/chromedriver/2.31/bin/chromedriver')
driver = webdriver.PhantomJS('/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')

# 구개수 접속
def get_page(no):
    url = "http://www.ppomppu.co.kr/zboard/view.php?id=phone3&page=1&divpage=11&no="+str(no)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select('body > div.wrapper > div.contents > div.container > div > table > tbody > tr > td > table > tbody > tr > td > font.view_title2')
    info = soup.select('body > div.wrapper > div.contents > div.container > div > table > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td')

    print(title)
    print(info)


max = 98920
for n in range(max, max-10, -1) :
    get_page(n)
