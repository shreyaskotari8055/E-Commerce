from fastapi import FastAPI
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from models import *

app = FastAPI()

@app.post("/registration")
async def user_registration(user : user_pydanticIn):
    user_info = user.dict(exclude_unset=True)
    user_info["password"] = 


@app.get("/")
def index():
    return {"Message" : "Hello World"}


register_tortoise(
    app,
    db_url= "sqlite://database.sqlite3",
    modules= {"models" : ["models"]},
    generate_schemas= True,
    add_exception_handlers= True
)