import json
import os
import time
import requests
from requests_toolbelt import MultipartEncoder
datanames = os.getcwd()
datanames2 = os.listdir(datanames)
 
os.mkdir("./output")
pt="./output"
SCKEY = os.environ["SCKEY"]
SCKEY2 = os.environ["SCKEY2"]
URLKEY = os.environ["URLKEY"]
 
 
 
 
 
 
def bulid():
    id=''
    for dataname in datanames2:
        wenjiandizhi2=pt+"/"+dataname
        print("遍历文件夹")
        if os.path.splitext(dataname)[1] == '.ISO':  # 目录下包含.json的文件
            print("没有manifest文件。。")
            print("else-os.getcwd()。。"+str(os.getcwd()))
            print("else-os.listdir(datanames)。。"+str(os.listdir(datanames)))
            os.system('ls')
            os.system('pwd')
 
            url = URLKEY
            # files = {'file': open(dizhi, 'rb')}  #
            # data = {
            #     "name": "ISO.ISO",
            #     "puid": SCKEY,
            #     "_token": SCKEY2,
            # }
            # r = requests.post(url, files=files, data=data, timeout=120)
 
            m = MultipartEncoder(
                fields={'name': dataname, 'puid': SCKEY,'_token': SCKEY2,
                        'file': (dataname, open(wenjiandizhi2, 'rb'))}
            )
            time.sleep(6)
            headers = {
                "Content-Type": m.content_type,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
                "Connection": 'close'
            }
            r = requests.post(url, data=m,
                              headers=headers, timeout=(7,12))
            time.sleep(6)
            res=r.text
            # print(res)
            jsonobj = json.loads(res)
            msg=jsonobj['msg']
            print(msg)
            toCntPercent = jsonobj['objectId']
            id=toCntPercent
            with open('id.txt', 'a') as f:
                f.write('\n')
                f.write(toCntPercent)
                print(toCntPercent)
        else:
            print("没文件")
    return id
if __name__ == '__main__':
    bulid()
