import unittest
import sqlite3
from sqlite3 import connect
from customers_db.customer_db import CustomersDB


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
        for row in cursor.execute("""SELECT * FROM customers;"""):
            print(row)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_add_customer(self):
        # arrange
        db = CustomersDB(self.connection)
        db.add_customer('James', 'Bond', 'james.bond@mail.com', '444', 'POLSKA')
        cursor = self.connection.cursor()

        # act
        cursor.execute("""
        SELECT *
        FROM customers;
        """)

        # assert
        expected = (
            ('James', 'Bond', 'james.bond@mail.com', '444', 'POLSKA'),
            ('Jan', 'Nowak', 'jan.nowak@mail.com', '111', 'USA'),
            ('Marcin', 'Kowalski', 'marcin.kowalski@mail.com', '222', 'USA'),
            ('James', 'Bond', 'james.bond@mail.com', '333', 'USA')
        )

        self.assertEqual(tuple(cursor), expected)

    def test_find_customer_by_first_name(self):
        # arrange
        db = CustomersDB(self.connection)

        # act
        actual = tuple(db.find_customer_by_first_name('James'))

        # assert
        expected = ('James', 'Bond', 'james.bond@mail.com', '333', 'USA'),

        self.assertEqual(actual, expected)

    def test_find_customers_by_country(self):
        # arrange
        db = CustomersDB(self.connection)

        # act
        actual = tuple(db.find_customer_by_country('USA'))

        # assert

        expected = (
            ('Jan', 'Nowak', 'jan.nowak@mail.com', '111', 'USA'),
            ('Marcin', 'Kowalski', 'marcin.kowalski@mail.com', '222', 'USA'),
            ('James', 'Bond', 'james.bond@mail.com', '333', 'USA')
        )

        self.assertEqual(actual, expected)

#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)