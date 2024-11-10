import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movies_id):
    movies_id = str(movies_id)
    API_key = "8265bd1679663a7ea12ac168da84d2e8"
    url = "https://api.themoviedb.org/3/movie/"+movies_id+"?api_key="+API_key+"&language=en-US"
    #print(url)
    response = requests.get(url)
    data = response.json()
    #st.text(url)
    poster_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    
    return poster_path


def recommand(movie):
    index = movies[movies['title']==movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    recommanded_movies=[]
    poster = []
    for i in movie_list:
        movies_id=movies.iloc[i[0]].movie_id
        movies_title = movies.iloc[i[0]].title
        #fethch poster using API:
        poster_path = fetch_poster(movies_id)
        #print(poster_path)
        recommanded_movies.append(movies_title)
        poster.append(poster_path)

    return recommanded_movies,poster


movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommand System')

select_movie = st.selectbox('Choose a movie name ', movies['title'].values)
if st.button('Recommend'):
    name,poster = recommand(select_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
