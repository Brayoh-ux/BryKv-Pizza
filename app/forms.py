from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField ,SelectField , BooleanField, PasswordField, SubmitField
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

class OrderForm(FlaskForm):
    email = StringField('Enter email to recieve reciept', validators=[Required(), Email()] )
    pizza = SelectField('Choose Pizza', choices=[('Grilled Chicken'), ('Chicken Wrap Special'),('Ice-cream Summer') , ('Veggie Special'), ('Delux Cheese Bugger')], validators=[Required()])
    size = SelectField('Choose size', choices = [('small'), ('medium'), ('large')], validators=[Required()])
    crust = SelectField('Choose Crust',choices=[('Crispy'), ('Stuffed'), ('Glutten Free')] ,validators=[Required()])
    toppings = SelectField('Choose Toppings', choices=[('Mushrooms'), ('Blackolives'), ('cheese'), ('Green Pepper')], validators=[Required()])
    no_of_pizzas = IntegerField('How many Pizzas?', validators=[Required()])
    submit = SubmitField('Order Now')