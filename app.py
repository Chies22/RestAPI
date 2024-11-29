from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route("/")
def Checking():
    return"successfull"
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or not 'name' in data or not 'description' in data or not 'price' in data:
        return jsonify({'error': 'Bad Request'}), 400
    product = {
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__== '_main_':
    app.run(debug=True)