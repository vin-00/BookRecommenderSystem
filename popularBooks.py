import streamlit as st
import pickle

popular_df = pickle.load(open("popular_df.pkl","rb"))

popular_df = popular_df[(popular_df['Book-Title']!="The Hitchhiker's Guide to the Galaxy") & (popular_df['Book-Title']!="Outlander") & (popular_df['Book-Title']!="The Color Purple") ]

# These are added so that my website has some breathing space
st.write("")
st.write("")
st.write("")

st.header("Popular Books")

st.write("")
st.write("")


for i in range(10):
    columns = st.columns(5)

    for j in range(5):
        with columns[j]:
            with st.container():
                row = popular_df.iloc[i*5+j]
                st.markdown(f"<h5>{row['Book-Title']}</h5>", unsafe_allow_html=True)
                st.write("")
                st.write(row['Book-Author'])
                st.image(row['Image-URL-L'])
                col1 , col2 = st.columns(2)
                with col1 :
                    st.write("")
                with col2 :
                    st.button(str(round(row['avg_rating'], 1))+"  ⭐" , key=i*5+j)
    
    st.write("")
    st.write("")
    st.write("")

