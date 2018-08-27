import xlrd
import pymongo
import json

datafile="D:\MIP\Manchester-housing.xlsx"
def parseFile(datafile):
    workbook=xlrd.open_workbook(datafile)
    sheet=workbook.sheet_by_name("Sheet1")

    data=[[sheet.cell_value(r,col)
            for col in range(sheet.ncols)]
                for r in range(sheet.nrows)]
    return data

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["MIP"]
    data=parseFile(datafile)
    json_string = json.dumps(data)
    print(json_string)
    #mycol.collection.insert_one(json_string)
except mydb.error as e:
    mycol.rollback()
    raise
finally:
    myclient.close()