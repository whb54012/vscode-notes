import requests
# 导入模板
headers={'键':'值'}
# 添加请求头
cookies={'键':'值'}
# 添加cookie,也可直接写在headers里面
params={'键':'值'}
params="键=值"
# 为url后面添加参数
data={'键':'值'}
data="键=值"
# 为post请求添加请求体
t=requests.get('url',headers=headers,cookies=cookies,params=params,timeout='超时时间')
# get请求
t=requests.post('url',headers=headers,data=data,cookies=cookies,params=params)
# post请求

