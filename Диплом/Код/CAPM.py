import pandas as pd
from bs4 import BeautifulSoup
import requests

def risk():
    #Из расчетов Дамодарана береи ERP & CRP
    df_dam = pd.read_excel('http://www.stern.nyu.edu/~adamodar/pc/datasets/ctryprem.xlsx',
                           sheet_name='Regional Weighted Averages')
    CRP = (df_dam.loc[df_dam['Country'] == 'Russia', 'Country Risk Premium'].values[0]) * 100 #в %
    ERP = (df_dam.loc[df_dam['Country'] == 'United States', 'Equity Risk Premium'].values[0]) * 100
    return ERP, CRP

#Облигации США
def risk_free_rate():
    soup = BeautifulSoup(requests.get('https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData').text,'lxml')
    table = soup.find_all('m:properties')
    tbonds = []
    for i in table:
        tbonds.append([i.find('d:new_date').text[:10], i.find('d:bc_10year').text])
    df_bonds = pd.DataFrame(tbonds, columns=['date', '10y'])
    df_bonds.iloc[:, 1:] = df_bonds.iloc[:, 1:].apply(pd.to_numeric) / 100
    df_bonds['date'] = pd.to_datetime(df_bonds['date'])
    Rf = (df_bonds['10y'].mean()) * 100
    print(df_bonds)
    return Rf

def CAPM(ERP, CRP, Rf):
    df_beta = pd.read_excel('Расчет_бет.xlsx')
    lst = []
    for beta in df_beta['BETA']:
        CAPM = Rf + beta * (ERP + CRP)
        lst.append(CAPM)
    d = {'TRADE_CODE': df_beta['TRADE_CODE'], 'CAPM': lst}
    df_CAPM = pd.DataFrame(d)
    df_total = df_beta.merge(df_CAPM)
    df_total.to_excel('Расчет_CAPM.xlsx', index=False)
    print('Check file: Расчет_CAPM')
    return 0

ERP, CRP = risk()
Rf = risk_free_rate()
CAPM(ERP, CRP, Rf)

