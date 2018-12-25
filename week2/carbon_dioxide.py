import pandas as pd

def co2():
    df_data = pd.read_excel('ClimateChange.xlsx',sheet_name ='Data')
    df_country = pd.read_excel('ClimateChange.xlsx',sheet_name ='Country')
    df_series = pd.read_excel('ClimateChange.xlsx',sheet_name ='Series')


    df_data.replace('..','0',inplace=True)#将。。替换为0
    df_co2 = df_data[df_data['Series code']=='EN.ATM.CO2E.KT']

    
    a = df_co2.columns[list(range(6,28,1))] #??????????
    df_co2_emission = df_co2[a]
    df_co2_emission = df_co2_emission.astype('int')

    df = df_co2[['Country code','Country name','Series code','Series name']]
    df['total_emission'] = df_co2_emission.apply(lambda x: x.sum(),axis=1)
    df = df[df['total_emission']!=0]

    df_country_new = df_country[['Country code','Income group']]
    df_final=pd.merge(df,df_country_new,left_on='Country code',right_on='Country code')

    df_emission_total= df_final.groupby(by='Income group').sum() #sum_emission 
    df_max = df_final.groupby(by='Income group').max() #max_emission 
    df_min=df_final.groupby(by='Income group').min() #max_emission 

    temp =pd.merge(df_emission_total,df_max,on='Income group')
    results = pd.merge(temp,df_min,on='Income group')
    results = results[['total_emission_x','Country name_x','total_emission_y','Country name_y','total_emission']]


    name = ['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
    results.columns = name

    return results
