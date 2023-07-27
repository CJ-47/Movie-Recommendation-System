import streamlit as st
import pickle
import requests
import pandas as pd
st.title("Movie Recommendation System")
movies_list=pd.read_pickle('movies.pkl')
similarity=pd.read_pickle('similarity.pkl')

selection_pane=st.selectbox('Enter the name of the movie you watched recently', movies_list['title'].values )
st.text('You Entered : '+selection_pane)
def recommend(chose):
    movie_index=movies_list[movies_list['title']==chose].index[0]
    distance=similarity[movie_index]
    recommendations=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    matches=[]
    posters=[]
    for movie in recommendations :
        matches.append(movies_list.iloc[movie[0]].title)
        posters.append(get_poster(movies_list.iloc[movie[0]].id))
    return matches,posters    

def get_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ee4249c04b22f89aded064751f04232d'.format(movie_id)).json()
    return 'https://image.tmdb.org/t/p/original/'+response['poster_path']


if st.button('Watched Movie Recommendations '):
    wait=st.warning('Fetching data from TMDB server...')
    result,images=recommend(selection_pane)
    cols = st.columns(len(result),gap='small')
    for mvname in range(len(result)) :
      with cols[mvname]:
       st.text(result[mvname])
       st.image(images[mvname])
    wait.empty()

