from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField ,SelectField , BooleanField, PasswordField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo,ValidationError
from app.models import User



class RegForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(min =2, max =20)])
    email = StringField('Email', validators=[Required(), Email() ])
    password = PasswordField('Password', validators=[Required(), Length(min =8)])
    password_confirm = PasswordField('Confirm Password', validators=[Required(), EqualTo('password'), Length(min =8)])
    submit =SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Ooop! Someone took this username!!')
        

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('OH Shaks! Someone took that email!')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class OrderForm(FlaskForm):
    email = StringField('Enter email to recieve reciept', validators=[Required(), Email()] )
    pizza = SelectField('Choose Pizza', choices=[('Grilled Chicken'), ('Chicken Wrap Special'),('Ice-cream Summer') , ('Veggie Special'), ('Delux Cheese Bugger')], validators=[Required()])
    size = SelectField('Choose size', choices = [('small'), ('medium'), ('large')], validators=[Required()])
    crust = SelectField('Choose Crust',choices=[('Crispy'), ('Stuffed'), ('Glutten Free')] ,validators=[Required()])
    toppings = SelectField('Choose Toppings', choices=[('Mushrooms'), ('Blackolives'), ('cheese'), ('Green Pepper')], validators=[Required()])
    no_of_pizzas = IntegerField('How many Pizzas?', validators=[Required()])
    submit = SubmitField('Order Now')

class UpdateMenu(FlaskForm):
    pizza = StringField('Pizza', validators=[Required()])
    pizza_amount = IntegerField('Price', validators=[Required()])
    p_size = SelectField('Size', choices=[('small'), ('medium'), ('large')])
    crust = StringField('Crust')
    crust_amount = IntegerField('Price', validators=[Required()])
    toppings = StringField('Toppings', validators=[Required()])
    top_size = IntegerField('Price', validators=[Required()])
    submit = SubmitField('Add Menu')