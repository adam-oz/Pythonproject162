import unittest
from LemonadeStand import MenuItem, LemonadeStand, DuplicateMenuItemError, MissingMenuItemError


class TestLemonadeStand(unittest.TestCase):

    def setUp(self):
        self.stand = LemonadeStand("Test Stand")
        self.lemonade = MenuItem("lemonade", 0.5, 1.5)
        self.cookie = MenuItem("cookie", 0.2, 1.0)

        self.stand.add_menu_item(self.lemonade)
        self.stand.add_menu_item(self.cookie)

    def test_duplicate_item(self):
        with self.assertRaises(DuplicateMenuItemError):
            self.stand.add_menu_item(self.lemonade)

    def test_sales_update(self):
        self.stand.enter_sales("lemonade", 8)
        self.assertEqual(self.stand.number_of_item_sold("lemonade"), 8)

    def test_missing_item(self):
        with self.assertRaises(MissingMenuItemError):
            self.stand.enter_sales("cake", 2)

    def test_profit_margin(self):
        result = self.stand.profit_margin_for_item("cookie")
        self.assertAlmostEqual(result, 0.8)

    def test_total_profit(self):
        self.stand.enter_sales("lemonade", 10)
        self.stand.enter_sales("cookie", 5)
        self.assertEqual(self.stand.total_profit_for_stand(), 14)


if __name__ == "__main__":
    unittest.main()
