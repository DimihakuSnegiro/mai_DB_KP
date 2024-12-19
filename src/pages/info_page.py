import streamlit as st
import pandas as pd
from repositories.info import fetch_movie_info, fetch_series_info, fetch_anime_info, fetch_reviews
from repositories.help_func import movie_exist, anime_exist, series_exist

def display_media_info():
    st.title("Информация о фильмах, сериалах и аниме")

    category = st.selectbox("Выберите категорию", ["Фильмы", "Сериалы", "Аниме"])

    action = st.radio("Что вы хотите сделать?", ["Посмотреть информацию", "Посмотреть отзывы"])

    title = st.text_input("Введите название произведения")

    if title:
        if action == "Посмотреть информацию":
            if category == "Фильмы":
                if movie_exist(title):
                    data = fetch_movie_info(title)
                    st.subheader("Информация о фильме")
                    st.text(f"Название: {data['title']}")
                    st.text(f"Описание: {data['description']}")
                    st.text(f"Год выпуска: {data['release_year']}")
                    st.text(f"Длительность: {data['duration']} минут")
                    st.text(f"Режиссер: {data['director']}")
                    st.text(f"Страна: {data['country']}")
                    st.text(f"Язык: {data['language']}")
                    st.text(f"Жанр: {data['genre']}")
                else:
                    st.error("Фильм не найден.")
            
            elif category == "Сериалы":
                if series_exist(title):
                    data = fetch_series_info(title)
                    st.subheader("Информация о сериале")
                    st.text(f"Название: {data['title']}")
                    st.text(f"Описание: {data['description']}")
                    st.text(f"Год выпуска: {data['release_year']}")
                    st.text(f"Количество сезонов: {data['number_of_seasons']}")
                    st.text(f"Количество серий: {data['number_of_episodes']}")
                    st.text(f"Создатель: {data['creator']}")
                    st.text(f"Страна: {data['country']}")
                    st.text(f"Язык: {data['language']}")
                    st.text(f"Жанр: {data['genre']}")
                else:
                    st.error("Сериал не найден.")
            
            elif category == "Аниме":
                if anime_exist(title):
                    data = fetch_anime_info(title)
                    st.subheader("Информация об аниме")
                    st.text(f"Название: {data['title']}")
                    st.text(f"Описание: {data['description']}")
                    st.text(f"Год выпуска: {data['release_year']}")
                    st.text(f"Количество серий: {data['number_of_episodes']}")
                    st.text(f"Студия: {data['studio']}")
                    st.text(f"Страна: {data['country']}")
                    st.text(f"Язык: {data['language']}")
                    st.text(f"Жанр: {data['genre']}")
                else:
                    st.error("Аниме не найдено.")

        elif action == "Посмотреть отзывы":
            if category == "Фильмы":
                if movie_exist(title):
                    reviews = fetch_reviews("movies", title)
                    if reviews:
                        st.subheader("Отзывы")
                        reviews_df = pd.DataFrame(reviews, columns=['User', 'Rating', 'Comment'])
                        st.dataframe(reviews_df)
                    else:
                        st.warning("Отзывы отсутствуют для данного фильма.")
                else:
                    st.error("Фильм не найден.")
            
            elif category == "Сериалы":
                if series_exist(title):
                    reviews = fetch_reviews("series", title)
                    if reviews:
                        st.subheader("Отзывы")
                        reviews_df = pd.DataFrame(reviews, columns=['User', 'Rating', 'Comment'])
                        st.dataframe(reviews_df)
                    else:
                        st.warning("Отзывы отсутствуют для данного сериала.")
                else:
                    st.error("Сериал не найден.")
            
            elif category == "Аниме":
                if anime_exist(title):
                    reviews = fetch_reviews("anime", title)
                    if reviews:
                        st.subheader("Отзывы")
                        reviews_df = pd.DataFrame(reviews, columns=['User', 'Rating', 'Comment'])
                        st.dataframe(reviews_df)
                    else:
                        st.warning("Отзывы отсутствуют для данного аниме.")
                else:
                    st.error("Аниме не найдено.")
