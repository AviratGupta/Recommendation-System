import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(poster(movie_id))
    return recommended_movies,recommended_movies_poster

def poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=1b2a71cd9926f36493eca112d192e801&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

movies_dict = pickle.load(open("movies_dict.pkl","rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl","rb"))

st.title("MOVIE RECOMMENDER")

selected_movie = st.selectbox("your selected Movie",movies["title"].values)

if st.button("RECOMMEND"):
    recommendation_name,posters = recommend(selected_movie)
    c1,c2,c3,c4,c5 = st.columns(5)
    with c1:
        st.text(recommendation_name[0])
        st.image(posters[0])
    with c2:
        st.text(recommendation_name[1])
        st.image(posters[1])
    with c3:
        st.text(recommendation_name[2])
        st.image(posters[2])
    with c4:
        st.text(recommendation_name[3])
        st.image(posters[3])
    with c5:
        st.text(recommendation_name[4])
        st.image(posters[4])