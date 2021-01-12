#imports
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from pathlib import Path

#functions

# Code door Niels van Schaik 18150845

# Main function die de dictionary returnt met de colums naar keuze binnen een set huizen.
# Deze functie vraagt om het begin en eind van de huizen reeks die je wilt inladen. dit is tot EN MET het einde
# De andere input is een simpele dictionary waarin je de sheetnamen stopt en de bijbehorende colums die je in de df wilt
# De student nummer is nodig voor de loadpath anders gaat het mis met de rechten (want rechten zijn kut).
def load(house_start: int, house_end: int, sheets_and_colums: dict, stdnt_nr: int):
    loadpath = '/home/' + str(stdnt_nr) + '/notebooks/zero/DATA/'
    check_values(house_start, house_end, sheets_and_colums, loadpath)
    houses_with_colums = {}
    for i in range(house_start, house_end + 1):
        houses_with_colums[i] = create_dataframe(i, sheets_and_colums, loadpath)
    return houses_with_colums

# houseswc[i] = dataframe house i
# Functie dat verwijst naar alle checkers en checkt zelf wat values
def check_values(house_start: int, house_end: int, sheets_and_colums: dict, loadpath: str):
    check_dict(sheets_and_colums)
    if house_start < 1:
        raise Exception("The first house can't be lower than 1.")
    if house_end > 120:
        raise Exception("There are no more then 120 houses in the database.")
    if house_start > house_end:
        raise Exception("Start house needs to be lower then end house.")
    try:
        np.load(loadpath + "solar_001.npy")
    except:
        raise Exception("coulden't load test data. Maybe something went wrong with the privileges or the student number")
    
    
# Checkt of de dictionary correct is opgesteld en de juiste variable types heeft
def check_dict(sheets_and_colums: dict):
    for sheet, colums in sheets_and_colums.items():
        if type(sheet) is not str:
            raise Exception("The keys of the dictionary needs te be a string.")
        for colum in colums:
            if colum < 1:
                raise Exception("The column number must be 1 or higher. (The index is already the timestamp and doesn't need to be in the dataframe)")
            if type(colum) is not int:
                raise Exception("The values of columns need to be defined in integers.")

                
# Maakt een df met de benodigde collomen van de gegeven dict
def create_dataframe(house: int, sheets_and_colums: dict, loadpath: str):
    house = nParse3(house)
    df = pd.DataFrame()
    for sheet, colums in sheets_and_colums.items():
        try:
            df_temp = pd.DataFrame(np.load(loadpath + sheet + '_' + house + '.npy'))
            df_temp = df_temp.set_index(pd.DatetimeIndex(pd.to_datetime(df_temp[0],unit='s').values))
            df_temp = df_temp.resample('5min').sum()
            for colum in colums:
                df[str(sheet) + "_" + str(colum)] = df_temp[colum]
        except:
            print("something went wrong with the data: " + loadpath + sheet + '_' + house + '.npy')
    return df

                
# Output a string that is 3 decimals long. Levy en Jefry kunnen uitleg geven
def nParse3(n):
    number = str(n)
    if len(number) == 1:
        number = "00" + number
    elif len(number) == 2:
        number = "0" + number
    elif len(number) == 3:
        number = number
    return str(number)