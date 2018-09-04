import sqlite3
from contextlib import contextmanager
import sys

DB = "Inventory.db"

def first_launch():
    try:
        conn = sqlite3.connect(DB)
    except:
        sys.exit("Error")


@contextmanager
def access_db():
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()

