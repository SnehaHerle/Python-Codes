#! /usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "sneha.herle@gmail.com"
toaddr = "sneha.herle@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Email through Python!"
 
body = "Hey there! I sent this through Python modules. It is so fascinating to do this! Yay! *_*"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "dreamnit")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
