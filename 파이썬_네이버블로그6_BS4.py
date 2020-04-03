# 구글 크롤링 - BS & Selenium 사용 - 김플 스튜디오

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl ='https://www.google.com/search?q='
plusUrl = input('무엇을 검색할 까요 :')
url = baseUrl + quote_plus(plusUrl)

#  webdriver로 브라우저 제어. webdriver사용 chrome 브라우저에 문법 적용. webdriver 압축풀고 같은 폴더에 넣음

driver = webdriver.Chrome() 
driver.get(url)

# selenium 적용.

html = driver.page_source  # 웹드라이버로 열린 페이지 소스를 받음
soup = BeautifulSoup(html)  # html에 들어있는 페이지 소스가 들어감

cl_r = soup.select('.r')  # 선택자로 가져오는 것은 리스트로 반환

for i in cl_r:
    # print(i.select('.LC20lb DKV0Md'))  # select() 메소드는 리스트로 반환된 객체에 속성으로 'text' 없음. 즉 text를 불러오지 못함. 그래서 select_one()은 text 가능
    print(i.select_one('.LC20lb DKV0Md'))    # .r 클래스에 속해 있는 제목 부분에 해당하는 클래스 
    print(i.a.attrs['href'])   # 링크를 가져옴
    print()  # 정리정돈용
driver.close()   # 크롬 webdriver를 닫아줌




  