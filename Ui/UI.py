import uuid

from Domain.Product import Product
from Service.ServiceProduct import ServiceProduct


class Ui:
    def __init__(self, serviceProduct: ServiceProduct):
        self.serviceProduct = serviceProduct

    def print_menu(self):
        print("1. Add person")
        print("2. Delete person")
        print("3. Modify person")
        print("4. Find product by name")
        print("5. Show all products")
        print("x. Exit")

    def runMenu(self):
        while True:
            self.print_menu()
            option = input("Give an option: ")
            if option == "1":
                self.add_product()
            elif option == "2":
                self.delete_product()
            elif option == "3":
                self.update_product()
            elif option == "4":
                self.find_product_by_name()
            elif option == "5":
                self.get_all()
            elif option == "x":
                break
            else:
                print("Wrong option!!!")

    def add_product(self):
        try:
            idProduct = uuid.uuid4()
            name = input("Name: ")
            price = input("Price: ")
            provider = input("Provider: ")
            self.serviceProduct.add(idProduct,name,price,provider)
        except Exception as e:
            print(e)

    def delete_product(self):
        try:
            id = input("Give the id of the product you want to delete: ")
            self.serviceProduct.delete(id)
        except Exception as e:
            print(e)

    def update_product(self):
        try:
            id = input("Give the id of the product you want to update: ")
            name = input("New name: ")
            price = input("New price: ")
            provider = input("New provider: ")
            self.serviceProduct.update(id,name,price,provider)
        except Exception as e:
            print(e)

    def find_product_by_name(self):
        try:
            name = input("Give the product's name: ")
            print(self.serviceProduct.find_product_by_name(name))
        except Exception as e:
            print(e)

    def get_all(self):
        for elem in self.serviceProduct.get_all():
            print(elem)
