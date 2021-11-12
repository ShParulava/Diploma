import pandas as pd
import numpy as np

def add_date():
    df_quotes = pd.read_excel('Котировки_за_10_лет.xlsx', dtype={'<DATE>': str})
    df_quotes['<DATE>'] = pd.to_datetime(df_quotes['<DATE>'], format='%Y-%m-%d') #меняет формат на тип date
    # Создаем список
    lst_TRADE_CODE = df_quotes.TRADE_CODE.unique()
    lst_TRADE_CODE = [x for x in lst_TRADE_CODE if str(x) != 'nan']  # убираем значение nan
    # Добавляем пропущенные значения
    dfs = []
    for i in lst_TRADE_CODE:
        df_i = df_quotes[df_quotes.TRADE_CODE == i]
        mux = pd.MultiIndex.from_product([df_i.TRADE_CODE.unique(),
                                          pd.date_range(df_i['<DATE>'].min(),
                                                        df_i['<DATE>'].max())],
                                         names=['TRADE_CODE', '<DATE>'])
        df_i = df_i.set_index(['TRADE_CODE', '<DATE>']).reindex(mux, fill_value=0).reset_index()
        dfs.append(df_i) #будет список df
    return dfs
# Заполняем данными с предыдущих дней
def add_close(dfs):
    # Cоздаем новый df
    lst_trade = []
    lst_date = []
    lst_close = []
    lst_vol = []
    for df_i in dfs:
        np_df_i_trade = np.array(df_i['TRADE_CODE'])
        np_df_i_date = np.array(df_i['<DATE>'])
        np_df_i_close = np.array(df_i['<CLOSE>'])
        np_df_i_vol = np.array(df_i['<VOL>'])
        lst_trade.append(np_df_i_trade)
        lst_date.append(np_df_i_date)
        lst_close.append(np_df_i_close)
        lst_vol.append(np_df_i_vol)
    lst_all_trade = []
    for lst_i in lst_trade:
        for j in lst_i:
            lst_all_trade.append(j)
    lst_all_date = []
    for lst_i in lst_date:
        for j in lst_i:
            lst_all_date.append(j)
    lst_all_close = []
    for lst_i in lst_close:
        for j in lst_i:
            lst_all_close.append(j)
    for i in range(1, len(lst_all_close)):
        if lst_all_close[i] == 0:
            lst_all_close[i] = lst_all_close[i - 1]
    lst_all_vol = []
    for lst_i in lst_vol:
        for j in lst_i:
            lst_all_vol.append(j)
    df_all = pd.DataFrame()
    df_all['TRADE_CODE'] = pd.Series(lst_all_trade)
    df_all['<DATE>'] = pd.Series(lst_all_date)
    df_all['<CLOSE>'] = pd.Series(lst_all_close)
    df_all['<VOL>'] = pd.Series(lst_all_vol)
    df_all.to_excel("Пополненные_котировки_за_10_лет.xlsx", index=False)
    print('Check file: Пополненные_котировки_за_10_лет')
    return df_all

dfs = add_date()
df = add_close(dfs)


