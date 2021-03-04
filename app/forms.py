from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo

class RegForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(min =2, max =20)])
    email = StringField('Email', validators=[Required(), Email() ])
    password = PasswordField('Password', validators=[Required(), Length(min =8)])
    password_confirm = PasswordField('Confirm Password', validators=[Required(), EqualTo('password'), Length(min =8)])
    submit =SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email() ])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit =SubmitField('Login')
