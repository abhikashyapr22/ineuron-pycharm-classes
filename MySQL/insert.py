import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root",passwd="Abhishek@1067")
cursor = mydb.cursor()
cursor.execute("insert into mysql_python.company_emp_info values(1, 'Abhishek', 'Kumar', 800000)")
mydb.commit()

cursor.execute("select * from mysql_python.company_emp_info")
#print(cursor.fetchall())

for i in cursor.fetchall():
    print(i)