from llama_cpp import Llama
from dotenv import load_dotenv
import os

load_dotenv()
# Step 1: Create a llama wrapper class for accessing the local LLM
#route = "C:/Users/mjh2g/Documents/GitHub/CSS583_KMS_Project/LLM-Server"
#llm = Llama(model_path= route + "/llm-models/llama-2-7b-chat.ggmlv3.q4_1.bin", n_ctx=512, n_batch=32, verbose=False)
llm = Llama(model_path=os.getenv("MODEL_PATH"), n_ctx=os.getenv("LLAMA_N_CTX"), n_batch=os.getenv("LLAMA_N_BATCH"), verbose=os.getenv("LLAMA_N_VERBOSE"))
print("Complete Step 1")
# Step 2: Import a LLM class to act as a response model for the API endpoints
from models import LLM

'''
from pydantic import BaseModel, Field
class LLM(BaseModel):
    llm_input: str = Field(...)
    print("Complete Step 2")
'''
# Step 3: Create the API routers for connecting with the local LLM to retrieve a definition and retrieve extracted keywords
from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder

llm_router = APIRouter()
print("Complete Step 3")
# Step 4: Create API end point for retrieving definition when a term is provided
@llm_router.post("/", response_description="Make an LLM call", status_code=status.HTTP_201_CREATED, response_model=LLM)
def llm_call(text: LLM = Body(...)):
    text = jsonable_encoder(text)
    # Step 4.1: Create a system and instruction prompt for the LLM to produce a definition for a term
    system_prompt = 'You are a term defining task that provides definitions for terms that are provided. Please ensure response is limited to a concise definition'
    instruction_prompt = 'Please generate a definition for the following term: '
    print("Complete Step 4.1")
    
    # Step 4.2: Apply the term sent to the LLM
    #instruction_prompt += text['llm_input']
    instruction_prompt += text['text']
    
    print("Complete Step 4.2")
    print(instruction_prompt)
    # Step 4.3: Send prompt, which consists of the system and instruction prompt, to the LLM to retrieve a response from the LLM
    prompt= f"""<s>[INST] <<SYS>>{system_prompt}<</SYS>>\n{instruction_prompt} [/INST]"""
    print("Complete Step 4.3")
    # Step 4.4: Retrieve response, format, and send in a response dictionary object
    output = llm(prompt,temperature = 0.7, max_tokens=512,top_k=20, top_p=0.9, repeat_penalty=1.15)
    res = output['choices'][0]['text'].strip()
    #response = {"llm_input" : res}
    response = {"text" : res}
    print(response)
    return response

# Step 5: Create API endpoint for extracting keywords when a definition is provided
@llm_router.post("/keywords", response_description="Keywords LLM call", status_code=status.HTTP_201_CREATED, response_model=LLM)
def llm_keyword_call(text: LLM = Body(...)):
    text = jsonable_encoder(text)
    # Step 5.1: Create a system and instruction prompt for the LLM to extract keywords from a definition
    system_prompt = 'You are a keyword extracting task that extracts keywords or key phrases from a provided body of text. Please ensure response is limited to a Python list format like this: [keyword, keyword, keyword, keyword]'
    instruction_prompt = 'Please extract the keywords from the following body of text: '
    print("Complete Step 5.1")
    # Step 5.2: Apply the definition sent to the LLM
    #instruction_prompt += text['llm_input']
    instruction_prompt += text['text']
    print("Complete Step 5.2")
    print(instruction_prompt)
    # Step 5.3: Send prompt, which consists of the system and instruction prompt, to the LLM to retrieve a response from the LLM
    prompt= f"""<s>[INST] <<SYS>>{system_prompt}<</SYS>>\n{instruction_prompt} [/INST]"""
    print("Complete Step 5.3")
    # Step 5.4: Retrieve response, format, and send in a response dictionary object
    output = llm(prompt,temperature = 0.7, max_tokens=512,top_k=20, top_p=0.9, repeat_penalty=1.15)
    res = output['choices'][0]['text'].strip()
    #response = {"llm_input" : res}
    response = {"text" : res}
    print(response)
    return response

'''
Keyword extraction Option 2 - utilization of KeyLLM. This approach has not been tested with a local LLM, but has been tested with transformers from hugging face. When tested, can often run slower.


from keybert import KeyLLM
kw_model = KeyLLM(llm)
keywords = kw_model.extract_keywords(body_of_text)
'''