# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import argparse
import sys
import pandas as pd
from time import sleep
import numpy as np


init()


columns = []


def read_input_path(input_path):
    """
    This function reads the input path and returns the nature of the data
    """
    print(f"READING {input_path} ...")

    data_frame = pd.read_csv(input_path, low_memory=False)
    sleep(2)
    count = 0
    for column in data_frame:

        columns.append(column)
        count += 1

    print(f"\nFOUND {count} columns in the dataset.")
    print(f"Dataframe shape: {data_frame.shape}")
    print("Done")

    print(
        f"\nThe following are the data types for each of the columns:\n {data_frame.dtypes}\n"
    )

    return data_frame


def analyze_data(data_frame):
    """
    This function analyzes data to check for various insights
    """

    # this keeps track of each columns values
    value_counts = []

    print(f"GETTING NUMBER OF ENTRIES FOR EACH COLUMN.")
    for column in data_frame:
        value_count = {
            "column": column,
            "number_of_entries": f"{Fore.WHITE}{data_frame[column].value_counts()}",
        }

        value_counts.append(value_count)

    sleep(1.5)
    print("Done")


def find_missing_data(dataframe):
    """
    Find missing columns in provided dataset
    
    """
    total_count = dataframe.isnull().sum() #get total count of all null values
    percentage = dataframe.isnull().sum() / dataframe.isnull().count() * 100 #get percentage of all null values
    concat = pd.concat([total_count, percentage], axis=1, keys=["Total", "Percentage"])
    types = []
    for col in dataframe.columns:
        dtype = str(dataframe[col].dtype)
        types.append(dtype)
    concat["Types"] = types
    return np.transpose(concat)


arg_parser = argparse.ArgumentParser(
    description="Read and analyze data from a dataset", epilog="Enjoy the program 😊"
)

arg_parser.add_argument(
    "path",
    metavar="path",
    type=str,
    help="Path to SQLite file",
)

args = arg_parser.parse_args()

input_path = args.path

if input_path is not None:
    dataframe = read_input_path(input_path)
    analyze_data(dataframe)
    sleep(2)
    print(f"Finding Missing values\n")
    print(f"{find_missing_data(dataframe)}\n")

else:
    print("Please provide a valid input file.")
