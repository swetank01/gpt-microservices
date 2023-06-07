from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    # Code for retrieving product information
    # Retrieve product details from database or other sources
    # ...

    products = [
        {'id': 1, 'name': 'Product 1', 'price': 10.0},
        {'id': 2, 'name': 'Product 2', 'price': 20.0},
        {'id': 3, 'name': 'Product 3', 'price': 30.0}
    ]

    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Code for retrieving a specific product
    # Retrieve product details based on the provided product_id
    # ...

    product = {'id': product_id, 'name': 'Product {}'.format(product_id), 'price': 10.0}

    return jsonify(product)

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Code for updating a product
    # Retrieve updated product details from request data
    # ...

    # Update the product in the database or perform other necessary operations
    # ...

    return 'Product updated successfully'

if __name__ == '__main__':
    app.run(port=5001)
