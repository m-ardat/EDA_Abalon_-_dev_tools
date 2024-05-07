# EDA_Abalon_&_dev_tools

## Project Description

The project examines the main approaches to data analysis and development tools. Based on physical measurements, predict the age of the abalone.
The repository contains:
- рexploratory analysis of data from physical measurements of abalone and its age - `EDA_abalone.ipynb`;
- the processes of learning, testing, tuning and interpretation of the machine learning model - `ML_abalone.ipynb`;
- files for deployment and deployment of an interactive dashboard that allows you to track the decision-making process of the model - `app`.

## Table of Contents

- [Project Description](#project-description)
- [EDA](#eda)
- [ML](#ml)
- [Deployment](#deployment)
- [How to Install and Run the Project](#how-to-install-and-run-the-project)
- [How to Use the Project](#how-to-use-the-project)
- [Author](#author)
- [License](#license)
### EDA
In the process of exploratory analysis, the influence of categorical and continuous features on the target variable was investigated. For each feature, the hypothesis of its significance has been tested by statistical methods.


### ML
In this project, we have built several models that predict the age of the abalone.

We settled on the KNeighborsRegressor model with hyperparameters selected using GridSearchCV. The MAE indicator was chosen as the target metric, which showed an error of ~1.5 for the selected model.

### Deployment
In this project, we built an interactive dashboard and wrapped it in a docker container.

Using Docker, we created a Dockerfile that contains all the necessary instructions to build a container with our dashboard.

### How to Install and Run the Project
Please note that you need to have Docker on your computer to perform the above steps. If you do not have it, please install Docker before starting the process.

To start the dashboard, follow these steps:

1. Open a terminal on your computer.

2. Download the image from Docker Hub by running the command:
```
$ docker pull maxardat/dbabalone
```
This will download the dashboard image to your computer.

3. Pull up the container from the downloaded image by running the command:
```
$ docker run maxardat/dbabalone
```
This will create and start the dashboard container.

4. A link will appear in the terminal. Copy this link and paste it into the address bar of your web browser.

After clicking the link, you will see the dashboard open in your web browser. You can now view and use the dashboard to analyze the data.

### How to use the project
This dashboard allows you to explore swap values, the importance of permutations, the interaction effect, partial dependency graphs, all kinds of performance graphs.

### Author
- Maxim Ardat - [GitHub](https://github.com/m-ardat), [Telegram](https://t.me/m_ardat)
### License
This project is licensed under the MIT license. For more information, see the [LICENSE](/LICENSE) file.
