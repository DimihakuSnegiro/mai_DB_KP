from repositories.admin_conn import get_all_movies, get_all_series, get_all_anime, get_all_non_admin_users
import streamlit as st

def show_id():
    st.title("Выберите чьё id вывести")

    action = st.selectbox(
        'Выберите, чьи ID вывести:',
        ['Фильмы', 'Сериалы', 'Аниме', 'Пользователи']
    )

    if action == "Фильмы":
        movies = get_all_movies()
        st.dataframe(movies)  

    elif action == "Сериалы":
        series = get_all_series()
        st.dataframe(series) 

    elif action == "Аниме":
        anime = get_all_anime()
        st.dataframe(anime)  

    elif action == "Пользователи":
        users = get_all_non_admin_users()
        st.dataframe(users) 