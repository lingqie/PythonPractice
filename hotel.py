# encoding=utf-8
import requests
import codecs
import time
from bs4 import BeautifulSoup

index="http://zh.macaotourism.gov.mo/plan/hotel.php?class=1"
URL="http://zh.macaotourism.gov.mo/plan/hotel.php?class="

def download_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    }
    try:
        data=requests.get(url,headers,timeout=None).content
        return data
    except (requests.ConnectionError,IndexError,UnicodeEncodeError,requests.exceptions.ReadTimeout):
        print "Timeout or ConnectionError"

def find_data_in_html_content(data,j):
    soup=BeautifulSoup(data)
    alldiv=soup.findAll('div',class_="hotel_item")

    xiaohua_list=[]
    for div in alldiv:
        link=div.find('a').get('onclick')
        if(link==None):
            link=div.find('a').find_next_sibling("a").get('onclick')
        clicklink=link.split("\'")
        fax,tel=find_tel_fax(download_page("http://zh.macaotourism.gov.mo/plan/"+clicklink[1]))
        xiaohua=div.find('div').find('a').text
        xiaohuaTxT= u'{xiaohuas}'.format(xiaohuas="{\"nameZh\":\""+xiaohua+"\",\"nameEh\":\"\",\"number\":\""+'%03d'%j+"\",\"tel\":\""+tel+"\",\"fax\":\""+fax+"\",\"email\":\"\"}")
        # print xiaohuaTxT
        xiaohua_list.append(xiaohuaTxT)
        j+=1
    return xiaohua_list,j

def find_tel_fax(data):
    soup=BeautifulSoup(data)
    fax=""
    tel=""
    infodiv=soup.findAll('div',class_="travelagen_hotel_detail_content_info")
    for div in infodiv:
        if u"電話" in div.text:
            tel=div.text.split(":")[1]
        if u"傳真" in div.text:
            fax=div.text.split(":")[1]
    return fax,tel


def main():
    url=URL
    i=1
    j=1
    with codecs.open('hotel.js','wb',encoding='utf-8') as fp:
        while i<=4:
            nowurl = url+str(i)
            print nowurl
            i+=1
            html=download_page(nowurl)
            xiaohuas,j=find_data_in_html_content(html,j)
            fp.write(u'[{xiaohuas}]'.format(xiaohuas=','.join(xiaohuas)))

if __name__=='__main__':
    main()
