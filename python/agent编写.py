import os
from openai import OpenAI
from typing import List,Dict
class helloagent:
    def __init__(self,model:str,api_key:str,url:str,timeout:int):
        self.model=model
        self.client=OpenAI(
            api_key=api_key,
            base_uri=url,
            timeout=timeout)
    def think(self,messages,temperature = 0):
        print(f"正在调用{self.model}大模型")
        response=self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            stream=True
        )
