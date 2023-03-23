import os

import requests
import os
import re
import urllib
import urllib.request
import os
from internetdownloadmanager import Downloader
import pandas as pd
import time

import os
import time
from urllib.parse import unquote

import requests

dizhi='https://files-cdn.cnblogs.com/files/blogs/738530/hebin.zip?download=true'
r2=requests.get('https://files-cdn.cnblogs.com/files/blogs/738530/hebin.zip?download=true')
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
        urll='https://files-cdn.cnblogs.com/files/blogs/738530/hebin.zip?download=true'

        file_name1 = get_file.get(url=urll,stream=True)
        file_name = get_file_name(urll, file_name1.headers)
        print("文件名称：" + file_name)
        get_file.close()



    return file_name

def batch_rename(file_dir, old_ext, new_ext):
    list_file = os.listdir(file_dir) # 返回指定目录
    for file in list_file:
        ext = os.path.splitext(file) # 返回文件名和后缀
        if old_ext == ext[1]:   # ext[1]是.doc,ext[0]是1
            newfile = ext[0] + new_ext
            os.rename(os.path.join(file_dir, file),
                      os.path.join(file_dir, newfile))

def zhuyao():
    ptt=start(dizhi)
    with open(ptt,mode='wb') as f:
        f.write(r2.content)
    try:
        batch_rename(".", ".zip", ".py")
    except:
        print("重命名失败")








