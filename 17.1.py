'''

Author: Hafsa Aman
This is a demonstration of exercise 17.1

'''

import sqlite3
connection = sqlite3.connect('books.db')
import pandas as pd
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM titles', connection)

df = pd.read_sql('SELECT * FROM author_ISBN', connection)
df.head()

pd.read_sql('SELECT first, last FROM authors', connection)

pd.read_sql("""SELECT isbn, title, edition, copyright
            FROM titles
            WHERE title LIKE '%How to Program'
            ORDER BY title""" , connection)

pd.read_sql("""SELECT first, last, isbn
            FROM authors
            INNER JOIN author_ISBN
                ON authors.id = author_ISBN.id
            ORDER BY last, first""" , connection).head()
