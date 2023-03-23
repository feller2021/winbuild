import os
import re
import urllib
import urllib.request
import os
from internetdownloadmanager import Downloader
import pandas as pd
import time
import xiazaihebin
import os
import time
from urllib.parse import unquote

import requests

if os.path.exists("./output"):
    print(f"切割文件夹已经存在，无需创建")
else:
    os.mkdir("./output")
    print(f"切割文件夹不存在，已经创建")

if os.path.exists("./"+"Id.txt"):
    print(f"Id.txt已经存在，无需创建")
else:

    print(f"Id.txt不存在，创建中")
    file = open("./Id.txt", 'w')

    # 写入内容信息
    # file.write(text)

    file.close()
    print('文件创建成功')


headers = {
    "Content-Type": "d0.ananas.chaoxing.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
    "Referer": 'https://sharewh.chaoxing.com/'
}
def zhenurl(url):
    r2=requests.get(url)


    str22 = str(r2.text)#window.location.href
    url = re.findall('downloadUrl = \'(.+?)\';', str22)
    ddd=str(url)
    d1=ddd.replace('[\'', '')
    d2=d1.replace('\']', '')
    print(d2)
    return d2



def get_file_name(url, headers):
    filename = ''
    if 'Content-Disposition' in headers and headers['Content-Disposition']:
        disposition_split = headers['Content-Disposition'].split(';')
        if len(disposition_split) > 1:
            if disposition_split[1].strip().lower().startswith('filename='):
                file_name = disposition_split[1].split('=')
                if len(file_name) > 1:
                    filename = unquote(file_name[1])
    if not filename and os.path.basename(url):
        filename = os.path.basename(url).split("?")[0]
    if not filename:
        return time.time()
    return filename


def start(url):
    with requests.Session() as get_file:
        urll=zhenurl(url)

        file_name1 = get_file.get(url=urll,stream=True, headers=headers,timeout=10)
        file_name = get_file_name(urll, file_name1.headers)
        print("文件名称：" + file_name)
        get_file.close()



    return file_name



returnDict = {}
localtime = time.localtime(time.time())#获取当前时间
filetime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))#把获取的时间转换成"年月日格式”
# print(filetime)
pt="./output"
files= os.listdir(pt)
s = []

def isfilecunzai(filename):
    k=False
    for file in files:
        s.append(file)

    for yuansu in s:
        if filename in yuansu :

            k=True
            break
    # print(k)
    return k

def batch_rename(file_dir, old_ext, new_ext):
    list_file = os.listdir(file_dir) # 返回指定目录
    for file in list_file:
        ext = os.path.splitext(file) # 返回文件名和后缀
        if old_ext == ext[1]:   # ext[1]是.doc,ext[0]是1
            newfile = ext[0] + new_ext
            os.rename(os.path.join(file_dir, file),
                      os.path.join(file_dir, newfile))


try:
    itemIds = []

    wenjianminqianwu=''
    with open('Id.txt', 'r') as f:

        for line in f.readlines():
            line = line.strip('\n')
            itemIds.append("https://sharewh.chaoxing.com/share/download/"+line)


    for i in itemIds:
        # print(i)



        if os.path.splitext(start(i))[-1] == ".zip":
            r2=requests.get(zhenurl(i),headers=headers,stream=True)
            print("下载manifest文件")


            ptt="./output/"+start(i)
            with open(ptt,mode='wb') as f:


                f.write(r2.content)
            try:
                batch_rename("output/", ".zip", "")
            except:
                print("重命名失败")




        else:





            ptt="./output/"+start(i)
            if isfilecunzai(start(i))==True:
                print("文件已存在，跳过下载")
                # break
            else:
                print("开始下载。。。")

                r2=requests.get(zhenurl(i),headers=headers,stream=True)
                print("下载正式切片文件")
                with open(ptt,mode='wb') as f:
                    f.write(r2.content)

        wenjianminqianwu=start(i)

    wenjianminqianwu=wenjianminqianwu[0:8]















except:

    print("下载异常")

print("对文件进行合并中...")



xiazaihebin.zhuyao()
val = os.system('hebin.py -m '+wenjianminqianwu+filetime+'_zh-cn.iso')



