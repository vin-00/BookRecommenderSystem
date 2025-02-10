import streamlit as st

st.title("Book recommendation System")

pg = st.navigation([st.Page("popularBooks.py" , title='Popular Books'), st.Page("recommender.py", title='Get a recommendation')])
pg.run()

