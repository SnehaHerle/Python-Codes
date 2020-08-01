#! /usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "sneha.herle@gmail.com"
toaddr = "sneha.herle@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "An attachment through Python!"
 
body = "Hey Capt! I sent this attchment using Python modules. *_* Damn fascinating."
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "1.jpg"
attachment = open("/media/sneha/10DE098510DE0985/Fav Pics/1.jpg", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "dreamnit")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

