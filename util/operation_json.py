import json
class OperationJson:
     def __init__(self):
         self.data =self.read_data()
     #读取JSON文件
     def read_data(self):
        with open('../dataconfig/user.json',encoding='gb18030', errors='ignore') as fp:
            data = json.load(fp)
            return data
     #关键字获取数据
     def get_data(self,id):
         data = self.data[id]
         return data
if __name__ == '__main__':
     opjson = OperationJson()
     print(opjson.get_data('loginout'))
