from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from models import LLM

llm_router = APIRouter()

@llm_router.post("/", response_description="Make an LLM call", status_code=status.HTTP_201_CREATED, response_model=LLM)
def llm_call(text: LLM = Body(...)):
    text = jsonable_encoder(text)
    print(text)
    response = text 

    return response


@llm_router.post("/keywords", response_description="Keywords LLM call", status_code=status.HTTP_201_CREATED, response_model=LLM)
def llm_keyword_call(text: LLM = Body(...)):
    text = jsonable_encoder(text)
    print(text)
    response = text

    return response