import wget
import pandas
import logging
import os
from glob import glob

def download():
    for filename in glob("*.csv"):
        os.remove(filename)
    url='https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_TpsReel.csv'
    wget.download(url)
    csv=pandas.read_csv('TAM_MMM_TpsReel.csv',sep=';')
    return csv

def stations():
    df=download()
    station_list=[]
    stations=(df['stop_name'].tolist())
    for i in stations:
        if i not in station_list:
            station_list.append(i)
    return station_list

  

