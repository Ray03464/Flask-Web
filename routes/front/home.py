from app import app
from flask import render_template
from products import products as products_list
@app.route('/')
def index():  # put application's code here
    products = products_list
    return render_template('index.html', products=products_list, modules='index')