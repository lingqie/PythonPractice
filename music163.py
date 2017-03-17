#coding=utf-8
from selenium import webdriver
import time
import requests
import codecs
from bs4 import BeautifulSoup

URL="http://music.163.com/#/user/home?id=61032034"
index="https://erogamescape.dyndns.org/"

def download_page(url):
    driver =webdriver.PhantomJS()
    driver.get(url)
    # 等待网页加载完毕
    time.sleep(20)
    driver.save_screenshot("1.jpg")
    content = driver.page_source
    driver.close()
    return content.encode('utf-8')

    # print driver.page_source.encode('utf-8')


def parse_html(data):
    soup=BeautifulSoup(data,"lxml")
    alldiv = soup.find("div", class_="m_record")
    # print alldiv
    for div in alldiv:
        print div

def main():
    url=URL
    data=download_page(url)
    parse_html(data)

if __name__=='__main__':
    main()
