import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pickle, joblib
import sys, os

from sklearn.preprocessing import OneHotEncoder, PowerTransformer, QuantileTransformer, MinMaxScaler

from IPython.display import HTML

sys.path.append(os.path.dirname(os.getcwd()))

import warnings
warnings.filterwarnings("ignore")


# Ampliar tamaño columnas
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)

def predicciones():
    orig=pd.read_csv('../csv/F1_ML_original.csv')
    orig.drop(columns='Unnamed: 0', axis=1, inplace=True)
    for year in range(2023,2024):
        for GP in list(set(orig['track'][orig.year==year])):
            podio=pred(GP, year)
            print(podio[['driver', 'podium']].head(3))
    return None

def pred(GP,year):

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
        print(':::::'*12)
        print('PREDICCIÓN {} {} ····'.format(GP, year))
        pred=modelo.predict(df_pred)
        print(':::::'*12)

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



def parrilla(GP, year):
    orig=pd.read_csv('../csv/F1_ML_original.csv')
    orig.drop(columns='Unnamed: 0', axis=1, inplace=True)
    parrilla=orig[['driver', 'grid']][(orig.year==year)&(orig.track==GP)]
    return parrilla