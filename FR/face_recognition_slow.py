import face_recognition
import cv2
import numpy as np

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import random

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.
# print("10")
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
# print("10")
# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# # # # Load a second sample picture and learn how to recognize it.
# jennifer_image = face_recognition.load_image_file("frame2.jpg")
# jennifer_face_encoding = face_recognition.face_encodings(jennifer_image)[0]

# hannah_image = face_recognition.load_image_file("frame.jpg")
# hannah_face_encoding = face_recognition.face_encodings(hannah_image)[0]


# george_image = face_recognition.load_image_file("George2.jpg")
# george_face_encoding = face_recognition.face_encodings(george_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    # jennifer_face_encoding,
    # hannah_face_encoding,

    # george_face_encoding
    
    # biden_face_encoding
]
known_face_names = [
    "Barack Obama",
    # "Jennifer",
     # "George"
     # "Hannah"
]
#print("10")


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    cv2.imwrite("frame.jpg",frame)   

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"



        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]


        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)




    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()


if (name!="Unknown"):
    print("Unlocked")
else:

    def rand_x_digit_num(x, leading_zeroes=True):
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

    print("locked")
