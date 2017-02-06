# encoding=utf-8
import requests
import codecs
from bs4 import BeautifulSoup

name="1.jpg"
url="http://cuiqingcai.com/wp-content/themes/Yusi/timthumb.php?src=http://qiniu.cuiqingcai.com/wp-content/uploads/2016/02/bg1-e1454442892955.jpg&h=64&w=100&q=90&zc=1&ct=1"

def saveImg(imageURL,fileName):
    data=requests.get(url,stream=True)
    with open(name, 'wb') as f:
        f.write(data.content)

def mkdir(path):
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

def main():
    # saveImg(url,name)

if __name__=='__main__':
    main()
