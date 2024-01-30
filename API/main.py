from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from pymongo import MongoClient
from contextlib import asynccontextmanager
from routes import router as dict_router
import os

load_dotenv() # dont move to lifespan function

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Will execute on startup
    print("Executing Startup Code")
    app.mongodb_client = MongoClient(os.getenv("ATLAS_URI"))
    app.database = app.mongodb_client[os.getenv("DB_NAME")]
    yield
    print("Executing Shutdown Code")
    # after yield -> will be executed on shutdown
    app.mongodb_client.close()

app = FastAPI(lifespan=lifespan)

app.include_router(dict_router,
                   tags=[os.getenv("DB_DEFINITION_TAG")],
                   prefix=os.getenv("DB_DEFINITION_PREFIX"))

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")), log_level="info")
