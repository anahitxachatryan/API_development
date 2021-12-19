from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.param_functions import Body
from pydantic import BaseModel
from random import randrange

from starlette.status import HTTP_204_NO_CONTENT

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    public:bool = True
    voting:Optional[int] = None
    


my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
            {"title2":"title of post 2","content":"content of post 2","id":2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_post_by_index(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {"message":"Hello"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.get("/post/{id}")
def get_post(id: int):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} was not found")
    return {"post_detail":post}

@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):

    index = find_post_by_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exsist")
    my_posts.pop(index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/post/{id}")
def update_post(id: int, post: Post):
    post_dict = post.dict()
    index = find_post_by_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exsist")
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data":post_dict}