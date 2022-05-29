<h1 align="center">Algostats

## Table of contents
1. [About the project](#introduction)
    * [Salient Features](#features)
    * [Comaptible Platforms](#platforms)
    * [Technology Stack](#stack)
2. [Algorithms used](#algorithms)
    * [Recommender Algorithms](#recal)
    * [Sorting Algorithms](#sortal)
3. [Dataset used](#dataset)
4. [Guide to Getting Started](#start)
    * [Prerequisites](#prereq)
    * [Installation](#install)
5. [Navigating through the App](#nav)
    * [Search page](#search)
    * [Recommendations and Statistics page](#recstats)

## About the project <a name="introduction"></a>
***
* A website based application created to demonstrate the roles played by variou types of algrithm in a movie recommender system used by web streaming applications like Netflix.
* The algorithms used and compared include:

    * Machine Learning and Deep Learning models for the main recommender system.
    * Sorting algorithms used in the recommenders to sort the similarity distance.

* Built during the Microsoft Intern Engage 2022 program as a part of the Algorithms problem statement.

###  <a name="#features">Salient Features</a>
* Takes input movie from the user and displays the top 5 recommendations as given by the Machine Learning/Deep Learning algorithm.

* Displays comparisions between various comparative parameters for the algorithms and finally suggests the ideal algorithms in each case.

### Technology Stack <a name="#stack"></a>
1. _**Front-End**_ : HTML,CSS,Bootstrap
2. _**Back-End**_ : Flask
3. _**ML Model**_ : Natural Language Toolkit, Scikit-Learn, FuzzyWuzzy and Surprise python libraries


## Algorithms used <a name="algorithms"></a>
***
The following algorithms were analyzed :
### 1. Recommender Algorithms  <a name="#recal"></a>
Three main kinds of Machine Learning algorithms used for recommender systems in streaming applications were used in this project

1. _**Collaborative filtering**_: Predictions made based on users behaviour and similarity with other users. The <ins>K Nearest Neighbours</ins> algorithm was used to implement this.

2. _**Content-Based filtering**_: Predictions made on the basis of keywords and descriptions. <ins>Bag of Words</ins> algorithm was used to implement this.

3. _**Hybrid Recommendation**_: Predictions are made based on both content-based and collaborative filtering to suggest a broader range of products. A combination of <ins>Cosine similarity</ins> (content-based) and <ins>Singular Value Decomposition</ins> (collaborative) were used to implement this.

### 2. Sorting Algorithms  <a name="#sortal"></a>
The following sorting algorithms were used in each of the recommender system to sort the distances of the suggested movie from the entered one, i.e, how close or far a recommendation is.

* Bubble sort: choice 0
* Insertion sort: choice 1
* Selection sort: choice 2
* Merge sort: choice 3
* Heap sort: choice 4



## Dataset used <a name="dataset"></a>
***
The dataset used for these algorithms is the **MovieLens** dataset made publicly available by GroupData, a research lab at the University of Minnesota for research purposes. The dataset consists of data collected over a long time from the various ratings and data available on the MovieLens website.

I used the MovieLens Latest Datasets abd the TMDb 5000 movies dataset for the models, which consists of several datasets including that of ratings, credits, tags, movies, links and movie metadata that consists of all the information regarding a movie including the language,year of release, tagline, budget, revenue etc.

The MovieLens dataset is available in two sizes, both of which were used for the models: 
* _**Small dataset**_ having 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users aong with 10,000 movie metatdata.
* _**Full dataset**_ having 27,000,000 ratings and 1,100,000 tag applications applied to 58,000 movies by 280,000 users. Includes tag genome data with 14 million relevance scores across 1,100 tags along with 45,000 movie metadata. 

The TMDb dataset contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.

The dataset used for the main ML pipeline is the TMDb dataset. The MovieLens dataset has been used for training different kinds of recommender algorithms and their analysis.

## Guide to Getting Started  <a name="start"></a>
***
### Prerequisites  <a name="#recal"></a>

### Installation  <a name="#install"></a>

## Navigating through the App <a name="nav"></a>
***
### Search page  <a name="#search"></a>
The first page of the application, you can type the name of the movie in the search bar and click the search icon.

![Search Page](https://github.com/sriya26/Recommender_System/blob/main/images/search-page.PNG)


### Recommendations and Statistics page <a name="#recstats"></a>
After searching, you will be redirected to the next page that will give you the top 5 recommendations made by the ML algorithms used.

![Recommendations](https://github.com/sriya26/Recommender_System/blob/main/images/recs.PNG)

On scrolling down or by clicking the 'Algorithms' option in the nav bar, you can see the comparisions made between the different algorithms used in the recommender system in the form of graphs and other information.

![Recommender Algorithm](https://github.com/sriya26/Recommender_System/blob/main/images/recal.PNG)

The features taken to compare the performance of the recommendation algorithms include RAM Usage, Training time and Prediction time while those for sorting algorithms include Time taken and Space complexity.
   
![Sorting Algorithm](https://github.com/sriya26/Recommender_System/blob/main/images/sort.PNG)

<ins>Note</ins>: Accuracy cannot be a parameter used in comparing the recommender algorithms due to the different nature of recommendations by each of the algorithm types.







