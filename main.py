from fastapi import FastAPI
from routers import user

app = FastAPI()

app.include_router(user.router)


@app.get("/")
async def read_root():
    return {"message": "Hello, User Management World!"}
