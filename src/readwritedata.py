import dateutil

import src.config as cfg
import pandas as pd

class readwritedata:
    
    def generate_csv(filelocation):
        data = pd.read_csv(filelocation)
        data.shape
        data = data.dropna()
        data['datetime'] = data['datetime'].apply(dateutil.parser.parse, dayfirst=True)
        data['datetime'] = data['datetime'].dt.date
        data = data.groupby(['datetime']).agg({"ds":"first", "Year":"first", "Vancouver":"sum", "Portland":"sum", "San Francisco":"sum", "Seattle":"sum"})
        print(data)
        data.to_csv(cfg.csvactualfile_location, index=False)
    
    try:
        generate_csv(cfg.csvrawfile_location)
    except :
        print("Exception")
        raise
    finally:
        print("final")