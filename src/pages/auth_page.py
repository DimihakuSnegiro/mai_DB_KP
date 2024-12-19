import streamlit as st
from repositories.auth_conn import reg_new_user, check_auth_user, return_user_data,check_new_user_login, check_new_user_email
from services.input_validation import valid_login, valid_email, valid_password

def registration_page():
    st.title("Регистрация")

    login = st.text_input("Логин")
    email = st.text_input("Электронная почта")
    password = st.text_input("Пароль", type='password')
    role = st.selectbox(
        "Выберите роль",
        ["user", "admin"],
        index = 0
    )

    if st.button("Зарегистрироваться"):
        if login and email and role and password:
            if (not valid_login(login)):
                st.error("Некорректный логин")
            elif (not valid_email(email)):
                st.error("Некорректный email")
            elif (not valid_password(password)):
                st.error("Некорректный пароль")
            else:
                if check_new_user_login(login):
                    if check_new_user_email(email):
                        st.success("Вы успешно зарегистрированы!")

                        reg_new_user(login, email, role, password)

                        user_data = return_user_data(login, password)
                        st.session_state.user_info = user_data
                        st.session_state.page = "initial"
                    else:
                        st.error("Пользователь с такой почтой уже существует")
                else:
                    st.error("Пользователь с таким логином уже есть")

        else:
            st.error("Пожалуйста, заполните все поля.")

    if st.button("Уже есть аккаунт? Войти"):
        st.session_state.page = "login"


def login_page():
    st.title("Вход в аккаунт")

    login = st.text_input("Логин")
    password = st.text_input("Пароль", type='password')

    if st.button("Войти"):
        if login and password:
            if (check_auth_user(login, password)):
                st.error("Неправильный логин или пароль")
            else:
                st.success("Вы успешно вошли в аккаунт!")
                user_data = return_user_data(login, password)
                st.session_state.user_info = user_data
                st.session_state.page = "initial"
        else:
            st.error("Пожалуйста, введите логин и пароль.")

    if st.button("Нет аккаунта? Зарегистрироваться"):
        st.session_state.page = "registration"