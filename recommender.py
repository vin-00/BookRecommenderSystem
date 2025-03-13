import streamlit as st

import numpy as np
import pickle

pt = pickle.load(open("pt.pkl","rb"))
similarity_scores = pickle.load(open("similarity_scores.pkl","rb"))
books = pickle.load(open("books.pkl","rb"))


def recommend(book_name ,number):
    book_idx = np.where(pt.index==book_name)[0][0]
    
    y= []
    number+=1
    similar_items = sorted(list(enumerate(similarity_scores[book_idx])), key=lambda x : x[1], reverse=True)[1:number]
    for i in similar_items:
        idx = i[0]
        temp = books[books['Book-Title']==pt.index[i[0]]].drop_duplicates('Book-Title')
        temp = temp.iloc[0]
        y.append({'title':temp['Book-Title'] , 'url':temp['Image-URL-L'] , 'author':temp['Book-Author']})
    return y


book_list = pt.index.tolist()


col1 , col2 = st.columns([3,1])
with col1 :
    book_name = st.selectbox(
        "Select a book",
        book_list
    )

with col2 :
    number = st.selectbox(
        "Number of recommendations",
        (5,10,15)
    )


if st.button("Recommend"):

    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    recommended_books = recommend(book_name , number)

    for i in range(number//5):
        columns = st.columns(5)
        for j in range(5):
            idx = i*5 + j

            with columns[j]:
                st.markdown(f"<h5>{recommended_books[idx]['title']}</h5>", unsafe_allow_html=True)
                st.write(recommended_books[idx]['author'])
                st.image(recommended_books[idx]['url'])

        
        st.write("")
        st.write("")
       
    
