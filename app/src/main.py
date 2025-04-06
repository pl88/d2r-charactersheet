from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, EmailStr


import hashlib
import random


def generate_token(user):
    random.seed(user)
    token = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()[:32]
    return token





class SignUpRequest(BaseModel):
    email: EmailStr
    password: str


class SignUpResponse(BaseModel):
    token: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/users/", response_model=SignUpResponse)
async def cerate_user(user: SignUpRequest):
    print(f"Creating user {user.email}, password {user.password}")
    token = generate_token(user.email)
    print(f"Generated token {token}")
    return SignUpResponse(token=token)


if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)

