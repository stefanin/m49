#! /usr/bin/python3.8
# 2020.6.24 syslogdel-add.py new script for insert message in syslogdel

import pymongo
import time
import sys
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["M49"]
try:
    print ("Add this message :", sys.argv[1], "in syslogdel")
    db.syslogdel.insert_one({'message': sys.argv[1]})
    
except:
    print("mmmm, please type syslogdel-add.py MESSAGE if the message contain specific MESSAGE")
    print("mmmm, please type syslogdel-add.py .*MESSAGE*. if the message contain  MESSAGE")
    print("mmmm, please type syslogdel-add.py MESSAGE*. if the message start to MESSAGE")
    print("mmmm, please type syslogdel-add.py .*MESSAGE if the message end to MESSAGE")