class Config(object):
    SECRET_KEY = '123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Dev%40123@localhost:3306/little_test?charset:utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'FALSE'
    MAIL_DEBUG = False
    MAIL_SUPPRESS_SEND = False
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = '1176479480@qq.com'
    MAIL_PASSWORD = 'fakjnmytkwswhjgi'
    FLASK_MAIL_SENDER = '1176479480@qq.com'
    FLASK_MAIL_SUBJECT_PREFIX = '修改密码' 
    FLASK_ADMIN = '1659522889@qq.com'
    GOODS_NUM = 4


class ProdConfig(Config):
    pass


class DevConfig(Config):
    ENV = 'DEVELOPMENT'
    DEBUG = True
