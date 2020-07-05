import pymongo
import time
import datetime

RELEASE="M49server 0.5.4 build 20.7.5"
M49Servername='server3'
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.M49
DATEserver=datetime.datetime.now()
db.devices.update_one({'Name':M49Servername}, {'$set':{'date': DATEserver, 'System':RELEASE}})

    
def cputemp():
    '''
    2020.6.24 verify the cpu temperature and add to systemlog and devices
    2020.7.2 try/except if not the host is a Raspberry PI
    '''
    try:
        with open(r"/sys/class/thermal/thermal_zone0/temp") as File:
            CurrentTemp = File.readline()
        CPUtemp=str(float(CurrentTemp) / 1000)
        print('CPU Temperature',CPUtemp)
        db.systemlog.insert_one({'date': DATEserver, 'CPUtemp': CPUtemp})
        db.devices.update_one({'Name':M49Servername}, {'$set':{'CPUtemp': CPUtemp}})
        File.close()
        
    except:
        print(' file not found')

def ProcessLog():
    '''
    2020 06 25 insert collection in  processlog from syslog message INProcessLog
    '''
    print('************* ProcessLog ', end="")
    # select the syslog collection contain INProcessLog and set Status 49
    syslogMSGquery = {'message' : {'$regex' : ".*INProcessLog*."}}
    db.syslog.update_many(syslogMSGquery, {'$set':{'Status':49}})
    # select syslog with status = 49
    conta=0
    for msg in db.syslog.find({'Status':49}):
        # compose the ProcessLog record
        message_clean=msg['message'].replace("<14>INProcessLog#","").split(",")
        ProcessLogName = message_clean[0]
        ProcessLogdate = message_clean[3]
        processlogMSG={
        'IP':msg['host'],
        'Name': ProcessLogName,
        'Pid': message_clean[1],
        'Pname': message_clean[2],
        'date': DATEserver }
        #print(processlogMSG)
        #break
        # add ProcessLog records
        db.processlog.insert_one(processlogMSG)
        conta+=1

    # delete syslog with status = 49
    db.syslog.delete_many({'Status':49})
    print(conta)

