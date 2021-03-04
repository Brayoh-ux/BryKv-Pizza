from flask import render_template,flash, url_for, redirect, request
from app import app, db 
from app.models import Pizza
from app.forms import RegForm, LoginForm

POST = 'POST'
GET = 'GET'

@app.route('/')
def home():
    if request.method == GET:
        products = Pizza.query.all()
        return render_template('home.html', products = products)
    else:
        print('***** POST REQUEST *****')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}! ','success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'registration', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form = form, title = 'login')

@app.route('/about')
def about():
    return render_template('about.html',title='about')

@app.route('/cart')
def cart():
    return render_template('cart.html',title = 'cart')
