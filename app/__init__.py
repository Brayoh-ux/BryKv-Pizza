from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vvndkdsj237nbntog87kkvd'

bootstrap.init_app(app)

from app import views