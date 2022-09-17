#"""https://docs.google.com/document/d/18CC8vSvQNHZ7iI7gTbKbBJdGCY2dVNjZ/edit 'Shankar22@'"""
import mysql.connector as connection

mydb=  connection.connect(host ="localhost", user = "root", passwd  = "Shankar22@")

print(mydb)
cursor = mydb.cursor()
#cursor.execute("create database Darshan")
#cursor.execute("show databases")
cursor.execute("create table Darshan.ineuron(employee_id int (5), Name varchar (100), mail_id varchar(20), sal int (10))")
#print(cursor.fetchall())