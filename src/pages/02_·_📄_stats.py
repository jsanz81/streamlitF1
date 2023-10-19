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
st.image('../img/F1.png', width=300)
st.subheader('',divider ='red')


df=pd.read_csv('../csv/F1_Ml_original.csv')

# dummy DataFrame

c1,c2=st.columns([0.35,0.65])

with c1:
    stat=st.selectbox('Seleccionar',
                 ('Posiciones por año', 
                  'Media de posiciones por conductor. Top 10. (no year/team needed)',
                  'Media posiciones por equipo. Top 10. (no year/team needed)',
                  'Media posiciones equipo y sus conductores',
                  'Ganadores por GP/temporada'
                  ),
                  index=None,
                  placeholder='Choose a stat'
    )

    an=st.selectbox('year',
                        [2020,2021,2022,2023],
                        index=None,
                        placeholder='Choose a year'
                        )

    # dr=st.selectbox('driver',
    #                 ['alonso', 'sainz', 'max_verstappen', 'hamilton'])
    
    tm=st.selectbox('team',
                    ('ferrari', 'mercedes', 'mclaren', 'aston_martin','all'),
                    placeholder='Choose a team',
                    index=None
                    )
    
with c2:
    if st.button('Mostrar'):

        if stat==None: st.write(' 🡰 Choose a stat')
        
        else:
                if stat=='Posiciones por año':
                        st.write(pos_año(df,an))
                elif stat=='Media de posiciones por conductor. Top 10. (no year/team needed)':
                        st.write(media_pos_driver(df))
                elif stat=='Media posiciones por equipo. Top 10. (no year/team needed)':
                        st.write(media_pos_finales(df))
                elif stat=='Media posiciones equipo y sus conductores':
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
                               st.write('Choose a team')
                        else: st.write(media_team_driver(df,tm))
                elif stat=='Ganadores por GP/temporada':
                       if an==None:
                        st.write("  \n")
                        st.write("  \n")
                        st.write("  \n")
                        st.write("  \n")
                        st.write('Choose a year')
                       else: 
                             st.write(winner(df,an))


    # st.write('DATAFRAME EJEMPLO')
    # st.write(pd.DataFrame({'driver': ['alonso', 'rafa nadal', 'hamilton', 'schumacher', 'gasol', 'sainz', 'vettel', 'modric', 'kross','bellingham'],
    #                    'puesto': [1,2,3,4,5,6,7,8,9,10]}))


