import sqlite3
conn = sqlite3.connect('./stock.db')
sql = """
    INSERT INTO  stocks VALUES (?, ?,?);
     """
# sql = """
#     INSERT INTO  stocks VALUES (:code, :nm,:price);
#      """
list = [['1','a기업',100]
        ,['1','a기업',100]
        ,['1','a기업',100]]

cur = conn.cursor()
# cur.execute(sql, {'code':1001,'nm':'구글','price':9})
cur.executemany(sql, list)
conn.commit()
cur.close()
conn.close()
