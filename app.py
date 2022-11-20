import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recomender(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similar[movie_index]
    movie_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]

    recomended_movies=[]
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = df.iloc[i[0]]['movie_id']
        recommended_movie_posters.append(fetch_poster(movie_id))
        recomended_movies.append(df.iloc[i[0]]['title'])
    return recomended_movies,recommended_movie_posters


df=pickle.load(open('movies.pkl','rb'))
similar=pickle.load(open('similar.pkl','rb'))

movies_list=df['title'].values
st.title('Movie Recommender System')

option=st.selectbox(
    'Enter movie name',
    (movies_list))
#st.write(len(movies_list))


if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recomender(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

