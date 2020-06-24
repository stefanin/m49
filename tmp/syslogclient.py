
import logging

import logging.handlers

#Create you logger. Please note that this logger is different from  ArcSight logger.

my_logger = logging.getLogger('MyLogger')

#We will pass the message as INFO

my_logger.setLevel(logging.INFO)

#Define SyslogHandler

handler = logging.handlers.SysLogHandler(address = ('192.168.1.252',514))

#X.X.X.X =IP Address of the Syslog Collector(Connector Appliance,Loggers  etc.)

#514 = Syslog port , You need to specify the port which you have defined ,by default it is 514 for Syslog)

my_logger.addHandler(handler)

#Example: We will pass values from a List

List1 = ['Manchester','Chelsea','Arsenal']

for row in List1:

     my_logger.info("I was in " +List1[0])
