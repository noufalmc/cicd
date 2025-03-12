import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()




@app.get("/cicd/v1/getHealth")
def getHealthCheck()->str:
    return '{"Health":"OK"}'



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)