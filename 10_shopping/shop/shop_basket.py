from shop.shop_product import Product


class ShopBasket:

    def __init__(self):
        self.products = []

    def basket_total(self):
        return len([product.quantity for product in self.products])

    def product_add(self, name, price):
        for product in self.products:
            if product.name == name:
                product.quantity += 1
                return self
        self.products.append(Product(name, price))
        return self

    def product_idx(self, index):
        return self.products[index]

    def summary(self, tax=21):
        net_value = sum([product.price * product.quantity
                         for product in self.products])
        return round(net_value * (1 + tax/100.0), 2)

    def basket_view(self):
        print("Basket: ")
        for product in self.products:
            print(f"\t{product}")
