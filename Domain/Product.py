class Product:
    def __init__(self, idProduct, name, price, provider):
        self.idProduct = idProduct
        self.name = name
        self.price = price
        self.provider = provider

    def get_id(self):
        return self.idProduct

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_provider(self):
        return self.provider

    def set_name(self, name):
        self.name = name

    def set_price(self,price):
        self.price = price

    def set_provider(self, provider):
        self.provider = provider

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Provider: {self.provider}"