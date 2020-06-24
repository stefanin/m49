#! /usr/bin/python3.8
#pm2 start bin/M49server.py --name M49server.py --interpreter python3.8 --restart-delay 180000

import pymongo
import time
RELEASE="Devicelog rel. 0.5.0 build 20.6.20"
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["M49"]
deviceslog = db["deviceslog"]
devices = db["devices"]

print (RELEASE," start %s" % time.ctime(), flush=True)
for log in deviceslog.find({'Status':0}):
    print(log['Name'])
    newdevice=True
    log_id=log['_id']
    # replace the devices row
    for device in devices.find({'Name':log['Name']}):
        print('update device ',device['Name'])
        newdevice=False
        log.pop('_id') #remove the item id
        devices.replace_one({'Name':log['Name']},log)
    #new devices
    if newdevice:
        print('new device ',log['Name'] )
        devices.insert_one(log)
    #update the devicelog.status =1
    deviceslog.update_one({'_id':log_id}, {'$set':{'Status':1}})

print (RELEASE," stop %s" % time.ctime(), flush=True)

        