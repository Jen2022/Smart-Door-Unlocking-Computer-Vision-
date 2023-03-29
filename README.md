# Smart-Door-Unlocking-Computer-Vision-

In this system, security that combines the functions of smart phone and home network system. It enables the users to monitor visitors in real-time, remotely via the IoT-based doorbell installed near the entrance door to a house. This system makes security as further autonomous by capturing the image automatically and processing the image for facial matching and uses mail communication to the server to confirm the intruder is known or unknown. And also make them as a known person by entering the OTP which is sent to the mail server.

Security has always been an important issue in the home or office. A remote home security system offers many more benefits apart from keeping home owners, and their property, safe from intruders. The system is composed of the Doorbell interfaced with Arduino, when the doorbell is pressed, the camera gets triggered and captures their image and searches for their face with its database which already has registered faces.If it is an authorized person the door will open, otherwise it sends an OTP with the image of the intruder to server mail. Only when the non authorized person enters that OTP, He gets access.

In this proposed system, we are having database of authorized person list by registering their faces by entering OTP, so that non authorized person can’t able to enter the home until they entering the OTP. Whenever some person pressing calling bell switch, the camera gets triggered and capture the image of the intruder and checks that the image to the database, if that face is not matching with the database, it sends an email containing that intruder image and OTP, when intruder type the OTP by the owners' knowledge then it allows to enter. 


