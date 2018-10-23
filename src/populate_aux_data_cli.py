from argparse import ArgumentParser

from delib.source import CsvFileSource
from delib.store import MongoStore

from data_engineering.cli.constants import (DATABASE_URL, DATABASE_NAME, AUX_DATA_COLLECTION)


parser = ArgumentParser()
parser.add_argument('--bau_q3f_file', type=str,
                    help='Absolute path Bau q3f mapping file')
parser.add_argument('----vdn_file=/ingestion-data/vdn.csv', type=str,
                    help='Absolute path to outages mapping file')

args = parser.parse_args()

vdn_file_path = args.vdn_file
outages_file_path = args.outages_file

vdn_source = CsvFileSource(vdn_file_path)
outages_source = CsvFileSource(outages_file_path)

vdn = {'name': 'vdn', 'data': vdn_source.run_raw_query(None)}
outages = {'name': 'outages', 'data': outages_source.run_raw_query(None)}

db = MongoStore(url=DATABASE_URL, database=DATABASE_NAME)

db.put(AUX_DATA_COLLECTION, (vdn, outages))
