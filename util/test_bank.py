import requests
import json
import urllib3
num = 5846
url2 = 'http://p2pxin.rongtuojinrong.com/rongtuoxinsoc/user/paorxercijiangli'
url = "http://api.uat.rongtuoyunlian.cn/php/recommend/getRecommendIdentity"
#https://onlineuat.cupdata.com/openapi/api/gateway

# data = {
# "identity": "0x4fca57771d96d933d8801b4a49ef3117ba88865ae573e489289d4d63811ddcde",
# "amount": "10000",
# "sms_code": "965236",
# "sms_seq": "1",
# "appid": "pc",
# "user_id": "2592",
# "scbUserId": "14544",
# "token": "443fa0c05e2e80762283310a53b7989e"
# }
# for i in range(0,5):
#     res = requests.post(url=url,data=data).json()
#     print(res)
# data = {
#
# "rongxinIdentity": "0x44a0ac0de5450d58033aafe68c52f7cc7e14408726390ba08416ae41d295203d",
#
# }
# urllib3.disable_warnings()
# res = requests.post(url=url,data=data,verify=False).json()
# print(res)


data = {
"rongxinIdentity": "0xf3b256499718ae0731ae7ad4070ae1b91aafccfa8507db3a304f37d74f5fcb8d"
}
urllib3.disable_warnings()
res = requests.post(url=url,data=data).json()
print(res)


# for i in range(0,50):
#     urllib3.disable_warnings()
#     res = requests.post(url=url,data=data,verify=False)
#     print(res)
#     num = num + 1

#
'''
查询一二级合伙人接口
http://api.uat.rongtuoyunlian.cn/php/recommend/getRecommendIdentity'''


