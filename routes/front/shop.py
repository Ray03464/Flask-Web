from app import app
from flask import render_template
from products import products as products_list
@app.route('/shop')
def shop():
    return render_template('shop.html', modules='shop')