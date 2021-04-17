from util.operation_excel import OpertionExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import math
import json
class DependentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OpertionExcel()
        self.run = RunMethod()
        self.data = GetData()
    #通过case_id去获得该case_id的数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data
    #执行依赖测试获取的数据
    def run_dependent(self):
        row_num = self.opera_excel.get_rows_num(self.case_id)
        request_data =self.data.get_data_for_json(row_num)
        url = self.data.get_url(row_num)
        method = self.data.get_request_way(row_num)
        header = self.data.is_header(row_num)
        #method,url,data=None,header=None
        run_depen = self.run.run_main(method,url,request_data,header)
        return json.loads(run_depen)
    #根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,rowx):
        depend_data = self.data.get_dependent_data(rowx)
        response_data = self.run_dependent()
        # print(depend_data)
        # print(response_data)
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]






