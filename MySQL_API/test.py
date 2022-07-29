import csv

from app import MySQL_API


mysql_ob = MySQL_API('root', 'Abhishek@1067')

# cursor = mysql_ob.get_cursor()
# cursor.execute("show databases")
# print(cursor.fetchall())

mysql_ob.dql("use classicmodels")

records2 = mysql_ob.dql("select * from customers")
# for i in records:
#     print(i)

mysql_ob.save_query('records2', records2)

# with open("records.txt", 'w') as f:
#     write = csv.writer(f)
#     write.writerows(records)

#mysql_ob.check_connection()


