# Author: Adam Osman
# GitHub username: adam-oz
# Date: 04/24/2026
# Description: Tracks items, sales, and profit.


class DuplicateMenuItemError(Exception):
    """Error if item already exists."""
    pass


class MissingMenuItemError(Exception):
    """Error if item not found."""
    pass


class MenuItem:
    """Represents one menu item."""

    def __init__(self, name, wholesale_cost, selling_price):
        """Sets up the item."""
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Returns the name."""
        name = self._name
        return name

    def get_wholesale_cost(self):
        """Returns the cost."""
        cost = self._wholesale_cost
        return cost

    def get_selling_price(self):
        """Returns the price."""
        price = self._selling_price
        return price


class LemonadeStand:
    """Represents the stand."""

    def __init__(self, name):
        """Sets up the stand."""
        self._name = name

        menu_dictionary = {}
        self._menu = menu_dictionary

        sales_dictionary = {}
        self._sales_record = sales_dictionary

    def get_name(self):
        """Returns the stand name."""
        stand_name = self._name
        return stand_name

    def add_menu_item(self, menu_item):
        """Adds an item."""
        item_name = menu_item.get_name()

        if item_name in self._menu:
            raise DuplicateMenuItemError

        self._menu[item_name] = menu_item

        starting_sales = 0
        self._sales_record[item_name] = starting_sales

    def enter_sales(self, item_name, amount_sold):
        """Adds sales for an item."""
        if item_name not in self._menu:
            raise MissingMenuItemError

        current_sales = self._sales_record[item_name]
        new_sales_total = current_sales + amount_sold
        self._sales_record[item_name] = new_sales_total

    def number_of_item_sold(self, item_name):
        """Returns how many sold."""
        if item_name not in self._menu:
            raise MissingMenuItemError

        number_sold = self._sales_record[item_name]
        return number_sold

    def profit_margin_for_item(self, item_name):
        """Returns profit per item."""
        if item_name not in self._menu:
            raise MissingMenuItemError

        item = self._menu[item_name]

        selling_price = item.get_selling_price()
        wholesale_cost = item.get_wholesale_cost()

        profit_margin = selling_price - wholesale_cost
        return profit_margin

    def total_profit_for_stand(self):
        """Returns total profit."""
        total_profit = 0

        for item_name in self._menu:

            item = self._menu[item_name]

            selling_price = item.get_selling_price()
            wholesale_cost = item.get_wholesale_cost()

            profit_per_item = selling_price - wholesale_cost

            number_sold = self._sales_record[item_name]

            total_for_this_item = profit_per_item * number_sold

            total_profit = total_profit + total_for_this_item

        return total_profit


def main():
    """Example run using TV shows."""
    stand = LemonadeStand("Streaming Stand")

    breaking_bad = MenuItem("Breaking Bad", 5.0, 10.0)
    stranger_things = MenuItem("Stranger Things", 4.0, 9.0)
    the_office = MenuItem("The Office", 3.0, 8.0)

    stand.add_menu_item(breaking_bad)
    stand.add_menu_item(stranger_things)
    stand.add_menu_item(the_office)

    stand.enter_sales("Breaking Bad", 7)
    stand.enter_sales("Stranger Things", 5)
    stand.enter_sales("The Office", 10)

    try:
        stand.enter_sales("Game of Thrones", 3)
    except MissingMenuItemError:
        print("That show is not in the catalog.")

    total_profit = stand.total_profit_for_stand()
    print("Total profit:", total_profit)


if __name__ == "__main__":
    main()