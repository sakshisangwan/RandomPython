import MySQLdb
cxn = MySQLdb.connect(user='root', passwd='penny123')
# cxn.query('CREATE DATABASE test1')
# cxn.query("GRANT ALL ON test.* to ''@'localhost'")
cxn.commit()
cxn.close()

cxn = MySQLdb.connect(db='test1', user='root', passwd='penny123')
cur = cxn.cursor()
cur.execute('CREATE TABLE users(login VARCHAR(8), userid INT)')

cur.execute("INSERT INTO users VALUES('john', 7000)")
cur.execute("INSERT INTO users VALUES('jane', 7001)")
cur.execute("INSERT INTO users VALUES('bob', 7002)")

cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")

for data in cur.fetchall():
	print '%s\t%s' % data