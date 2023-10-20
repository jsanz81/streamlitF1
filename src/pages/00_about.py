import streamlit as st

st.set_page_config(page_title="F1 Streamlit 🏆 🏁 🏎️ 🏎️ 🏎️ ",
                    page_icon="🏎️",
                    layout="wide")
#                    initial_sidebar_state='collapsed')

st.title('F1 Predictor 🏆 🏁 🏎️ 🏎️ 🏎️')
st.caption('Jose Alberto Sanz')
st.subheader('Streamlit project :: The Bridge Jun 2023', divider ='red')
st.image('../img/F1.png', width=150)
st.subheader('',divider ='red')


t1,t2,t3,t4,t5=st.tabs(['Problema', 'Soluciones', 'Modelos', 'Resultados/variables', 'Decisions/Consecuencias'])

with t1:
    st.subheader('¿Qué problema o necesidad vamos a resolver?')
    st.text('» Predicción lo más ajustada posible de los resultados de las carreras de Fórmula 1')
    st.subheader('¿Podemos solucionarlo con ML?')
    st.text('» ML ofrece soluciones idóneas para este tipo de problema,')
    st.text('ya que permite a partir de un conjunto de datos ordenado')
    st.text('con los resultados de todas las carreras,')
    st.text('entrenar diferentes modelos y proponer una clasificación y comprobar su fiabilidad')

with t2:
    st.subheader('¿Qué solución aporta tu modelo de ML?')
    st.text('» Devuelve una lista ordenada con la predicción del podio de una carrera')
    st.text('» Para carreras futuras, necesitamos al menos')
    st.text('la información del puesto de parrilla de salida de esa carrera')
    st.caption('* Por falta de tiempo, no podemos predecir el resultado de la carrera de este fin de semana')

with t3:
    st.subheader('¿Qué modelos has probado?')
    st.text('lineal, arbol, forest, gradiante, super vector machine')
    st.text('» Todos supervisados')
    st.text('» Para el entrenamiento tenemos todos los resultados de cada carrera')
    st.text('» Tanto de clasificación, como de regresión:')
    st.text('» El resultado final debe ser un entero')
    st.text('» En los casos de regresión, se han ordenado los resultados de menor a mayor, para componer el podio')

with t4:
    st.subheader('¿Qué resultados y conclusiones has obtenido?')
    st.text('» Hay varios modelos que han dado un resultadoc on media por debajo de 2 puestos respecto a la clasificación real')

    
    st.subheader('¿Cuáles han sido las variables de mayor impacto?')

    t4c1, t4c2, t4c3=st.columns([0.1,0.4,0.5])
    with t4c1:
            b=st.button('» heatmap')
    with t4c2:
            if b:
                st.text('» heatmap/correlación')
                st.image('../img/heatmap_f1_original.png', caption='heatmap Variables F1')

                st.write('Una vez terminado el dataset final con los datos de las carreras anteriores:')
                st.text('» baseline: arbol de regresión')
                st.text('Feature Importances:')
                st.text('grid: con un 0.5')                        
                st.text('puntos en la carrera anterior: 0.05')
                st.text('Circuito: 0.04')

    with t4c3:
         if b:
            st.write('» heatmap zoom')
            st.image('../img/heatmap_f1_original_2.png', caption='heatmap zoom')


with t5:
    st.subheader('¿Qué decisiones o acciones te permiten llevar a cabo tu modelo? ¿Qué consecuencias tiene en negocio?')

    st.write("Dos enfoques:")
    st.write('» Personal:')
    st.write('Frivolizando, puede servir como aliciente para las apuestas deportivas')
    st.write('» Profesional:')
    st.write('Suponiendo que este trabajo este dedicado a un equipo, lo ideal sería que ayudara al equipo a tomar decisiones estratégicas en caso de que haya que priorizar a un piloto')

    


