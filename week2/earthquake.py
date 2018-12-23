import pandas as pd
import numpy as np


def clean():
    df = read_csv('earthquake.csv')

    df1 = df[['time','latitude','longitude','depth','mag']]
    df2 = df[['place']]

    for i in range(0,len(df2)):
        if ',' in df2.iloc[i]['place']:
            df2.iloc[i]['place'] = df2.iloc[i]['place'].split(',')[1]
        else:
            df2.iloc[i]['place'] = np.nan

    df_clean = pd.concat([df1,df2],axis=1)

    df_clean = df_clean.dropna(axis=0,how='any')

    df_clean = df_clean.dropduplicates()

    df_clean.rename(columns={'place':'region'},inplace=True)

    return df_clean
