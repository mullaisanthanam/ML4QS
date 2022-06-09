# Import the relevant classes.
from Chapter2.CreateDataset import CreateDataset
from util.VisualizeDataset import VisualizeDataset
from util import util
from pathlib import Path
import copy
import os
import sys

import pandas as pd

# Chapter 2: Initial exploration of the dataset.

DATASET_PATH = Path('./datasets/')
RESULT_PATH = Path('./intermediate_datafiles/')
RESULT_FNAME = 'chapter2_result_new.csv'

GRANULARITIES = [60000, 250]

# We can call Path.mkdir(exist_ok=True) to make any required directories if they don't already exist.
[path.mkdir(exist_ok=True, parents=True) for path in [DATASET_PATH, RESULT_PATH]]

print('Please wait, this will take a while to run!')

# seconds to timestamp conversion
# def add_timestamp(file, col_name):
#     print('Reading data from test')
#     timeFile = 'time.csv'
#     data =  (pd.read_csv(DATASET_PATH / timeFile, skipinitialspace=True))
    # dataNew = pd.read_csv(DATASET_PATH/ file, skipinitialspace=True)
#     print(data['system time'][0])
#     dataNew['label_start'] =1000000000*(dataNew['label_start'])
#     dataNew['label_end'] =1000000000*(dataNew['label_end'])
#     return dataNew

# new_acc = add_timestamp('labels.csv', 'time')
# new_acc.to_csv(DATASET_PATH / 'formatted_labels.csv')
# new_acc = add_timestamp('Gyroscope.csv', 'time')
# new_acc.to_csv(DATASET_PATH / 'formatted_gyroscope.csv')
# new_acc = add_timestamp('Light.csv', 'time')
# new_acc.to_csv(DATASET_PATH / 'formatted_light.csv')
# new_acc = add_timestamp('Location.csv', 'time')
# new_acc.to_csv(DATASET_PATH / 'formatted_location.csv')

datasets = []
for milliseconds_per_instance in GRANULARITIES:
    print(f'Creating numerical datasets from files in {DATASET_PATH} using granularity {milliseconds_per_instance}.')

    # Create an initial dataset object with the base directory for our data and a granularity
    dataset = CreateDataset(DATASET_PATH, milliseconds_per_instance)

    # Add the selected measurements to it.

    # We add the accelerometer data (continuous numerical measurements) of the phone and the smartwatch
    # and aggregate the values per timestep by averaging the values
    dataset.add_numerical_dataset('formatted_accelerometer.csv', 'timestamp', ['x','y','z'], 'avg', 'acc_phone_')
    dataset.add_numerical_dataset('formatted_gyroscope.csv', 'timestamp', ['x','y','z'], 'avg', 'gyr_phone_')
    dataset.add_numerical_dataset('formatted_light.csv', 'timestamp', ['lux'], 'avg', 'light_phone_')
    # dataset.add_numerical_dataset('formatted_location.csv', 'timestamp', ['latitude','longitude','speed'], 'avg', 'location_phone_')
    
    dataset.add_event_dataset('formatted_labels.csv', 'label_start', 'label_end', 'label', 'binary')

    # Get the resulting pandas data table
    dataset = dataset.data_table

    # Plot the data
    # DataViz = VisualizeDataset(__file__)

    # # Boxplot
    # DataViz.plot_dataset_boxplot(dataset, ['acc_phone_x','acc_phone_y','acc_phone_z'])

    util.print_statistics(dataset)
    datasets.append(copy.deepcopy(dataset))

# Make a table like the one shown in the book, comparing the two datasets produced.
util.print_latex_table_statistics_two_datasets(datasets[0], datasets[1])

# Finally, store the last dataset we generated (250 ms).
dataset.to_csv(RESULT_PATH / RESULT_FNAME)

# Lastly, print a statement to know the code went through

print('The code has run through successfully!')
