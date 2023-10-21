import streamlit as st
import glob
import importlib
import re
import pandas as pd
import numpy as np
import time
from strmlt_func import pos_año, media_pos_finales, media_pos_driver, media_team_driver, winner

st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=150)
st.subheader('',divider ='red')


df=pd.read_csv('../csv/F1_Ml_original.csv')

# dummy DataFrame

c1,c2=st.columns([0.35,0.65])

with c1:

    stat=st.selectbox('Seleccionar',
                 ('Media de posiciones por piloto. (Top 10 2011-2023)',
                  'Media posiciones por equipo. (Top 10 2011-2023)',
                  'Posiciones por año (seleccionar Año)', 
                  'Media posiciones equipo y sus pilotos (Elegir equipo)',
                  'Ganadores por GP/temporada'
                  ),
                  index=None,
                  placeholder='Elegir stat'
    )

    an=st.selectbox('year',
                        [2020,2021,2022,2023],
                        index=None,
                        placeholder='Elegir año'
                        )

    
    tm=st.selectbox('team',
                    ('ferrari', 'mercedes', 'mclaren', 'aston_martin','all'),
                    placeholder='Elegir equipo',
                    index=None
                    )
    
with c2:
    if st.button('Mostrar'):

        if stat==None: st.write(' 🡰 Elegir stat')
        
        else:
                if stat=='Posiciones por año (seleccionar Año)':
                        if an==None: st.write('Elegir Año')
                        else: st.write(pos_año(df,an))
                elif stat=='Media de posiciones por piloto. (Top 10 2011-2023)':
                        st.write(media_pos_driver(df))
                elif stat=='Media posiciones por equipo. (Top 10 2011-2023)':
                        st.write(media_pos_finales(df))
                elif stat=='Media posiciones equipo y sus pilotos (Elegir equipo)':
                        if tm==None: 
                               st.write("  \n")
                               st.write("  \n")
                               st.write("  \n")
                               st.write("  \n")
                               st.write("  \n")
                               st.write("  \n")
                               st.write("  \n")
                               st.write("  \n")
                               st.write("  \n")
                               st.write('Elige un equipo')
                        else: st.write(media_team_driver(df,tm))
                elif stat=='Ganadores por GP/temporada':
                       if an==None:
                        st.write("  \n")
                        st.write("  \n")
                        st.write("  \n")
                        st.write("  \n")
                        st.write('Elegir año')
                       else: 
                             st.write(winner(df,an))


    # st.write('DATAFRAME EJEMPLO')
    # st.write(pd.DataFrame({'driver': ['alonso', 'rafa nadal', 'hamilton', 'schumacher', 'gasol', 'sainz', 'vettel', 'modric', 'kross','bellingham'],
    #                    'puesto': [1,2,3,4,5,6,7,8,9,10]}))


