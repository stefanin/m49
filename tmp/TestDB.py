import pymongo
from datetime import datetime
from mpingLIB import *
import ipaddress
import socket


def IpIcmpScan(ipscan):
    ipscan=ipscan+'/32'
    for addr, rtime in mping(ipscan).items():
                    return rtime


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["M49"]
mycol = mydb["devices"]
mydoc = mycol.find()
print(mydoc.count())
print(IpIcmpScan("172.18.4.1"))

i=0
for x in mydoc:
      print(x['Computer_Name'],end=" ")
      try:
          ip=socket.gethostbyname(x['Computer_Name'])
          print(ip,end=" ")
          print(IpIcmpScan(ip))
      except:
          print('errore')

      i=i+1
#  if(i==10):
#      break

print(socket.gethostbyname('IT-MI-L3493'))

myquery = { "Computer_Name": { "$gt": "IT-MI-" } }

mydoc = mycol.find(myquery)
print(str(conta(mydoc)))
for x in mydoc:
  print(x)

myquery = { "Computer_Name": { "$lt": "IT-MI-L3333" } }

mydoc = mycol.find(myquery)
print(str(conta(mydoc)))




myquery = { "Computer_Name": { "$gt": "IT-MI-D" } }

mydoc = mycol.find(myquery)
print(str(conta(mydoc)))



for x in mydoc:
  print(x)
