<h1 align="center">Analyzing Kaggle Data Science Survey of 2021</h1>

[View the live project here.](https://dataanalysis2021.herokuapp.com/)

Kaggle is a professional community for data scientists and machine learning engineers. They conduct developer surveys every year, and the collected data is available open-source on the web. With proper analysis, the Dataset would help us to answer real-world questions. For instance, we can find the most popular language that the data scientists use. Our project is to analyze the survey data and gather meaningful insights from it.

The questions that we answered as part of the analysis were given in the Data analysis. This readme.md file explains our project.

<h2 align="center"><img src="pics/proj.png"></h2>

## User Experience (UX)

-   ### Design
    -   Since the application is a commandline application, it has a simple User interface consisting of black background and white text.

    - The font of the interface is monospace.

        
## Features

- Runs in a commandline.
- Prompts a user for input wen needed


## Technologies Used

### Languages Used

-   [Python](https://en.wikipedia.org/wiki/HTML5)


### Frameworks, Libraries & Programs Used

1. [Pandas](https://pandas.pydata.org/)
    - .This is a Python library for data analysis and manipulation. It is what was used to read the CSV survey data and covert it into dataframes which could be easy to analyze.
2. [Numpy](https://numpy.org/)
    - This is a tool for scientific coputing using Python. This helps us group our data into arrays, we also used it to access functions that were necessary for making decisions of attributes in our dataframes.
3. [Time](https://fonts.google.com/)
    - This module provides various time-related functions.
4. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
5. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
6. [Heroku:](https://heroku.com)
    - This is the platform that gave us the environment for easy deployment.



## Deployment

### Heroku

The project was deployed to Heroku using the following steps...

1. Create a [Heroku account](https://signup.heroku.com/login).
2. Create a Heroku app.
<h3 align="center"><img src="pics/1.png"></h3>
3. Go to the Deploy tab and connect the app to Github. This will be helpful for automatic deploys.
<h2 align="center"><img src="pics/2.png"></h2>
4. Then You can select the Github repository to connect to the Heroku app.
<h2 align="center"><img src="pics/3.png"></h2>


### Locally
1. Add a requirements.txt to you project using ```pip3 install -r requirements.txt```
<h2 align="center"><img src="pics/4.png"></h2>
The presence of this file is important as Heroku will read the Procfile each time the application is deployed and then install dependecies from this file.
using the first command.
<h2 align="center"><img src="pics/5.png"></h2>



## Credits

### Code

-   [Gitpod](https://gitpod.io): The development of this project was made easy. They provided a really efficient workspace for developed this Python based application.

-   [Kaggle](https://kaggle.com): Most of te data analysis knowledge that was used to develop this application was inspired by the work of the brilliant data scientists on the platform.

-   [Python](https://python.org/) : The programming language that made building thhe application easier. With a wide variety of in-built standard library tools, the applicationn development was made easy

### Content

-   All content was written by the developer.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   All Images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.