import streamlit as st
from repositories.admin_conn import (
    user_exists,
    is_admin,
    get_movie_ratings_by_user,
    get_series_ratings_by_user,
    get_anime_ratings_by_user,
    check_anime_review_exists,
    check_movie_review_exists,
    check_series_review_exists,
    delete_anime_review,
    delete_movie_review,
    delete_series_review
)

from repositories.personal_account import get_user_statistics, get_user_info, get_user_reviews

def admin_page():
    choose = ["Информация о пользователе", "Удалить оценку"]
    options = st.selectbox("Выберите действие", choose)

    if options == "Информация о пользователе":
        user_id = st.number_input("Введите ID пользователя", min_value=1, key="user_id_input")

        if user_id:
            if st.button("Показать информацию"):
                if not user_exists(user_id):
                    st.error(f"Пользователь с ID {user_id} не существует.")
                else:
                    if is_admin(user_id):
                        st.error("Вы не можете смотреть информацию об админах")
                        return
                    user_info = get_user_info(user_id)
                    if user_info:
                        st.write(f"### Информация о пользователе с ID {user_id}")
                        st.write(f"**Имя пользователя**: {user_info['username']}")
                        st.write(f"**Email**: {user_info['email']}")
                        st.write(f"**Роль**: {user_info['role']}")
                        st.write(f"**Дата регистрации**: {user_info['created_at']}")
                    else:
                        st.error("Не удалось получить информацию о пользователе.")

                    stats = get_user_statistics(user_id)
                    if stats:
                        st.write(f"### Статистика пользователя с ID {user_id}")
                        st.write(f"**Фильмов**: {stats['movies_count']}")
                        st.write(f"**Сериалов**: {stats['series_count']}")
                        st.write(f"**Аниме**: {stats['anime_count']}")
                    else:
                        st.error("Ошибка при получении статистики.")

            categories = ['Movies', 'Series', 'Anime']
            category = st.selectbox("Выберите тип контента", categories)

            if st.button("Показать оценки"):
                if category == "Movies":
                    ratings = get_movie_ratings_by_user(user_id)
                elif category == "Series":
                    ratings = get_series_ratings_by_user(user_id)
                elif category == "Anime":
                    ratings = get_anime_ratings_by_user(user_id)

                if not ratings.empty:
                    st.write(f"### Оценки пользователя с ID {user_id} в категории: {category.capitalize()}")
                    st.dataframe(ratings)  
                else:
                    st.write(f"Оценки пользователя с ID {user_id} в категории {category.capitalize()} не найдены.")

            if st.button("Показать отзывы"):
                reviews = get_user_reviews(user_id, category.lower())
                if not reviews.empty:
                    st.write(f"### Отзывы пользователя в категории: {category.capitalize()}")
                    st.dataframe(reviews)
                else:
                    st.write(f"Отзывы в категории {category.capitalize()} не найдены.")
        
        elif not user_id:
            st.error("Введите ID пользователя.")
    
    elif options == "Удалить оценку":
        categories = ['Movies', 'Series', 'Anime']
        choice = st.selectbox("Выберите тип контента", categories)
        delete_id = st.number_input("Введите ID оценки", min_value=1, step=1, key="delete_id_input")

        if st.button("Удалить оценку"):
            if delete_id:
                if choice == "Anime":
                    if not check_anime_review_exists(delete_id):
                        st.error(f"Оценки с ID {delete_id} для аниме не существует.")
                        return
                    delete_anime_review(delete_id)
                    st.success("Операция выполнена успешно!")
                elif choice == "Movies":
                    if not check_movie_review_exists(delete_id):
                        st.error(f"Оценка с ID {delete_id} для фильма не существует.")
                        return
                    delete_movie_review(delete_id)
                    st.success("Операция выполнена успешно!")
                elif choice == "Series":
                    if not check_series_review_exists(delete_id):
                        st.error(f"Оценка с ID {delete_id} для сериала не существует.")
                        return
                    delete_series_review(delete_id)
                    st.success("Операция выполнена успешно!")
            else:
                st.error("Введите ID оценки.")
