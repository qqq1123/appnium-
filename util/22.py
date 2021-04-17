import requests
import json
import urllib3

url = "https://regapi.mail.163.com/unireg/call.do?jsessionid=1605153146170&cmd=register.start"

data={
    "name": "test_rongtuo_045",
    "flow": "main_v2",
    "uid": "test_rongtuo_045@163.com",
    "password": "lrd123456",
    "confirmPassword": "lrd123456",
    "mobile": "13964035142",
    "from": "163mail",
    "startTime": "1605602821510"
    }


ww = requests.post(url=url,data=data).json()
print(ww)


#
# def add_01(a,b):
#     n=a+b
#     return n
#
#
# add_01(1,2)
#
