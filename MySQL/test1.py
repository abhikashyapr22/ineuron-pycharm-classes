import mysql.connector as connection


try:
    mydb = connection.connect(host="localhost",user="root",passwd="*********",use_pure=True)

    # check if the connection is established
    query = "show databases"

    cursor = mydb.cursor()    # create cursor to execute to queries
    cursor.execute(query)
    print(cursor.fetchall())

    cursor.execute("create table mysql_python.Company_emp_Info (EmpID int, EmpName varchar(20), surname varchar(20),Salary int)")

except Exception as e:
    mydb.close()
    print(str(e))
