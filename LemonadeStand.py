# Author: Adam Osman
# GitHub: adam-oz
# Date: 04/24/2026
# Description: Tracks menu items and sales for a lemonade stand


class DuplicateMenuItemError(Exception):
    pass


class MissingMenuItemError(Exception):
    pass


class MenuItem:
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        return self._name

    def get_wholesale_cost(self):
        return self._wholesale_cost

    def get_selling_price(self):
        return self._selling_price


class LemonadeStand:
    def __init__(self, name):
        self._name = name
        self._menu = {}
        self._sales = {}

    def get_name(self):
        return self._name

    def add_menu_item(self, item):
        name = item.get_name()

        if name in self._menu:
            raise DuplicateMenuItemError

        self._menu[name] = item
        self._sales[name] = 0

    def enter_sales(self, item_name, amount):
        if item_name not in self._menu:
            raise MissingMenuItemError

        self._sales[item_name] += amount

    def number_of_item_sold(self, item_name):
        if item_name not in self._menu:
            raise MissingMenuItemError

        return self._sales[item_name]

    def profit_margin_for_item(self, item_name):
        if item_name not in self._menu:
            raise MissingMenuItemError

        item = self._menu[item_name]
        return item.get_selling_price() - item.get_wholesale_cost()

    def total_profit_for_stand(self):
        total = 0

        for name in self._menu:
            margin = self.profit_margin_for_item(name)
            sold = self.number_of_item_sold(name)
            total += margin * sold

        return total


def main():
    stand = LemonadeStand("Lemons R Us")

    lemonade = MenuItem("lemonade", 0.5, 1.5)
    cookie = MenuItem("cookie", 0.8, 1.7)

    stand.add_menu_item(lemonade)
    stand.add_menu_item(cookie)

    try:
        # not on menu → should raise exception
        stand.enter_sales("pancake", 4)
    except MissingMenuItemError:
        print("Tried to record sales for something not on the menu.")

    stand.enter_sales("lemonade", 12)
    stand.enter_sales("cookie", 6)

    print("Total profit:", stand.total_profit_for_stand())


if __name__ == "__main__":
    main()
