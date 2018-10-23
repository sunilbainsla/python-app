from argparse import ArgumentParser
import xlrd
from openpyxl import load_workbook
import pandas as pd
import json
from delib.source import CsvFileSource
from delib.store import MongoStore
from delib.store.database_store import Index
from data_engineering.cli.constants import (DATABASE_URL, DATABASE_NAME, BAU_Q3F_AHT_FRAUD)

def parseFile(datafile,db):
    datasheets = pd.ExcelFile(datafile)
    
    bau_sheets = []
    for sheet in datasheets.sheet_names:
        bau_sheets.append(datasheets.parse(sheet))
        print(bau_sheets)
        print("\n")
    db.create(BAU_Q3F_AHT_FRAUD)
    db.create_index(BAU_Q3F_AHT_FRAUD, '_hash', Index.TEXT)
    db.create_index(BAU_Q3F_AHT_FRAUD, 'date', Index.ASCENDING)
    db.create_index(BAU_Q3F_AHT_FRAUD, 'created_at', Index.ASCENDING)
    db.create_index(BAU_Q3F_AHT_FRAUD, 'updated_at', Index.ASCENDING)
    data = pd.concat(bau_sheets)
    data.dropna(thresh = 1)
    ahtdata = {'name': 'AHT', 'data': data}
    db.put(BAU_Q3F_AHT_FRAUD, (ahtdata))
    print(data)
  

dataFile = pd.ExcelFile("D:/GitLloyds/Python/mm-wp-dataengineering/Forecasts.xlsx")
db = MongoStore(url='localhost:27017', database='wfp')
parseFile(dataFile,db)


