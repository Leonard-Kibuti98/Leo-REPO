import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',db='general',password='')
if(mydb):
	print('connection successfull')
else:
	print('connection unsuccessfull')