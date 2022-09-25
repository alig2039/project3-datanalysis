# Analyzing Kaggle Data Science Survey of 2021

## Project description

Kaggle is a professional community for data scientists and machine learning engineers. They conduct developer surveys every year, and the collected data is available open-source on the web. The 2021 survey data is available [here](https://www.kaggle.com/competitions/kaggle-survey-2021/data). With proper analysis, the Dataset would help us to answer real-world questions. For instance, we can find the most popular language that the data scientists use. Our project is to analyze the survey data and gather meaningful insights from it.

As a first step, we will clean the data by removing null values and outliers in each column. Then, refactor the columns in such a way that help us in analysis. Then we performed data analysis on the cleaned dataset.

The questions that we answered as part of the analysis were given in the Data analysis. This readme.md file explains our project.


## Data Source
The dataset is very diverse and came from the Kaggle Data Science survey. Kaggle has data collected through surveys from 2017 to 2021. We choose 2021 to analyze for the project. The participants mostly from the US, India, and EMEA regions. The majority of the survey respondents had a background of developer/ coding experience. 

Dataset can be downloaded from the mentioned below link:

Download Link -> https://www.kaggle.com/competitions/kaggle-survey-2021/data

The data are available in the CSV format which is 35.2MB in size. For this project, I focused on specific features. As a result, I specifically chose columns which required for our analysis and dropped the ones which were not required.

The reason why I chose this dataset is because of its diverse nature and it was completely uncleaned. 

## Key insights
1. Majority of the people who took part in the survey were Students.
2. Python is the most recommended programming language for beginners.
3. Python is also the most used programming language among all the participants followed by R.
4. Majority of the participants were from India and the United States of America.
5. Majority of the participants were male.


## Tools used in the project
Here are the thir-party  Python tools that were used in the project
1. Pandas: This is a Python library for data analysis and manipulation.
2. Numpy:This is a tool for scientific coputing using Python.
3. Colorama: This is a Python tool for helping us to have colored text in the commandline.
4. Time: This is a tool that provides us with access to time-related functions.


## How the program works
By running the scipt `run.py`, we call the various functions that parse the CSV data, clean it up and then obtain insights. The insights are then written to a text file called `results.txt`.

To run the file,
```
python3 run.py
```

