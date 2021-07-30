from config import Config


def create_msg(to, email_code):
    from flask_mail import Message
    msg = Message(Config.FLASK_MAIL_SUBJECT_PREFIX,
                  sender=Config.FLASK_MAIL_SENDER, recipients=[to])
    msg.body = 'Sended by flask-email'
    msg.html = '''
        <h1> Hi </h1>
        <h3>欢迎来到 <b>Flask-little_test</b>!</h3>
        <p>
            您的验证码为 &nbsp;&nbsp; <b>{mailcode}</b> &nbsp;&nbsp; 赶快去完善注册信息吧！！！
        </p>

        <p>感谢您的支持和理解</p>
        <p>来自：Flask-little_test</p>
        '''.format(mailcode=email_code)
    return msg