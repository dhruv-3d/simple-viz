import pandas as pd
import numpy as np


def load_data():
    print('\nReading the data...\n')

    xl = pd.ExcelFile('./PCPwr.xlsx')
    df = xl.parse('Sheet1')

    print('\nPreparing the data...\n')    

    df.rename(columns = {'Start-Time ':'Start-Time'}, inplace = True) 
    df['Start-Time'] = pd.to_datetime(df['Start-Time'], format="%d/%m/%Y %H:%M:%S")
    df['Up-Time'] = (df['Start-Time'] - df['Start-Time'].shift()) / np.timedelta64(1, 'h')
    df['Dates'] = df['Start-Time'].dt.date

    # df = df.assign(UPTime = lambda x: (x['Start-Time'] - x['Start-Time'].shift()))


    # data = df['UPTime'][1]
    print(df.head())

    return df
