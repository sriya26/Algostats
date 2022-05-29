import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df2 = pd.read_csv('./dataset/tmdb.csv')

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])
all_titles = [df2['title'][i] for i in range(len(df2['title']))]


def get_recommendations(name):
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    tit = df2['title'].iloc[movie_indices]
    dat = df2['release_date'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['Title', 'Year'])
    return_df['Title'] = tit
    return_df['Year'] = dat
    return return_df
