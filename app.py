import streamlit as st
import pickle
import requests

movies=pickle.load(open('MovRec.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

MovRec= movies['title'].values

st.header("Movie Recommender System")
select_val= st.selectbox("Select A Movie From The Dropdown", MovRec)



def recommend(movie):
  index=movies[movies['title']==movie].index[0]
  distance= sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
  rec_mov= []
  for i in distance[1:]:
    movies_id=movies.iloc[i[0]].id
    rec_mov.append(movies.iloc[i[0]].title)

  return rec_mov  



if st.button("Recommend Shows to Watch"):
    mov_name= recommend(select_val)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
       st.text(mov_name[0])
    with col2:
       st.text(mov_name[1])
    with col3:
       st.text(mov_name[2])
    with col4:
       st.text(mov_name[3])
    with col5:
       st.text(mov_name[4])
    pass


