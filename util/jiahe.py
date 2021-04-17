import requests,json

url = 'https://api.rongtuoyunlian.cn/buyer/buyerPcOrder/saveOrderInfo'

data = {
'addrId': '4963',
'goodsIdStr': '965',
'goodsNumStr': '1',
'shopName': '测试企业线上专用',
'sourceType': 'pc',
'faceFlag': '1',
'saleSpecIdStr': '1156',
'appid': 'pc',
'user_id': '1729',
'scbUserId': '17',
'token': '92e7c1b3e3dd575c23552553845e82ef'
}


re = requests.post(url=url,data=data).json()
print(re)