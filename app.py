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
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('Admin/dashboard.html', catalogo=catalogo)

@app.route('/cliente')
def cliente():
    return render_template('Client/index.html', catalogo=catalogo)

@app.route('/carrito')
def carrito_view():
    return render_template('Client/cart.html', items=carrito.get_items(), total=carrito.total())

@app.route('/agregar/<id>')
def agregar(id):
    if id in catalogo:
        carrito.add(catalogo[id])
    return redirect(url_for('cliente'))

@app.route('/vaciar')
def vaciar():
    carrito.clear()
    return redirect(url_for('carrito_view'))


@app.route('/admin/agregar', methods=['POST'])
def agregar_producto():
    id = request.form['id']
    name = request.form['name']
    price = float(request.form['price'])
    stock = int(request.form['stock'])

    if id not in catalogo:
        catalogo[id] = Product(id, name, price, stock)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
