import re
import requests
def zhenurl(url):
    r2=requests.get(url)
 
 
    str22 = str(r2.text)#window.location.href
    url = re.findall('downloadUrl = \'(.+?)\';', str22)
    ddd=str(url)
    d1=ddd.replace('[\'', '')
    d2=d1.replace('\']', '')
    print(d2)
    return d2
