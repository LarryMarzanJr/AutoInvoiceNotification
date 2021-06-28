import sqlite3

koneksi = sqlite3.connect('customer.db')

c = koneksi.cursor()

# EXAMPLE FOR CREATING TABLE
# c.execute("""CREATE TABLE customer (
#     id integer,
#     nama text,
#     email text,
#     mobile_phone text,
#     tagihan integer,
#     billing_month text,
#     billing_year integer,
#     sent integer
#     )""")

# EXAMPLE FOR INSERTING DATA INTO TABLE
# c.execute("INSERT INTO customer VALUES (1, 'Jun', 'larry.marzanjr@gmail.com', '+6287846644887', '200000', 'MEI', 2021, 1)")
# c.execute("INSERT INTO customer VALUES (2, 'Jun', 'larry.marzanjr@gmail.com', '+6287846644887', '200000', 'JUNI', 2021, 0)")
# c.execute("INSERT INTO customer VALUES (3, 'Edward', 'edward.marzanjr@gmail.com', '+6282196660447', '200000', 'JUNI', 2021, 0)")
# c.execute("INSERT INTO customer VALUES (4, 'Cici', 'jr.network.tomohon@gmail.com', '+6285398916361', '200000', 'JUNI', 2021, 0)")

# EXAMPLE FOR SELECTING AND VIEWING TABLE DATA
c.execute("SELECT * FROM customer WHERE sent=0")
print(c.fetchall())

koneksi.commit()

koneksi.close()