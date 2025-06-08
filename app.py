# app.py

from flask import Flask, render_template, request, redirect, url_for
from product import Product
from Cart import Cart

app = Flask(__name__)
carrito = Cart()

catalogo = {
    "1": Product("1", "Manzana", 0.5),
    "2": Product("2", "Banana", 1.0),
    "3": Product("3", "Agua", 0.75)
}

@app.route('/')
def index():
    return render_template('index.html', catalogo=catalogo)

@app.route('/add/<id>')
def add(id):
    if id in catalogo:
        carrito.add(catalogo[id])
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    return render_template('cart.html', items=carrito.get_items(), total=carrito.total())

@app.route('/clear')
def clear():
    carrito.clear()
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
