import uvicorn
from fastapi import FastAPI,Query
from fastapi.responses import JSONResponse ,FileResponse
from fastapi.staticfiles import StaticFiles
from system_utilize import StreamVideo
import threading
from fastapi import File, UploadFile
import shutil
import os


app = FastAPI()

streaming = StreamVideo()

app.mount("/static",StaticFiles(directory='static'),name='static')

stream_thread= None



streaming.check_model_is_download()
if not streaming.model_is_download:
    streaming.download_model()
    
streaming.loadModel()



@app.get("/")
def read_root():
    
    return FileResponse("static/index.html")
    

@app.get("/devices")
def list_devices():
    return streaming.list_devices()

@app.get("/start")
def start_streaming(source_id :str=  Query("0")):
    
    global stream_thread
    print("hi")
    
    if streaming.running:
        return {"messgae" : "Streaming is already running"}
    
    streaming.running = True
    stream_thread = threading.Thread(target=streaming.startStreaming ,args=(int(source_id),))
    stream_thread .start()
    
    return {"message" : "Streaming started"}

@app.get("/stop")
def stop_streaming():
    
    if not streaming.running:
        return {"message" : "Streaming is not running"}
    
    streaming.running = False

    return {"message" : "Streaming stopped"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    file_location = f"{upload_folder}/{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    streaming.running =True
    image = streaming.startStreaming(file_location,show=False)
    print(image)
    print(type(image))
    return {"message": f"File '{file.filename}' uploaded successfully"}



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9090)