import pandas as pd

#Получаем листинг компаний
def listing():

    df_list = pd.read_csv("https://www.moex.com/ru/listing/securities-list-csv.aspx?type=1", sep=',', encoding="cp1251")
    #Приводим к нижнему регистру
    df_list.EMITENT_FULL_NAME = df_list.EMITENT_FULL_NAME.str.lower()
    #Убраем банки
    df_list = df_list[~df_list.EMITENT_FULL_NAME.str.contains('банк*')]
    df_list = df_list[~df_list.EMITENT_FULL_NAME.str.contains('сбер*')]
    #Удаляем ненужные столбцы
    df_list = df_list.drop(['RN', 'SUPERTYPE', 'ISIN', 'REGISTRY_NUMBER', 'DECISION_DATE', 'OKSM_EDR',
                            'REG_COUNTRY', 'QUALIFIED_INVESTOR', 'HAS_PROSPECTUS', 'IS_CONCESSION_AGREEMENT',
                            'IS_MORTGAGE_AGENT', 'INCLUDED_DURING_CREATION', 'SECURITY_HAS_DEFAULT',
                            'SECURITY_HAS_TECH_DEFAULT', 'INCLUDED_WITHOUT_COMPLIANCE',
                            'RETAINED_WITHOUT_COMPLIANCE', 'HAS_RESTRICTION_CIRCULATION', 'OBLIGATION_PROGRAM_RN',
                            'EARLY_REPAYMENT', 'INCLUDE_DATE', 'CFI_FOREIGN', 'ISIN_UNDERLYING_ASSET',
                            'CFI_UNDERLYING_ASSET', 'PIF_STATUS', 'PIF_STATUS_HIST',
                            'OBLIGATION_PROGRAM_DATE', 'Unnamed: 46', 'ONLY_EMITENT_FULL_NAME'], axis=1)
    #Убираем NaN
    df_list = df_list.dropna(subset=['TRADE_CODE']).reset_index(drop=True)
    #Выбираем только те строки в нужном столбце, которые нам необходимы
    df_list = df_list[(df_list.INSTRUMENT_TYPE.str.contains('Акция обыкновенная')) |
                      (df_list.INSTRUMENT_TYPE.str.contains('Акция привилегированная')) |
                      (df_list.INSTRUMENT_TYPE.str.contains('Облигация биржевая')) |
                      (df_list.INSTRUMENT_TYPE.str.contains('Облигация корпоративная')) |
                      (df_list.INSTRUMENT_TYPE.str.contains('Еврооблигация'))].reset_index(drop = True)

    #Убираем компании, содержащие прив акции
    df_pr_st = df_list[df_list.INSTRUMENT_TYPE.str.contains('Акция привилегированная')]
    lst_s = df_pr_st.EMITENT_FULL_NAME
    df_list = df_list.loc[~df_list.EMITENT_FULL_NAME.isin(lst_s)].reset_index(drop=True)

    df_list.to_excel('Листинг_компаний.xlsx', index=False, encoding='cp1251')

    print('Check file: Листинг_компаний')

    return df_list

listing()


