import streamlit as st
from streamlit_effects import fireworks
st.set_page_config(page_icon="😇", page_title="For-Fun", layout= "wide")
tab1, tab2, tab3  = st.tabs(["Про этот сайт", "Что-то", "Эксперименты"])

with tab1:
    st.title("Приветствую, Вопросы,for fun")
    st.header("Здесь я делаю прикольные штучки")
    col1, col2, col3 = st.columns([1,2,3])
with col3:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1PnerTq2zJZms9SgmrUk1Yjr9lTM1opuS9kMdMq2XjA&s=10", width= 500)
    
        
with tab3:
    score = 0
    st.title("Вопросы")
    q1 = st.radio("Что лутчше использывать в 2026?" , ["LCI", "Dekstop","Website"])
    if st.button("Проверить", key=12345):
        if q1 is None:
            st.warning("Нажми на кнопку")
        else:
            score = 1 if q1 == "Website" else 0 
        st.subheader(f"Результат:{score} из 1")
        if score == 1:
            st.success("Правильно ответил")
            fireworks(duration=5)
            st.progress(1/3)
        else:
            st.progress(0/3)
            st.error("Не правильно")

with tab3:
    score = 1
    st.title("Вопросы")
    q1 = st.radio("Начем я делал этот сайт?" , ["Python+Streamlit", "Pythin","JavaScript"])
    if st.button("Проверить", key=123456):
        if q1 is None:
            st.warning("Нажми на кнопку")
        else:
            score = 2 if q1 == "Python+Streamlit" else 1 
        st.subheader(f"Результат:{score} из 2")
        if score == 2:
            st.success("Правильно ответил")
            fireworks(duration=5)
            st.progress(2/3)
        else:
            st.progress(1/3)
            st.error("Не правильно")


with tab3:
    score = 2
    st.title("Вопросы")
    q1 = st.radio("Какой язык легче?" , ["Java", "Python","JavaScript"])
    if st.button("Проверить", key=123456797):
        if q1 is None:
            st.warning("Нажми на кнопку")
        else:
            score = 3 if q1 == "Python"  else 2 
        st.subheader(f"Результат:{score} из 3")
        if score == 3:
            st.success("Правильно ответил")
            st.balloons()
            st.progress(3/3)
        else:
            st.progress(2/3)
            st.error("Не правильно")


