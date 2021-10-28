# Daum News 에서


import requests
from bs4 import BeautifulSoup


i = 0
for page_number in range(1, 4):
    url = "https://news.daum.net/breakingnews/digital?page={}".format(page_number)
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    url_list = doc.select('ul.list_news2 a.link_txt')

    for url in url_list:
        i += 1
        print('-- NEWs -> {}번 -------------------------'.format(i))
        new_url = url['href']
        print('# URL:   {}'.format(new_url))
        result = requests.get(new_url)

        doc = BeautifulSoup(result.text, 'html.parser')
        title = doc.select('h3.tit_view')[0].get_text()
        contents = doc.select('section p')
        contents.pop(-1)  # remove(-1)은 오류
        content = ''

        print('# 뉴스 제목: {}'.format(title))
        for info in contents:
            content += info.get_text();
        print('# 뉴스 본문: {}'.format(content))
