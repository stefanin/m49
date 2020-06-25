RELEASE="M49Client 0.5.4 build 20.6.24"
SERVERIP="192.168.1.3"
SERVER_URL = "https://"+SERVERIP
INFO = "/info"
DEVICESLOG="/deviceslog-add"
import requests
import socket
import getpass
import time
import os
import sys
import urllib3
import wmi
import logging
import logging.handlers
import datetime
urllib3.disable_warnings()
NewTestTime=900
ncliclo = 0
#disable proxy
proxies = {
  "http": None,
  "https": None,
}

# configure SysLog
M49logger = logging.getLogger('M49Logger')
M49logger.setLevel(logging.INFO)
handler = logging.handlers.SysLogHandler(address = ('192.168.1.3',514))
M49logger.addHandler(handler)





#by github.com/angeloped/get_serial_number.py
# wmic bios get serialnumber#Windows
# hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid#Linux
# ioreg -l | grep IOPlatformSerialNumber#Mac OS X
def getSerialNumber():
    os_type = sys.platform.lower()
    if "win" in os_type:
    	command = "wmic bios get serialnumber"
    elif "linux" in os_type:
    	command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "darwin" in os_type:
    	command = "ioreg -l | grep IOPlatformSerialNumber"
    return os.popen(command).read().replace("\n","").replace("	","").replace(" ","").replace("SerialNumber","")

def getSystem():
    os_type = sys.platform.lower()
    if "win" in os_type:
    	command = "wmic OS get Caption"
    elif "linux" in os_type:
    	command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "darwin" in os_type:
    	command = "ioreg -l | grep IOPlatformSerialNumber"
    return os.popen(command).read().replace("\n","").replace("                   ","").replace("Caption","")

def dirtree(dir='.'):
    '''
        it list the tree files, starting the dir position
    '''
    fileslog=[]
    for root, dirs, files in os.walk(dir, topdown=False):
       for name in files:
          filesdato = {'nomefile':os.path.join(root, name)}
          fileslog.append(filesdato)
       for name in dirs:
          filesdato = {'file':os.path.join(root, name)}
          fileslog.append(filesdato)
    return fileslog

def SendProcessLog():
    SendProcessLogdate=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.117Z")
    #print(SendProcessLogdate)
    if "Windows" in System:
        conn = wmi.WMI()
        syslogMSGNum=0
        for process in conn.Win32_Process():
            processrecord =hostname+","+str(process.ProcessId)+","+process.Name+","+str(SendProcessLogdate)+","
            #print(process.ProcessId, process.HandleCount, process.Name)
            syslogMSG='INProcessLog#'+str(processrecord)
            M49logger.info(syslogMSG)
            syslogMSGNum+=1
        print("Send ",syslogMSGNum," process")


hostname = socket.gethostname()
username = getpass.getuser().lower()
serialNumber=getSerialNumber()
System= getSystem()
print(RELEASE,hostname,username,serialNumber,System)


#wmic bios get Name,Manufacturer,ReleaseDate,SerialNumber,SMBIOSBIOSVersion
#wmic OS get Caption,OSArchitecture,Version
#wmic diskdrive get model,name,size
#wmic product get Name,Vendor,Version,InstallDate

#disable


while True: #invio dati ogni NewTestTime
    while True: # invio dati login ip

        try:
            richiesta= requests.head(SERVER_URL+INFO,proxies=proxies, verify=False)# find info
            print(richiesta.status_code)
            if richiesta.status_code == 200:

                ip = socket.gethostbyname(socket.gethostname())
                VPNhostname = socket.gethostname()
                print(ip)
                numFiles= len(dirtree())

                data = {'IP': ip, 'Name': hostname, 'User': username,'Serial_Number': serialNumber, 'System':System, 'numFiles': numFiles }
                richiesta= requests.post(url = SERVER_URL+DEVICESLOG, data = data,proxies=proxies, verify=False)
                print(richiesta.text)
                SendProcessLog()
                break
        except:
            pass

        print(INFO+" not live")
        time.sleep(20)
    ncliclo=ncliclo+1
    print("wait "+str(NewTestTime)+" sec ncliclo n°"+str(ncliclo))
    time.sleep(NewTestTime)#test ogni 10 minuti prod ogni 30 minuti
