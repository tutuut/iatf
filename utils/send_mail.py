import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from iatf.iatf.utils.read_config import ReadConfig

configs = ReadConfig()

class Send_email():
    def __init__(self):
        self.smtpserver = configs.config('smtp.smtpserver')
        self.port = configs.config('smtp.port')
        self.timeout = configs.config('smtp.timeout')
        self.username = configs.config('smtp.username')
        self.password = configs.config('smtp.password')
        self.sender = configs.config('smtp.sender')
        self.receivers = configs.config('smtp.receivers')

        self.smtpObj = smtplib.SMTP(self.smtpserver, self.port, self.timeout)
        self.smtpObj.login(self.username, self.password)

    def _message(self, msg,from_, to, subject, type, *files):
        message = MIMEMultipart()
        message['From'] = Header(from_, 'utf-8')
        message['To'] = Header(to, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        message.attach(MIMEText(msg, type, 'utf-8'))
        count = 1
        for file in files:
            names = locals()
            names['appendix_' + str(count)] = MIMEText(open(file, 'rb').read(), 'plain', 'utf-8')
            names['appendix_' + str(count)]['Content-Type'] = 'application/octet-stream'
            names['appendix_' + str(count)].add_header('Content-Disposition', 'attachment', filename = self._get_filename(file))
            message.attach(names['appendix_' + str(count)])
            count += 1
        return message

    def send(self, msg, from_, to, subject, type, *files):
        '''
        :param msg: 消息内容，若为html格式，type设为'html'
        :param from_: 发送者
        :param to: 接收者
        :param subject: 标题
        :param type: 普通内容 'plain'，HTML格式 'html'
        :param files: 文件，可传多个文件
        :return:
        '''
        try:
            self.smtpObj.sendmail(self.sender, self.receivers, self._message(msg, from_, to, subject, type, *files).as_string())
            print('邮件发送成功！')
        except smtplib.SMTPException as e:
            print(e)
        self.smtpObj.quit()

    def _get_filename(self, path):
        return os.path.split(path)[-1]


if __name__ == '__main__':
    try:
        mail = Send_email()
        mail.send('<h1>hello</h1>','from','to','title','html', './api.xlsx', 'help.py')
    except Exception as e:
        print(e)
