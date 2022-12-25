from fastapi import FastAPI
from routes.index import user
# uvicorn main:app --reload

app = FastAPI()

app.include_router(user)