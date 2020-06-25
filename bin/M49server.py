#! /usr/bin/python3.8
#pm2 start bin/M49server.py --name M49server.py --interpreter python3.8 --restart-delay 180000

from M49lib import *
deviceslog = db["deviceslog"]
devices = db["devices"]

print (RELEASE," start %s" % time.ctime(), flush=True)
cputemp()
ProcessLog()
print("************* deviceslog ", end="")
conta=0
for log in deviceslog.find({'Status':0}):
    #print(log['Name'])
    newdevice=True
    log_id=log['_id']
    # replace the devices row
    for device in devices.find({'Name':log['Name']}):
        #print('update device ',device['Name'])
        newdevice=False
        log.pop('_id') #remove the item id
        devices.replace_one({'Name':log['Name']},log)
    #new devices
    if newdevice:
        #print('new device ',log['Name'] )
        devices.insert_one(log)
    #update the devicelog.status =1
    deviceslog.update_one({'_id':log_id}, {'$set':{'Status':1}})
    conta+=1
print(conta)
# clear syslog collections from syslodel
print("************* syslog batch delete",end="")
conta=0
for sysdelcoll in db.syslogdel.find({}):
    delstr = sysdelcoll['message']
    myquery = {'message' : {'$regex' : delstr}}
    x = db.syslog.delete_many(myquery)
    print(sysdelcoll['message']," : ",x.deleted_count)
    conta+=1

print(conta)

print (RELEASE," stop %s" % time.ctime(), flush=True)

        