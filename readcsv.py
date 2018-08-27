import csv
import pymongo

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["MIP"]
    with open('D:\MIP\Manchester-housing.xlsx') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            x=mycol.insert_one(row)
            print(row)
except mydb.error as e:
    mycol.rollback()
    raise
finally:
    myclient.close()
    csvfile.close()