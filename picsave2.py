# encoding=utf-8
from selenium import webdriver
import requests
import codecs
import time
from bs4 import BeautifulSoup

# index="http://www.qiushibaike.com"
URL="https://xn--bck3aza1a2if6kra4ee0hf.gamewith.jp/article/show/20722"
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
    alltr=soup.find('table',class_="sorttable").findAll('tr')
    result_list=[]
    for tr in alltr:
        name=tr.contents[0].text
        imgpath=""
        for x in tr.children:
            if(x.img):
                imgpath=x.img.get('src')
        # charname
        shuxing=tr.contents[1].text
        # shuxing
        zhongzu=tr.contents[2].text
        # zhongzu
        personTxT= u'{person}'.format(person=
"{\"name\":\""+name+"\",\
\"imgpath\":\""+imgpath+"\",\
\"shuxing\":\""+shuxing+"\",\
\"zhongzu\":\""+zhongzu+"\"}")
        print personTxT.encode('utf-8')
        result_list.append(personTxT)

    # xiaohua_list=[]
    # driver =webdriver.PhantomJS()
    # for img in alldiv:
    #     path=img.get('src')
    #     if '/a/s' in path:
    #         print path
    #         xiaohua_list.append(path)
    #
    # for i,path in enumerate(xiaohua_list):
    #     # driver.get(path);
    #     # driver.save_screenshot("4%02d.png"%i)
    #     pic = requests.get(path)
    #     fp = open("/Users/developer/Documents/blog/gbf/image/ssr/1%02d.png"%(i+1), 'wb')
    #     fp.write(pic.content)
    #     # print position+each
    #     fp.close()
    #
    # driver.close()
    # return xiaohua_list

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
