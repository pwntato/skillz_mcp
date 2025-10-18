from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/skillz")
def read_skillz():
    if os.path.exists("/skillz"):
        return {"skillz_contents": os.listdir("/skillz")}
    else:
        return {"error": "skillz directory not found"}
