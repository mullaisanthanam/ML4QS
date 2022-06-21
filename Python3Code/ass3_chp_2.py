# Import the relevant classes.
from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
from datetime import datetime
from util import util
from pathlib import Path
import copy
import os
import sys
import calendar
import pandas as pd

# Chapter 2: Initial exploration of the dataset.

DATASET_PATH = Path('./datasets/ass3_datasets')
RESULT_PATH = Path('./intermediate_datafiles/assigment_3')
RESULT_FNAME = 'ass3_chp2_result.csv'

GRANULARITIES = [50000, 80000]


# We can call Path.mkdir(exist_ok=True) to make any required directories if they don't already exist.
[path.mkdir(exist_ok=True, parents=True) for path in [DATASET_PATH, RESULT_PATH]]

print('Please wait, this will take a while to run!')


# def add_timestamp(file, col_name):
#     #     print('Reading data from test')
#     file = 'reduced_glasses.csv'
#     data =  (pd.read_csv(DATASET_PATH / file, skipinitialspace=True))
    # timestamp = datetime.timestamp(currentDateTime)

    # dataNew = pd.read_csv(DATASET_PATH/ file, skipinitialspace=True)
#     print(data['system time'][0])
    # data['timestamp'] = []
#     for i in range(len(data['DATE'])):
#         strdate = data.iat[i, 1]
#         # dt_tuple = tuple([str(x) for x in strdate[:19].split('.')])
#         # date_final = dt_tuple[0]
#         # dt=datetime.strptime(date_final, '%y/%m/%d %H:%M:%S')
#         dt_tuple=tuple([int(x) for x in strdate[:10].split('/')])+tuple([int(x) for x in strdate[11:18].split(':')])
#         print(dt_tuple)
#         # d = datetime(dt_tuple)
#         # ttuple = d.timetuple()
#         itimestamp = calendar.timegm(dt_tuple)
#         data.at[i, 12] =1000000000*(itimestamp)
#         # data.at[i, 12] =1000000000*(datetime.timestamp(dt))
#     #    data['timestamp'].append(timestamp)
#     return data
# def add_timestamp(file, col_name):
#     print('Reading data from test')
#     timeFile = 'labels.csv'
#     dataNew =  (pd.read_csv(DATASET_PATH / timeFile, skipinitialspace=True))
#     # print(data['system time'][0])
#     dataNew['label_start'] =1000000000*(dataNew['label_start'])
#     dataNew['label_end'] =1000000000*(dataNew['label_end'])
#     return dataNew
# new_acc = add_timestamp('labels.csv', 'time')
# new_acc.to_csv(DATASET_PATH / 'formatted_labels.csv')

datasets = []
for milliseconds_per_instance in GRANULARITIES:
    print(f'Creating numerical datasets from files in {DATASET_PATH} using granularity {milliseconds_per_instance}.')

    # Create an initial dataset object with the base directory for our data and a granularity
    dataset = CreateDataset(DATASET_PATH, milliseconds_per_instance)

    dataset.add_numerical_dataset('formatted_glasses_dataset.csv', 'timestamp', ['ACC_X','ACC_Y','ACC_Z', 'GYRO_X', 'GYRO_Y', 'GYRO_Z',
     'EOG_L', 'EOG_R', 'EOG_H', 'EOG_V'],
     'avg', 'glasses_')
    
    # Add the selected measurements to it.

    # We add the accelerometer data (continuous numerical measurements) of the phone and the smartwatch
    # and aggregate the values per timestep by averaging the values
    
    dataset.add_event_dataset('formatted_labels.csv', 'label_start', 'label_end', 'label', 'binary')

    # Get the resulting pandas data table
    dataset = dataset.data_table

    # Plot the data
    DataViz = VisualizeDataset(__file__)

    # # Boxplot
    DataViz.plot_dataset_boxplot(dataset, ['glasses_GYRO_X','glasses_GYRO_Y','glasses_GYRO_Z'])

    util.print_statistics(dataset)
    datasets.append(copy.deepcopy(dataset))

# Make a table like the one shown in the book, comparing the two datasets produced.
util.print_latex_table_statistics_two_datasets(datasets[0], datasets[1])

# Finally, store the last dataset we generated (250 ms).
dataset.to_csv(RESULT_PATH / RESULT_FNAME)

# Lastly, print a statement to know the code went through

print('The code has run through successfully!')

