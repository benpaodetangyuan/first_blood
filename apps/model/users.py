from flask_login import UserMixin
from apps.model import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    isAdmin = db.Column(db.Boolean())

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = password
        if email == '1176479480@qq.com':
            self.isAdmin = True
        else:
            self.isAdmin = False

    def __repr__(self):
        return "<User '{}'>".format(self.username)

    @property
    def password(self):
        return "Password is not readable!"

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, user_pwd):
        return check_password_hash(self.password_hash, user_pwd)
