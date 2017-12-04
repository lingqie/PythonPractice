# encoding=utf-8
from selenium import webdriver
import requests
import codecs
import time
from bs4 import BeautifulSoup

# index="http://www.qiushibaike.com"
URL="https://xn--bck3aza1a2if6kra4ee0hf.gamewith.jp/article/show/20722"
URL2="https://xn--bck3aza1a2if6kra4ee0hf.gamewith.jp/article/show/20723"
URL3="https://xn--bck3aza1a2if6kra4ee0hf.gamewith.jp/article/show/20724"
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

def find_data_in_html_content(data,prefiximage,floder):
    soup=BeautifulSoup(data,"lxml")
    alltr=soup.find('table',class_="sorttable").findAll('tr')
    result_list=[]
    for l,tr in enumerate(alltr):
        Id=prefiximage+"%03d"%(l);
        if(l!=0):
            name=tr.contents[0].text
            imgPath=""
            weapon=""
            for x in tr.children:
                if(x.a):
                    detailLink=x.a.get('href')
                    allTable=BeautifulSoup(download_page(detailLink)).findAll('table')
                    for table in allTable:
                        if u'レア/属性' in table.tr.contents[0]:
                            for i, r in enumerate(table):
                                if(i==3):
                                    for s,d in enumerate(r.children):
                                        if(s==0):
                                            print d.text.encode('utf-8')
                                            weapon=d.text.split('/')[1]
                if(x.img):
                    imgPath=x.img.get('src')
                    pic = requests.get(imgPath)
                    repalcedName=name.replace("/","-")
                    filepath="/Users/developer/Documents/blog/gbf/image/%s/%s.png"%(floder,repalcedName);
                    fp=open(filepath,'wb')
                    fp.write(pic.content)
            # charname
            shuxing=tr.contents[1].text
            # shuxing
            zhongzu=tr.contents[2].text
            # zhongzu
            personTxT= u'{person}'.format(person=
"{\"id\":\""+Id+"\",\
\"name\":\""+name+"\",\
\"weapon\":\""+weapon+"\",\
\"shuxing\":\""+shuxing+"\",\
\"zhongzu\":\""+zhongzu+"\"}")
            print personTxT.encode('utf-8')
            result_list.append(personTxT)
    return result_list

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
    ssrurl=URL
    srurl=URL2
    rurl=URL3
    ssrhtml=download_page(ssrurl)
    srhtml=download_page(srurl)
    rhtml=download_page(rurl)
    result1=find_data_in_html_content(ssrhtml,"0","ssr")
    find_data_in_html_content(srhtml,"1","sr")
    find_data_in_html_content(rhtml,"2","r")
    with codecs.open('ssr.txt','wb',encoding='utf-8') as fp:
        fp.write(u'{result}'.format(result='\n\n'.join(result1)))

if __name__=='__main__':
    main()
