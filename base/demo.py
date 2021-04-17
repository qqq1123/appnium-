import requests
import json
class RunMain:
    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)


    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)


    def run_main(self,url,method,data=None):
        res = None
        if method == 'get':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/login/'
    data = {
    'username': '123321',
    'password': '1231231'
    }
#print(run_main(url,'GET'))
    res = RunMain()
    print(res.run_main(url,'post',data))


