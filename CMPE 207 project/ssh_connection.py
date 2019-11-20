import paramiko
import datetime
import os.path
import time
import sys
import re

#Adding User File
user_file = 'user.txt'

#Verifying if the user is valid
if os.path.isfile(user_file) == True:
    print("\n -- Username and password file is valid -- \n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()
        
#Adding commands file
cmd_file = 'cmd.txt'

#Verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n -- Command file is valid --\n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys.exit()
    
#Open SSHv2 connection to the device
def ssh_connection(ip):
    
    global user_file
    global cmd_file
    
    #Creating SSH CONNECTION
    try:
        #Define SSH parameters
        selected_user_file = open(user_file, 'r')

        selected_user_file.seek(0)

        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        
        selected_user_file.seek(0)
        
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        #Logging into device
        session = paramiko.SSHClient()
        
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        #Connect to the device using username and password          
        session.connect(ip.rstrip("\n"), username = username, password = password)
        
        #Start an interactive shell session on the router
        connection = session.invoke_shell()	
        
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)
        
        #Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)
        
        selected_cmd_file = open(cmd_file, 'r') 
        
        selected_cmd_file.seek(0)
        
        #Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        #Closing the user file
        selected_user_file.close()
        
        #Closing the command file
        selected_cmd_file.close()
        
        #Checking command output for IOS syntax errors
        router_output = connection.recv(65535)
        
        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))
            
        else:
            print("\nDONE for device {}. Data sent to file at {}.\n".format(ip, str(datetime.datetime.now())))
            
        #Test for reading command output
        #print(str(router_output) + "\n")
        
        #Searching for the CPU utilization value within the output of "show processes top once"
        cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)* us,", router_output)
        
        #Extracting the second group, which matches the actual value of the CPU utilization and decoding to the UTF-8 format from the binary data type
        utilization = cpu.group(2).decode("utf-8")
        
        #Printing the CPU utilization value to the screen
        #print(utilization)
        
        #Opening the CPU utilization text file and appending the results
        with open("cpu.txt", "a") as f:
            f.write(utilization + "\n")

        with open("cpu1.txt", "a") as f:
            f.write(utilization + "\n")
        
        #Closing the connection
        session.close()
     
    except paramiko.AuthenticationException:
        print("* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")
