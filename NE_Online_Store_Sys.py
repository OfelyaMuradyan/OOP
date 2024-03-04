class Product:
    def __init__(self, product_id, product_name, price, inventory_count):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.inventory_count = inventory_count
        self.dynamic_pricing = DynamicPricing()

    def apply_discount(self, discount_percentage):
        self.price *= ((100 - discount_percentage) / 100)

    
    def sell(self, quantity = 0):
        self.inventory_count -= quantity
        if quantity > 5:
            self.dynamic_pricing.modified_price(self)
        print(self.price)

class DynamicPricing:
    def modified_price(self,product):

        product.apply_discount(5)

product = Product(1, 'bread', 500, 20)
product.sell(10)
product.sell(-10)

