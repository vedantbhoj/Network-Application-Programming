import difflib
import datetime
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from netmiko import ConnectHandler

#Defining the device to be monitored
ip = '10.10.10.3'

#Defining the device type for running netmiko (SSH management to Network Devices)
device_type = 'arista_eos'

#Defining the username and password for running netmiko
username = 'admin'
password = 'andrewbond'

#Defining the command to send to each device
command = 'show running'
command1 = 'show ip int brief'

#Connecting to the device via SSH
session = ConnectHandler(device_type = device_type, ip = ip, username = username, password = password, global_delay_factor = 3)

#Entering enable mode
enable = session.enable()

#Sending the commands and storing the output (running configuration)
output = session.send_command(command)
output += session.send_command(command1)

#Defining the file from yesterday, for comparison.
device_cfg_old = 'cfgfiles/' + ip + '_' + (datetime.date.today() - datetime.timedelta(days = 1)).isoformat()

#Writing the command output to a file for today.
with open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'w') as device_cfg_new:
    device_cfg_new.write(output + '\n')

#Extracting the differences between yesterday's and today's files in HTML format
with open(device_cfg_old, 'r') as old_file, open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'r') as new_file:
    difference = difflib.HtmlDiff().make_file(fromlines = old_file.readlines(), tolines = new_file.readlines(), fromdesc = 'Yesterday', todesc = 'Today')
    
#Sending the differences via email

#Defining the e-mail parameters
fromaddr = 'theoriginalcmpe207@gmail.com'
recipients = ['theoriginalcmpe207@gmail.com', 'vedant.bhoj@sjsu.edu', 'haoran.chen@sjsu.edu','ketan.rudrurkar@sjsu.edu', 'tejas.madappa@sjsu.edu']
toaddr = ", ".join(recipients)

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'CPU Utilization Graph and Configuration Report'

#Attach Graph image to the email body
ImgFileName = 'CPU_graph.png'
img_data = open(ImgFileName, 'rb').read()
image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
msg.attach(image)
msg.attach(MIMEText(difference, 'html'))

#Sending the email via Gmail's SMTP server on port 587
server = smtplib.SMTP('smtp.gmail.com', 587)

#SMTP connection is in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
server.starttls()

#Logging in to Gmail and sending the e-mail
server.login('theoriginalcmpe207', 'Panda@321')
server.sendmail(fromaddr, recipients, msg.as_string())
print('-- Email is sent to following recipients:'+ toaddr +' successfully -- \n')
print('-- Email contains CPU Utilization graph and Configuration Report -- \n')
server.quit()

#End Of Program
