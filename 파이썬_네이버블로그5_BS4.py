#파이썬 크롤링후 csv파일로 저장방법. 자바스크릡트가 주로 사용된 네이버 모바일 버전 view탭 을 적용해 봄

import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


# <a href="https://m.blog.naver.com/piersn/221875443017" class="api_txt_lines total_tit" onclick="return goOtherCR(this, 'a=rvw*b.link&amp;r=1&amp;i=90000003_0000000000000033A8CE9549&amp;u='+urlencode(this.href))"><mark>블로그</mark> 글을 만들기 위한 머티리얼(재료)과 작업과정</a>


search = input('검색어를 입력하세요: ')
url = f'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={quote_plus(search)}'
#   url내 search에 quote_plus적용..input()에 적용시 다른곳에서 search 변수를 사용하는데 어려움이 있을 가능성이 있기 때문.. 

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
total = soup.select('.api_txt_lines.total_tit')
# select사용 .클라스로 탐색
#  print(total[0]) 확인용도

searchList=[]  

for i in total:
    # print(i.text)
    # print(i.attrs['href'])
    # print()

    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)

# print(searchList)

f = open(f'{search}.csv', 'w', encoding='utf8', newline='')
csvwriter = csv.writer(f)
for i in searchList:
    csvwriter.writerow(i)

f.close()

print('완료되었읍니다')  

# 해당 폴더로 들어가보면 엑셀파일로 클로링한 내용이 저장되어 있음