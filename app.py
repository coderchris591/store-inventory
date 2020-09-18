from collections import OrderedDict
from peewee import *
import csv
import datetime

db = SqliteDatabase("inventory.db")

class Product(Model):
    #Creates an auto-incremeting integer primary key.
    product_id = AutoField()

    product_name = CharField(max_length=200, unique = True)

    product_quantity = IntegerField(default=0)

    product_price = IntegerField(default=0)

    date_updated = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the database and the tables."""
    db.connect()
    db.create_tables([Product], safe = True)


def read_csv ():
    with open('inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        product_dicts = list(reader)
        for product in product_dicts:
            Product.create(
                product_name = product['product_name'])


def menu():
    """Displays menu options"""
    pass

def display_product():
    """Displays products by its product_id"""
    pass

def add_product():
    """Adds product to the database"""
    pass

def backup():
    """Creates a backup database"""
    pass

menu = OrderedDict ([
        ('v', 'display_product'),
        ('a', 'add_product'),
        ('b', 'backup')
])

if __name__ == '__main__':
    initialize()
    read_csv()
