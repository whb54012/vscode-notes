import requests#激活模板
for i in range(1,256):
    ip = f"?c={i}"
    url = f"http://localhost:3000/%E7%BD%91%E9%A1%B5/%E4%B8%BB%E9%A1%B5/%E9%9F%B3%E4%B9%90.php{ip}"
    try:
        requests.get(url,timeout=2)#设置检测参数和超时时间
        print(url)
    except:
        pass