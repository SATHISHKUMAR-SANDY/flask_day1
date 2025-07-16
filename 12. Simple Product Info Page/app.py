from flask import Flask


app = Flask(__name__)
products = {
    101: {
        "name": "Wireless Mouse",
        "price": 599.00,
        "stock": 25,
        "status": "Available"
    },
    102: {
        "name": "Bluetooth Headphones",
        "price": 1299.00,
        "stock": 10,
        "status": "Low Stock"
    },
    103: {
        "name": "USB Keyboard",
        "price": 499.00,
        "stock": 0,
        "status": "Out of Stock"
    },
    104: {
        "name": "Webcam 1080p",
        "price": 999.00,
        "stock": 15,
        "status": "Available"
    },
    105: {
        "name": "Laptop Stand",
        "price": 699.00,
        "stock": 5,
        "status": "Low Stock"
    }
}


@app.route('/product/<id>')
def product_details(id):

    product = products.get(int(id))
    return f"""
    <h1>Product Detail
    <h2>Product Name : {product['name']}</h2>
    <h2>Product Price : {product['price']}<h2>
    <h2>Product stock : {product['stock']}<h2>
    <h2>Product status : {product['status']}<h2>

"""
@app.route('/products')
def list_products():
    table = "<table border='1' cellpadding='10'><tr><th>ID</th><th>Name</th></tr>"
    for id, product in products.items():
        table += f"<tr><td>{id}</td><td>{product['name']}</td></tr>"
    table += "</table>"
    return f"""
    <h1>Product List</h1>
    {table}
    """


if __name__ == '__main__':
    app.run(debug=True,port=8000)