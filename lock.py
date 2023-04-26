import serial
import time
import cv2
import cvzone
import requests
import pyttsx3
count=0
from cvzone.HandTrackingModule import HandDetector
serialcomm = serial.Serial('COM6', 9600)
serialcomm.timeout = 1
cap=cv2.VideoCapture(0) 
detector = HandDetector(detectionCon=1, maxHands=1)
while True:
    engine = pyttsx3.init()
    success,img =cap.read()
    img=cv2.resize(img,(500, 350))
    img=detector.findHands(img)
    l,box = detector.findPosition(img,draw=False)
    if l:
        f=detector.fingersUp()        
        s=(list(map(int,f)))
        w=0
        e='\n'
        for q in s:
            w +=q      
        serialcomm.write(e.encode())
        serialcomm.write(str(w).encode()) 
        print(str(w))   
        time.sleep(1)
        if(str(w))=="3":
           print("door open")
           count=count+1
           if count==2:
            engine.say("PIN MATCH successfully door open")
            engine.runAndWait()
            print("door open")
            count=0
           #ifttt_webhook_url = 'https://maker.ifttt.com/trigger/door/json/with/key/cjNbfQUucocxxj9DoAjUbi'
           #requests.post(ifttt_webhook_url)
  
    cv2.imshow('Image',img)  
    if cv2.waitKey(20) & 0xFF == 27:
        break                
cv2.destroyAllWindows()
