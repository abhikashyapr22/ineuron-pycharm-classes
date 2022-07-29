import csv

import mysql.connector as conn

# mydb = conn.connect(host="localhost", user="root", passwd="Abhishek@1067")
# cursor = mydb.cursor()


class MySQL_API:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.mydb = conn.connect(host="localhost", user=self.user, passwd=self.password)
        self.cursor = self.mydb.cursor()

    def get_cursor(self):
        if self.mydb:
            print('Connection is ok')
            cur = self.mydb.cursor()
            return cur

    def check_connection(self):
        if self.mydb:
            print("Connection is live")
        else:
            print("Connection is not live")

    def ddl(self, operation):
        """
        1 - check connection ?
        operation = [create database, create table, alter table, drop table
        :param operation:
        :return:
        """
        if self.mydb:
            try:
                self.check_connection()
            except Exception as e:
                print('Not connected to mysql server', e)

    def dml(self, operation):
        '''
        oprations = [insert, upadte, delete]
        :param operation:
        :return:
        '''

    def dql(self, query):
        """

        :param query:
        :return:
        """
        if self.mydb:
            self.cursor.execute(f"{query}")
            return self.cursor.fetchall()
        else:
            print("connection is not live")

    def save_query(self, file_name, records):
        try:
            with open(f"{file_name}.txt", "w") as f:
                write = csv.writer(f)
                write.writerows(records)
        except Exception as e:
            print(e)

