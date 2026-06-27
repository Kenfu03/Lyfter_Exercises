class Inventory:
    product_list : list[Product] = []


    def add_product(self, product):
        self.product_list.append(product)


    def show_all(self):
        for product in self.product_list:
            print(f"- {product.name}, {product.amount} at ${product.price} each")


    def calc_value(self):
        calc = 0
        for product in self.product_list:
            calc += product.amount * product.price
        return calc


class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


store_inventory = Inventory()
product1 = Product("Mouse", 5000, 3)
product2 = Product("Monitor", 10000, 1)
product3 = Product("Microfono", 3000, 6)
product4 = Product("Memory", 2000, 8)

store_inventory.add_product(product1)
store_inventory.add_product(product2)
store_inventory.add_product(product3)
store_inventory.add_product(product4)

store_inventory.show_all()
print(f"The total value is: ${store_inventory.calc_value()}")