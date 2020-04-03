# 파이썬 beautifulsoup 크롤링 예제 네이버 블로그 검색결과 크롤러 만들기2편 리팩토링 - 김플 스튜디오
# 1편은 검색어가 파이썬으로 고정..이를 리팩토링 필요- baseurl과 plusurl로 나누어 결합
# 또한 검색어 입력시 한글을 읽을 수 있도록 urllib.parse 모듈 및 quote_plus 인스턴스 적용하고 plusurl인자를 그 안에 담음

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='
plusUrl = input('검색어를 입력하세요: ')

# url = baseUrl + plusUrl
url = baseUrl + urllib.parse.quote_plus(plusUrl)

# print(url)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()

