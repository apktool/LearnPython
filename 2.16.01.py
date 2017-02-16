# SQLite

import sqlite3 

conn=sqlite3.connect('test.db')
cursor=conn.cursor()

temp=cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
print(temp)

temp=cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print(temp)

temp=cursor.execute('select * from user where id=?',('1',))
temp=cursor.fetchall()
print(temp)

# 下面这句等价于fetchall
for row in temp:
    print(row)

cursor.close()
conn.close()
