import schedule  #比APScheduler要简单，但是没有APScheduler强大，无法持久化任务，也无法动态增加删$
                 #通过 pip install schedule 即可安装。
import time
global int_a
int_a = 1
#抓出网页原始码(要安装套件 pip install requests 和 Beautifulsoup4 )
from queue import Empty
import string
from typing import Text
import urllib.request as req
import requests
import re
import bs4 #载入套件beautifulsoup4 叫bs4
import ssl          #全局取消证书验证，如果用的是requests模块的get方法，里面有一个verify参数，将其设成False就可以了。
ssl._create_default_https_context = ssl._create_unverified_context  #全局取消证书验证
# url 传参数格式：http://127.0.0.1/bilingualplan/?no1_position_x=30&no1_position_y=15&no2_position_x=60&no2_position_x=15&working_lighter=Working_lighter&screen=screen&meeting_room_video_on_off=Meeting_room_video_on_off&office_video_on_off=Office_video_on_off&work_route=B_line&Leave_message=%E6%9C%89%E9%97%AE%E9%A2%98%E8%AF%B7%E7%95%99%E8%A8%80
def crawler():
    global int_a
    url="https://www.moh.gov.sg/"
    url_2="http://bilingualplan.com"
    url_3="https://ems156.com"
    url_4="http://127.0.0.1/bilingualplan/"
    classString_1="semibold pt-3"  # 修饰日期+时间：As of 24 Dec 2021, 12:00pm的class, 
    classString_2="stat-item "     # 块 div 的 class,包含有 big-number 的 p, 用在v2和之前的版本
    classString_3="number"         # 修饰New Case等主要数字的class

    #建立一个Requst物件，附加 Request Headers 的信息 
    #請求程式碼中加入 user-agent 以及 content-type
    #user-agent 字串適用於確認用端資訊的欄位，比方說瀏覽器版本號以及作業系統，也是反爬蟲時可能會確認的欄位
    #content-type 則是設定資源請求的格式，讓伺服器知道我們要請求的格式，以防被伺服器因無法確認格式而拒絕
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")         # 正确显示中文
        #print(data)
    root=bs4.BeautifulSoup(data,"html.parser")       # 需要Beautifulsoup4帮助解析html格式文件
    # 第一步：取日期数字：

    datetitles = root.find("p", class_=classString_1)  # 寻找class = "semibold pt-3"的 p 标签
    #print(datetitles.string)                        #打印有  p 标签的包含的字符串

    newcaseDatepy = datetitles.string[6:17]
    print(newcaseDatepy)

    # 第二步：取新增加数字

    newcaseNumber=root.findAll("p", class_=classString_3)
    newcaseNumberpy = newcaseNumber[2].string
    localPCR = newcaseNumber[3].string
    localART = newcaseNumber[4].string
    importedPCR = newcaseNumber[5].string
    importedART = newcaseNumber[6].string
    print(localPCR)
    print(localART)
    print(importedPCR)
    print(importedART)
    #newcaseNumberpy = newcaseNumber[2].string
    #newcaseNumberint = int((localPCR).replace(",",""))+int((localART).replace(",",""))+int((importedPCR).replace(",",""))+int((importedART).replace(",",""))
    #newcaseNumberpy = f"{newcaseNumberint:,d}" #其中冒号后面的部分是格式说明符。逗号是所需的分隔符，因此f"{num:_d}"使用下划线而不是逗号。
    print(newcaseNumberpy)

    res=requests.get(url_2,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    },params={"newcaseNumber":newcaseNumberpy,"newcaseDate":newcaseDatepy,"localPCR":localPCR,"localART":localART,"importedPCR":importedPCR,"importedART":importedART})

    res=requests.get(url_3,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    },params={"newcaseNumber":newcaseNumberpy,"newcaseDate":newcaseDatepy,"localPCR":localPCR,"localART":localART,"importedPCR":importedPCR,"importedART":importedART})

    res=requests.get(url_4,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"
    },params={"newcaseNumber":newcaseNumberpy,"newcaseDate":newcaseDatepy,"localPCR":localPCR,"localART":localART,"importedPCR":importedPCR,"importedART":importedART})

    print(res)
    #print(res.text)

    int_a = int_a + 1
    if int_a > 1:
      schedule.clear()
      exit(0)           #exit(1) 表示发生了错误进行退出，而 exit(0) 则表示程序是正常退出>$

#crawler()
schedule.every(8).seconds.do(crawler)
while True:
    #启动服务
    schedule.run_pending()
    time.sleep(1) #推迟5执行的秒数
