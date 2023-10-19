import streamlit as st
import glob
import importlib
import re
import pandas as pd
import numpy as np
import time
import pickle
import os
import sys

# Get the parent directory
# print(os.pardir)
# parent_dir = os.path.dirname(os.path.realpath(__file__))
# print(parent_dir)
# print('sys.path', sys.path)
# Add the parent directory to sys.path

# par1=os.path.abspath(os.pardir)
# par2=os.path.abspath(par1)
# par3=os.path.abspath(par2)
# print(os.pardir)
# print(par1)
# print(par2)
# print(par3)

# sys.path.append(os.path.join(parent_dir, os.pardir))

sys.path.append(os.path.dirname(os.getcwd()))

#from ..src.predict import pred, predicciones, parrilla

from strmlt_func import predecir, parrilla, pred2



st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=100)
st.subheader('',divider ='red')



# DF CON PARRILLA DE SALIDA
# DRIVER | PARRILLA

c1, c2,c3 = st.columns([0.2,0.3,0.5])

df=pd.read_csv('../csv/F1_ML_con_prev.csv')
orig=pd.read_csv('../csv/F1_ML_original.csv')

listaGPs=list(set(orig['track'][orig.year.isin([2022,2023])]))
listaGPs.append("")
listaGPs.sort()

with c1:
    year=st.radio('year', options=[2022,2023], horizontal=True)
    GP=st.selectbox('GP', options=listaGPs)
    


# muestra parrilla de salida carrera elegida

with c2:
    st.write('::: Parrilla de Salida :::')
    if GP=="": 
        st.write('Elige GP')
    else:
        # check si existe esa carrera ese año
        gp_a=list(set(orig['track'][orig.year==year]))
        if GP in gp_a:
            st.write('{} {}'.format(GP, year))
            st.dataframe(parrilla(GP,year), hide_index=True)
        else:
             st.write('No se ha corrido esa carrera ese año')
             st.write('Elige otra')

    #st.write(df[(df.year==2023) & (df.track=='Qatar GP')][['driver', 'grid']].sort_values('grid'))
    # st.write(pd.DataFrame({'driver': ['alonso', 'rafa nadal', 'hamilton', 'schumacher', 'gasol', 'sainz', 'vettel', 'modric', 'kross','bellingham'],'puesto': [1,2,3,4,5,6,7,8,9,10]}))


# llamar a funcion predecir()


with c3:
    st.write('::: Predicción :::')
    if st.button("Predict"):
            if GP=="":
                 st.write(':::::'*12)
                 st.write('Elige GP')
            else:
                st.write('{} {} ····'.format(GP, year))
                podio=pred2(GP,year)
                st.dataframe(podio[['driver', 'podium']].head(3), hide_index=True)
                st.success('🏎️ 🏁 🏆')


# with c4:
#         st.write('')


