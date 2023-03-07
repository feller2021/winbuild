import json
import os
import requests
 
datanames = os.getcwd()
datanames2 = os.listdir(datanames)
SCKEY = os.environ["SCKEY"]
SCKEY2 = os.environ["SCKEY2"]
URLKEY = os.environ["URLKEY"]
 
 

 
def bulid():
    id=''
    for dataname in datanames2:
        if os.path.splitext(dataname)[1] == '.ISO':  # 目录下包含.json的文件
 
            print(datanames + "/" + dataname)
            dizhi = datanames + "/" + dataname
            url = URLKEY
            files = {'file': open(dizhi, 'rb')}  # 
            data = {
                "name": "ISO.ISO",
                "puid": SCKEY,
                "_token": SCKEY2,
            }
            r = requests.post(url, files=files, data=data,timeout=120) 
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
