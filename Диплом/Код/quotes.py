import pandas as pd
import time
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from datetime import datetime

df_listing = pd.read_excel('Листинг_компаний.xlsx')
df_l = df_listing[df_listing.INSTRUMENT_TYPE.str.contains('Акция*')] #из листинга компаний выбираем только акции

#Глобальные переменные
periods = {'tick': 1, 'min': 2, '5min': 3, '10min': 4, '15min': 5, '30min': 6,
               'hour': 7, 'daily': 8, 'week': 9, 'month': 10}
period = 8  # Задаём период. Выбор из periods
market = 0  # Можно не задавать. Это рынок, на котором торгуется бумага
start = "01.05.2011"
end = "01.05.2021"
FINAM_URL = "http://export.finam.ru/"  # Сервер, на который стучимся

#Функция получения котировок акций
def quotes():
    #Лок переменные
    tickers = {'ALRS': 81820, 'RUAL': 414279, 'ENPG': 929597, 'AFKS': 19715, 'AFLT': 29, 'GAZP': 16842, 'GMKN': 795,
               'LSRG': 19736, 'DSKY': 473181, 'MVID': 19737, 'MGNT': 17086, 'MAGN': 16782, 'MTSS': 15523,
               'MOEX': 152798, 'LKOH': 8, 'NLMK': 17046, 'PIKK': 18654, 'PLZL': 17123, 'SFIN': 491359, 'CHMF': 16136,
               'FLOT': 2101210, 'TGKA': 18382, 'TRMK': 18441, 'HYDR': 20266, 'FEES': 20509, 'PHOR': 81114,
               'ENRU': 16440, 'UPRO': 18584, 'SGZH': 465236, 'RNFT': 6, 'MSNG': 17370, 'NVTK': 17273, 'ROSN': 20402,
               'MRKU': 35238, 'AQUA': 17564, 'AKRN': 13855, 'APTK': 20702, 'AMEZ': 19651, 'BELU': 18684, 'OGKB': 15544,
               'KMAZ': 74549, 'MSTT': 20309, 'MRKZ': 20107, 'MRKP': 20235, 'MRKC': 2423588, 'ORUP': 17713,
               'RASP': 20286, 'MRKV': 16917, 'MSRS': 20346, 'MRKS': 16080, 'SVAV': 18176, 'TGKN': 15965, 'VSMO': 9,
               'IRGZ': 21078, 'BLNG': 152517, 'LVHK': 16276, 'LPSB': 152676, 'MSST': 81858, 'NPOF': 20892,
               'MGNZ': 19915, 'ARSA': 436091, 'SIBG': 81882, 'ALNU': 484229, 'ACKO': 82460, 'ABRD': 15522,
               'UTAR': 16452, 'ASSB': 81901, 'BRZL': 17257, 'VLHZ': 82115, 'GAZT': 81399, 'GAZS': 81398, 'GAZC': 436120,
               'GTSS': 488918, 'GTRK': 152397, 'RTGZ': 2, 'SIBN': 449114, 'GRNT': 20125, 'GCHE': 16825, 'DASB': 19724,
               'DVEC': 20708, 'FESH': 152876, 'GTLC': 487432, 'EELT': 82001, 'ZVEZ': 81918, 'ZILL': 409486,
               'IDVP': 81786, 'RUSI': 1667866, 'INGR': 17137, 'ISKJ': 16329, 'KLSB': 81943, 'KUNF': 75094,
               'KSGR': 20710, 'KOGK': 81903, 'KMTZ': 17359, 'KZMS': 35285, 'KBTK': 20947, 'MERF': 152516, 'MFON': 20737,
               'ODVA': 901174, 'GEMA': 16359, 'MRSB': 81944, 'MORI': 81929, 'NSVZ': 414560, 'UWGN': 81287,
               'NFAZ': 81947, 'NKSH': 450432, 'NKHP': 19629, 'NMTP': 15189, 'SATR': 22843, 'UNAC': 175781,
               'UCSS': 81896, 'PAZA': 74779, 'RBCM': 81933, 'CHGZ': 20637, 'ROST': 20321, 'RKKE': 20412, 'MRKK': 20681,
               'MRKY': 66893, 'RUGR': 181316, 'ROLO': 20712, 'RUSP': 16455, 'RZSB': 17698, 'HALS': 2380905,
               'SVET': 18371, 'TTLK': 1258079, 'TRFM': 20716, 'TUZA': 74746, 'TUCH': 20717, 'UKUZ': 19623,
               'URKA': 82611, 'URKZ': 74584, 'LIFE': 74561, 'TRCN': 83121, 'PRFN': 21000, 'CHKZ': 21001, 'CHMK': 20999,
               'CHEP': 81934, 'ELTZ': 82493, 'UNKL': 81917, 'YAKG': 420644, 'TNSE': 35363, 'DIOD': 81992,
               'NAUK': 181934, 'RGSS': 473000, 'SLEN': 2135775, 'SMLT': 22525, 'KMEZ': 15547,'IMOEX': 13851}
    lst = []  # Пустой список для заполнения его данными в df строками
    for ticker in tickers:
        #Преобразуем даты:
        start_date = datetime.strptime(start, "%d.%m.%Y").date()
        start_date_rev = datetime.strptime(start, '%d.%m.%Y').strftime('%Y%m%d')
        end_date = datetime.strptime(end, "%d.%m.%Y").date()
        end_date_rev = datetime.strptime(end, '%d.%m.%Y').strftime('%Y%m%d')
        #Все параметры упаковываем в единую структуру
        params = urlencode([('market', market),  #На каком рынке торгуется бумага
                            ('em', tickers[ticker]),  #Вытягиваем цифровой символ, который соответствует бумаге.
                            ('code', ticker),  #Тикер нашей акции
                            ('apply', 0),
                            ('df', start_date.day),  #Начальная дата, номер дня (1-31)
                            ('mf', start_date.month - 1),  #Начальная дата, номер месяца (0-11)
                            ('yf', start_date.year),  #Начальная дата, год
                            ('from', start_date),  #Начальная дата полностью
                            ('dt', end_date.day),  #Конечная дата, номер дня
                            ('mt', end_date.month - 1),  #Конечная дата, номер месяца
                            ('yt', end_date.year),  #Конечная дата, год
                            ('to', end_date),  #Конечная дата
                            ('p', period),  #Таймфрейм
                            ('f', ticker + "_" + start_date_rev + "_" + end_date_rev),  #Имя сформированного файла
                            ('e', ".csv"),  #Расширение сформированного файла
                            ('cn', ticker),  #Ещё раз тикер акции
                            ('dtf', 1), #В каком формате брать даты. Выбор из 5 возможных. См. страницу https://www.finam.ru/profile/moex-akcii/sberbank/export/
                            ('tmf', 1),  #В каком формате брать время. Выбор из 4 возможных.
                            ('MSOR', 0),  #Время свечи (0 - open; 1 - close)
                            ('mstime', "on"),  #Московское время
                            ('mstimever', 1),  #Коррекция часового пояса
                            ('sep', 1),  #Разделитель полей	(1 - запятая, 2 - точка, 3 - точка с запятой, 4 - табуляция, 5 - пробел)
                            ('sep2', 1),  #Разделитель разрядов
                            ('datf', 1),  #Формат записи в файл. Выбор из 6 возможных.
                            ('at', 1)])  #Нужны ли заголовки столбцов
        #Составляем url
        url = FINAM_URL + ticker + "_" + start_date_rev + "_" + end_date_rev + ".csv?" + params
        print("Стучимся на Финам по ссылке: " + url)
        rq = Request(url, headers={'User-Agent': 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 YaBrowser/20.12.2.105 Yowser/2.5 Safari/537.36',
           'accept': '*/*'})
        while True:
            try:
                with urlopen(rq) as urll:
                    s = urll.read()
                    string = s.decode('cp1251')
                    str = string.split('\r\n')
                #Прошло без ошибок, выходим
                break
            except Exception as e:
                print(e)
                #Ждем секунду перед повтором запроса
                time.sleep(1)
        #Заполняем df
        colm = str[0].split(',')
        for item in str[1:]:
            lst.append(item.split(','))
        print('Данные тикера', ticker, "добавлены в список")
        print('________________________________')
    print('DONE')
    df_quotes = pd.DataFrame(lst, columns = colm)
    df_quotes = df_quotes[['<TICKER>', '<DATE>', '<CLOSE>', '<VOL>']]
    df_quotes = df_quotes.rename(columns={'<TICKER>': 'TRADE_CODE'})
    df_quotes.to_excel('Котировки_за_10_лет.xlsx', index=False, encoding='cp1251')
    print('Check file: Котировки_за_10_лет')
    return df_quotes
#Проверка
def checking_values(df_quotes):
    k = 0
    need = []
    for i in list(df_l.TRADE_CODE):
        if i not in set(df_quotes.TRADE_CODE):
            k += 1
            need.append(i)
    #print("Данных по истории", k, "акций в нашем файле нет")
    return need
'''
Был произведен поиск вручную исторических данных этих акций, но безуспешно.
Данных нет, поэтому они были исключены из листинга.
Также из списка были исключены компании, у которых есть привилегированные акции. Данные компании сложны в оценке
'''
def new_listing(need):
    #Убираем компании у которых нет историй по акциям
    df_st = df_listing.loc[df_listing.TRADE_CODE.isin(need)]
    lst_st = df_st.EMITENT_FULL_NAME
    df_total = df_listing.loc[~df_listing.EMITENT_FULL_NAME.isin(lst_st)].reset_index(drop=True)
    df_total.to_excel('Новый_листинг_компаний.xlsx', index=False)
    print('Check file: Новый_листинг_компаний')
    return df_total

df = quotes()
lst = checking_values(df)
df_new = new_listing(lst)


