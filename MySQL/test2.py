import mysql.connector as conn

mydb = conn.connect(host = "localhost", user= "root", passwd="**********")
cursor = mydb.cursor()

# cursor.execute("create database mysql_python")
#
# cursor.execute("show databases")
# print(cursor.fetchall())
# cursor.execute("use mysql_python ")
#cursor.execute("create table mysql_python.Company_emp_Info (EmpID int, EmpName varchar(20), surname varchar(20),Salary int)")

cursor.execute("select * mysql_python.Company_emp_Info")
#print(cursor.fetchall())
