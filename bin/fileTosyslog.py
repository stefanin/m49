
import os
import time
import logging
import logging.handlers
import socket
import sys

M49logger = logging.getLogger('M49Logger')
M49logger.setLevel(logging.INFO)
hostname = socket.gethostname()

fileSeek=0
fileStatus=0
conta=0
fileStatuslast=0

def leggefiletosyslog(fileName,fileSeek,M49logger):
        try:    
            f = open(fileName, "r")
            f.seek(fileSeek)# posizione precedente
            with f as l:
                content=f.read().splitlines()
                fileSeek=f.tell()
            f.close()
            #print(fileSeek)
            for riga in content:
                #print(hostname,"#",riga)
                M49logger.info(hostname+"#"+riga)
        except:
            print("Errore file ",fileName)
            M49logger.info(hostname+"#"+"Errore file "+fileName)        
        return fileSeek 


try:
    handler = logging.handlers.SysLogHandler(address = (sys.argv[1],514))
    M49logger.addHandler(handler)
    fileName=sys.argv[2]
    while True:
        print("Verifico i file")
        try:
            fileStatus=os.stat(fileName).st_size
            #print(fileStatus)
            if (fileStatus>fileStatuslast): #file incrementato
                    fileStatuslast=leggefiletosyslog(fileName,fileStatuslast,M49logger)
            conta+=1
        except:
            print("Errore file ",fileName)
            M49logger.info(hostname+"#"+"Errore file "+fileName)        

        print("Ho finito n°: ",conta)
        time.sleep(20)

except:
    print("!mmmm, fileTosyslog SYSLOGSERVERIP FILE")
