
class CommonUtil:
    #判断一个字符串是否在另外一个字符串中
    def is_contain(self,str_one,str_two):
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
