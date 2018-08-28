import csv
import time
import utils as util
import pandas as pd
import config as cfg

try:
    rawdata = pd.read_csv(cfg.csvrawfile_location)
    rawdata.shape
    print ('Validate null cells')
    #header=rawdata.head(0)
    rawdata=rawdata.dropna()
    print ('Store the dataframe as a new CSV')
    #sum = rawdata['Vancouver'] + rawdata['Portland'] + rawdata['San Francisco'] + rawdata['Seattle'] + rawdata['Los Angeles'] + rawdata['San Diego'] + rawdata['Las Vegas'] + rawdata['Phoenix'] + rawdata['Albuquerque'] + rawdata['Denver'] + rawdata['San Antonio'] + rawdata['Dallas'] + rawdata['Houston'] + rawdata['Kansas City'] + rawdata['Minneapolis'] + rawdata['Saint Louis'] + rawdata['Chicago'] + rawdata['Nashville'] + rawdata['Indianapolis'] + rawdata['Atlanta'] + rawdata['Detroit'] + rawdata['Jacksonville'] + rawdata['Charlotte'] + rawdata['Miami'] + rawdata['Pittsburgh'] + rawdata['Toronto'] + rawdata['Philadelphia'] + rawdata['New York'] + rawdata['Montreal'] + rawdata['Boston'] + rawdata['Beersheba'] + rawdata['Tel Aviv District'] + rawdata['Eilat'] + rawdata['Haifa'] + rawdata['Nahariyya'] + rawdata['Jerusalem']
    rawdata.insert(39,'toTotaltalcount',util.addTotal(rawdata))
    rawdata.to_csv(cfg.csvactualfile_location,index=False)
    util.print_csv(rawdata)
except:
    print("Exception")
    raise
finally:
    print("final")