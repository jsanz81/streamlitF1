import streamlit as st

st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=100)
st.subheader('',divider ='red')


t1,t2,t3,t4,t5,t6=st.tabs(['Problema', 'Soluciones', 'Modelos', 'Resultados/Conclusiones', 'Variables', 'Decisions/Consecuencias'])

with t1:
    st.subheader('¿Qué problema o necesidad vamos a resolver?')
    st.text('Predicción lo más ajustada posible de los resultados de las carreras de Fórmula 1')
    st.subheader('¿Podemos solucionarlo con ML?')
    st.text('ML ofrece soluciones idóneas para este tipo de problema,')
    st.text('ya que permite a partir de un conjunto de datos ordenado')
    st.text('con los resultados de todas las carreras,')
    st.text('entrenar diferentes modelos y comprobar su fiabilidad')

with t2:
    st.subheader('¿Qué solución aporta tu modelo de ML?')
    st.text('Devuelve una lista ordenada con la predicción del podio de una carrera')
    st.text('Para carreras futuras, necesitamos al menos')
    st.text('la información del puesto de parrilla de salida de esa carrera')

with t3:
    st.subheader('¿Qué modelos has probado?')
    st.text('Todos supervisados')
    st.text('Para el entrenamiento tenemos todos los resultados de cada carrera')
    st.text('Tanto de clasificación, como de regresión:')
    st.text('El resultado final debe ser un entero')
    st.text('En los casos de regresión, se han ordenado los resultados de menor a mayor, para componer el podio')

with t4:
    st.subheader('¿Qué resultados y conclusiones has obtenido?')
    st.text('Gradient Boost Regressor, es el que mejor resultado ha ofrecido')
    
with t5:
    st.subheader('¿Cuáles han sido las variables de mayor impacto?')
    st.text('heatmap/feature importances')
    st.image('../img/heatmap_f1_original.png', caption='heatmap Variables F1')
    st.text('baseline: feature importances, con un arbol de regresión')
    st.text('')

with t6:
    st.subheader('¿Qué decisiones o acciones te permiten llevar a cabo tu modelo? ¿Qué consecuencias tiene en negocio?')
    st.write()

