# encoding=utf-8
from selenium import webdriver
import requests
import codecs
import time
from bs4 import BeautifulSoup

# index="http://www.qiushibaike.com"
URL="http://seesaawiki.jp/aigis/d/%a5%d7%a5%e9%a5%c1%a5%ca"
# position = '/Users/developer/Documents/blog/aigis/image/golden'

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
    alldiv=soup.findAll('img')
    xiaohua_list=[]
    driver =webdriver.PhantomJS()
    for img in alldiv:
        path=img.get('src')
        if '/a/s' in path:
            print path
            xiaohua_list.append(path)

    for i,path in enumerate(xiaohua_list):
        # driver.get(path);
        # driver.save_screenshot("4%02d.png"%i)
        pic = requests.get(path)
        fp = open("/Users/developer/Documents/blog/aigis/image/platinum/5%02d.png"%(i+1), 'wb')
        fp.write(pic.content)
        # print position+each
        fp.close()

    driver.close()
    return xiaohua_list

def main():
    url=URL
    # with codecs.open('xiaohua.txt','wb',encoding='utf-8') as fp:
    #     while url:
    html=download_page(url)
    find_data_in_html_content(html)
    # fp.write(u'{xiaohuas}'.format(xiaohuas='\n\n'.join(xiaohuas)))
    # time.sleep(20)

if __name__=='__main__':
    main()
