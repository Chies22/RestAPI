import requests

BASE_URL = 'http://localhost:5000/products'

def add_product(name, description, price):
    product = {
        'name': name,
        'description': description,
        'price': price
    }
    try:
        response = requests.post(BASE_URL, json=product)
        if response.status_code == 201:
            print('Product added successfully:', response.json())
        else:
            print('Failed to add product:', response.json())
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

def get_products():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print('Products:', response.json())
        else:
            print('Failed to retrieve products:', response.json())
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

# Example usage
add_product('Laptop', 'A high-performance laptop', 999.99)
get_products()