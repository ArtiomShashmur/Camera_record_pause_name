import cv2
import os 

class CameraRec:

    def __init__ (self):
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            print ('Error opened')
            return
        self.firstName = "test.mp4"
        self.recording = False
        self.fps = 30.0
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        self.Run()

        self.camera.release()
        cv2.destroyAllWindows()

    def Run(self):
        while True:
            ret, frame = self.camera.read()

            if not ret:
                print ('Error ret')
                break

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break
            elif key == ord(' '):
                self.RecordingCamera(frame)

            if self.recording:
                self.RedCircle(frame)
                self.record.write(frame)


            cv2.imshow('Result', frame)

    def RecordingCamera(self, frame):
        
        if not self.recording:
            self.record = cv2.VideoWriter(self.firstName, self.fourcc,self.fps, (frame.shape[1], frame.shape[0]))
            self.recording = True
        else:
            self.recording = False
            self.record.release()
            self.newName = input("New Name: ")
            if not self.newName:
                self.newName = self.firstName
            self.newNameFile = self.newName + '.mp4'
            os.rename(self.firstName, self.newNameFile)

    def RedCircle (self, frame):
        cv2.circle(frame, (10,10),5,(0,0,255),thickness=-1)

CameraRec()
