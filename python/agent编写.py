import os
from openai import OpenAI
from typing import List,Dict
class helloagent:
    def __init__(self,model:str,api_key:str,url:str,timeout:int):
        self.model=model
        self.client=OpenAI(
            api_key=api_key,#密钥
            base_url=url,#api接口
            timeout=timeout)#超时时间
        # 大模型属性配置，创建openai对象
    def think(self,messages,temperature = 0):
        try:
            print(f"正在调用{self.model}大模型")
            response=self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True)#流式输出，大模型一个一个吐字符
            print("大语言模型响应成功:")
            # 大模型内部openai的方法create函数配置
            li=[]
            for check in response:
                # 循环读取response的内容
                if not check.choices:
                    continue
                content=check.choices[0].delta.content or ""
                li.append(content)
            return "".join(li)
        except Exception as e:
            print(f"调用LLM API时发生错误: {e}")
            return 0;
if __name__=='__main__':
    agent=helloagent(
        model="deepseek-chat",
        api_key="sk-f358a7dd29764a978d9f4da9d29eaf2c",
        url="https://api.deepseek.com/v1",
        timeout=60
    )
contents=""
# while(1>0):
#     content=input("请输入问题")
#     Messages = [
#         {"role": "system", "content": "你是擅长写Python代码的编程助手,回答简洁清晰"},
#         {"role": "user", "content": f"{content}"+','+f"{contents}"}
#     ]
#     reponse=agent.think(Messages)
#     contents=contents+","+content+","+reponse#上下文拼接
#     print(reponse)
#直接上下文拼接，大模型无法区分哪句话是谁说的
Messages = [
        {"role": "system", "content": "你是擅长写Python代码的编程助手,回答简洁清晰"}
    ]
while(1>0):
    content=input("请输入问题")
    if content=="exit":
        break
    Messages.append(
        {"role": "user", "content": f"{content}"}
    )
    reponse=agent.think(Messages)
    Messages.append(
        {"role": "assistant", "content": f"{reponse}"}
    )
    print(reponse)
print(Messages)



