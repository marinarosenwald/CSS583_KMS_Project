from llama_cpp import Llama
from dotenv import load_dotenv
import os

load_dotenv()

class LLM_Llama():
    def __init__(self) -> None:
        self.llm = Llama(model_path=os.getenv("MODEL_PATH"), n_ctx=int(os.getenv("LLAMA_N_CTX")), n_batch=int(os.getenv("LLAMA_N_BATCH")), verbose=os.getenv("LLAMA_N_VERBOSE"))
        self.instruction = ""
        self.system_prompt = ""
        self.instruction_prompt = ""
        
    def llm_call(self,input):
        # Step 1: Create a system and instruction prompt for the LLM to produce a definition for a term
        self.system_prompt = 'You are a term defining task that provides definitions for terms that are provided. Please ensure response is limited to a concise definition'
        self.instruction_prompt = 'Please generate a definition for the following term: '

        # Step 2: Apply the term sent to the LLM
        self.instruction_prompt += input

        # Step 3: Send prompt, which consists of the system and instruction prompt, to the LLM to retrieve a response from the LLM
        prompt= f"""<s>[INST] <<SYS>>{self.system_prompt}<</SYS>>\n{self.instruction_prompt} [/INST]"""

        # Step 4: Retrieve response, format, and send in a response dictionary object
        output = self.llm(input,temperature = 0.7, max_tokens=448,top_k=20, top_p=0.9, repeat_penalty=1.15) #Note, change prompt to input
        res = output['choices'][0]['text'].strip()

        '''
        # Step 5: Perform a clean up of the LLM response to retrieve ONLY definition
        res = res.split("\n",10)
        length = len(res)
        print(res[length-1])
        return res[length-1]
        '''
        print(res)
        return res
    
    def llm_keyword_extraction(self,input):
        # Step 1: Create a system and instruction prompt for the LLM to extract keywords from a definition
        self.system_prompt = 'You are a keyword extracting task that extracts keywords or key phrases from a provided body of text. Please ensure response is limited to a Python list format like this: [keyword, keyword, keyword, keyword]'
        self.instruction_prompt = 'Please extract the keywords from the following body of text: '
        
        # Step 2: Apply the definition sent to the LLM
        self.instruction_prompt += input
        
        # Step 3: Send prompt, which consists of the system and instruction prompt, to the LLM to retrieve a response from the LLM
        prompt= f"""<s>[INST] <<SYS>>{self.system_prompt}<</SYS>>\n{self.instruction_prompt} [/INST]"""
        
        # Step 4: Retrieve response, format, and send in a response dictionary object
        output = self.llm(prompt,temperature = 0.7, max_tokens=512,top_k=20, top_p=0.9, repeat_penalty=1.15)
        res = output['choices'][0]['text'].strip()
        '''
        # Step 5: Perform a clean up of the LLM response to retrieve ONLY keywords
        res = res.split("\n",10)
        length = len(res)
        print(res[length-1])
        return res[length-1]
        '''
        print(res)
        return res
    
    # Optional function
    def llm_keyword_extraction_keyllm(self,input):
        # Keyword extraction Option 2 - utilization of KeyLLM. This approach has not been tested with a local LLM, but has been tested with transformers from hugging face. When tested, can often run slower.
        from keybert import KeyLLM
        kw_model = KeyLLM(self.llm)
        keywords = kw_model.extract_keywords(input)

