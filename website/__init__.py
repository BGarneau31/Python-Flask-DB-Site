from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # taking blueprints in views and auth and telling app that they are url we need
    from .views import views
    from .auth import auth

    # actually register the blueprints containing the urls for each page in the app
    app.register_blueprint(views, url_prefix='/')
    # url_prefix tells app what to put before all urls in each blueprint (in this case none cause dont need it but maybe for a book website it'd be chapter and the blueprints could contain each indiv page)
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
