import numpy as np 
import cv2
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import random

print("10")

# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# cap=cv2.VideoCapture(0)
# if True:
#   	ret,img=  cap.read();
#   	cv2.imwrite("frame.jpg",img)   
# else:
# 	break  # save frame as JPEG file
# while True:
# 	ret,img=  cap.read();
# 	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 	faces= face_cascade.detectMultiScale(gray, 1.3, 5)
# 	for (x,y,w,h) in faces:
# 		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# 	cv2.imshow('img',img)
	      

# 	k= cv2.waitKey(30) & 0xff
# 	if k==27:
# 		break
# cap.release()
# cv2.destroyAllWindows()

def rand_x_digit_num(x, leading_zeroes=True):
    """Return an X digit number, leading_zeroes returns a string, otherwise int"""
    if not leading_zeroes:
        # wrap with str() for uniform results
        return random.randint(10**(x-1), 10**x-1)  
    else:
        if x > 6000:
            return ''.join([str(random.randint(0, 9)) for i in xrange(x)])
        else:
            return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)

a = str(rand_x_digit_num(6))

fromaddr = "trolltillyoudie@gmail.com"
toaddr = "clearemail2022@gmail.com"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "An attachment"
  
# string to store the body of the mail 
body = "The OTP is "+ a

  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "frame.jpg"
attachment = open(r'frame.jpg', "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "rasberryqwerty") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 