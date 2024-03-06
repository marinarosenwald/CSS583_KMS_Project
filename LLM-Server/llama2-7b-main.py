from llama_cpp import Llama
llm = Llama(model_path="C:/Users/mjh2g/Documents/GitHub/CSS583_KMS_Project/LLM-Server/llm-models/llama-2-7b-chat.ggmlv3.q4_1.bin",
            n_ctx=512, n_batch=32, verbose=False)
instruction = input("User: ")
print(instruction)
system = 'you are ai system'
print(system)
prompt = f"[INST] <<SYS>><</SYS>>\n{instruction} [/INST]"
print(prompt)
output = llm(prompt,temperature = 0.7, max_tokens=512,top_k=20, top_p=0.9, repeat_penalty=1.15)
print(output)
res = output['choices'][0]['text'].strip()
print('Llama2: ' + res)