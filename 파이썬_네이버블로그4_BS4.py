# 여러페이지 크롤링하기


import urllib.request
import urllib.parse
from bs4 import BeautifulSoup





#  baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='

# plusUrl = input('검색어를 입력하세요:')
plusUrl = urllib.parse.quote_plus(input('검색어를 입력하세요:'))

# # url = baseUrl + urllib.parse.quote_plus(plusUrl)

# url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusUrl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}'
# #  print(url) # 확인용

pageNum = 1

count = 1  # 정리정돈을 위하여 추가

i = input('몇페이지까지 크롤링 할까요? :')

lastPage = int(i)*10 -9  
# input()은  문자열로 반환하므로 숫자형으로 바꾸고, 페이지 당 10개 항목이 있어 페이지 넘어갈때 10씩 증가하므로 10곱하고 9을 빼편 각페이지 첫번째 항목은 1, 11, 21, 31....... 


while pageNum < lastPage + 1:   # 10페이지를 넣으면 lastPage가 91이되고, 페이지 넘버도 91이되어 결국 9페이지까지만 스크롤링함. 따라서 1을 더하면 92가 되어 pageNum이 lastNum보다 작으므로 10페이지까지 출력

    url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusUrl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}'


    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    blog_title = soup.find_all(class_ = 'sh_blog_title')

    print(f'-------{count}페이지 결과입니다--------')

    for i in blog_title:
        print(i.attrs['title'])
        print(i.attrs['href'])
        print()    # 정리정돈용   
    print()
    pageNum += 10      # 한페이지 마다 10개 항목씩 있어, 페이지 넘어갈때 10씩 
    count +=1    # 정리정돈용


#   https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&sm=tab_pge&srchby=all&st=sim&where=post&start=11

#   https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&sm=tab_pge&srchby=all&st=sim&where=post&start=21

#   https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&sm=tab_pge&srchby=all&st=sim&where=post&start=31  