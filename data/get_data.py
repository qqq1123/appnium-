from util.operation_excel import OpertionExcel
from data import data_congfig
from util.operation_json import OperationJson
class GetData:
    def __init__(self):
        self.opera_excel = OpertionExcel()
    #获取执行case个数 excel行数
    def get_case_lines(self):
        lines = self.opera_excel.get_lines()
        return lines
    #获取是否执行
    def get_is_run(self,rowx):
        flag = None
        colx = int(data_congfig.get_run())
        run = self.opera_excel.get_cell_value(rowx,colx)
        if run == 'yes':
            flag = True
        else:
            flag = False
        return flag
    #是否携带header
    def is_header(self,rowx):
        col = int(data_congfig.get_head())
        header = self.opera_excel.get_cell_value(rowx,col)
        if header == 'yes':
            return data_congfig.get_header_value()
        else:
            return None
    #获取请求方式 request_way
    def get_request_way(self,rowx):
        col = int(data_congfig.get_request_way())
        request_method = self.opera_excel.get_cell_value(rowx,col)
        return request_method
    #获取URL
    def get_url(self,rowx):
        col = int(data_congfig.get_url())
        url = self.opera_excel.get_cell_value(rowx,col)
        return url
    #获取请求数据data
    def get_request_data(self,rowx):
        col = int(data_congfig.get_data())
        request_data = self.opera_excel.get_cell_value(rowx,col)
        if request_data == '':
            return None
        else:
            return request_data
    #通过获取关键字拿到data数据
    def get_data_for_json(self,rowx):
        operation_json = OperationJson()
        request_data = operation_json.get_data(self.get_request_data(rowx))
        return request_data
    #获取预期结果
    def get_expcet_data(self,rowx):
        col = int(data_congfig.get_expect())
        expcet_data = self.opera_excel.get_cell_value(rowx,col)
        if expcet_data == "":
            return None
        return expcet_data
    def write_result(self,rowx,value):
        col = int(data_congfig.get_request())
        self.opera_excel.write_value(rowx,col,value)

    #获取excel里的依赖返回数据
    def get_dependent_data(self,rowx):
        col = int(data_congfig.get_data_depend())
        depen_data = self.opera_excel.get_cell_value(rowx,col)
        if depen_data == "":
            return None
        else:
            return depen_data
    #判断是否有依赖数据
    def is_depend(self,row):
        col = int(data_congfig.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id
    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_congfig.get_field_data_depend())
        data = self.opera_excel.get_cell_value(row,col)
        if data == "":
            return None
        else:
            return data
if __name__ == '__main__':
    get = GetData()





