import pandas as pd
import numpy as np
def co2():
    #读取数据
    df_data = pd.read_excel('ClimateChange.xlsx',sheet_name ='Data')
    df_country = pd.read_excel('ClimateChange.xlsx',sheet_name ='Country')
    df_series = pd.read_excel('ClimateChange.xlsx',sheet_name ='Series')


    df_data = df_data[df_data['Series code'] =='EN.ATM.CO2E.KT']
    a = df_data.columns[list(range(6,28,1))]
    df_co2_emission = df_data[a]
    df_co2_emission.replace({'..': pd.np.NaN}, inplace=True)
    data = df_co2_emission.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    data.dropna(how='all', inplace=True)
    df = df_data[['Country name']]
    df['total_emission'] = data.apply(lambda x: x.sum(),axis=1)
    df = df[df['total_emission']!=0]




    
    
    df_country_new = df_country[['Country name','Income group']]
    df_final=pd.merge(df,df_country_new,left_on='Country name',right_on='Country name')
    
    

    df_emission_total= df_final.groupby(by='Income group').sum() #sum_emission 
    df_max = df_final.groupby(by='Income group').max() #max_emission 
    df_min=df_final.groupby(by='Income group').min() #max_emission 

    temp =pd.merge(df_emission_total,df_max,on='Income group')
    results = pd.merge(temp,df_min,on='Income group')


    name = ['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
    results.columns = name

    return results
