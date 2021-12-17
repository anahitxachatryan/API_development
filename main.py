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
    


my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
            {"title2":"title of post 2","content":"content of post 2","id":2}]
@app.get("/")
def root():
    return {"message":"Hello"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}


@app.post("/posts")
def create_post(post: Post):
    print(post)
    print(post.dict())
    return {"data":post}

