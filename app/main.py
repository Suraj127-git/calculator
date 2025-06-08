from fastapi import FastAPI
from app.routers import calculator

app = FastAPI()
app.include_router(calculator.router)
