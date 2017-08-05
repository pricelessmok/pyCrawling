from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/usr/local/Cellar/chromedriver/2.31/bin/chromedriver')
driver = webdriver.PhantomJS('/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs')

# 구개수 접속
driver.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=phone3')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#클래스 이름이니까 시발아 샵 지우지마라 이걸로 몇 시간 지랄했냐
notices = soup.select('#revolution_main_table > tbody > tr > td > a')

for n in notices:
    print(n.text.strip())
