import streamlit as st
import glob
import importlib
import re
import pandas as pd
import numpy as np
import time
from strmlt_func import predecir, carousel_img

st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=300)
st.subheader('',divider ='red')

st.write('» about me')
st.markdown('· A punto de graduarme en Data Scicence ...')
st.markdown('· Apasionado del la música, el deporte y ahora más que nunca de los datos')

st.text('· Podéis investigar un poco más este proyecto en: ')
url = "https://github.com/jsanz81/streamlitF1"
st.markdown("»»» [Github streamlitF1](%s)" % url)


