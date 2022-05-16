'''

Author: Hafsa Aman
This is a demonstration of exercise 17.2

'''

import sqlite3
connection = sqlite3.connect('books.db')
import pandas as pd
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM titles', connection)
