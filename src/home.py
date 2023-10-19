
import streamlit as st
import glob
import importlib
import re
import pandas as pd
import numpy as np
import time
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from strmlt_func import carousel_img


st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=300)
st.subheader('',divider ='red')

st.write('PÁGINA DE INICIO')
c1,c2,c3=st.columns(3)
with c2:
    cont=st.container()
    carousel_img(cont) 
    
    # carrusel de imagenes de coches ::: revisar, modificar imagenes