import streamlit as st
import pickle
import pandas as pd
import requests
movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
# api_key = f69a959fd22a72496ca835bf7b8f1291
# "https://api.themoviedb.org/3/movie/movie_id?language=en-US"
# http://image.tmdb.org/t/p/w500/your_poster_path
def fetch_poster(movie_id):
    
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f69a959fd22a72496ca835bf7b8f1291")
    data = response.json()
    # st.text(data)
    # st.text(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f69a959fd22a72496ca835bf7b8f1291")
    poster_path = data['poster_path']
    
    return 'http://image.tmdb.org/t/p/w500/'+ poster_path

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list  = sorted(list((enumerate(distance))),reverse=True,key= lambda x :x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[[i[0]]].title.to_numpy()[0])
        recommended_movies_posters.append(fetch_poster(movies.iloc[[i[0]],:]['movie_id'].to_numpy()[0]))
    return recommended_movies,recommended_movies_posters


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].unique()
)
if st.button('Recommend'):
    name , posters = recommend(selected_movie_name) # recommedations is a a list
    # for i in recommendations:
    #     st.write(i)

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.header(name[0])
        st.image(posters[0])

    with col2:
        st.header(name[1])
        st.image(posters[1])

    with col3:
        st.header(name[2])
        st.image(posters[2])
    with col5:
        st.header(name[3])
        st.image(posters[3])
    with col5:
        st.header(name[4])
        st.image(posters[4])