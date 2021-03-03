from flask import render_template,flash, url_for, redirect
from app import app
from app.forms import RegForm, LoginForm


@app.route('/')
def home():
    title = 'Pizza  app project'
    return render_template('home.html', title =title)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}! ','success')
        return redirect(url_for('home'))

    title = 'Pizza Register'
    return render_template('register.html', title = title, form = form)

@app.route('/login', methods =['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data =='brayo@g.com' and form.password.data == 'password1':
            flash(' login successful!','success')
            return redirect(url_for('home'))
        else:
            flash('Invalid password or email!','danger')

    title = 'Pizza login'
    return render_template('login.html', form = form, title = title)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order')
def order():
    return render_template('order.html')