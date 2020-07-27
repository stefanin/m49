from M49lib import *
import getpass
hostname = socket.gethostname()
username = getpass.getuser().lower()
db.devices.insert_one({'Status': 3, 'Name':hostname, 'User': username, 'IP': 'localhost', 'System':RELEASE})
db.devices.create_index([ ("Status", -1) ])
