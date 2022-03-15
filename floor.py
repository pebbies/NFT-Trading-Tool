import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 as sq
import csv

frame1 = pd.read_csv("C:\\Users\\Stone\\Desktop\\ojbk_2\\nft_stats.txt")
#watch_list = frame1.to_csv("C:\\Users\\Stone\\Desktop\\ojbk_2\\watchlist.csv", mode = 'a', header = False)

conn = sq.connect("C:\\Users\\Stone\\Desktop\\nft_database\\nft_database.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS nft (project_name, date, floor_price);")
conn.commit()

with open("C:\\Users\\Stone\\Desktop\\ojbk_2\\watchlist.csv", "r") as r:
    data = csv.DictReader(r)
    to_db = [(i['project_name'], i['date'], i['floor_price']) for i in data]

c.executemany("INSERT INTO t (project_name, date, floor_price) VALUES (?, ?, ?);", to_db)
conn.commit()
conn.close()






