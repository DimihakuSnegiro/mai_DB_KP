import streamlit as st
from repositories.help_func import movie_exist, anime_exist, series_exist, get_id_anime, get_id_movie, get_id_series
from repositories.delete_content import delete_movie, delete_anime, delete_series, delete_anime_rating, delete_movie_rating, delete_series_rating

def delete_content_page():
    st.title("Удаление произведения")

    production_type = st.selectbox("Выберите тип произведения", ["anime", "movie", "series"])

    title = st.text_input("Введите название произведения для удаления")

    if st.button("Удалить"):
        if not title:
            st.error("Пожалуйста, введите название произведения.")
        else:
            if production_type == "movie":
                if not movie_exist(title):
                    st.error(f"Фильм '{title}' не найден.")
                else:
                    delete_movie_rating(get_id_movie(title))
                    delete_movie(title)
                    st.success(f"Фильм '{title}' успешно удалён.")
            
            elif production_type == "series":
                if not series_exist(title):
                    st.error(f"Сериал '{title}' не найден.")
                else:
                    delete_series(title)
                    st.success(f"Сериал '{title}' успешно удалён.")
            
            elif production_type == "anime":
                if not anime_exist(title):
                    st.error(f"Аниме '{title}' не найдено.")
                else:
                    delete_anime(title)
                    st.success(f"Аниме '{title}' успешно удалено.")
