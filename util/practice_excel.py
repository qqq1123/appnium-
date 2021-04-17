import xlrd
from xlutils.copy import copy
#联系读取excel方法1
"""
def get_sheet_data(fp = '../dataconfig/practice_data.xls',sheet_id=0):
    excel = xlrd.open_workbook(fp)
    data = excel.sheets()[sheet_id]
    return data

def get_lines():
    data = get_sheet_data()
    lins = data.nrows
    return lins
def get_coll():
    data = get_sheet_data()
    coll = data.ncols
    return coll



def read_excel():
    data = get_sheet_data()
    names = []
    jobs = []
    Gender = []
    ability = []
    Age = []
    for i in range(data.nrows):
        cells = data.row_values(i)
        name = cells[0]
        job = cells[1]
        Genders = cells[2]
        abilitys = cells[3]
        Ages = cells[4]
        names.append(name)
        jobs.append(job)
        Gender.append(Genders)
        ability.append(abilitys)
        Age.append(Ages)
    return names,jobs,Gender,Age,ability
data = read_excel()
print(data[1])
print(data[2])
print(data[3])
print(data)
"""
#联系读取excel方法2

def get_sheet_data(fp = 'E:\\api_test_star\\dataconfig\\practice_data.xls' ,sheet_id=0):
    data = xlrd.open_workbook(fp)
    sheet_data = data.sheets()[sheet_id]
    return sheet_data
def get_lines():
    sheet_data = get_sheet_data()
    lines = sheet_data.nrows
    return lines

def get_cell_value(rowx,colx):
    sheet_data = get_sheet_data()
    cell_value_data = sheet_data.cell_value(rowx,colx)
    return cell_value_data

def read_excel(colnameindex=0):
    data_excel = get_sheet_data()
    lines = get_lines()
    colnames = data_excel.row_values(colnameindex)
    list = []
    for rownum in range(1,lines):
        row = data_excel.row_values(rownum)
        # print(row)
        excel = {}
        for i in range(len(colnames)):
            excel[colnames[i]] = row[i]
            # print(excel[colnames[i]])
        # print(excel)
        list.append(excel)
    return list

def main():
    tables = read_excel()
    for i in tables:
        print(i)

if __name__ == '__main__':
    main()

#练习写入excel数据
"""
def get_sheet_data(fp='../dataconfig/practice_data.xls',sheet_id=0):
    excel_data = xlrd.open_workbook(fp)
    sheet_data = excel_data.sheets()[sheet_id]
    return sheet_data

def write_excel():
    headings = ['职位类别', '工作地址', '职位月薪', '工作地点', '工作经验要求',

                '职位要求', '最低学历要求']
    titile = ['1', '2', '3', '4', '5',

                '6', '7'

    ]
    fp = '../dataconfig/practice_data.xls'
    excel_data = xlrd.open_workbook(fp)
    write_data = copy(excel_data)
    sheet_data = write_data.get_sheet(0)
    # sheet_data.write(0, 5,"11")

    for i in range(0,len(headings)):
         for a in range(0,5):
            sheet_data.write(a,i,headings[i])



    # for a in range(0,len(titile)):
    #     sheet_data.write(0, a, titile[a])
    write_data.save(r'../dataconfig/practice_data.xls')
write_excel()
print(write_excel())
"""





