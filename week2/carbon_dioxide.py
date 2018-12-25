import pandas as pd
import numpy as np
def co2():
    #读取数据
    df_data = pd.read_excel('ClimateChange.xlsx',sheet_name ='Data')
    df_country = pd.read_excel('ClimateChange.xlsx',sheet_name ='Country')
    df_series = pd.read_excel('ClimateChange.xlsx',sheet_name ='Series')


    df_data.replace('..',np.NaN,inplace=True)#将..替换为0.
    df_co2 = df_data[df_data['Series code']=='EN.ATM.CO2E.KT'] #选择co2排放数据

    df_co2 = df_co2.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    df_co2.dropna(how='all', inplace=True)  

    
    a = df_co2.columns[list(range(6,28,1))] #选择不同年份的排放数据
    df_co2_emission = df_co2[a]
    df_co2_emission = df_co2_emission.astype('float')#转变为列

    df = df_co2[['Country name']]
    df['total_emission'] = df_co2_emission.apply(lambda x: x.sum(),axis=1)
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
