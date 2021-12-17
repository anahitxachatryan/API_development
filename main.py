from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello"}

@app.get("/posts")
def get_posts():
    return {"message":"Posts are located here!"}

