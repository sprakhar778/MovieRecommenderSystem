import streamlit
import streamlit as st
import pickle
import pandas as pd
import requests

#-----------------------------------------------------
movie_dict=pickle.load(open('movie.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similiarity=pickle.load(open('similarity.pkl','rb'))
#------------------API----------------------------------





#

#
# x=[83,85]
# fetch_poster(x[0])
# fetch_poster(19995)
# fetch_poster(x[1])

#

from time import sleep
def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/'+str(movie_id) +"?api_key=ea44cb3b0ab51859a0cb6bebe729f7d0&language=en-US"
    response= requests.get(url)
    response=response.json()
    print(response)
    if response['belongs_to_collection'] is not None:
        x='https://image.tmdb.org/t/p/w500'+response["belongs_to_collection"]["poster_path"]
    else:
        x = 'https://image.tmdb.org/t/p/w500' + response["poster_path"]
    # st.write(response)
    # st.image(x)

    return x

# st.image(fetch_poster(811))
# st.image(fetch_poster(2067))


#-------------------------------------------------
def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    vector = similiarity[movies_index]
    movies_list = sorted(list(enumerate(vector)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    poster_image=[]
    for i in movies_list:
        movies_id=movies.iloc[i[0]].id
        # st.write(movies_id)
        # st.image(fetch_poster(movies_id))
        #  fetch movie from api
        recommended_movies.append(movies.iloc[i[0]].title)
        # print(movies_id)
        img_url = fetch_poster(movies_id)
        poster_image.append(img_url)




    return recommended_movies,poster_image
# recommend('Avatar')

st.title("Movie Recommender System")
# selected_movie='Avatar'
selected_movie= st.selectbox(
    'How would you like to get similiar movies,choose your favourite movie?',
    (movies['title'].values))
name,path=recommend(selected_movie)

if st.button('Recommend'):
    # st.image(fetch_poster(811))
    # st.image(fetch_poster(2067))

    for i in range(5):
        st.header(name[i])
        st.image(path[i])







