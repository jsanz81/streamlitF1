# clf
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# reg
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score

import sys
import os
import pandas as pd
import numpy as np
import streamlit as st

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
    # recall
    print('Precission: ', precision_score(y, p))

    # precission
    print('Recall: ', recall_score(y, p))

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


