from flask import render_template, url_for, redirect
from app import app, 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')