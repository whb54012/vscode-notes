import requests
# 导入模板
headers={'键':'值'}
# 添加请求头
cookies={'键':'值'}
# 添加cookie,也可直接写在headers里面
params={'键':'值'}
# 为get请求添加参数
data={'键':'值'}
# 为post请求添加请求体
requests.get('url',headers='请求头',timeout='超时时间')