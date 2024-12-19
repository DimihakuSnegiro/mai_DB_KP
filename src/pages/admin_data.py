import streamlit as  st

def admin_data_page():
    st.write("Ваши данные")
    st.write(f"Ваш id: '{st.session_state.user_info[0]}'")
    st.write(f"Ваше имя: '{st.session_state.user_info[1]}'")
    st.write(f"Почта: '{st.session_state.user_info[2]}'")
    st.write(f"Роль: '{st.session_state.user_info[3]}'")
    st.write(f"Ваш аккаунт создан '{st.session_state.user_info[4]}'")