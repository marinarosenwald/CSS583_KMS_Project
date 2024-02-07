from llama_cpp import Llama
llm = Llama(model_path="./llm-models/llama-2-7b-chat.ggmlv3.q4_1.bin",
            n_ctx=512, n_batch=32, verbose=False)
instruction = input("User: ")

system = 'you are ai system'
prompt = f"[INST] <<SYS>><</SYS>>\n{instruction} [/INST]"
output = llm(prompt,temperature = 0.7, max_tokens=512,top_k=20, top_p=0.9, repeat_penalty=1.15)
res = output['choices'][0]['text'].strip()
print('Llama2: ' + res)