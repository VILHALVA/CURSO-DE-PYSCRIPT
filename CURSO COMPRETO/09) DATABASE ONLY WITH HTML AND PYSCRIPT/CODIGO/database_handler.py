import sqlite3
from js import console
conn = sqlite3.connect('database.db')

def create(*args, **kwargs):
    conn.execute('''CREATE TABLE items
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ietm_name           TEXT    NOT NULL,
    quantity            INT     NOT NULL)''')
    

def insert(*args, **kwargs):
    item = Element('item').element.value
    quantity = Element('quantity').element.value
    conn.execute("INSERT INTO items (ietm_name, quantity) VALUES ('{}', {})".format(item, quantity))
    console.log("Inserting data...")

def fetch(*args, **kwargs):
    cursor = conn.execute("SELECT id, ietm_name, quantity from items")
    for row in cursor:
        console.log(row[0], row[1], row[2])