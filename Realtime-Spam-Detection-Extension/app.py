import requests 
import uvicorn
from fastapi import FastAPI,Query
from fastapi.responses import JSONResponse ,FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.components.data_integstion import ScrapedData

    
app = FastAPI()

class URLRequest(BaseModel):
    url: str
    


@app.post("/check_spam")
def serve_ui(request:URLRequest):
    url = request.url
    
    data=ScrapedData()
    result = data.check_url_for_spam(url)
    print(result)
    return {"label": result}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)