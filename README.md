# Analyze the Kaggle data science survey of 2021 Using Python
This script is used to analyze and show insights on various trends in machine learning and data science over many geographical regions. The data used is got from the Kaggle 2021 Survey.

## About the data
The data of the survey analyzed was downloaded as [kaggle_survey_2021_responses.csv](https://www.kaggle.com/competitions/kaggle-survey-2021/data).

## How I Analyzed this data
The script was written using the Python programming language with a combination of many Python technologies like.

1. [Pandas](https://pandas.pydata.org/): This is a Python library for data analysis and manipulation.
2. [Numpy](https://numpy.org/):This is a tool for scientific coputing using Python.
3. [Colorama](https://super-devops.readthedocs.io/en/latest/misc.html): This is a Python tool for helping us to have colored text in the commandline.
4. [ArgParse](https://docs.python.org/3/library/argparse.html): This is a Python standard library tool for helping us to parse command-line options, commands and sub-commands.
5. [Time](https://docs.python.org/3/library/time.html): This is a tool that provides us with access to time-related functions.

Using all the above, I created a Python script that takes in an input CSV dataset, parses and analyzes the data and finally export the insights into a human readable form in a txt file. 


# How to run the code
Run the code with the command below.
```
python3 run.py  <path_to_survey_data>  <path_to_output-file> ```

For example, 

```
python3 run.py kaggle_survey_2021_responses.csv output.txt
```

This runs the `run.py` file with `kaggle_survey_2021_responses.csv` as the input dataset. `output.txt` is the output file which which will contain the various important insights from the survey.

