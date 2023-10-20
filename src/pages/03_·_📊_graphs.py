import streamlit as st
import glob
import importlib
import re
import pandas as pd
import numpy as np
import time
from strmlt_func import predecir, carousel_img, graficos, plot_4_drivers

st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=150)
st.subheader('',divider ='red')

# st.subheader('*** GRAPHS ***',divider ='red')

c1,c2,c3=st.columns([0.2, 0.5, 0.3])

with c1:
   
   # SELECCION DE CONDUCTORES Y AÑO PARA MOSTRAR GRÁFICO

    a=year=st.radio('year', options=[2020,2021,2022,2023], horizontal=True)
    sh=st.button('Show!')
    dr = st.multiselect(label='Driver',
                       options=['alonso','hamilton', 'max_verstappen', 'sainz'],
                       #default='alonso'
                       )
    
   

with c2:
    st.write('» Posiciones por carrera. Temporada {} «'.format(a))
    if sh:

        if (not a) & (not dr):
            st.text('Seleccionar año y al menos un piloto')
        elif (not a):
            st.text('Seleccionar Año')
        elif (not dr):
            st.text('Seleccionar al menos un piloto')
        else:
            st.write(graficos(dr, a))
            #st.write(plot_4_drivers())


