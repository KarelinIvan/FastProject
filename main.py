from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from middleware import LogMiddleware
from routers import user, auth

app = FastAPI()

# Middleware для логирования запросов
app.add_middleware(LogMiddleware)

# Middleware для обработки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)


@app.get("/")
async def read_root():
    return {"message": "Hello, User Management World!"}
