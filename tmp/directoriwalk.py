import os
import time
import requests
import urllib3
import datetime

urllib3.disable_warnings()

SERVER_URL = "https://localhost"
FILESLOG_URL = "/fileslog-add"
hostname="it-mi-l3333"
fileslog=[]
datetime=datetime.datetime.now(datetime.timezone.utc)
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      filesdato = {'file':os.path.join(root, name)}
      fileslog.append(filesdato)
   for name in dirs:
      filesdato = {'file':os.path.join(root, name)}
      fileslog.append(filesdato)
#for riga in range(len(fileslog)):
#    print(fileslog[riga])
#disable
proxies = {
  "http": None,
  "https": None,
}
#richiesta= requests.post(url = SERVER_URL+FILESLOG_URL, data = fileslog[0],proxies=proxies, verify=False)
print("Start send data")
for riga in range(len(fileslog)):
    #print(fileslog[riga])
    richiesta= requests.post(url = SERVER_URL+FILESLOG_URL, data = fileslog[riga],proxies=proxies, verify=False)
    #print(richiesta.text)
print("Stop send data")
