from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # pizza = db.relationship('Pizza', backref='pizza', lazy ='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Pizza(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pizza = db.Column(db.String, index=True, unique=True)
    pizza_amount = db.Column(db.Integer, index=True, unique=True)
    p_size = db.Column(db.String, index=True, unique=True)
    crust = db.Column(db.String, index=True, unique=True)
    crust_amount = db.Column(db.String, index=True, unique=True)
    toppings = db.Column(db.String, index=True, unique=True)
    top_size = db.Column(db.String, index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return 'Pizza <{}>'.format(self.pizza)