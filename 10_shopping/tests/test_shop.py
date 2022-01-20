import unittest
from shop.shop_basket import ShopBasket


class TestShopBasketEmpty(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[INFO] Basket without any product")
        cls.basket = ShopBasket()

    @classmethod
    def tearDownClass(cls):
        print("tearing down class")
        del cls.basket

    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(self.basket.basket_total(), 0)

    def test_product_index_out_of_range_raise_error(self):
        self.assertRaises(IndexError, self.basket.product_idx, 0)

    def test_summary_should_be_zero(self):
        self.assertEqual(self.basket.summary(), 0)


class TestShopBasketWithOneProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[INFO] Basket with one product")
        cls.basket = ShopBasket().product_add('milk', 3.0)

    @classmethod
    def tearDownClass(cls):
        print("tearing down class")
        del cls.basket

    def test_size_of_basket_should_be_one(self):
        self.assertEqual(self.basket.basket_total(), 1)

    def test_summary_should_have_tax(self):
        self.assertEqual(self.basket.summary(), 3.63)

    def test_product(self):
        self.assertEqual(self.basket.product_idx(0).name, 'milk')

    def test_product_index_out_of_range_raise_error(self):
        self.assertRaises(IndexError, self.basket.product_idx, 1)


class TestShopBasketWithTwoProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[INFO] Basket with two product")
        cls.basket = ShopBasket() \
            .product_add('milk', 1.0) \
            .product_add('cola', 2.0)

    @classmethod
    def tearDownClass(cls):
        print("tearing down class")
        del cls.basket

    def test_size_of_basket_should_be_two(self):
        self.assertEqual(self.basket.basket_total(), 2)

    def test_order_of_products(self):
        self.assertEqual(self.basket.product_idx(1).name, 'cola')
        self.assertEqual(self.basket.product_idx(0).price, 1.0)

    def test_summary_should_have_tax(self):
        self.assertEqual(self.basket.summary(), 3.63)

    def test_product_index_out_of_range_raise_error(self):
        self.assertRaises(IndexError, self.basket.product_idx, 3)
