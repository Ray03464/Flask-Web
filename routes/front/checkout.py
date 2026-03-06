from app import app
from flask import render_template
from products import products as products_list
@app.route('/checkout')
def checkout():
    return render_template('checkout.html', modules='checkout')