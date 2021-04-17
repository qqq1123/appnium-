import requests
import json
import urllib3.packages
class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            # urllib3.contrib.pyopenssl.inject_into_urllib3()
            res = requests.post(url=url,data=data,headers=header,verify=False)
        else:
            # urllib3.contrib.pyopenssl.inject_into_urllib3()
            res = requests.post(url=url,data=data,verify=False)
        return json.dumps(res.json(),indent=2, sort_keys=False, ensure_ascii=False)


    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            requests.packages.urllib3.disable_warnings()
            res = requests.get(url=url,data=data,headers=header,verify=False)
        else:
            # urllib3.contrib.pyopenssl.inject_into_urllib3()
            res = requests.get(url=url,data=data,verify=False)
        return json.dumps(res.json(),indent=2, sort_keys=False, ensure_ascii=False)


    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res =  self.get_main(url,data,header)
        return res


