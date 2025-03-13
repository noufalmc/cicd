import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/cicd/v1/getHealth")
def getHealthCheck() -> str:
    # Checking the health status for confirming
    return '{"Health":"OK"}'

@app.get("/cicd/v1/say_hello")
def say_hello() -> str:
    # Checking the health status for confirming
    return '{"message":"Say Hello"}'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
