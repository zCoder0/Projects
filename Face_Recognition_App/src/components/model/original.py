import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity 
import cv2
from mtcnn import MTCNN
from src.exception.ExceptionBase import ProjectException
import sys
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
from keras_facenet import FaceNet
import pandas as pd

class FaceRecognize:
    
    def __init__(self):
        try:
            #create objects
            self.facenet = FaceNet()
            self.detector = MTCNN()
            self.known_faces={}
            print("finished")
        except Exception as e:
            ProjectException(e,sys)
    
    def face_detect(self, image ,name="Face1"):
        try:
            img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            faces = self.detector.detect_faces(img_rgb)

            if faces:  # Check if any face is detected
                for face in faces:
                    if 'box' in face and face['box']:
                        x, y, w, h = face['box']

                        # Draw rectangle
                        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)

                        # Crop and resize
                        face_crop = img_rgb[y:y + h, x:x + w]
                        crop = cv2.resize(face_crop, (160, 160))

                      
                        #cv2.imshow(name, image)
                        self.name = name

                        return crop  # Return only one cropped face for now

            else:
                print("No face detected.")
                
        except Exception as e:
            print(f"Error: {e}")

    
    def face_embedding(self,crop_image):
        try:
            face_emb = self.facenet.embeddings([crop_image])[0]
            self.known_faces[self.name] = face_emb
            return face_emb
        except Exception as e:
            ProjectException(e,sys)
        
    def save_datas(self):
        try:
            np.save(f"src/components/dataset/{self.name}.npy", self.known_faces[self.name], allow_pickle=True)
        except Exception as e:
            ProjectException(e,sys)
            
    def load_knowfaces(self):
        try:
            known_face={}
            path = "src/components/dataset"
            file_list = os.listdir(path)
            for file in file_list:
                file_path = path+'/'+file
                print(file_path)
                loaded_data = np.load(file_path,allow_pickle=True)
                known_face[file.replace(".npy","")] = loaded_data
            return known_face
        
        except Exception as e:
            ProjectException(e,sys)
            

    def recognize_face(self,test_embedding, known_faces , threshold=0.6):
        try:
            best_score = -1
            identity = "Unknown"
            for name, saved_embedding in known_faces.items():
                score = cosine_similarity([test_embedding], [saved_embedding])[0][0]
                print(score)
                if score > best_score and score > threshold:
                    best_score = score
                    identity = name
            return identity
        except Exception as e:
            ProjectException(e,sys)
            
    def live_face_recognition(self):
        
        try:
            video = cv2.VideoCapture(0)

            while True:
                name=""
                ret, frame = video.read()
                crop = self.face_detect(frame)
                if crop is not None:
                    emb = self.face_embedding(crop)

                    known_faces_dict= self.load_knowfaces()
                    test_embedding = emb
                    name = self.recognize_face(test_embedding,known_faces_dict)
                    cv2.putText(frame, name, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

                
                cv2.imshow("Live Face Recognition", frame)
                    
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            video.release()
            cv2.destroyAllWindows()
        except Exception as e:
            ProjectException(e,sys)
