from llama_cpp import Llama
from dotenv import load_dotenv
import os

load_dotenv()

class LLM_Llama():
    _self = None

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self):
        self.llm = Llama(model_path=os.getenv("MODEL_PATH"), n_ctx=int(os.getenv("LLAMA_N_CTX")), n_batch=int(os.getenv("LLAMA_N_BATCH")), verbose=os.getenv("LLAMA_N_VERBOSE"))
        self.instruction_prompt = ""
        
    def llm_call(self,input):
        # Step 1: Retrieve response, format, and send in a response dictionary object
        print("starting LLM call")
        output = self.llm(input,temperature = 0.7, max_tokens=448,top_k=20, top_p=0.9, repeat_penalty=1.15) #Note, change prompt to input
        print("finished LLM call")
        res = output['choices'][0]['text'].strip()

        return res
    
    def llm_keyword_extraction(self,input):
        print("starting LLM Keywords call")
        # Step 1: Create a system and instruction prompt for the LLM to extract keywords from a definition
        self.instruction_prompt = 'Please extract the keywords from the following body of text: '
        
        # Step 2: Apply the definition sent to the LLM
        self.instruction_prompt += input        
        
        # Step 3: Retrieve response, format, and send in a response dictionary object
        output = self.llm(self.instruction_prompt,temperature = 0.7, max_tokens=512,top_k=20, top_p=0.9, repeat_penalty=1.15)
        print("finished LLM call")
        res = output['choices'][0]['text'].strip()
        

        return res
    
    def llm_keyword_definition(self,input):
        print("starting LLM Definition call")
        # Step 1: Create a system and instruction prompt for the LLM to extract keywords from a definition
        self.instruction_prompt = 'Please define '
        
        # Step 2: Apply the definition sent to the LLM
        self.instruction_prompt += input        
        
        # Step 3: Retrieve response, format, and send in a response dictionary object
        output = self.llm(self.instruction_prompt,temperature = 0.7, max_tokens=512,top_k=20, top_p=0.9, repeat_penalty=1.15)
        print("finished LLM call")
        res = output['choices'][0]['text'].strip()
        

        return res
    '''
    # Optional function
    def llm_keyword_extraction_keyllm(self,input):
        # Keyword extraction Option 2 - utilization of KeyLLM. This approach has not been tested with a local LLM, but has been tested with transformers from hugging face. When tested, can often run slower.
        from keybert import KeyLLM
        kw_model = KeyLLM(self.llm)
        keywords = kw_model.extract_keywords(input)
    '''
