import sys
sys.path.append('E:\\api_test_star')
from base.runmethod import RunMethod
from data.get_data import GetData
from util.operation_excel import *
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.dataexcel = OpertionExcel
        self.commonutil = CommonUtil
        self.sendemail = SendEmail()
    #程序执行主入口
    def go_on_run(self):
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_url(i)
            method = self.data.get_request_way(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            expect = self.data.get_expcet_data(i)
            depend_case = self.data.is_depend(i)
            if depend_case != None:
                 # print("`````11`")
                 self.depend_data = DependentData(depend_case)
                 #获取返回结果里面的依赖
                 depend_respones_data = self.depend_data.get_data_for_key(i)
                 #获取依赖的key
                 depend_data = self.data.get_depend_field(i)
                 #将返回结果里面的依赖赋值给依赖数据
                 data[depend_data] = depend_respones_data

            if is_run == True:
                run_main = self.run_method.run_main(method,url,data,header)
                # print(type(run_main))
                # print(type(expect))
                print(run_main)
                if expect in run_main:
                     self.data.write_result(i,"pass")
                     pass_count.append(i)
                else:
                     self.data.write_result(i,run_main)
                     fail_count.append(i)
        self.sendemail.send_main(pass_count,fail_count)


if __name__ == '__main__':
     run = RunTest()
     run_go = run.go_on_run()
     print(run_go)

