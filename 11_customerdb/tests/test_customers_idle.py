import unittest
import sqlite3
from sqlite3 import connect
#from customer_db import CustomersDB             


class CustomersDB:

    def __init__(self, connection):
        self.connection = connection

    def add_customer(
            self,
            first_name,
            last_name,
            email,
            phone,
            country
    ):
        cursor = self.connection.cursor()
        sql = """
            INSERT INTO customers
            VALUES (:first_name, :last_name, :email, :phone, :country);"""
        cursor.execute(sql, locals())
        self.connection.commit()
        return cursor.lastrowid

    def find_customer_by_first_name(self, first_name):
        cursor = self.connection.cursor()
        sql = """
            SELECT * FROM customers WHERE first_name LIKE :first_name
            ORDER BY first_name, last_name;"""
        cursor.execute(sql, locals())
        for row in cursor:
            yield row

    def find_customer_by_country(self, country):
        cursor = self.connection.cursor()
        sql = """
            SELECT * 
            FROM customers 
            WHERE country LIKE :country
            ORDER BY first_name, last_name;"""
        cursor.execute(sql, locals())
        for row in cursor:
            yield row




class TestCustomersDB(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers
            (
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                phone TEXT,
                country TEXT
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('Jan', 'Nowak', 'jan.nowak@mail.com', '111', 'USA'),
            ('Marcin', 'Kowalski', 'marcin.kowalski@mail.com', '222', 'USA'),
            ('James', 'Bond', 'james.bond@mail.com', '333', 'USA')
        ]

        insert_sql = """INSERT INTO customers VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_add_customer(self):
        # arrange
        db = CustomersDB(self.connection)
        db.add_customer('Jan', 'Chmura', 'jan.chmura@mail.com', '444', 'POL')
        cursor = self.connection.cursor()

        # act
        cursor.execute("""
        SELECT * 
        FROM customers 
        ORDER BY first_name, last_name;
        """)

        # assert

        expected = (
            ('Jan', 'Chmura', 'jan.chmura@mail.com', '444', 'POL'),
            ('Jan', 'Nowak', 'jan.nowak@mail.com', '111', 'USA'),
            ('Marcin', 'Kowalski', 'marcin.kowalski@mail.com', '222', 'USA'),
            ('James', 'Bond', 'james.bond@mail.com', '333', 'USA')
        )
        self.assertEqual(tuple(cursor), tuple(expected))

if __name__ == '__main__':
    unittest.main(verbosity=2)


    # def test_find_customer_by_first_name(self):
    #     pass
    #
    # def test_find_customers_by_country(self):
    #     pass

