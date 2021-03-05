from flask import render_template,flash, url_for, redirect,request
from app import app,db, mail
from app.forms import RegForm, LoginForm, OrderForm,UpdateMenu
from flask_login import current_user, login_user,logout_user,login_required
from app.models import User,Pizza
from .email import mail_message
from flask_mail import Mail,Message


@app.route('/')
def home():
    title = 'Pizza  app project'
    return render_template('home.html', title =title)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password_hash = form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message('Welcome to Pizza App. We value you', 'email/welcome', user.email, user = user)

        return redirect(url_for('admin'))

    title = 'Pizza Register'
    return render_template('register.html', title = title, form = form)

@app.route('/login', methods =['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None :
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('admin'))
        
        flash("Invalid email or password")
    title  = 'login page'

    return render_template('login.html', form = form, title = title)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order', methods =['GET', 'POST'])
def order():
    form = OrderForm()
    if request.method == 'POST':
        email = request.form['email']
        pizza = request.form['pizza']
        size = request.form['size']
        crust = request.form['crust']
        toppings = request.form['toppings']
        no_of_pizzas = request.form['no_of_pizzas']


        message = Message(subject=[email, pizza, size, crust, toppings, no_of_pizzas], recipients=[email], sender='apppizza35@gmail.com')

        message.body = 'Thank you for shopping with us. Your pizza will be delivered 30 minutes from now or sooner!!'
        mail.send(message)

        flash('Oder was succefull!')
        return redirect(url_for('home'))

    return render_template('order.html', form = form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home.html')

@app.route('/admin')
@login_required
def admin():
    posts = [
        {'body': 'Am the body!'}
    ]
    return render_template('admin.html', posts = posts)

@app.route('/updated_menu', methods = ['GET', 'POST'])
@login_required
def update():
    form = UpdateMenu()
    if form.validate_on_submit():
        pizza = Pizza(pizza = form.pizza.data, pizza_amount =form.pizza_amount.data, p_size = form.p_size.data, crust = form.crust.data,
        crust_amount = form.crust_amount.data, toppings = form.toppings.data,top_size = form.top_size.data)
    
        db.session.add(pizza)
        db.session.commit()

        flash('Menu created', 'success')
        return redirect(url_for('admin'))

    title = 'Menu updata page'
    return render_template('updated_menu.html',title = title, form =form)
