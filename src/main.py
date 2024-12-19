import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from pages.auth_page import registration_page, login_page
from pages.add_content_page import add_content_page
from pages.delete_content_page import delete_content_page
from pages.comment_page import review_management_page
from pages.media_page import media_page
from pages.personal_account_page import user_dashboard
from pages.info_page import display_media_info
from pages.get_admin_id import show_id
from pages.admin_panel import admin_page
from pages.admin_data import admin_data_page

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "registration"

    if st.session_state.page == "registration":
        registration_page()
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "initial":
        if st.session_state.user_info[3] == "admin":
            st.title(f"Добро пожаловать, {st.session_state.user_info[1]}!")
            st.title(f"Ваша роль {st.session_state.user_info[3]}")

            st.sidebar.title("Навигация")
            page = st.sidebar.radio(
                "Перейти к странице",
                ["Добавить", "Удалить", "Рейтинг", "Информация о произведениях", "Получить id", "Ваши данные", "Админ-панель"],
            )
            if st.sidebar.button("Выход"):
                st.session_state.user_info = ()
                st.session_state.page = "registration"
                switch_page("main")

            if page == "Добавить":
                add_content_page()
            elif page == "Удалить":
                delete_content_page()
            elif page == "Рейтинг":
                media_page()
            elif page == "Информация о произведениях":
                display_media_info()
            elif page == "Получить id":
                show_id()
            elif page == "Ваши данные":
                admin_data_page()
            elif page == "Админ-панель":
                admin_page()
        else:
            st.title(f"Добро пожаловать, {st.session_state.user_info[1]}!")
            st.title(f"Ваша роль {st.session_state.user_info[3]}")

            
            st.sidebar.title("Навигация")
            page = st.sidebar.radio(
                "Перейти к странице",
                ["Оценка", "Рейтинг", "Личный кабинет", "Информация о произведениях"],
            )

            if st.sidebar.button("Выход"):
                st.session_state.user_info = ()
                st.session_state.page = "registration"
                switch_page("main")

            if page == "Оценка":
                review_management_page()
            elif page == "Рейтинг":
                media_page()
            elif page == "Личный кабинет":
                user_dashboard()
            elif page == "Информация о произведениях":
                display_media_info()


if __name__ == "__main__":
    main()
