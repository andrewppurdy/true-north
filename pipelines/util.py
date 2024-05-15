import os
import petl as etl

#set some directory paths
THIS_DIR = os.path.dirname(__file__)
TOP = os.path.abspath(os.path.join(THIS_DIR, os.pardir))

WDIR = os.path.join(TOP, 'working')
DATA_DIR = os.path.join(TOP, 'src/_data')
METADATA_DIR = os.path.join(TOP, 'metadata')

def etl_load(working, fname):
    '''load `fname`.csv from `working`.'''
    assert fname[-3:] == 'csv', 'Not a csv file'  
    data = etl.fromcsv(os.path.join(working, fname))
    return data

def etl_write(data, path, type='.csv'):
    '''write `data` to a csv (or other if declared) file located at path.'''
    return etl.tocsv(data, f'{path}{type}')