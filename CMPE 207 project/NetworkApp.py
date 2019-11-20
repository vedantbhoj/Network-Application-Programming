import sys
import time
import os
import time
from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads

#Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

#Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#Verifying the reachability of each IP address in the list
try:
    ip_reach(ip_list)
    
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#Calling threads creation function for the SSH connection
n = 1
while (n<=30):
    create_threads(ip_list, ssh_connection)
    time.sleep(10)
    n = n + 1

#End of program