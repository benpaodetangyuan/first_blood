from flask import Flask
from flask_login import LoginManager
from config import DevConfig
from flask_script import Manager, Server
from apps.model import db
from apps.model.users import User
from apps.model.goods import Goods
from apps.view import cache
from apps.view.users import user_bp, UserLoginResource, UserRegisterResourse, UserResetResource, UserUpgradeResourse
from apps.view.goods import good_bp, HomeResourse, Grounding, UnderCarriage
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(DevConfig)
    app.register_blueprint(user_bp)
    app.register_blueprint(good_bp)
    cors = CORS(app)
    cors.init_app(app)
    api = Api(app=app)
    api.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail = Mail(app)
    mail.init_app(app)
    app.app_context().push()
    migrate = Migrate(app, db)
    migrate.init_app(app)
    manager = Manager(app)
    manager.add_command("server", Server())
    api.add_resource(HomeResourse, '/', endpoint='home')
    api.add_resource(UserLoginResource, '/login', endpoint='login')
    api.add_resource(UserRegisterResourse, '/register', endpoint='register')
    api.add_resource(UserResetResource, '/reset_password', endpoint='reset_password')
    api.add_resource(UserUpgradeResourse, '/upgrade_password', endpoint='upgrade_password')
    api.add_resource(Grounding, '/grounding', endpoint='grounding')
    api.add_resource(UnderCarriage, '/undercarriage', endpoint='undercarriage')

    # db.drop_all()
    # db.create_all()

    @manager.shell
    def make_shell_context():
        return dict(app=app, db=db, User=User, Goods=Goods)

    return app
