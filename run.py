# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os
import argparse
import sys
import sqlite3
import pandas as pd
from colorama import init,Back,Fore


init()


def read_input_path(input_path):
    """
        This function reads the input path and returns the nature of the data
    """
    print(f"READING {input_path}") 

    data_frame=pd.read_csv(input_path)

    print(f"COLUMNS PRESENT IN DATASET")

    for column in data_frame:
        print(f"- {column}")

    return data_frame


def analyze_data(data_frame):
    """
    This function analyzes data to check for various insights
    """
    print("\n NATURE OF DATASET")
    print(data_frame.info())
    print("\n ANALYZING VALUES")
    print("\n\n==================================")

    for column in data_frame:
        print(f"{Fore.BLUE}  Analyzing Column: '{Fore.WHITE + column}'")
        print(f"{Fore.WHITE}{data_frame[column].value_counts()}")
        print("\n\n==================================")


arg_parser = argparse.ArgumentParser(
    description="Read and analyze data from a dataset",
    epilog="Enjoy the program 😊"
)

arg_parser.add_argument(
    "path",
    metavar="path",
    type=str,
    help="Path to SQLite file",
)

args = arg_parser.parse_args()

input_path = args.path #

if input_path is not None:
    dataframe=read_input_path(input_path)
    analyze_data(dataframe)
