# 웹스크랩핑 및 csv 파일 저장방법

import urllib.request
from bs4 import BeautifulSoup
import csv

hdr = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.melon.com/chart/day/index.htm'

req = urllib.request.Request(url, headers=hdr)
# html = urllib.request.urlopen(url).read()
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup)    # 406 또는 403 에러발생..통상 header값이 없는 경우 발생.. 직접 브라우저를 열고 접근하지 않은 경우 발생..헤더값 넣기위한 hdr 변수 만듬. req변수만들고, html 변수에 넣어줌

# lst50 = soup.select('.lst50')  #select로 가져오면  list로 반환

# print(lst50[0])

# for i in lst50:
#     print(i.select_one('.rank').text, end='위 ')  # 텍스트 가져오고 가로로 정열 및 end='위' 첨가

#     # print(i.select_one('.ellipsis.rank01').text)    # text만 출력
#     print(i.select_one('.ellipsis.rank01').a.text, end=' ')
#     print(i.select_one('.ellipsis.rank02').a.text, end=' ')  # a태그내 text만 가저오기 (빈줄 없애기)
#     print(i.select_one('.ellipsis.rank03').a.text, end=' ')  # end='' 가로 정열 형식으로 출력됨 
#     break  # 한번만 반복하고 멈치도록


lst_100 = soup.select('.lst50, .lst100')  #메론 구조를 보니, lst50과 lst100이 같은내용에 클라스 값만 다름. 그래서 for in 문 사용하여 100위 까지 한번에 불러 올 수 있는 구조  


# for i in lst_100:
#     print(i.select_one('.rank').text, end='위 ')  # 텍스트 가져오고 가로로 정열 및 end='위' 첨가

#     # print(i.select_one('.ellipsis.rank01').text)    # text만 출력
#     print(i.select_one('.ellipsis.rank01').a.text, end=' ')
#     print(i.select_one('.ellipsis.rank02').a.text, end=' ')  # a태그내 text만 가저오기 (빈줄 없애기)
#     print(i.select_one('.ellipsis.rank03').a.text, end=' ')  # end='' 가로 정열 형식으로 출력됨 
#     # break  # 한번만 반복하고 멈치도록


melonList = [] # 불러온것 저장위해 빈 리스트 만듬
for i in lst_100:
    temp = [] # 빈리스트에 리스트를 추가하기위하여 빈 리스트를 또 만듬
    temp.append(i.select_one('.rank').text)  # temp 리스트에 append메소드로 텍스트 추가. 프린트 할 것이 아니므로 end='위'는 필요 없으니 지움
    temp.append(i.select_one('.ellipsis.rank01').a.text)
    temp.append(i.select_one('.ellipsis.rank02').a.text)  
    temp.append(i.select_one('.ellipsis.rank03').a.text)  
    melonList.append(temp)  # temp에 담긴 리스트 형식의 내용을 melonList에 담음

# print(melonList)

with open('melon100_file2.csv', 'w', encoding='utf-8', newline='') as f:
    # melon100_file.csv파일 만들어 여기에 내용담음. newline='' 줄바굼. encoding은 utf-8, cp949 MS949, euk=kr등
    wrt = csv.writer(f)
    wrt.writerow(['순위','아티스트', '곡명', '앨범'])   # 파일 보기 좋도록 맨위에 분류항목을 만들어줌)
    wrt.writerows(melonList)

# with open('melon100.csv', mode='w' , encoding= 'utf-8', newline='') as f:
     
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow(['순위','아티스트', '곡명', '앨범'])   # 파일 보기 좋도록 맨위에 분류항목을 만들어줌
#     writer.writerows(melonList)


