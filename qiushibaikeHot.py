# encoding=utf-8
import requests
import codecs
import time
from bs4 import BeautifulSoup

index="http://www.qiushibaike.com"
URL="http://www.qiushibaike.com/hot/page/1"

def download_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    }
    try:
        data=requests.get(url,headers,timeout=None).content
        return data
    except (requests.ConnectionError,IndexError,UnicodeEncodeError,requests.exceptions.ReadTimeout):
        print "Timeout or ConnectionError"

def find_data_in_html_content(data):
    soup=BeautifulSoup(data)
    alldiv=soup.findAll('div',class_="article block untagged mb15")

    xiaohua_list=[]
    for div in alldiv:
        xiaohua=div.find('span').text
        xiaohua_list.append(xiaohua)

    nextPage=soup.find('span',class_='next')
    if nextPage:
        if u'下一页' in nextPage.text:
            print index+nextPage.parent['href'].split('?')[0]
            return xiaohua_list,index+nextPage.parent['href']
    else:
        print data
        print "next Page miss"
    return xiaohua_list,None

def main():
    url=URL
    with codecs.open('xiaohua.txt','wb',encoding='utf-8') as fp:
        while url:
            html=download_page(url)
            xiaohuas,url=find_data_in_html_content(html)
            fp.write(u'{xiaohuas}'.format(xiaohuas='\n\n'.join(xiaohuas)))
            time.sleep(20)

if __name__=='__main__':
    main()
