from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pymongo import MongoClient
from contextlib import asynccontextmanager
from routes.dict_routes import dict_router
from routes.llm_routes import llm_router
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dict_router,
                   tags=[os.getenv("DEFINITION_TAG")],
                   prefix=os.getenv("DEFINITION_PREFIX"))
app.include_router(llm_router,
                   tags=[os.getenv("LLM_TAG")],
                   prefix=os.getenv("LLM_PREFIX"))

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")), log_level="info")
