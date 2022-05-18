import sqlite3
#conn  = sqlite3.connect(':memory:')#일회성
conn  = sqlite3.connect('stock.db')#해당 위치에 파일로 새성, connection when aleady have file
print(sqlite3.version)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE  stocks (st_code varchar2(10)
                        ,st_nm varchar2(100)
                        ,st_price number)
""")
cur.close()
conn.close()
