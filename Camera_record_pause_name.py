import cv2
import os 


camera = cv2.VideoCapture(0)


if not camera.isOpened():
        print ("Erroropened")


recording = False
key_q = ord ('q')
key_space = ord(' ')
second_name = 'test.mp4'

while True:
    ret , frame = camera.read()
    key = cv2.waitKey(1)& 0xFF

    if not ret:
        print("Error ret")
        break

    if key == key_q:
        break
    elif key == key_space:

        if not recording:
            record = cv2.VideoWriter(second_name, cv2.VideoWriter_fourcc(*'mp4v'),30.0,(frame.shape[1],frame.shape[0]))
            recording = True        
        else:
            recording = False
            record.release()
            new_name = input("New name record: ")
            if not new_name:
                 new_name = "Noname"
            new_fileName = new_name + '.mp4'

            os.rename(second_name, new_fileName)

                 
    if recording:
         cv2.circle(frame, (10,10),5,(0,0,255),thickness=-1)
         record.write(frame)
    
    cv2.imshow('Frame', frame)


camera.release()
cv2.destroyAllWindows()
