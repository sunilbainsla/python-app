import csv
import time

import config as cfg

try:
   with open(cfg.csvrawfile_location) as csvfile:
        reader = csv.DictReader(csvfile)
        #for i, row in reader:
        for i, row in enumerate(reader):
            if row["Vancouver"] is None or row["Vancouver"] == "":
                print("12")
            if i<2:
                print(row)
            else:
                break
except:
    csvfile.close()
    raise
finally:
    csvfile.close()