products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

products_category = {}

for product in products:
    category = product.get("category")
    price = product["price"]
    
    if category not in products_category:
        products_category[category] = price
    else:
        products_category[category] += price


print(products_category)
    
        