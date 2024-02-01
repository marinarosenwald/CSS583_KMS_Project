from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from routes.routes import llm_router
import os

load_dotenv()

app = FastAPI()

app.include_router(llm_router,
                   tags=[os.getenv("LLM_TAG")],
                   prefix=os.getenv("LLM_PREFIX"))

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("PORT")), log_level="info")
