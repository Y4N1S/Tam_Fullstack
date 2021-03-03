import wget
import pandas
import logging
import os
if "TAM_MMM_TpsReel.csv" :
def download():
    url='https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'
    wget.download(url)
    csv=pandas.read_csv('TAM_MMM_TpsReel.csv',sep=';')
    return csv

def stations():
    df=download()
    stations=set(df['stop_name'].tolist())
    return stations


  

