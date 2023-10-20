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


dict_mae={'linear regression' : 2.230905633223684,
        'logistic regression' : 2.7017543859649122,
        'tree clasiffication' : 2.6491228070175437,
        'tree regression' : 3.06140350877193,
        'forest clasiffication' : 2.6666666666666665,
        'forest regression' : 2.1228070175438596,
        'gradient boost regressor' : 2.01781871966688,
        'gradient boost classifier' : 2.7982456140350878,
        'linear svc' : 3.1008771929824563,
        'linear svr' : 2.5219298245614037,
        'svc' : 2.9210526315789473,
        'svr' : 2.587719298245614,
        'xgboost' : 2.258771929824561}

pd_d=pd.DataFrame.from_dict([dict_mae])
pd_d=pd_d.T
pd_d.columns=['MAE']


c1,c2,c3=st.columns(3)

with c1:
    st.subheader('MODELOS SUPERVISADOS')
    st.dataframe(pd_d.sort_values(by='MAE'), height=14*35)
    st.caption('scoring MAE: Mean Absolute Error')
with c2:
    st.write('')    
with c3:
    st.write('')