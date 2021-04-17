import requests
import json



# #徽商查询电子账户

url ='http://api.uat.rongtuoyunlian.com/pay/hsQuery/OpenBankD_AcctQryByMob.json'

data = {
"PHONE": "15910089073"
}


ww = requests.post(url=url,data=data).json()
print(ww)


# print(ww)


#徽商查询余额

# url = 'http://api.uat.rongtuoyunlian.com/pay/hsQuery/OpenBankD_BalanceQuery.json'
#
#
# data ={
# "CARDNBR": "9930041005560180167"
# }
#
#
#
# ww = requests.post(url=url,data=data).json()
# print(ww)

