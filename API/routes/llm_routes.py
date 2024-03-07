from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
import os
import httpx
from models import LLM

llm_router = APIRouter()

@llm_router.post("/", response_description="Make an LLM call", status_code=status.HTTP_201_CREATED, response_model=LLM)
def llm_call(text: LLM = Body(...)):
    text = jsonable_encoder(text)
    response = httpx.post('http://' + os.getenv("LLM_SERVER_URL") + 'llm-server/',
                          json=text,
                          headers={"Content-Type": "application/json"})
    return response.json()


@llm_router.post("/keywords", response_description="Keywords LLM call", status_code=status.HTTP_201_CREATED, response_model=LLM)
def llm_keyword_call(text: LLM = Body(...)):
    text = jsonable_encoder(text)
    response = httpx.post('http://' + os.getenv("LLM_SERVER_URL") + 'llm-server/keywords',
                          json=text,
                          headers={"Content-Type": "application/json"})
    return response.json()