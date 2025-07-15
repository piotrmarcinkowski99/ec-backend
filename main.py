from fastapi import FastAPI
from app.api import auth, tasks
from fastapi.middleware.cors import CORSMiddleware

from app.middlewares.auth_middleware import AuthorizeRequestMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(AuthorizeRequestMiddleware)

app.include_router(auth.router, prefix="/auth", tags=["Atuhorization"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])