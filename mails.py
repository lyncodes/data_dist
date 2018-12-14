import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd


def read_email_para():
    config = pd.read_excel("configuration.xlsx")
    return config


def send_email(choice, current_time, mail_logger, zip_file_name):
    config = read_email_para()
    mail_logger.info(choice + "（邮件参数尝试读取）")
    title, mesag, src, pwd, to, cp = ['0', '0', '0', '0', '0', '0']
    # 读取邮件参数
    try:
        title = config[config.file_name == choice]['title'].values[0]
        mesag = config[config.file_name == choice]['mesag'].values[0]
        src = config[config.file_name == choice]['src'].values[0]
        pwd = config[config.file_name == choice]['pwd'].values[0]
        to = config[config.file_name == choice]['to'].values[0]
        cp = config[config.file_name == choice]['cp'].values[0]

        mail_logger.info(choice + "（邮件参数读取成功）")
    except:
        mail_logger.critical(choice + "（邮件参数读取失败）")
    # 如名字所示Multipart就是分多个部分
    msg = MIMEMultipart()
    msg["Subject"] = title
    msg["From"] = src
    msg["To"] = to
    msg["Cc"] = cp

    # ---这是文字部分---
    try:
        if mesag == '':
            mail_logger.warning(choice + "邮件正文为空")
        email_text = mesag
        part = MIMEText(email_text)
        msg.attach(part)
        mail_logger.info(choice + "邮件正文添加完成")
    except:
        mail_logger.critical(choice + "邮件正文添加失败")
    # ---这是附件部分---
    try:
        zip_name = zip_file_name
        part = MIMEApplication(open(zip_name, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=zip_name)
        msg.attach(part)
        mail_logger.info(choice + "邮件附件添加成功")
    except:
        mail_logger.critical(choice + "邮件附件添加失败")
    # mail server ip
    s = smtplib.SMTP("mail.*********.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
    mail_logger.info(choice + "登录邮件服务器（尝试）")
    try:
        s.login(src, pwd)  # 登陆服务器
        mail_logger.info(choice + "登录邮件服务器（成功）")
    except:
        mail_logger.critical(choice + "登录邮件服务器（失败）")
    mail_logger.info(choice + "发送邮件（尝试）")
    try:
        s.sendmail(src, to.split(",") + cp.split(","), msg.as_string())  # 发送邮件
        mail_logger.info(choice + "发送邮件（成功）")
    except:
        mail_logger.critical(choice + "发送邮件（失败）")
    s.close()
