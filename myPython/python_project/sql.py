import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root',
db='my_test')
cur = conn.cursor()
cur.execute("SELECT * FROM users")
for r in cur.fetchall():
           print(r)
conn.close()