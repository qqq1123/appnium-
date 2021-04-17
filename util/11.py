# import xlrd
# fp = '../dataconfig/practice_data.xls'
# by_name=u'Sheet2'
# xl = xlrd.open_workbook(fp)
# xls = xl.sheet_by_name(by_name)
# data = xls.nrows
# # aa = xls.cell_value(2,1)
# print(data)
#











s = 'abaccdeff'
result = {}
def first_uniq_char(s):
    if type(s) is not str:
        raise Exception("您输入的不是字符串,请重新输入")
    for i in s:
        if i not in result:
            result[i] = 1
            print(result)
        else:
            result[i] = result[i] + 1
            print(result)
    for r in result:
        if result[r] == 1:
            print(r)
            return r

    return ' '


print(first_uniq_char(s))