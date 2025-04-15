from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello! This is /home/vir/projects/d2r-charactersheet/d2r-charactersheet/src/main.py!"}

