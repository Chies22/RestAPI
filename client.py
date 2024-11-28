import requests

# API endpoint URL
url = "http://127.0.0.1:5000/"

# Create a new product
data = {'name': 'New Product', 'description': 'This is a new product', 'price': 19.99}
response = requests.post(url, json=data)

if response.status_code == 201:
    print("Product created successfully!")
    new_product = response.json()
    print(f"New product: {new_product}")
else:
    print(f"Error creating product: {response.status_code} {response.text}")

# Get all products
response = requests.get(url)

if response.status_code == 200:
    products = response.json()
    print("Products:")
    for product in products:
        print(f"- {product['name']} ({product['price']})")
else:
    print(f"Error retrieving products: {response.status_code} {response.text}")