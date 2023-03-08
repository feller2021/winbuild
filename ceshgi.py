import henin
import json
import os
import time
import requests
from requests_toolbelt import MultipartEncoder
datanames = os.getcwd()
datanames2 = os.listdir(datanames)
SCKEY = os.environ["SCKEY"]
SCKEY2 = os.environ["SCKEY2"]
URLKEY = os.environ["URLKEY"]
 
 
 
os.mkdir("./output")
pt="./output"
id=''
 
def batch_rename(file_dir, old_ext, new_ext):
    list_file = os.listdir(file_dir) # 返回指定目录
    for file in list_file:
        ext = os.path.splitext(file) # 返回文件名和后缀
        if old_ext == ext[1]:   # ext[1]是.doc,ext[0]是1
            newfile = ext[0] + new_ext
            os.rename(os.path.join(file_dir, file),
                      os.path.join(file_dir, newfile))
 
 
if not os.path.getsize(pt):
    print("为空!我切片！")
    os.system('ls')
    os.system('pwd')
    for dataname in datanames2:
        if os.path.splitext(dataname)[1] == '.ISO':  # 目录下包含.json的文件
 
            print(datanames + "/" + dataname)
            dizhi = datanames + "/" + dataname
            
            anz=os.system('pip3 install filesplit')
            val = os.system('henin -c dizhi -s 240000')
            # val = os.system('henin -m zh-cn_dc141532.iso')
            print (val)
 
 
 
 
else:
    print("不为空！ 我上传！")
    files= os.listdir(pt) #得到文件夹下的所有文件名称
    s = []
    url = URLKEY
    for file in files: #遍历文件夹
        wenjiandizhi2=pt+"/"+file
        # print(wenjiandizhi)
        if os.path.splitext(file)[0] == 'manifest':
            print("else-os.getcwd()。。"+str(os.getcwd()))
            print("else-os.listdir(datanames)。。"+str(os.listdir(datanames)))
            os.system('ls')
            os.system('pwd')
            batch_rename(pt, "", ".zip")
            time.sleep(6)
            wenjianm=file+".zip"
            manifestdizhi=pt+"/"+wenjianm
            time.sleep(6)
            print("file:"+file)
            print("manifestdizhi:"+manifestdizhi)
 
            m = MultipartEncoder(
                fields={'name': wenjianm, 'puid': SCKEY,'_token': SCKEY2,
                        'file': (wenjianm, open(manifestdizhi, 'rb'))}
            )
            time.sleep(6)
            print("file:"+file)
            print("manifestdizhi:"+manifestdizhi)
            headers = {
                "Content-Type": m.content_type,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
                "Connection": 'close'
            }
            with requests.Session() as up:
                r = up.post(url, data=m,
                            headers=headers, timeout=(7,12))
                res=r.text
                jsonobj = json.loads(res)
                msg=jsonobj['msg']
                print(msg)
                toCntPercent = jsonobj['objectId']
                id=toCntPercent
 
        else:
            print("没有manifest文件。。")
            print("else-os.getcwd()。。"+str(os.getcwd()))
            print("else-os.listdir(datanames)。。"+str(os.listdir(datanames)))
            os.system('ls')
            os.system('pwd')

            m = MultipartEncoder(
                fields={'name': file, 'puid': SCKEY,'_token': SCKEY2,
                        'file': (file, open(wenjiandizhi2, 'rb'))}
            )
            time.sleep(6)
            headers = {
                "Content-Type": m.content_type,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
                "Connection": 'close'
            }
            with requests.Session() as up:
                r = up.post(url, data=m,
                            headers=headers, timeout=(7,12))
                res=r.text
                jsonobj = json.loads(res)
                msg=jsonobj['msg']
                print(msg)
                toCntPercent = jsonobj['objectId']
                id=toCntPercent
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        with open('id.txt', 'a') as f:
            f.write('\n')
            f.write(toCntPercent)
            print(toCntPercent)
