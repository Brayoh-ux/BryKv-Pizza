import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT= 587
    MAIL_USERNAME = 'apppizza35@gmail.com'
    MAIL_PASSWORD = 'vbbmnmhgo45687##'
    MAIL_USE_TLS= True

class ProdConfig(Config):
    DUBUG = True