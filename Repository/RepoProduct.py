import psycopg2

import database_config
from Domain.Product import Product



class RepoProduct:
    def __init__(self):
        self.__repo = self.__read()

    @staticmethod
    def connect():
        try:
            mydb2 = psycopg2.connect(
                host=database_config.host,
                user=database_config.user,
                password=database_config.password,
                port=database_config.port,
                database=database_config.database
            )
            return mydb2
        except psycopg2.Error as y:
            print(f"Error connecting to database:\n {y}")
            return None

    def __read(self):
        result = []
        if self.connect() is None:
            raise Exception("↓ Something is wrong with the connection! ↓")
        cursor = self.connect().cursor()
        cursor.execute('SELECT idProduct, name, price, provider FROM public."Products"')

        for elem in cursor.fetchall():
            result.append(Product(elem[0], elem[1], elem[2], elem[3]))
        cursor.close()
        return result

    def __insert(self, elem: Product):
        conn = self.connect()
        cursor = conn.cursor()
        sql = ('INSERT INTO public."Products" (idProduct, name, price, provider)'
               ' VALUES (%s, %s, %s,%s)')
        person_data = (str(elem.get_id()), elem.get_name(), elem.get_price(), elem.get_provider())

        cursor.execute(sql, person_data)
        conn.commit()
        cursor.close()
        conn.close()

    def __delete(self, elem: Product):
        conn = self.connect()
        cursor = conn.cursor()
        sql = 'DELETE FROM public."Products" WHERE idProduct = %s'

        cursor.execute(sql, (str(elem.get_id()),))
        conn.commit()
        cursor.close()
        conn.close()

    def __update(self, idp, p: Product):
        conn = self.connect()
        cursor = conn.cursor()
        sql = ('UPDATE public."Products" SET name= %s,price= %s, provider= %s WHERE id_person= %s')

        cursor.execute(sql, (p.get_name(), p.get_price(), p.get_provider(), idp))
        conn.commit()
        cursor.close()
        conn.close()

    def add(self, product: Product):
        self.__insert(product)
        self.__repo = self.__read()

    def delete(self, product: Product):
        self.__delete(product)
        self.__repo = self.__read()

    def update(self, idc, product: Product):
        self.__update(idc, product)
        self.__repo = self.__read()

    def find_by_id(self, idc):
        conn = self.connect()
        cursor = conn.cursor()
        sql = ('SELECT idProduct, name, price, provider FROM public."Products" WHERE id_person= %s LIMIT 1; ')

        cursor.execute(sql, (str(idc),))
        elem = cursor.fetchone()
        if elem is None:
            return None
        else:
            return (Product(elem[0], elem[1], elem[2], elem[3], ))

    def get_all(self):
        return self.__repo

    def size(self):
        return len(self.__repo)
