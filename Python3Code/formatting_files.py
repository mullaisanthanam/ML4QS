from util import util
from pathlib import Path
from datetime import datetime
import copy
import os
import sys
import calendar
import pandas as pd


DATASET_PATH = Path('./datasets/ass3_datasets')
RESULT_PATH = Path('./intermediate_datafiles/assigment_3')
RESULT_FNAME = 'new_glasses.csv'


# We can call Path.mkdir(exist_ok=True) to make any required directories if they don't already exist.
[path.mkdir(exist_ok=True, parents=True) for path in [DATASET_PATH, RESULT_PATH]]

print('Please wait, this will take a while to run!')

# file = 'glasses.csv'
# df =  pd.read_csv(DATASET_PATH / file, skipinitialspace=True)
# # 29th and 30th data
# new_result = df.iloc[:1053464]

# new_result.to_csv(RESULT_PATH / RESULT_FNAME)

file = 'ass3_chp2_result.csv'
def add_timestamp():
    print('Reading data from test')
    data =  (pd.read_csv(DATASET_PATH / RESULT_FNAME, skipinitialspace=True))
    for i in range(len(data['DATE'])):
        strdate = data.iat[i, 2]
        print(strdate)
        dt_tuple=tuple([int(x) for x in strdate[:10].split('/')])+tuple([int(x) for x in strdate[11:18].split(':')])+tuple([int(x) for x in strdate[18:].split('.')])
        print(dt_tuple)
        print(dt_tuple[7])
        itimestamp = calendar.timegm(dt_tuple)
        data.at[i, 'timestamp'] =1000000000*(itimestamp+dt_tuple[7])

    return data
# def add_timestamp_label():
#     print('Reading data from test')
#     data =  (pd.read_csv(DATASET_PATH / file, skipinitialspace=True))
#     for i in range(len(data['from'])):
#         strdate = data.iat[i, 4]
#         print(strdate)
#         dt_tuple=tuple([int(x) for x in strdate[:10].split('-')])+tuple([int(x) for x in strdate[11:].split(':')])
#         dt_tuple = dt_tuple + (00,)
#         print(dt_tuple)
#         itimestamp = calendar.timegm(dt_tuple)
#         data.at[i, 'label_start'] =1000000000*(itimestamp)
#     for i in range(len(data['to'])):
#         strdate = data.iat[i, 5]
#         print(strdate)
#         dt_tuple=tuple([int(x) for x in strdate[:10].split('-')])+tuple([int(x) for x in strdate[11:].split(':')])
#         dt_tuple = dt_tuple + (00,)
#         print(dt_tuple)
#         itimestamp = calendar.timegm(dt_tuple)
#         data.at[i, 'label_end'] =1000000000*(itimestamp)
#     return data
# def add_timestamp(col_name):
#     print('Reading data from test')
#     timeFile = 'labels.csv'
#     dataNew =  (pd.read_csv(DATASET_PATH / timeFile, skipinitialspace=True))
#     # print(data['system time'][0])
#     dataNew['label_start'] =1000000000*(dataNew['label_start'])
#     dataNew['label_end'] =1000000000*(dataNew['label_end'])
#     return dataNew
# data =  (pd.read_csv(RESULT_PATH / file, skipinitialspace=True))
# for i in range(len(data))
# data = data.dropna(axis=0)
# print(data.head())
new_data = add_timestamp()
new_data.to_csv(DATASET_PATH / 'formatted_glasses_dataset.csv', index=False)