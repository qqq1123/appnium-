import xlrd
from xlutils.copy import copy
class OpertionExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/ceshi.xls'
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取单元格的行数
    def get_lines(self):
        tables = self.data.nrows
        return tables
    #获取某一个单元格的内容
    def get_cell_value(self,rowx,colx):
        tables = self.data.cell_value(rowx,colx)
        return tables
    #写入数据到excel
    def write_value(self,rowx,colx,value):
        # 传入参数rowx, colx, value
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(rowx,colx,value)
        write_data.save(self.file_name)
    #根据对应的case_id找到对应的行号的内容
    def get_rows_data(self,case_id):
        row_num = self.get_rows_num(case_id)
        row_data = self.get_row_values(row_num)
        print(row_data)
        return row_data

    #根据对应的case_id找到对应的行号
    def get_rows_num(self,case_id):
        num = 0
        cols_data = self.get_cols_data()
        for cols_data in cols_data:
            if case_id in cols_data:
                return num
            num = num+1

    #根据对应的行号找到对应的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols




if __name__ == '__main__':
    opers = OpertionExcel()
    print(opers.get_data().nrows)
    print(opers.get_lines())
    print(opers.get_cell_value(2,2))
