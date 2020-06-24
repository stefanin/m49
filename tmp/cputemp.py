from M49lib import *
import pymongo
import datetime
with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
        CurrentTemp = File.readline()
CPUtemp=str(float(CurrentTemp) / 1000)
print(CPUtemp)
db.systemlog.insert_one({'date': datetime.datetime.now(), 'CPUtemp': CPUtemp})
db.devices.update_one({'Name':M49Servername}, {'$set':{'date': datetime.datetime.now(),'CPUtemp': CPUtemp}})

File.close()
