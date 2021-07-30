import random
from flask import Blueprint
from flask_restful import Resource, reqparse, inputs
from apps.model import db
from apps.model.users import User
from apps.util import create_msg
from . import mail, cache
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user', __name__)
login_parse = reqparse.RequestParser()
login_parse.add_argument('username', type=str, help='用户名格式错误！', nullable=False, location='form')
login_parse.add_argument('password', type=str, help='密码格式错误', nullable=False, location='form')


class UserLoginResource(Resource):
    def get(self):
        pass

    def post(self):
        args = login_parse.parse_args()
        username = args.get('username')
        password = args.get('password')
        user = User.query.filter_by(username=username).first()
        print(user.check_password(password))
        if user is not None and user.check_password(password):
            allow_login = True
            return allow_login
        else:
            allow_login = False
            return allow_login


register_parse = reqparse.RequestParser()
register_parse.add_argument('username', type=str, help='用户名格式错误！', nullable=False, location='form')
register_parse.add_argument('email',
                            type=inputs.regex(r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'),
                            help='邮箱格式错误！', nullable=False, location='form')
register_parse.add_argument('password', type=str, help='密码格式错误', nullable=False, location='form')


class UserRegisterResourse(Resource):
    def get(self):
        pass

    def post(self):
        args = register_parse.parse_args()
        username = args.get('username')
        email = args.get('email')
        password = args.get('password')
        user = User.query.filter_by(username=username, email=email).first()
        if user is None:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            register_succeed = True
            return register_succeed
        else:
            register_succeed = False
            return register_succeed


reset_parse = reqparse.RequestParser()
reset_parse.add_argument('email', type=inputs.regex(r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'),
                         help='邮箱格式错误！', nullable=False, location='form')


class UserResetResource(Resource):
    def get(self):
        pass

    def post(self):
        args = reset_parse.parse_args()
        email = args.get('email')
        user = User.query.filter_by(email=email)
        if user is None:
            reset_succeed = False
            return reset_succeed
        else:
            cache.set("email", email)
            code = ('%06d' % random.randint(0, 99999))
            cache.set("code", code)
            msg = create_msg(email, code)
            mail.send(msg)
            reset_succeed = True
            return reset_succeed


upgrade_parse = reqparse.RequestParser()
upgrade_parse.add_argument('password', type=str,
                           help='密码格式错误', nullable=False, location='form')

upgrade_parse.add_argument('code', type=str,
                           help='验证码错误', nullable=False, location='form')


class UserUpgradeResourse(Resource):
    def get(self):
        pass

    def post(self):
        args = upgrade_parse.parse_args()
        new_password = args.get('password')
        code = args.get('code')
        print(code)
        print(cache.get('code'))
        if code != cache.get('code'):
            upgrade_succeed = False
            return upgrade_succeed
        else:
            email = cache.get("email")
            user = User.query.filter_by(email=email).first()
            new_password_hash = generate_password_hash(new_password)
            sql = "UPDATE users SET password_hash =:newPasswordHash WHERE password_hash=:oldPasswordHash"
            db.session.execute(sql, {'newPasswordHash': new_password_hash, 'oldPasswordHash': user.password_hash})
            db.session.commit()
            upgrade_succeed = True
            return upgrade_succeed
