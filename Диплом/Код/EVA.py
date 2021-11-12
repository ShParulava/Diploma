import pandas as pd
import numpy as np

df_wacc = pd.read_excel('Расчет_WACC.xlsx')
df_ebit = pd.read_excel('EBIT.xlsx')

def nopat():
    nopat = []
    e = np.array(df_ebit.EBIT)
    for i in e:
        nopat.append(float(i)*0.8)
    df_ebit['NOPAT'] = nopat
    df_e = df_ebit[['TRADE_CODE', 'EBIT', 'NOPAT', 'LINKS', 'DISCLOSURE_RF_INFO_PAGE']]
    df = df_wacc.merge(df_e)
    df = df.loc[df['EBIT'] != 0]
    df.reset_index(drop=True)
    return df

def eva(df):
    eva = []
    EVA = []
    ce = np.array(df.CE)
    wacc = np.array(df.WACC)
    nopat = np.array(df.NOPAT)
    eva.append(nopat - wacc * ce)
    for i in eva:
        for j in i:
            EVA.append(j)

    df['EVA'] = EVA
    df.to_excel('EVA.xlsx', index = False)
    print('EVA посчитана!')
    print('Check file: EVA')
    return 0

df = nopat()
eva(df)


