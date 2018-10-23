import pytest
from src.readwritedata import readwritedata
import src.config as config

def test_one():
     assert 1

def test_generate_csv():
    assert readwritedata.generate_csv('D:/GitLloyds/Python/python-app2/src/raw.csv')