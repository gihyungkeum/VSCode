# 파이썬 beautifulsoup 크롤링 예제 네이버 블로그 검색결과 크롤러 만들기 - 김플 스튜디오
# 콘솔창에서 pip install beautifulsoup4

import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()

