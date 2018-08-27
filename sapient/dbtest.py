import cx_Oracle
import csv
connstr='travelLink/travelLink@localhost:1521/xe'
conn = cx_Oracle.connect(connstr)
print(conn)
curs = conn.cursor()
curs.arraysize=50
curs.execute('SELECT first_name, last_name,mark from student where MARK >= 70 order by MARK desc')

results = curs.fetchall() 
with open('data.csv','w',newline='') as csvfile:
	a=csv.writer(csvfile,delimiter=',')
	a.writerows(results)
	print(results)
	print(curs.rowcount, "record(s) found")
	"""This is a 
multiline docstring."""
csvfile.close()
curs.close()
conn.close()