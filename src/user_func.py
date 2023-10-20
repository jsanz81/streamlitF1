# clf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# reg
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score

import sys
import os
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder, PowerTransformer, QuantileTransformer, MinMaxScaler



'''
FUNCIONES CREADAS PARA USO DE PREDICCIONES Y MODELOS

'''


# Ruta del sistema
# print('sys.path', sys.path)


# print('working directory', os.getcwd())

# os.chdir(os.path.dirname(__file__))

# print(os.getcwd())

# sys.path.append(
#     os.path.abspath(os.path.join(
#         os.path.dirname(__file__), os.path.pardir
#     ))
# )

# print('PATH DIRNAME: ', os.path.dirname(__file__))
# print('PATH PARDIR: ', os.path.pardir)
# parent=os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
# print('ABSPATH: ', os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
# print(parent)




'''
GENERA DICCIONARIO CON SCORERS
MAE, MSE, RMSE, R2
y LO DEVUELVE

EN EL MÉTODO QUE LE LLAMA 
SE GUARDA EN OTRO DICT CON KEY: TIPO DE MODELO Y VALUE: ESTE DICT

'''

def validators_reg(y,p):
    # MAE
    mae=mean_absolute_error(y, p)
    # MSE (Mean Squared Error)
    mse=mean_squared_error(y, p)
    # RMSE (Root Mean Squared Error)
    rmse=np.sqrt(mean_squared_error(y, p))
    # r2
    r2=r2_score(y, p)

    dict={'MAE':mae,
          'MSE':mse,
          'RMSE':rmse,
          'R2':r2}
    print(dict)
    return dict



'''
SCORING DE CLASIFICACIÓN
ACCURACY
PRECISION
RECALL
F1

'''

# Imprime scoring de clasificación
def validators_clf(y,p):
    # accuracy
    print('Accuracy: ', accuracy_score(y, p))
    # precision
    #print('Precision: ', precision_score(y, p, average='macro'))

    # recall
    # print('Recall: ', recall_score(y, p))

    # f1
    print('F1: ', f1_score(y, p))



'''
Recibe y_test, y_pred.
Muestra df con ambas columnas y una tercera con su diferencia
Devuelve dataframe

'''
def comparador(y,p): 
    c=pd.DataFrame({'test': y, 'pred':p})
    c['round']=c.pred.round().astype(int)
    c['dif']=c['test']-c['round']
    c.sample(5)
    return c


# En el df pasado como argumento, ordena los valores de la predicción de menor a mayor, dando valores de 1 a n
# sin alterar el orden inicial del df
def ordenar_pred(df, col):

    for gp in df.track:
        # df temp recibe los valores de driver y predicción del campeonato que corresponda
        df_temp=df[['driver', col]][df.track==gp]
        df_temp.columns=['driver', 'pred'] # renombrar columnas, porque cada una vendrá con el nombre de un modelo distinto
        
        # ordena los valores de menor a mayor y resetea el index (0 a n)
        df_temp.sort_values(by='pred', inplace=True)
        df_temp.reset_index(drop=True, inplace=True)

        # replace la ultima columna, (cada vez va a ter un nombre), con el valor de index+1
        df_temp.pred=df_temp.index+1  # cambia el valor de pred por el de index+1 (1 a n+1)

        # pasamos los pares driver-pred a un diccionario
        dic_temp={d:p for d,p in zip(df_temp.driver,df_temp.pred)}

        # la columna predicciones recibe el valor segun el nombre del conductor del diccionario, para no alterar el orden
        df[df.columns[-1]][df.track==gp]=df.driver.map(dic_temp)
        df[df.columns[-1]][df.track==gp].astype('int64')

        # devolvemos el df
    return df