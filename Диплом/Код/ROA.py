import pandas as pd
import numpy as np

df_ebit = pd.read_excel('EBIT.xlsx')
df_eva = pd.read_excel('EVA.xlsx')

roa = []
ROA = []
df_new_ebit = df_ebit[df_ebit['EBIT'] != 0]
df_new = df_eva[['NAME', 'TRADE_CODE', 'V']]
df = df_new.merge(df_new_ebit) #Объединяем таблицы
v = np.array(df.V)
ebit = np.array(df.EBIT)
roa.append(ebit/v)
for i in roa:
    for j in i:
        ROA.append(j)
df_eva['ROA'] = ROA
df_new = df_eva[['NAME', 'TRADE_CODE', 'WACC', 'ROA', 'EVA']]
df_new.to_excel('WACC & ROA & EVA.xlsx', index = False)




