"""from ultralytics import YOLO
import cv2

# Load the custom YOLO model
model = YOLO("Suspicious_Activities_nano.pt")

# Open webcam
cap = cv2.VideoCapture(0)
frame_limit = 100  # number of frames to run
count = 0

while count < frame_limit:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, show=True, conf=0.6)
    count += 1

cap.release()
cv2.destroyAllWindows()
"""

from system_utilize import StreamVideo


streaming = StreamVideo()


streaming.check_model_is_download()
if not streaming.model_is_download:
    streaming.download_model()
    
streaming.loadModel()
streaming.running =True
print(streaming.model)
streaming.startStreaming(0)
