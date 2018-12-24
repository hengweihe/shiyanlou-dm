import pandas as pd
import numpy as np


def clean():
    df = pd.read_csv('earthquake.csv')

    df1 = df[['time','latitude','longitude','depth','mag']]
    df2 = df[['place']]

    for i in range(0,len(df2)):
        if ',' in df2.iloc[i]['place']:
            df2.iloc[i]['place'] = df2.iloc[i]['place'].split(',')[1]
        else:
            df2.iloc[i]['place'] = np.nan

    df_clean = pd.concat([df1,df2],axis=1)

    df_clean = df_clean.dropna(axis=0,how='any')

    df_clean = df_clean.drop_duplicates()

    df_clean.rename(columns={'place':'region'},inplace=True)

    return df_clean



def mag_region():
    df = clean()
    df['mag'] = pd.cut(df.mag,bins=[0,2,5,7,9,50],right=False,labels=['micro','light','strong','major','great'])  #50随便选的一个很大的数字
    labels=['micro','light','strong','major','great']
    region = []
    times = []
    mag = []

    for mags in labels:
       if mags in df.mag.values:
           mag.append(mags)
           times.append(df[df.mag==mags].region.value_counts()[0])
           region.append(df[df.mag==mags].region.value_counts().index[0])
    df1 ={'mag':mag,'region':region,'times':times}


    
    df_final =pd.DataFrame(df1)
    df_final.set_index(['mag'],inplace=True)
    df_final.times = df_final.times.astype('int')

    
    return df_final
    
    
