# flask-mail | 发送邮件

from flask import Flask
from flask.ext.mail import Mail, Message


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=25,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='example@qq.com',
    MAIL_PASSWORD='awncypkfseigbjec',
    MAIL_DEBUG=True
)

mail = Mail(app)


@app.route('/')
def index():
    # sender 发送方哈，recipients 邮件接收方列表
    msg = Message('Hi!This is a test')
    msg.sender = 'example@qq.com'
    msg.recipients = ['example@domain.com']
    # msg.body 邮件正文
    msg.body = 'This is a first email'
    msg.html = '<h1>It is just test!</h1> body'
    # msg.attach 邮件附件添加
    # msg.attach("文件名", "类型", 读取文件）
    with app.open_resource("temp.py") as fp:
        # MIME(Multipurpose Internet Mail Extensions)多用途互联网邮件扩展类型
        msg.attach('example.py', 'text/plain', fp.read())

    mail.send(msg)
    print('Mail sent')
    return 'Sent'


if __name__ == '__main__':
    app.run()


'''
https://pythonhosted.org/Flask-Mail/
http://www.cnblogs.com/lonelycatcher/archive/2012/02/09/2343463.html
'''
