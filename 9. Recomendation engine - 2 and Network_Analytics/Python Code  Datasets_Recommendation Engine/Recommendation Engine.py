# Importing all required libraries, modules
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer # term frequency - inverse document frequncy is a numerical statistic that is intended to reflect how important a word is to document in a collecion or corpus
# from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from sqlalchemy import create_engine
import pymysql
import mysql.connector as connector

# import Dataset 
anime = pd.read_csv(r"C:\Users\Bharani Kumar\Desktop\Version 2 slides\Datasets\anime.csv", encoding = 'utf8')

# Database Connection

# Upload the Table into Database

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user = "user1",# user
                               pw = "user1", # passwrd
                               db = "recommenddb")) #database

anime.to_sql('anime', con = engine, if_exists = 'append', chunksize = 1000, index = False)


# Read the Table (data) from MySQL database

import mysql.connector as connector

con = connector.connect(host = 'localhost',
                  port = '3306',
                  user = 'user1',
                  password = 'user1',
                  database = 'recommenddb',
                  auth_plugin = 'mysql_native_password')

cur = con.cursor()
con.commit()

cur.execute('SELECT * FROM anime')
df = cur.fetchall()

anime = pd.DataFrame(df)
anime = anime.rename({0 : 'anime_id'}, axis = 1)
anime = anime.rename({1 : 'name'}, axis = 1)
anime = anime.rename({2 : 'genre'}, axis = 1)
anime = anime.rename({3 : 'type'}, axis = 1)
anime = anime.rename({4 : 'episodes'}, axis = 1)
anime = anime.rename({5 : 'rating'}, axis = 1)
anime = anime.rename({6 : 'members'}, axis = 1)

# Check for Missing values
anime["genre"].isnull().sum() 

# Impute the Missing values in 'genre' column for a movie with 'General' category
anime["genre"] = anime["genre"].fillna("General")

# Create a Tfidf Vectorizer to remove all stop words

tfidf = TfidfVectorizer(stop_words = "english")   # taking stop words from tfidf vectorizer 

# Transform a count matrix to a normalized tf-idf representation
tfidf_matrix = tfidf.fit(anime.genre)   

# Save the Pipeline for tfidf matrix

joblib.dump(tfidf_matrix, 'matrix')

os.getcwd()

mat = joblib.load("matrix")

tfidf_matrix = mat.transform(anime.genre)

tfidf_matrix.shape #12294, 47

# cosine(x, y)= (x.y⊺) / (||x||.||y||)
# Computing the cosine similarity on Tfidf matrix

cosine_sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

joblib.dump(cosine_sim_matrix, 'cosine_matrix')

# Create a mapping of anime name to index number
anime_index = pd.Series(anime.index, index = anime['name']).drop_duplicates()

# Example
anime_id = anime_index["Assassins (1995)"]

anime_id

# Custom Function to Find the TopN Movies to be Recommended

def get_recommendations(Name, topN):    
    # topN = 10
    # Getting the movie index using its title 
    anime_id = anime_index[Name]
    
    # Getting the pair wise similarity score for all the anime's with that 
    # anime
    cosine_scores = list(enumerate(cosine_sim_matrix[anime_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key = lambda x:x[1], reverse = True)
    
    # Get the scores of top N most similar movies 
    cosine_scores_N = cosine_scores[0: topN + 1]
    
    # Getting the movie index 
    anime_idx  =  [i[0] for i in cosine_scores_N]
    anime_scores =  [i[1] for i in cosine_scores_N]
    
    # Similar movies and scores
    anime_similar_show = pd.DataFrame(columns = ["name", "Score"])
    anime_similar_show["name"] = anime.loc[anime_idx, "name"]
    anime_similar_show["Score"] = anime_scores
    anime_similar_show.reset_index(inplace = True)  
    # anime_similar_show.drop(["index"], axis=1, inplace=True)
    return(anime_similar_show.iloc[1:, ])

rec = get_recommendations("No Game No Life Movie", topN = 10)

rec

