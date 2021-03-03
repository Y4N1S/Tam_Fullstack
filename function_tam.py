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

def lines():
    df=download()
    lines_list=[]
    lines=(df['route_short_name'].tolist())
    for i in lines:
        if i not in lines_list:
            lines_list.append(i)
    return lines_list

def stations_and_lignes():
    df = download()
    result = {}
    result['stop_name'] = str(df.iloc[0][3])
    result['route_short_name'] = int(df.iloc[0][4])
    result['trip_headsign'] = str(df.iloc[0][5])
    return result

