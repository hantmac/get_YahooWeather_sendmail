# -*- coding: utf-8 -*-

import os

# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

MAIL_USER='发件箱'
MAIL_TOKEN='网易邮箱授权码'
MAIL_FROM="FROM,可自己定制"
MAIL_SERVER="smtp.163.com" # 网易邮箱服务器

def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    msg = MIMEText(content, _subtype='html', _charset='utf-8')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub  # 设置主题
    msg['From'] = MAIL_FROM
    msg['To'] = ";".join(to_list)

    mail_server = MAIL_SERVER  # 设置服务器
    mail_user = MAIL_USER  # 用户名
    mail_pass = MAIL_TOKEN  # 口令

    try:
        s = smtplib.SMTP()
        #import pdb; pdb.set_trace()

        s.connect(mail_server)  # 连接smtp服务器
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(MAIL_FROM, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception as e:
        print(str(e))  # print error log
        return False
