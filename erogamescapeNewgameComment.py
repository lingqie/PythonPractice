#!/usr/bin/env python
# encoding=utf-8

import requests
import codecs
from bs4 import BeautifulSoup

URL="https://erogamescape.dyndns.org/~ap2/ero/toukei_kaiseki/comment_newgame.php"
index="https://erogamescape.dyndns.org/"

def download_page(url):
    # headers={
    #     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    # }
    data=requests.get(url).content
    return data

def parse_html(data):
    soup=BeautifulSoup(data)
    alldiv = soup.find('div',class_="coment")

    gal_name_list=[]
    for coment in alldiv.find_all('div'):
        name=coment.find('span',class_="futoji")
        point=coment.find('span',class_="red")
        gal_name_list.append([point.text,name.text])

    nextPage=soup.find('tbody').find('td').next_sibling.next_sibling.find('a')
    # 注意字符串要加上u开头，可以使用isinstance(nextPage,Unicode)来判断是否unicode
    if u'\u6b21\u306e' in nextPage.text:
        print index + nextPage['href']
        return gal_name_list,index + nextPage['href']
    return gal_name_list,None

def main():
    url=URL
    with codecs.open('gals.txt','wb',encoding='utf-8') as fp:
        while url:
            data=download_page(url)
            gals,url=parse_html(data)
            for datalist in gals:
                fp.write(u'point:{point}---{gals}\n'.format(gals=datalist[1],point=datalist[0]))

if __name__=='__main__':
    main()
