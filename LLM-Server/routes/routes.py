# Step 1: Create a llama wrapper class for accessing the local LLM
from llama2_7b_main import LLM_Llama
llm = LLM_Llama()

# Step 2: Import a LLM class to act as a receiving and response model for the API endpoints
from models import LLM

# Step 3: Create the API routers for connecting with the local LLM to retrieve a definition and retrieve extracted keywords
from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder

llm_router = APIRouter()

# Step 4: Create API end point for retrieving definition when a term is provided
@llm_router.post("/", response_description="Make an LLM call", status_code=status.HTTP_201_CREATED, response_model=LLM)
def llm_call(text: LLM = Body(...)):
    
    # Step 4.1: Extract the text from the user to send into the llama LLM
    text = jsonable_encoder(text)
    res = llm.llm_call(text['text'])

    # Step 4.2: Send definition back to user
    response = {"text" : res}
    print(response)
    return response

# Step 5: Create API endpoint for extracting keywords when a definition is provided
@llm_router.post("/keywords", response_description="Keywords LLM call", status_code=status.HTTP_201_CREATED, response_model=LLM)
def llm_keyword_call(text: LLM = Body(...)):

    # Step 5.1: Extract the text from the user to send into the llama LLM
    text = jsonable_encoder(text)
    res = llm.llm_keyword_extraction(text['text'])

    # Step 5.2: Send keywords back to user
    response = {"text" : res}
    print(response)
    return response