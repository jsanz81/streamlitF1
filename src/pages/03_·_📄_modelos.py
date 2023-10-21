import streamlit as st
import pandas as pd

st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=150)
st.subheader('',divider ='red')


dict_mae={'linear clasification':1.868421,
        'linear svr':1.885965,
        'svc':1.921053,
        'gradient boost regresor':1.938596,
        'svr':1.956140,
        'linear regresor':1.964912,
        'xgb':1.964912,
        'forest regresor':2.122807,
        'forest clasificatin':2.131579,
        'linear svc':2.333333,
        'gradiend boost clasification':2.491228,
        'tree clasification':2.578947,
        'tree regresion':2.614035
        }

pd_d=pd.DataFrame.from_dict([dict_mae])
pd_d=pd_d.T
pd_d.columns=['MAE']



c1,c2,c3=st.columns(3)

with c1:
    st.subheader('MODELOS SUPERVISADOS')
    st.dataframe(pd_d.sort_values(by='MAE'), height=14*35)
    st.caption('scoring MAE: Mean Absolute Error')

with c2:
    st.subheader('')
    st.write('Como librería de apoyo también se ha utilizado')
    st.write('Lazy Regressor')
    st.write('Que prueba de una vez varios modelos')
    st.write('Ofrece los siguientes como los de mejor scoring R2')
    st.text('GradientBoostingRegressor 0.65')
    st.text('ExtraTreesRegressor 0.62')
    st.text('RandomForestRegressor 0.61')
    st.text('XGBRegressor 0.57')
    st.write('')
    st.write('Ya que Gradient Boost Regresor está dentro de los modelos probados,lo seleccionamos para la parte final')

with c3:
    st.write('')