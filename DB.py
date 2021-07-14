if __name__ != '__main__' or __name__ == '__main__':
    import sqlite3 as sql
    DB = sql.connect('shop.db')
    cursor = DB.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS products(ID integer PRIMARY KEY, name Text, price Real, category Text)")


class Product:
    ID = 0
    name = ''
    price = 0.0
    category = ''

    @classmethod
    def addProduct(cls, name, price, cate):
        cls.name = name
        cls.price = price
        cls.category = cate
        cursor.execute(
            f"INSERT INTO products(name, price, category) VALUES ('{cls.name}', {cls.price}, '{cls.category}')")
        DB.commit()

    @classmethod
    def deleteProduct(cls, id):
        cls.ID = id
        cursor.execute(f"DELETE FROM products WHERE ID = {cls.ID}")
        DB.commit()

    @classmethod
    def modifyProduct(cls, id, name, price, cate):
        cls.ID = id
        cls.name = name
        cls.price = price
        cls.category = cate
        cursor.execute(f"UPDATE products set name = '{cls.name}'  where ID = '{cls.ID}'")
        cursor.execute(f"UPDATE products set price = '{cls.price}'  where ID = '{cls.ID}'")
        cursor.execute(f"UPDATE products set category = '{cls.category}'  where ID = '{cls.ID}'")
        DB.commit()

    @classmethod
    def selectPrice(cls, name):
        cls.name = name
        cursor.execute(f"SELECT price FROM products WHERE name = '{cls.name}'")
        result = cursor.fetchone()
        print(f"Price = {result[0]} $")
        return f"Price = {result[0]} $"

    @classmethod
    def showAll(cls):
        cursor.execute("SELECT * FROM products")
        count = 0
        result = cursor.fetchall()
        result2 = ''
        while count != len(result):
            result1 = f"ID: {result[count][0]}\tName: {result[count][1]}\tPrice: {result[count][2]}\tCategory: {result[count][3]}\n"
            result2 += result1
            count += 1
        return result2

    @classmethod
    def showAProduct(cls, ID):
        cls.ID = ID
        cursor.execute(f"SELECT * FROM products WHERE ID = {cls.ID}")
        result = cursor.fetchone()
        return f"ID: {result[0]}  Name: {result[1]}  Price: {result[2]} "

    @classmethod
    def showProductID(cls, name):
        cls.name = name
        cursor.execute(f"SELECT ID FROM products WHERE name = '{cls.name}'")
        result = cursor.fetchone()
        return f"Product ID is: {result[0]}"

    @classmethod
    def showAllNames(cls, cate):
        cls.category = cate
        cursor.execute(f"SELECT name FROM products WHERE category = '{cls.category}'")
        result = cursor.fetchall()
        re = []
        cont = 0
        for i in result:
            re += result[cont]
            cont += 1
        return re

    @classmethod
    def saveClose(cls):
        DB.commit()
        DB.close()
