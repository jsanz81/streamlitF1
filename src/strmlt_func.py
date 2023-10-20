import time
import pandas as pd
import numpy as np 
import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pickle
import joblib
import glob

import sys
import os

from sklearn.ensemble import GradientBoostingRegressor

sys.path.append(os.path.dirname(os.getcwd()))

'''

FUNCIONES CUSTOM PARA STREAMLIT


'''

# print('sys.path', sys.path)
# print(os.getcwd())

def parrilla(GP, year):
        
    orig=pd.read_csv('../csv/F1_ML_original.csv')
    orig.drop(columns='Unnamed: 0', axis=1, inplace=True)

    drivers=pd.read_csv('../csv/drivers.csv')
    #drivers.drop(columns='Unnamed: 0', axis=1, inplace=True)
    
    # diccionario de ids de drivers
    # alonso:4
    dict_drivers={id:d for id, d in zip(drivers.driverId,drivers.driverRef)}  

    # id de la carrera 
    race=set(orig['race'][(orig.year==year)&(orig.track==GP)])
    race=race.pop()

    results=pd.read_csv('../csv/results.csv')
    results=results[results.raceId==race]

    results['driver']=results['driverId'].map(dict_drivers)
    
    parrilla=results[['driver', 'grid']]
    parrilla.columns=['piloto', 'grid']

    # si alguna posición es 0, ha salido desde el pit_stop,, cambiar poe 23
    # cambiar por 
    parrilla.replace(0,23, inplace=True)
    return parrilla.sort_values('grid')
    

def res_real(GP, year):
        
    orig=pd.read_csv('../csv/F1_ML_original.csv')
    orig.drop(columns='Unnamed: 0', axis=1, inplace=True)

    drivers=pd.read_csv('../csv/drivers.csv')
    #drivers.drop(columns='Unnamed: 0', axis=1, inplace=True)
    
    # diccionario de ids de drivers
    # alonso:4
    dict_drivers={id:d for id, d in zip(drivers.driverId,drivers.driverRef)}  

    # id de la carrera 
    race=set(orig['race'][(orig.year==year)&(orig.track==GP)])
    race=race.pop()

    results=pd.read_csv('../csv/results.csv')
    results=results[results.raceId==race]

    results['driver']=results['driverId'].map(dict_drivers)
    
    real=results[['driver', 'position']]
    real.columns=['piloto', 'podium']
    real.sort_values('podium')
    return real


# Devuelve los datos de la siguiente carrera, en este caso, la última es Qatar

def predecir(): 
    # Leer modelo gradientboost
    # with open('../modelos/grid_gb_reg.pkl', 'rb') as gb:
    #     gb_reg = pickle.load(gb)

    # cargar:
    gb_reg=joblib.load('../modelos/grid_forest_reg.pkl')

    # seleccionar última carrera
    df=pd.read_csv('../csv/F1_ML_con_prev.csv')
    df.drop(columns=('Unnamed: 0'), axis=1, inplace=True)
    df_qatar=df[(df.year==2023)&(df.track=='Qatar GP')]

    # SOLO MUESTRA RESULTADOS REALES, NO ESTÁ PREDICIENDO
    st.write(df_qatar[['track','driver','grid', 'position']].head(3))
    # predecir la posición
    #pred=gb_reg.predict(df_qatar.drop(columns=('position'))) 

    
    # concatenar tabla con conductor y posición inicial con la predicción. Mostrar podio

    #podio=pd.concat([df_qatar[['team','driver', 'grid']], pred], columns=['team','driver','grid', 'podium'])
    #st.write(podio.sort_values('podium').head(3))
    
    # tabla dummy de ejemplo
    # st.write('Predicción Japón 2023')
    # st.write(pd.DataFrame({'driver': ['alonso','gasol', 'rafa nadal'],'puesto': [1,2,3]}))
    
    return None

def pred2(GP,year):

    # df original
    orig=pd.read_csv('../csv/F1_ML_original.csv')
    orig.drop(columns='Unnamed: 0', axis=1, inplace=True)

    # df con datos previos
    prev=pd.read_csv('../csv/F1_ML_con_prev.csv')
    prev.drop(columns='Unnamed: 0', axis=1, inplace=True)

    # df con dummies y scaler y 4 columnas con datos originales 
    # 'track', 'year', 'driver', 'team', 'grid'
    # para seleccionar/filtrar antes de pasar al modelo
    df_encoded=pd.read_csv('../csv/df_encoded.csv')
    df_encoded.drop(columns='Unnamed: 0', axis=1, inplace=True)

    # check si esa carrera existe ese año
    # lista de GPS el año elegido
    listaGPs=list(set(df_encoded['track_orig'][df_encoded.year_orig==year]))

    if GP in listaGPs:
        carrera=df_encoded[(df_encoded.year_orig==year)&(df_encoded.track_orig==GP)]

        # quitamos las 4 columnas con datos originales

        df_pred=carrera.loc[:,~carrera.columns.str.contains('_orig')]
        # print(carrera.head(1))


        # # leer modelo
        modelo=joblib.load('../modelos/grid_forest_reg.pkl')
        # print(modelo)

        # # predecir
        
        pred=modelo.predict(df_pred)
        

        final=carrera.loc[:,carrera.columns.str.contains('_orig')]

        final['pred']=pred

        # podio ordena las predicciones
        podio=final.sort_values(by='pred').reset_index(drop=True)
        podio['podio']=podio.index+1

        podio.columns=(['GP','year','driver', 'team', 'grid', 'pred', 'podium'])
        # print(podio[['GP', 'driver','podium']].head(3))
        return podio

    else: 
      
        return None


def carousel_img(contenedor): # hay 4 imagenes de coches car1, car2, car3, car4

    lista_coches=[imgcar for imgcar in glob.glob('../img/car*.png')]
    while True:
        # cargar imagen
        for car in lista_coches:
            contenedor=st.image(car)
            time.sleep(3) # 0.5 segundos por imagen
            contenedor.empty()


def return_df(df):
     # devuelve última carrera para predecir
    return df[(df.year==2023)&(df.track=='Qatar GP')]



# devuelve grafico segun datos pasados
# dr: driver. por defecto "alonso"
# an: año. por defecto 2023

def graficos(dr='alonso',an=2023):
    # tiene todos los datos reales
    # devolver grafico según datos 
    # lee f1_original
    # nombre carrera | conductor | posicion | puntos |
    df=pd.read_csv('../csv/F1_ML_original.csv')

    
    for d in dr:
        # si el piloto no corrió  ese año
        
        if d not in list(set(df['driver'][df.year==an])):
               st.write(':red[{}] no partició la temporada {}'.format(d,an))

        
        fig, ax=plt.subplots()
                        
        ax.set_xlabel("GP", color='red')
        ax.set_ylabel("Position", c='red')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines[['left', 'bottom']].set_color('red')
        ax.tick_params(colors='red')
        ax.invert_yaxis()
        ax.set_yticks(range(1, 18)) # rango de posiciones 1-18
        ax.set_ylim(18, 1)
        plt.grid(visible=True, alpha=0.1, color='grey')
        plt.margins(tight=True)
        plt.ylim(18,0)
        #plt.xlim(0,15)
        plt.xticks(rotation = 70, fontsize='small')


        
        
        res=df[['track','driver', 'team', 'grid', 'position', 'points']][(df.driver.isin(dr))&(df.year==an)]
        
        sns.lineplot(data=res, x=res.track,y=res.position, hue='driver', palette='rocket', marker='o', alpha=0.5)
        sns.move_legend(ax, "lower center",
                        bbox_to_anchor=(.5,1),  
                        ncols=4,
                        title=None, 
                        frameon=False)

    return fig



# Devuelve gráfica con plot de posiciones durante el año
def plot_4_drivers(): # customizar para uno o mas conductores (usar st.multiselect)

    df=pd.read_csv('../csv/F1_ML_original.csv')
    df=df[df.year==2023][['track','driver','position']].reset_index(drop=True)

    sns.set(rc={'figure.figsize':(12,9)})
    
    fig, ax = plt.subplots()
    ax.set_title("Resultados 2023")
    ax.set_xlabel("GP")
    ax.set_ylabel("Position")
    ax.grid(False) # quitar la cuadricula
    ax.set_yticks(range(1, 18)) # rango de posiciones 1-18
    ax.set_ylim(18,1)
    ax.invert_yaxis() # invertir eje y, para que el 1 salga arriba

    sns.lineplot(data=df[df.driver.isin(['alonso', 'sainz', 'max_verstappen', 'perez', 'hamilton'])],
            x='track', 
            y='position', 
            #color=dict_colores[driver],
            hue='driver',
        )
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.xticks(rotation = 45)
    #plt.show();
    
    return fig  # devuelve la figura con los datos


'''
 SUMA DE VECES QUE HA QUEDADO CADA PILOTO EN UNA POSICIÓN EN UN AÑO
'''

# Hay que pasarle el df original o un slice, según el año
def pos_año(f1_original, año=2023): # por defecto, año en curso
# devuelve tabla pivotada con la suma de puestos de cada piloto el año elegido
    return f1_original[f1_original.year==año].pivot_table(index='driver', 
                                                           columns=['year', 'position'], 
                                                           values='total_race_time', 
                                                           #margins=True,
                                                           aggfunc='count',
                                                           fill_value='--'
                                                           )



'''
 MEDIA GENERAL DE POSICIONES FINALES, EN LAS CARRERAS POR EQUIPO
'''
# Mejores equipos Mercedes/Red Bull
def media_pos_finales(df):
        return df.groupby('team').agg({'position':'mean', 'race':'count'}).sort_values(['position']).head(10)


'''
 MEDIA GENERAL DE POSICIONES FINALES, EN TODAS LAS CARRERAS POR CONDUCTOR. TOP TEN
'''

# hamilton y max_verstappen
def media_pos_driver(df):
    return df.groupby('driver').agg({'position':'mean', 'race':'count'}).sort_values(['position']).head(10)


'''
 MEDIA GENERAL DE POSICIONES FINALES, EN TODAS LAS CARRERAS POR EQUIPO Y DESGLOSADO CADA CONDUCTOR
'''

def media_team_driver(df,tm):
    # media de posiciones finales por equipo y conductor
    if tm=='all': # devuelve todo
        return df.groupby(['team', 'driver']).agg({'position':'mean', 'race':'count'}).sort_values(['team', 'position'])
    else: # si se le pasa un equipo(o lista de equipos), devuelve solo esos
        return df[df.team==tm].groupby(['team', 'driver']).agg({'position':'mean', 'race':'count'}).sort_values(['team', 'position'])



# ganador de cada carrera una temporada

def winner(df, yr=2023):
    return df[df.year==yr][['track','driver']][df.position==1]

