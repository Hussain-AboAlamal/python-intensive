"""
In this exercise, we are going to generate data and collect statistics about it.
1. Generate 75_000 items of Product, but add ability to specify any number of items to generate. For the price use random range from 0.10 to 2.15
2. Print statistics of average price per Product. Print in a table format, for example:
+-------+--------------+
Product | AveragePrice
+-------+--------------+
Tomato  | 0.75
Potato  | 0.12
Cucumber| 1.23
Pumkin  | 2.01
Corn    | 0.16
+-------+--------------+
Try to search a package, that can make your table look great. Remember to create requirements.txt for it
4. You code must be efficent as much as it can be, think about the RAM usage
5. Document your code with docstrings (module, classes and functions)
"""
from dataclasses import dataclass
from enum import IntEnum
from random import choice, uniform, random
import sys
from typing import Generator

from prettytable import PrettyTable


DECIMALS = 2


class Vegetable(IntEnum):
    Tomato = 1
    Potato = 2
    Cucumber = 3
    Pumkin = 4
    Corn = 5

@dataclass
class Product:
    product_id: int
    product_type: Vegetable
    product_price: float


def generate_random_product(id: int) -> Product:
    """Create a Product instance with random data

    Args:
        id (int): id of the instance

    Returns:
        Product: new instance with random data
    """

    vegs = [Vegetable.Tomato, Vegetable.Potato, Vegetable.Cucumber, Vegetable.Pumkin, Vegetable.Corn]

    type = choice(vegs)
    price = round(uniform(0.10, 2.15), DECIMALS)

    return Product(product_id=id, product_type=type, product_price=price)

class MyProductIterator:

    def __init__(self, end:int, step:int = 1):
        self.value = 1
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        result = generate_random_product(self.value)
        self.value += self.step
        return result

def generate_rows(data: dict[dict]) -> 'Generator[list[any]]':
    """Generate table rows to print from stats

    Args:
        data (dict[dict]): products statistics

    Yields:
        Generator[list[any]]: table body row
    """

    for key in data:
        stat = data[key]
        product_name = Vegetable(key).name
        avg_price = round(stat['price_sum'] / stat['count'], DECIMALS)
        row = [product_name, avg_price]
        yield row


def print_table(header: list[str], body: 'Generator[list[any]]') -> None:
    """Print stats table to console

    Args:
        header (list[str]): table header row
        body (Generator[list[any]]): table body rows
    """

    my_table = PrettyTable()

    my_table.field_names = header

    for row in body:
        my_table.add_row(row)
    
    print(my_table)


if __name__ == "__main__":
    # get input from console
    n = input("Please enter the number of products: ")
    # check that user has inserted a valid integer
    try:
        n = int(n)
        if n < 1 :
            print("number should be gretaer than or equal 1.")
            sys.exit(1)
    except ValueError:
        print(f"{n} is not a valid integer. Please try again.")
        sys.exit(1)

    my_itr = MyProductIterator(n)
    stats = {}

    # generate random products
    for item in my_itr:
        stat = stats.get(item.product_type)
        if stat:
            # if product type is already exist then increment count and price sum
            stat['count'] += 1
            stat['price_sum'] = round(stat['price_sum'] + item.product_price, DECIMALS)
        else:
            # if product is already exists then initialize the stat
            stats[item.product_type] = {
                'count': 1,
                'price_sum': item.product_price,
            }
    
    # print stats table to consoles
    header = ['Product', 'AveragePrice']
    body = generate_rows(stats)
    print_table(header, body)
