import streamlit as st
from repositories.help_func import movie_exist, anime_exist, series_exist
from repositories.add_content import add_movie, add_anime, add_series

def add_content_page():
    st.title("Добавление произведения")

    production_type = st.selectbox("Выберите тип произведения", ["anime", "movie", "series"])

    st.subheader("Введите информацию о новом произведении")

    if production_type == "movie":
        title = st.text_input("Название фильма")
        description = st.text_area("Описание")
        release_year = st.number_input("Год выпуска", min_value=1900, max_value=2100, step=1)
        duration = st.number_input("Продолжительность (в минутах)", min_value=1)
        director = st.text_input("Режиссёр")
        country = st.text_input("Страна производства")
        language = st.text_input("Язык")
        genre = st.text_input("Жанр")

        if st.button("Добавить фильм"):
            if title and description and release_year and duration and director and country and language and genre:
                if movie_exist(title):
                    st.error("Фильм с таким названием уже существует")
                else:
                    add_movie(title, description, release_year, duration, director, country, language, genre)
                    st.success(f"Фильм '{title}' успешно добавлен")
            else:
                st.error("Заполните все поля")

    elif production_type == "series":
        title = st.text_input("Название сериала")
        description = st.text_area("Описание")
        release_year = st.number_input("Год выпуска", min_value=1900, max_value=2100, step=1)
        seasons = st.number_input("Количество сезонов", min_value=1)
        episodes = st.number_input("Количество серий", min_value=1)
        creator = st.text_input("Создатель")
        country = st.text_input("Страна производства")
        language = st.text_input("Язык")
        genre = st.text_input("Жанр")

        if st.button("Добавить сериал"):
            if title and description and release_year and seasons and episodes and creator and country and language and genre:
                if series_exist(title):
                    st.error("Сериал с таким названием уже существует")
                else:
                    add_series(title, description, release_year, seasons, episodes, creator, country, language, genre)
                    st.success(f"Сериал '{title}' успешно добавлен")
            else:
                st.error("Заполните все поля")

    elif production_type == "anime":
        title = st.text_input("Название аниме")
        description = st.text_area("Описание")
        release_year = st.number_input("Год выпуска", min_value=1900, max_value=2100, step=1)
        episodes = st.number_input("Количество серий", min_value=1)
        studio = st.text_input("Студия")
        genre = st.text_input("Жанр")
        country = st.text_input("Страна производства")
        language = st.text_input("Язык")

        if st.button("Добавить аниме"):
            if title and description and release_year and episodes and studio and genre and country and language:
                if anime_exist(title):
                    st.error("Аниме с таким названием уже существует")
                else:
                    add_anime(title, description, release_year, episodes, studio, genre, country, language)
                    st.success(f"Аниме '{title}' успешно добавлено")
            else:
                st.error("Заполните все поля")
