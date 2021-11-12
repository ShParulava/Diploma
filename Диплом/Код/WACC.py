import pandas as pd
import numpy as np
from unidecode import unidecode

df_ = pd.read_excel('Расчет_CAPM.xlsx')
df_cap = pd.read_excel('Капитал.xlsx')

def create_df():
    df = df_cap.merge(df_)
    df = df.fillna('0') #Заполняем NaN нулями
    #Меняем тип данных
    df['CAPITAL, млн RUB'] = df['CAPITAL, млн RUB'].apply(lambda x: (unidecode(x).replace(' ', ''))).astype(float)
    df['CURRENT_LIABILITIES, млн RUB'] = df['CURRENT_LIABILITIES, млн RUB'].\
        apply(lambda x: (unidecode(x).replace(' ', ''))).astype(float)
    df['NET_PROFIT, млн RUB'] = df['NET_PROFIT, млн RUB'].apply(lambda x: (unidecode(x).replace(' ', ''))).astype(float)
    #Отдельно меняем тип данных для колонки LONG...
    lst_numbers = []
    a = np.array(df['LONG_TERM_LIABILITIES, млн RUB'])
    for item in a:
        new_number = ''
        for i in item:
            if i != ' ':
                new_number += i
        lst_numbers.append(new_number)
    a = np.array(lst_numbers).astype(float)
    df['LONG_TERM_LIABILITIES, млн RUB'] = a #Сохраняем новый стобец
    df = df.loc[df['CAPITAL, млн RUB'] > 0] #Выбираем только те компании, у которых капитал >0
    df = df.reset_index(drop = True)
    return df

def plus_nul(df):
    L_L = []
    C_L = []
    CAP = []
    N_P = []
    l_l = np.array(df['LONG_TERM_LIABILITIES, млн RUB'])
    c_l = np.array(df['CURRENT_LIABILITIES, млн RUB'])
    cap = np.array(df['CAPITAL, млн RUB'])
    n_p = np.array(df['NET_PROFIT, млн RUB'])
    for i in l_l:
        L_L.append(i * 10 ** 6)
    for j in cap:
        CAP.append(j * 10 ** 6)
    for k in c_l:
        C_L.append(k * 10 ** 6)
    for h in n_p:
        N_P.append(h * 10 ** 6)
    df['LONG_TERM_LIABILITIES, млн RUB'] = L_L
    df['CURRENT_LIABILITIES, млн RUB'] = C_L
    df['CAPITAL, млн RUB'] = CAP
    df['NET_PROFIT, млн RUB'] = N_P
    return df

#Заемный капитал
def cal_D(df):
    d = []
    D = []
    l_l = np.array(df['LONG_TERM_LIABILITIES, млн RUB'])
    c_l = np.array(df['CURRENT_LIABILITIES, млн RUB'])
    d.append(l_l + c_l)
    for i in d:
        for j in i:
            D.append(j)
    df['D'] = D
    print('Calculated D')
    return df

#Собственный капитал
def cal_E(df):
    df.rename(columns={'CAPITAL, млн RUB': 'E'}, inplace=True)
    print('Renamed E')
    return df

def ce(df):
    ce = []
    CE = []
    l_l = np.array(df['LONG_TERM_LIABILITIES, млн RUB'])
    c = np.array(df.E)
    ce.append(l_l + c)
    for i in ce:
        for j in i:
            CE.append(j)
    df['CE'] = CE
    print('Calculated CE')
    return df

#Активы
def cal_V(df):
    v = []
    V = []
    e = np.array(df['E'])
    d = np.array(df['D'])
    v.append(e + d)
    for i in v:
        for j in i:
            # print(i)
            V.append(j)
    df['V'] = V
    print('Calculated V')
    return df

#Веса
def weight(df):
    WE = []
    WD = []
    Wd = []
    We = []
    V = np.array(df['V'])
    E = np.array(df['E'])
    D = np.array(df['D'])
    WE.append(E / V)
    WD.append(D / V)
    for i in WD:
        for j in i:
            # print(i)
            Wd.append(j)
    for h in WE:
        for l in h:
            # print(i)
            We.append(l)
    df['Wd'] = Wd
    df['We'] = We
    print('Calculated We and Wd')
    return df

#Доходность заемного капитала
def ret_deb(df):
    D = np.array(df['D'])
    NE = np.array(df['NET_PROFIT, млн RUB'])
    rd = []
    Rd = []
    rd.append(NE/D)
    for i in rd:
        for j in i:
            # print(i)
            Rd.append(j)
    df['Rd'] = Rd
    print('Calculated Rd')
    return df

def wacc(df):
    df = df[['NAME', 'TRADE_CODE', 'BETA', 'CAPM', 'E', 'D', 'V', 'Wd', 'We', 'Rd', 'CE']]
    capm = np.array(df['CAPM'])
    wd = np.array(df['Wd'])
    we = np.array(df['We'])
    rd = np.array(df['Rd'])
    WACC = ((capm / 100) * we + rd * wd * 0.8)
    df['WACC'] = WACC
    df['WACC'] = df['WACC'].fillna(df['We'] * df['CAPM'])
    df.to_excel('Расчет_WACC.xlsx', index=False)

    print('Calculated WACC')
    print('Check file: Расчет_WACC')
    return df


df = create_df()
df_ = plus_nul(df)
df_t = cal_D(df_)
df_to = cal_E(df_t)
df_total = ce(df_to)
df_d = cal_V(df_total)
df_done = weight(df_d)
df_new = ret_deb(df_done)
wacc(df_new)

