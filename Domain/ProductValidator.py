from Domain.Product import Product


class ProductValidator:
    def validate(self, product: Product):
        errors = []
        if product.get_name() == "":
            errors.append("Name cannot be empty!!!")
        if product.get_provider() not in ["Sano", "Neves", "Loriand", "Agrosem"]:
            errors.append("Provider can be only Sano, Neves, Loriand or Agrosem!!!")
        if errors:
            raise ValueError(errors)