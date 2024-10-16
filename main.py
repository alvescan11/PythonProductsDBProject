from Domain.ProductValidator import ProductValidator
from Repository.RepoProduct import RepoProduct
from Service.ServiceProduct import ServiceProduct
from Ui.UI import Ui

if __name__ == '__main__':
    repo = RepoProduct()
    validator = ProductValidator()
    service = ServiceProduct(repo, validator)
    ui = Ui(service)
    ui.runMenu()