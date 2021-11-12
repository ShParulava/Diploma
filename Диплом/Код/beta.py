import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df = pd.read_excel("Пополненные_котировки_за_10_лет.xlsx")

def remove_st():
    lst_TRADE_CODE = df['TRADE_CODE'].unique()
    lst_TRADE_CODE = [x for x in lst_TRADE_CODE if str(x) != 'nan']  # убираем значение nan
    l = ["IMOEX"]
    for i in l:
        lst_TRADE_CODE.remove(i)
    return lst_TRADE_CODE

def beta(lst_TRADE_CODE):
    col = []
    beta = []
    for item in lst_TRADE_CODE:
        df_st = df[df['TRADE_CODE'] == item]

        df_im = df[df['TRADE_CODE'] == 'IMOEX']
        df_im = df_im.rename(columns={'TRADE_CODE': 'IMOEX', '<CLOSE>': '<CLOSE_IMOEX>',
                                      '<VOL>': '<VOL_IMOEX>'})
        df_inner = df_st.merge(df_im)
        # Счетаем доходность
        # для акций
        st_y = np.array(df_inner['<CLOSE>'])
        y_s_1 = st_y[7:]
        y_s_2 = st_y[:-7]
        y_st = ((y_s_1 - y_s_2) / y_s_2)
        #print(y_st)
        # для биржи
        im_y = np.array(df_inner['<CLOSE_IMOEX>'])
        y_i_1 = im_y[7:]
        y_i_2 = im_y[:-7]
        y_im = ((y_i_1 - y_i_2) / y_i_2)
        x = np.array(y_im).reshape((-1, 1))
        y = np.array(y_st)
        #Cтроим графики
        a = []
        for i in x:
            for j in i:
                a.append(j)
        plt.plot(a, y, '.', ms=10, markerfacecolor='darkblue')  # , ms=10, mec="k")
        z = np.polyfit(a, y, 1)
        y_hat = np.poly1d(z)(a)
        plt.plot(a, y_hat, "r--", lw=1)
        text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y, y_hat):0.3f}$"
        plt.gca().text(0.05, 0.95, text, transform=plt.gca().transAxes, fontsize=14, verticalalignment='top')
        plt.xlabel("Недельная доходность индекса IMOEX")
        plt.ylabel("Недельная доходность акции " + item)
        plt.show()
        # Cчитаем бета
        model = LinearRegression().fit(x, y)
        col.append(item)
        beta.append(model.coef_)
        #print('slope:', model.coef_)
        #print('____________________')
    return beta, col

def beta_save(beta, col):
    b = []
    for i in beta:
        for j in i:
            b.append(j)
    d = {'TRADE_CODE': col, 'BETA': b}
    df_beta = pd.DataFrame(d)
    df_beta.to_excel('Расчет_бет.xlsx', index=False)
    print('Check file: Расчет_бет')
    return 0

lst_TRADE_CODE = remove_st()
beta, col = beta(lst_TRADE_CODE)
beta_save(beta, col)


