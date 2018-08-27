import xlrd
import json
import cx_Oracle
import csv
connstr='travelLink/travelLink@localhost:1521/xe'
datafile="D:\MIP\Manchester-housing.xlsx"
def parseFile(datafile):
    workbook=xlrd.open_workbook(datafile)
    sheet=workbook.sheet_by_name("Sheet1")

    data=[[sheet.cell_value(r,col)
            for col in range(sheet.ncols)]
                for r in range(sheet.nrows)]
    return data

try:
    conn = cx_Oracle.connect(connstr)
    curs=conn.cursor()
    curs.arraysize=50
    data=parseFile(datafile)
    json_string = json.dumps(data)
    name='Bhai'
    curs.prepare( 'INSERT INTO MIP_DATA (name, data) VALUES ( :name,:data )' )
    curs.execute(None, {'name':name,'data':json_string})
    conn.commit()
except:
    # mycol.rollback()
    raise
finally:
    curs.close()