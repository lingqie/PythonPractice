#coding=utf-8
from selenium import webdriver
import time

# 如果是下载的exe，webdriver.PhantomJS(executable_path＝‘your exe path’)
driver =webdriver.PhantomJS()
driver.get("http://music.163.com/#/user/home?id=61032034")
# 等待网页加载完毕
time.sleep(20)
driver.save_screenshot('1.png')
content = driver.page_source
print content.encode('utf-8')
# print driver.page_source.encode('utf-8')
driver.close()
