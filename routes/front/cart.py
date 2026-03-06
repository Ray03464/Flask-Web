from app import app
from flask import render_template
from products import products as products_list
@app.route('/cart')
def cart():
    return render_template('cart.html', modules='cart')