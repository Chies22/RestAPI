from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from product import Product


app = Flask(__name__)
api = Api(app)

# In-memory storage (replace with database for production)
products = []
# testing the API
@app.route("/")
def Testing():
    return"Test"

class ProductList(Resource):
    def get(self):
        # Return list of all products
        return jsonify(products)

    def post(self):
        try:
            # Get JSON data from request
            data = request.get_json()
            name = data['name']
            description = data['description']
            price = float(data['price'])

            # Validate data
            if not all([name, description, price]):
                raise ValueError("Missing required fields")

            # Create product object (optional, use model)
            new_product = Product(name, description, price)
            products.append(new_product)

            # Return created product and 201 status code
            return jsonify(new_product), 201

        except (KeyError, ValueError) as e:
            # Handle invalid JSON or missing fields
            return jsonify({'error': str(e)}), 400


api.add_resource(ProductList, '/products')

if __name__ == '__main__':
    app.run(debug=True)