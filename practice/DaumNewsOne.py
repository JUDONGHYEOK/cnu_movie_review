# 웹 크롤링 => 네이버 뉴스

import requests
from bs4 import BeautifulSoup

# requuests => 웹사이트 코드 복사GET
# Beautifulsoup4 => requests GET 해온 코드에서 필요한 정보만 find해서 찾아오기

url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)


doc = BeautifulSoup(result.text, 'html.parser')
title = doc.select('h3.tit_view')[0].get_text()
contents = doc.select('section p')
contents.pop(-1) # remove(-1)은 오류
content=''

print('------------------------------------')
print('# 뉴스 제목: {}'.format(title))
print('------------------------------------')
for info in contents:
    content+=info.get_text();
print('# 뉴스 본문: {}'.format(content))
