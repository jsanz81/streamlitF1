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


t1,eda,t2,t3,t4,t5=st.tabs(['Problema', 'EDA', 'Soluciones', 'Modelos', 'Resultados/variables', 'Decisions/Consecuencias'])


with t1:
    st.subheader('¿Qué problema o necesidad vamos a resolver?')
    st.text('» Predicción lo más ajustada posible de los resultados de las carreras de Fórmula 1')
    st.subheader('¿Podemos solucionarlo con ML?')
    st.text('» ML ofrece soluciones idóneas para este tipo de problema,')
    st.text('ya que permite a partir de un conjunto de datos ordenado')
    st.text('con los resultados de todas las carreras,')
    st.text('entrenar diferentes modelos y proponer una clasificación y comprobar su fiabilidad')

with eda:
     st.write('Si recordamos el EDA de Julio, de este dataset, nos enfocamos en los tiempos de pitstop y su influencia en la mejora de resultados finales')
     st.write("Estos resultados se veian mejorados siempore que la variable equipo estaba incluida, por lo que hemos decidido mantener esas variables creadas, como la media de pitstop de cada piloto")
     st.write('Si se ha a aumentado unos segundos la barrera de corte de tiempo de pitstop, hasta los 38000ms, asi como solo los pilotos que han terminado la carrera ')

with t2:
    st.subheader('¿Qué solución aporta tu modelo de ML?')
    st.text('» Devuelve una lista ordenada con la predicción del podio de una carrera')
    st.text('Tras el estudio del dataset, realizado en Julio,')
    st.write('vimos que los tiempos de pit_Stop influian notablemnente en el resultado de carrera, siempre que el equipo estuviera agrupado de alguna manera, fuera team/piloto, o team/rango temporal')
    st.write('Por ello, hemos decidido dejar los valores de media de pitstop de cada carrera en este dataset como variable')
    st.write('junto al circuito, parrilla de salida, vuelta rapida, nº de vueltas, puntos, podio')
    st.write('La ultima parte previa al modelado, ha consistido en hacer un lag de los datos ropios de cada carrera y agruparlos justo con la carrera anterior')
    st.write('para no desvirtuar el modelo sobreentrenándolo al darle los resultados antes de predecirlos')
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

with t4:
    st.subheader('¿Qué resultados y conclusiones has obtenido?')
    st.text('» Hay varios modelos que han dado un resultado con una media de error absoluto por debajo de 2 puestos respecto a la clasificación real')

    
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
    st.write('Este modelo debe ayudar al equipo a tomar decisiones estratégicas en caso de que haya que priorizar a un piloto')

    


