class tool:
    # 一个工具执行器，负责管理和执行工具。
    def __init__(self):
        self.tools={};
# 创建一个工具字典
    def register(self,name:str,note:str,func:str):
        if name not in self.tools:
            self.tools[name]={"note":note,"note":func}
            print(f"工具 '{name}' 已注册。")
        

