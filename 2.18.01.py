# MySQL数据库的基本操作

import mysql.connector
from mysql.connector import errors

user='python'
passwd='Python@2017'
database='testDB'

DB_NAME='testDB'
tablename='employees'
TABLES={}
TABLES[tablename] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

# 建立连接
try:
	cnx=mysql.connector.connect(user=user,password=passwd,database=database)
except errors.Error as err:
	print("Connetion errors have done {}".format(err))
finally:
	cursor = cnx.cursor()

'''
try:
	cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)))
except errors.Error as err:
	print('Creation database errors have done {}'.format(err))
'''

# 创建表格
try:
	cursor.execute(TABLES[tablename])
except errors.Error as err:
	print('Creation table errors have done {}'.format(err))

# 插入数据
add_employee=("INSERT INTO employees "
				"(first_name, last_name, hire_date, gender, birth_date) "
				"VALUES (%s, %s, %s, %s, %s)")
data_employee=('Geert','Vanderkelen','2017-02-19','M','2017-01-01')
cursor.execute(add_employee,data_employee)
cnx.commit()

# 执行查询|--------
#cursor.execute('SELECT * FROM {}'.format(tablename))
cursor.execute('SELECT * FROM {} WHERE emp_no = %s'.format(tablename), ('1',))

# 获取查询结果
values = cursor.fetchall()
print(values)

# 删除表格
cursor.execute('DROP TABLE {}'.format(tablename))

cursor.close()
cnx.close()
