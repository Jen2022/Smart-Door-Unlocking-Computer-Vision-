import face_recognition
import cv2
import numpy as np
# from pyfirmata import *
# board = Arduino('COM3')
# board.servo_config(9, min_pulse=544, max_pulse=2400, angle=90)


import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import random

j=0
video_capture = cv2.VideoCapture(0)

jennifer_image = face_recognition.load_image_file("frame2.jpg")
jennifer_face_encoding = face_recognition.face_encodings(jennifer_image)[0]
jennifern_image = face_recognition.load_image_file("nospecs.jpg")
jennifern_face_encoding = face_recognition.face_encodings(jennifern_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    jennifer_face_encoding,
    jennifern_face_encoding
]
known_face_names = [
    "Jennifer",
    "Jennifer"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    cv2.imwrite("frame.jpg",frame)   


    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # BGR to RGB
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        name = "Unknown"

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)

            #  use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        j=1
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
 
   
    if j == 1:
        if (cv2.waitKey(1))or 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()

if (name!="Unknown"):
    b="Unlocked"
else:
    def rand_x_digit_num(x, leading_zeroes=True):
        if not leading_zeroes:
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
      
    msg['From'] = fromaddr 
      
    msg['To'] = toaddr 
      
    # storing the subject  
    msg['Subject'] = "Visitor at Your Door"
      
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
      
    s.sendmail(fromaddr, toaddr, text) 
      
    s.quit() 
    b="locked"
    print(a)
print(b)