import pymongo
import time
import datetime

RELEASE="M49server 0.5.4 build 20.6.24"
M49Servername='server3'
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["M49"]


def cputemp():
    '''
    2020.6.24 verify the cpu temperature and add to systemlog and devices
    '''
    with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
        CurrentTemp = File.readline()
    CPUtemp=str(float(CurrentTemp) / 1000)
    print('CPU Temperature',CPUtemp)
    db.systemlog.insert_one({'date': datetime.datetime.now(), 'CPUtemp': CPUtemp})
    db.devices.update_one({'Name':M49Servername}, {'$set':{'date': datetime.datetime.now(),'CPUtemp': CPUtemp, 'System':RELEASE}})
    File.close()
