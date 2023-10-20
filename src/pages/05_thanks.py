import streamlit as st

st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=150)
st.subheader('',divider ='red')

c1,c2,c3,c4=st.columns([0.2,0.3,0.1,0.4])

c1,c2=st.columns(2)

with c1:
    st.write('» agradecimientos')
with c2:
    st.write('A los profesores y compañeros de este bootcamp, ')
    st.write('por todo lo que hemos compartido y aprendido en estos meses')
    st.write(' Y lo que aun nos queda ...')
# with c3:
#     c=st.button('» Last click')

# with c4:
#     if c:
#         st.image('../img/ML_caricature.png', width=400)
    