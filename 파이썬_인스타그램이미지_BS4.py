# beautifulsoup와 selenium을 사용하여 자바스크립트로 만들어진 웹사이트를 크롤링 - 김플 스튜디오
# 실습할 폴더에 크롬드라이브 다운로드 압축을 풀어서 넣음 

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#  https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%9C%A0/

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 태그를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

# 인스타그램은 자바스크립트로 제작되어 beautifulsoup으로 크롤링 어려움. 따라서 selenium 문법을 적용

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)  # 인터넷 속도가 느린경우을 감안, 적당히  time.sleep(초) 를 넣어주는 것도 방업 

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w')  #실렉터를 쓰고 그안에 .클라스 연속넣을 수 있음

n=1
for i in insta:

    print('https://www.instagram.com'+ i.a['href'])
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        with open('./img_inst/'+plusUrl+str(n)+'.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)
    print()

driver.close()   # 드라이번 닫아줌
