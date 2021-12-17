from typing import Optional
from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    public:bool = True
    voting:Optional[int] = None
    



@app.get("/")
def root():
    return {"message":"Hello"}

@app.get("/posts")
def get_posts():
    return {"message":"Posts are located here!"}


@app.post("/createposts")
def create_post(post: Post):
    print(post.title)
    return {"data":post}

