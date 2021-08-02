#install the driver for MS SQL server "pyodbc"
# pip install pyodbc

import pyodbc

#IMPORT library 'pyodbc' and setup connecting using function pyodbc connect
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=************;DATABASE=Demo;Trusted_Connection=yes')
#Here we are connecting with
#Database -  Demo
#Authentication - Windows

#Pull the data in cursor object.in the outupt you can see object created
cursor = conn.cursor()
cursor.execute('select * from emp2')


#print data on screeen
for row in cursor:
    print(row)