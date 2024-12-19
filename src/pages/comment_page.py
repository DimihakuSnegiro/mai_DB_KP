import streamlit as st
from repositories.help_func import movie_exist, series_exist, anime_exist
from repositories.comments import (
    add_movie_review,
    add_series_review,
    add_anime_review,
    delete_movie_review,
    delete_series_review,
    delete_anime_review,
    check_movie_review_exists,
    check_series_review_exists,
    check_anime_review_exists,
)
from repositories.help_func import get_id_anime, get_id_movie, get_id_series

def review_management_page():
    st.title("Управление оценками и отзывами")
    user_id = st.session_state.user_info[0]  
    action = st.selectbox("Выберите действие", ["Добавить", "Удалить"])

    category = st.selectbox("Выберите категорию", ["Фильм", "Сериал", "Аниме"])

    if action == "Добавить":
        st.subheader("Добавление оценки и отзыва")

        title = st.text_input("Название произведения")
        rating = st.number_input("Оценка (от 0 до 10)", min_value=1, max_value=10, step=1)
        comment = st.text_area("Комментарий")

        if st.button("Добавить оценку и отзыв"):
            if not title and not comment:
                st.error("Пожалуйста, заполните все поля.")
            else:
                if category == "Фильм":
                    if not movie_exist(title):
                        st.error(f"Фильм '{title}' не найден.")
                    else:
                        movie_id = get_id_movie(title)
                        if check_movie_review_exists(user_id, movie_id):
                            st.error("Вы уже оставляли отзыв на этот фильм.")
                        else:
                            add_movie_review(user_id, movie_id, rating, comment)
                            st.success(f"Оценка и отзыв для фильма '{title}' успешно добавлены.")
                elif category == "Сериал":
                    if not series_exist(title):
                        st.error(f"Сериал '{title}' не найден.")
                    else:
                        series_id = get_id_series(title)
                        if check_series_review_exists(user_id, series_id):
                            st.error("Вы уже оставляли отзыв на этот сериал.")
                        else:
                            add_series_review(user_id, series_id, rating, comment)
                            st.success(f"Оценка и отзыв для сериала '{title}' успешно добавлены.")
                elif category == "Аниме":
                    if not anime_exist(title):
                        st.error(f"Аниме '{title}' не найдено.")
                    else:
                        anime_id = get_id_anime(title)
                        if check_anime_review_exists(user_id, anime_id):
                            st.error("Вы уже оставляли отзыв на это аниме.")
                        else:
                            add_anime_review(user_id, anime_id, rating, comment)
                            st.success(f"Оценка и отзыв для аниме '{title}' успешно добавлены.")

    elif action == "Удалить":
        st.subheader("Удаление оценки и отзыва")

        title = st.text_input("Название произведения")

        if st.button("Удалить оценку и отзыв"):
            if not title:
                st.error("Пожалуйста, введите название произведения.")
            else:
                if category == "Фильм":
                    if not movie_exist(title):
                        st.error(f"Фильм '{title}' не найден.")
                    else:
                        movie_id = get_id_movie(title)
                        if(check_movie_review_exists(user_id, movie_id)):
                            delete_movie_review(user_id, movie_id)
                            st.success(f"Оценка и отзыв для фильма '{title}' успешно удалены.")
                        else:
                            st.error(f"Вы не оценивали фильм '{title}'")
                elif category == "Сериал":
                    if not series_exist(title):
                        st.error(f"Сериал '{title}' не найден.")
                    else:
                        series_id = get_id_series(title)
                        if(check_series_review_exists(user_id, series_id)):
                            delete_series_review(user_id, series_id)
                            st.success(f"Оценка и отзыв для сериала '{title}' успешно удалены.")
                        else:
                            st.error(f"Вы не оценивали сериал '{title}'")
                elif category == "Аниме":
                    if not anime_exist(title):
                        st.error(f"Аниме '{title}' не найдено.")
                    else:
                        anime_id = get_id_anime(title)
                        if(check_anime_review_exists):
                            delete_anime_review(user_id, anime_id)
                            st.success(f"Оценка и отзыв для аниме '{title}' успешно удалены.")
                        else:
                            st.error(f"Вы не оценивали фильм '{title}'")
