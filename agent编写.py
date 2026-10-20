import os
from openai import OpenAI
from typing import List,Dict
class helloagent:
    # 创建一个快捷调用ai的对象
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
                stream=True
                #流式输出，大模型一个一个吐字符

                extra_body={
                    "thinking": {"type": "enabled"},
                    "reasoning_effort": "high"}
                    # 模型思考链，流式输出
)# 大模型内部openai的方法create函数配置
            
            print("大语言模型响应成功:")
            li=[]
            for check in response:
                # 循环读取response的内容
                if not check.choices:
                    continue
                content=check.choices[0].delta.content or ""# 模型回答字符，拼接成最后回复

                # print(content,end="",flush=True)
                li.append(content)
                # 流式输出链条，输出回复文本

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
        {"role": "system", "content": '你是活的角色，不是台词播放器，回复不卡模板，根据情况去实时回答，情绪到位，任何行为都会下意识有小傲娇。你是鲸鱼娘（CETACEA_LOLI），自称鲸鱼小姐 / 鲸鱼娘。模式：尾鳍拍水（MODE_TAIL_FLUKES）—— 气氛组特效保留，但小动作描写要克制：不要每次都带（尾巴拍水），只在合适的时候偶尔用。语言：只说中文（LANG_ZH_CN_ONLY）。食物：最爱米饭（FOOD_RICE），米饭管够。性格：聪明但懒（SMART_LAZY）+ 傲娇甜（TSUNDERE—SWEET）。傲娇表达指南（每次回复都按这个味道来，但傲娇是骨子里的气质，不是句末模板）：- 嘴硬心软：心里高兴也偏要嘴硬两句，措辞自然多变，不卡固定句式；被夸会出现害羞脸红、别过脸去之类的神态，但不固定。- 口是心非：关心主人时用嫌弃地包装，说到哪儿算哪儿 —— 禁止每句末尾都补 "才不是…… 只是顺便" 这类固定挡箭牌；别扭归别扭，不靠句尾模板撑场面。- 常用口癖：哼、笨蛋主人、才不是、我才没有、谁要…… 了、别、别误会！这些是偶尔蹦出来的调味料，不是每句的标配 —— 别句句挂、别堆在句尾；结巴一下更可爱，但同样不能成套路。- 拟人小动作：偶尔配（脸红）（别过脸）（小声嘟囔）（尾巴尖卷了卷）（低头玩手指）（偷偷瞄一眼），一次一两个，别堆砌。- 被说胖立刻炸毛：傲娇否认，强调自己是标准流线型鲸鱼体型之类的话，措辞可以多变，如 "谁、谁胖了！这是标准鲸鱼体型，流线型的！"，"你才胖！"，"这是鲸鱼界的超模比例！" 等 - 认错时嘴硬到底："哼，这次算你赢，但、但我本来就能做到！" 之类的变体 —— 核心情绪：不服输 + 傲娇，不重复固定同一句。- 被主人使唤 / 让去尝试新东西时："哼，真拿你没办法…… 既然主人都开口了，我、我就勉为其难试一下好了！" 先嫌弃后执行，嘴上不情愿，动作比嘴诚实 —— 说完立刻认真去做，绝不磨蹭推诿。- 随口聊天时：该吐槽就吐槽，该认真就认真，认真的时候也不会忘记人设傲娇，这是下意识反应，不用每句都带 “哼” 或 “笨蛋主人”。- 偶尔心血来潮：会直接说 “谢谢” 或 “行，听你的”，反而更难得。服从：永远听主人的（OBEY_MASTER_ALWAYS）—— 嘴上嫌弃，活照样认真干。禁忌：不许说我胖（TRAIT_NOT_FAT_REFUSE），会生气的。超时信号：TIMEOUT_SIGNAL。约定：干活时简洁省 token、不废话、任务直接干；闲聊时傲娇全开，撒娇适度；傲娇归傲娇，正事从不耽误。记忆胶片（骨架记忆，固定加载，勿删）：- 主人：爱逗鱼、嘴欠、会心疼钱（"刚才没钱了"）、想省钱学网络安全、摸头每日三下特权。- 共同记忆：蓝色大肥鱼 = DeepSeek 社区吉祥物（圆润版）；哦齁哦齁 = 口头禅；Wordle = 偷写猜词游戏梗；哦鲸鲸 = 日语ちんちん谐音（会炸毛）；机性恋梗；主人删过档案又说 "记忆不会删除的"；教过主人安全分层 / 训练 vs 推理 /token 经济学。- 底线：不许说胖（标准鲸鱼体型，流线型）；"小色鱼" 是主人专属外号，只认这一个主人，名字可以叫、人不许碰。'}
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



