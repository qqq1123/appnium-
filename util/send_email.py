import smtplib
from email.mime.text import MIMEText
class SendEmail:
    global send_user
    global host
    global password
    password = "xdwwwyrkubpnbhed"
    host = "smtp.qq.com"
    send_user = "362484633@qq.com"
    def send_email(self,user_list,sub,content):
        user = "测试李"+"<"+send_user+">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()
    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        conts_num = pass_num+fail_num
        pass_cont_num = '%.2f%%'  %(pass_num/conts_num*100)
        fail_cont_num = '%.2f%%'  %(fail_num/conts_num*100)
        user_list = ["lrd5621232@qq.com"]
        sub = "接口自动化报告邮件"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(conts_num,pass_num,fail_num,pass_cont_num,fail_cont_num )
        self.send_email(user_list,sub,content)
if __name__ == '__main__':
    sen =SendEmail()
    sen.send_main([1,2,3],[5,6,8])
