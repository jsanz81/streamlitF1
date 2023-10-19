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


st.subheader('*** INFO ABOUT ME ***',divider ='red')
st.write('github link')

st.write('*** INFO ABOUT PROJECT ***')
