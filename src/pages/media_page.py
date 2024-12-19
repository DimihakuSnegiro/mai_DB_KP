import streamlit as st
from repositories.get_media_data import get_media_data

def media_page():
    st.title("Media Ratings Viewer")

    category = st.selectbox("Choose a category", ["Movies", "Series", "Anime"])

    df = get_media_data(category)

    if "sort_order" not in st.session_state:
        st.session_state.sort_order = None

    sort_order = st.radio("Sort by rating", ["Ascending", "Descending", "Reset"], index=2)

    if sort_order == "Ascending":
        df_sorted = df.sort_values("average_rating", ascending=True)
        st.session_state.sort_order = "Ascending"
    elif sort_order == "Descending":
        df_sorted = df.sort_values("average_rating", ascending=False)
        st.session_state.sort_order = "Descending"
    else:
        if st.session_state.sort_order == "Ascending":
            df_sorted = df.sort_values("average_rating", ascending=True)
        elif st.session_state.sort_order == "Descending":
            df_sorted = df.sort_values("average_rating", ascending=False)
        else:
            df_sorted = df

    st.dataframe(df_sorted, use_container_width=True)