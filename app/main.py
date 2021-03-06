from typing import Optional
from typing import List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.param_functions import Body
from passlib.utils.decor import deprecated_function
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from . import models,utils,schemas
from . routers import post,user

 # to use autogenerated documentation use url: /doc or /redoc


models.Base.metadata.create_all(bind=engine)


app = FastAPI()



while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'API_development', user = 'postgres', password = 'qwerty111', 
        cursor_factory = RealDictCursor)
        cursor  = conn.cursor()
        print("database connection was successfull")
        break
    except Exception as error:
        print("connecting the database failed")
        print(error)
        time.sleep(3)



app.include_router(post.router)
app.include_router(user.router)
@app.get("/")
def root():
    return {"message":"Hello"}


