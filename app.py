import streamlit as st
import pickle
import pandas as pd

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list  = sorted(list((enumerate(distance))),reverse=True,key= lambda x :x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[[i[0]]].title.to_numpy()[0])
    return recommended_movies


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].unique()
)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name) # recommedations is a a list
    for i in recommendations:
        st.write(i)