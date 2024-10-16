from Domain.Product import Product
from Domain.ProductValidator import ProductValidator
from Repository.RepoProduct import RepoProduct


class ServiceProduct:
    def __init__(self, repo: RepoProduct, validator: ProductValidator):
        self.__repo = repo
        self.__validator = validator

    def add(self, idProduct, name, price, provider):
        self.__validator.validate(Product(idProduct, name, price, provider))
        self.__repo.add(Product(idProduct, name, price, provider))

    def delete(self, idc):
        if self.find_by_id(idc) is not None:
            self.__repo.delete(self.find_by_id(idc))
        else:
            raise ValueError("There is no person with this id !")

    def update(self, name, price, provider, idc):
        self.__repo.update(idc, Product(idc, name, price, provider))

    def find_product_by_name(self, name):
        for elem in self.__repo.get_all():
            if elem.get_name() == name:
                return elem

    def find_by_id(self, idc):
        return self.__repo.find_by_id(idc)

    def get_all(self):
        return self.__repo.get_all()

    def size(self):
        return self.__repo.size()