#  파이썬 beautifulsoup 크롤링 예제 네이버 블로그 검색결과 크롤러 만들기3편 이미지결과 한번에 다운로드 - 김플 스튜디오

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + quote_plus(plusUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

img = soup.find_all(class_="_img")

print(img[0])

n=1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:      # with 문을 사용 close() 문 생략..
        with open('./img/'+plusUrl + str(n) + ' .jpg', 'wb') as h:  # 번호(n)을 문자열로 바꾸고, 파일 형식 정하고('.jpg'), 읽어 오는데 이미지 파일이므로 바이너리로 읽어옴('wb'). 그리고 읽어온 파일을 저장할 할 폴더(img)를 하나 만들어 거이에 넣어줌('./img/')
            img = f.read()
            h.write(img)
    n +=1
    print(imgUrl)  # 잘실행되나 확인용

print('다운로드 완료')  # 잘 실해되나 확인용

