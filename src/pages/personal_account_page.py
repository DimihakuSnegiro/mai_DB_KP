import streamlit as st
import pandas as pd
from repositories.personal_account import get_user_statistics, get_user_reviews, get_user_info


def user_dashboard():
    st.title("Личный кабинет пользователя")
    USER_ID = st.session_state.user_info[0]
    
    option = st.selectbox("Выберите действие", (
        "Посмотреть статистику", 
        "Посмотреть свои комментарии",
        "Посмотреть информацию о юзере"
    ))

    if option == "Посмотреть статистику":
        stats = get_user_statistics(USER_ID)
        st.write("Статистика пользователя:")
        st.write(f"Общее количество оценок: {stats['movies_count'] + stats['series_count'] + stats['anime_count']}")
        st.write(f"Оценки фильмов: {stats['movies_count']}")
        st.write(f"Оценки сериалов: {stats['series_count']}")
        st.write(f"Оценки аниме: {stats['anime_count']}")
    
    elif option == "Посмотреть свои комментарии":
        category = st.selectbox("Выберите категорию", ("movies", "series", "anime"))
        reviews = get_user_reviews(USER_ID, category)

        if not reviews.empty: 
            st.write(f"Ваши отзывы в категории: {category}")
            st.dataframe(reviews, use_container_width=True)  
        else:
            st.write("Вы не оставляли отзывов в этой категории.")

    elif option == "Посмотреть информацию о юзере":
        user_info = get_user_info(USER_ID)

        if user_info:
            st.write("Информация о пользователе:")
            st.write(f"Имя пользователя: {user_info['username']}")
            st.write(f"Email: {user_info['email']}")
            st.write(f"Роль: {user_info['role']}")
            st.write(f"Дата регистрации: {user_info['created_at']}")
        else:
            st.write("Не удалось получить информацию о пользователе.")
