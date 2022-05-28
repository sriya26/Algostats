from re import X
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
import nltk
import ast
import sklearn as sk
import numpy as np
import pandas as pd
import csv
import sort
import time
import merge_sort
import heap_sort

movies = pd.read_csv('small_dataset.csv')
movies.head(10)
movies.info()
movies['original_language'].value_counts()
movies = movies[['genres', 'title', 'original_language', 'id', 'overview', 'popularity',
                 'production_companies', 'runtime', 'spoken_languages', 'vote_average', 'vote_count']]
movies.info()
movies.dropna(inplace=True)
print(movies.info())


def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


movies['genres'] = movies['genres'].apply(convert)
movies.head()
movies['production_companies'] = movies['production_companies'].apply(convert)
movies['spoken_languages'] = movies['spoken_languages'].apply(convert)
movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies['genres'] = movies['genres'].apply(
    lambda x: [i.replace(" ", "") for i in x])
movies['overview'] = movies['overview'].apply(
    lambda x: [i.replace(" ", "") for i in x])
# movies['title'] = movies['title'].apply(lambda x:[i.replace(" ", "") for i in x])
movies['production_companies'] = movies['production_companies'].apply(
    lambda x: [i.replace(" ", "") for i in x])
movies['tags'] = movies['genres'] + \
    movies['overview'] + movies['production_companies']
new_df = movies[['id', 'title', 'tags', 'original_language', 'popularity',
                 'runtime', 'spoken_languages', 'vote_average', 'vote_count']]
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
# At every space join x (basically list to string)
new_df.head()
# Apply stemming
# library for natural lang processing
ps = PorterStemmer()


def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
# We create a list and we append in the list all the root values of i
    return " ".join(y)


# Convert list to string
new_df['tags'] = new_df['tags'].apply(stem)
print(new_df)
# we import this with two hyperparameters max_features and stop_words
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()
# convert new_df tags to numpy array
similarity = cosine_similarity(vectors)
similarity[1]
if similarity.size != 0:
    print('no error')
else:
    print('error')


def choose():
    choice = input("Select your sorting method\n")
    # print(choice)
    if choice == 0:
        tic = time.time()
        sorted = sort.BubbleSort(similarity)
        toc = time.time()
        x = print(sorted(enumerate(sorted[100]),
                  reversed=True, key=lambda x: x[1])[1:6])
        return x
    elif choice == 1:
        tic = time.time()
        sorted = sort.InsertionSort(similarity)
        toc = time.time()
        x = print(sorted(enumerate(sorted[100]),
                  reversed=True, key=lambda x: x[1])[1:6])
        return x
    elif choice == 2:
        tic = time.time()
        sorted = sort.selectionSort(similarity)
        toc = time.time()
        x = print(sorted(enumerate(sorted[100]),
                  reversed=True, key=lambda x: x[1])[1:6])
        return x
    elif choice == 3:
        tic = time.time()
        sorted = merge_sort.mergeSort(similarity)
        toc = time.time()
        x = print(sorted(enumerate(sorted[100]),
                  reversed=True, key=lambda x: x[1])[1:6])
        return x
    elif choice == 4:
        tic = time.time()
        sorted = heap_sort.heapSort(similarity)
        toc = time.time()
        x = print(sorted(enumerate(sorted[100]),
                  reversed=True, key=lambda x: x[1])[1:6])
        return x
    # print(toc - tic)
# sorting on the basis of similarity with movie of index position 0.
# reversed
# enumerate to grab the index position while sorting and convert to list (converted to list of tuples)
# lambda for sorting on basis of second number.


def recommend(name):
    movie_index = new_df[new_df['title'] == name].index[0]
# this fetches the index position of the movie which is chosen by the user
    distance = similarity[movie_index]
# goes to in 14
    movies_list = sorted((enumerate(distance)),
                         reverse=True, key=lambda x: x[1])[1:6]
# Sort the distances goes to in 15
    for i in movies_list:
        print(new_df.iloc[i[0]].title)
    return new_df.iloc[i[0]].title
    # test = np.array(movie)
    # test = test.reshape((1,-1))
    # return new_df.iloc[i[0]].title


# recommend('Catwalk')
