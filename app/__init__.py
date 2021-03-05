from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_mail import Mail


bootstrap = Bootstrap()


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
mail = Mail(app)

migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


bootstrap.init_app(app)

from app import views, models