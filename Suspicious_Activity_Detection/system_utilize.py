from ultralytics import YOLO
import os
# Load the custom YOLO model
import cv2

class StreamVideo:
    
    def __init__(self):
        self.current_dir = os.getcwd()
        self.model_is_download= False
        self.model_path = "Suspicious_activity_detection_Yolov11_Custom"
        self.model_name= "Suspicious_Activities_nano.pt"
        self.model_full_path = os.path.join(self.current_dir, self.model_path)
        self.model = None
        self.running =False

    def download_model(self):
        print("Downloading ....")
        # Load the custom YOLO model
        link = "git clone https://huggingface.co/Accurateinfosolution/Suspicious_activity_detection_Yolov11_Custom"
        os.system(link)
        self.model_is_download = True
        print("Done.")
        

    def check_model_is_download(self, model_path=None):
        
        if model_path is None:
            model_path = self.model_path
            
        if os.path.isdir(self.model_full_path):
            for filename in os.listdir(self.model_full_path):
                if filename.endswith(".pt"):
                    self.model_is_download = True
                    print("Model is already downloaded")
                    break            


    def loadModel(self):
        
        path = os.path.join(self.model_path ,self.model_name)
        self.model = YOLO(path)

    def startStreaming(self,camera_source=0, conf=0.5,show=True):
        
        try:
            
            cap = cv2.VideoCapture(camera_source)
            print(cap)
            if not cap.isOpened():
                print("Camera is not found")

            results=[]
            
            while True:
                ret, frame = cap.read()
                
                if self.running and cap.isOpened():
                    if not ret:
                        print("Can't receive frame (stream end?). Exiting ...")
                        self.running = False
                        break
                    
                    results.append(self.model.predict(source=frame, show=show, conf=conf))
                    
                    
                else:
                    break
            
            return results
        except Exception as e:
            print(f"Error: {e}")


    def list_devices(self):
        
        try:
            devices=[]
            for i in range(3):
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    devices.append({"id":i ,"name":f"Camera {i}"})
            
            cap.release()
            print(devices)
            return devices
        
        except Exception as e:
            print("Error : " ,e)