#!/usr/bin/env python
import preprocessing
mysql = {'host': 'localhost',
         'user': 'root',
         'passwd': 'my secret password',
         'db': 'write-math'}
use_anonymous = True
csvrawfile_location='raw.csv'
csvactualfile_location='actual_data.csv'
oracle_constr='travelLink/travelLink@localhost:1521/xe'