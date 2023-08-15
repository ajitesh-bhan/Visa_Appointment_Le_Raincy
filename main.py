from automation import autmated_visa_appointment
from playsound import playsound
import time

music_file = './security-protocols.wav'
base_img =  './reference_img.png'
while True: #Infinite loop
    obj = autmated_visa_appointment(base_img)
    rslt= obj.main()
    count=0
    if rslt == False:
        while count!=10:
            playsound('./security-protocols.wav')
            count+=1
    time.sleep(600)

