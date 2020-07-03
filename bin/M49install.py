from M49lib import *
import socket
hostname = socket.gethostname()
db.devices.insert_one({'Status': 3, 'Name':hostname, 'User': 'root', 'IP': 'localhost', 'System':RELEASE})
db.devices.create_index([ ("Status", -1) ])
