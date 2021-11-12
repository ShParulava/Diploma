import requests
from bs4 import BeautifulSoup
import pandas as pd

Balance_URL = 'https://investfunds.ru/stocks/'
#user-agent: передается название браузера операционной системы
HEADERS = {'user-agent': 'ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 YaBrowser/20.12.2.105 Yowser/2.5 Safari/537.36',
           'accept': '*/*' }
#1ый набор ссылок
names_1 = {'ALROSA': 'ALRS', 'UC-RUSAL': 'RUAL', 'Aeroflot': 'AFLT', 'AFK-Sistema': 'AFKS',
         'Gazprom': 'GAZP', 'Norilsk-Nickel': 'GMKN', 'LSR-Group': 'LSRG', 'Detsky-Mir': 'DSKY',
         'Company-M-video': 'MVID', 'Magnit': 'MGNT', 'MMK': 'MAGN', 'Mobile-TeleSystems-MTS': 'MTSS',
         'Moscow-Exchange': 'MOEX', 'Lukoil': 'LKOH', 'NLMK': 'NLMK', 'PIK-Specialized-Developer': 'PIKK',
         'Polyus': 'PLZL', 'SAFMAR-Financial-investment': 'SFIN', 'Severstal': 'CHMF', 'TGC-1': 'TGKA', 'TMK': 'TRMK',
         'RusHydro': 'HYDR', 'FGC-UES': 'FEES', 'Phosagro': 'PHOR', 'Enel-Russia': 'ENRU', 'Unipro': 'UPRO',
         'Mosenergo': 'MSNG', 'NOVATEK': 'NVTK', 'Rosneft': 'ROSN', 'IDGC-of-Urals': 'MRKU',
         'Russian-Aquaculture': 'AQUA', 'Acron': 'AKRN', 'Beluga-Group': 'BELU', 'OGK-2-660': 'OGKB',
         'KAMAZ': 'KMAZ', 'Mostotrest': 'MSTT', 'MRSK-of-North-West': 'MRKZ', 'IDGC-of-Centre-and-Privolzhie': 'MRKP',
         'MRSK-of-Centr': 'MRKC', 'OR': 'ORUP', 'Raspadskaya': 'RASP', 'MRSK-of-Volga': 'MRKV', 'MOESK': 'MSRS',
         'MRSK-of-Sibiria': 'MRKS', 'SOLLERS': 'SVAV', 'TGC-14': 'TGKN', 'VSMPO-AVISMA': 'VSMO',
         'Irkutskenergo': 'IRGZ', 'Belon': 'BLNG', 'Levenhuk': 'LVHK', 'Lipetskaya-ESK': 'LPSB', 'NPO-Fizika': 'NPOF',
         'Arsagera-Asset-Management-Company-754': 'ARSA', 'ALROSA-Nurba': 'ALNU', 'Abrau-Durso': 'ABRD','Utair': 'UTAR',
         'VHZ': 'VLHZ', 'GAZ-Tech': 'GAZT', 'GTM': 'GTRK', 'Gazprom-Neft': 'SIBN', 'GIT': 'GRNT',
         'Cherkizovo-Group': 'GCHE', 'GTL': 'GTLC', 'European-electrical-engineering': 'EELT', 'Zvezda': 'ZVEZ',
         'IC-RUSS-INVEST': 'RUSI', 'INGRAD-PAO': 'INGR', 'Human-Stem-Cell-Institute': 'ISKJ', 'Koks': 'KSGR',
         'KZMS': 'KZMS', 'Kuzbasskaya-Toplivnaya-Company': 'KBTK', 'MERIDIAN': 'MERF', 'Megafon': 'MFON',
         'Mediaholding': 'ODVA', 'MMCB': 'GEMA', 'Morion': 'MORI', 'Nauka-Sviaz': 'NSVZ', 'Nizhnekamskshina': 'NKSH',
         'Novorossiysk-Grain-Plant': 'NKHP', 'Novorossiysk-Commercial-Sea-Port': 'NMTP',
         'United-Aircraft-Corporation': 'UNAC', 'RKK-Energia': 'RKKE', 'MRSK-of-North-Caucasus': 'MRKK',
         'MRSK-of-South-876': 'MRKY', 'Rusgrain-Holding': 'RUGR', 'Ruspolimet': 'RUSP', 'Yuzhny-Kuzbass': 'UKUZ',
         'Uralkali': 'URKA', 'Urals-Stampings-Plant': 'URKZ', 'TransContainer': 'TRCN', 'Chelpipe': 'CHEP',
         'YATEK': 'YAKG', 'TNS-energo': 'TNSE', 'Diod': 'DIOD', 'NPO-Nauka': 'NAUK', 'Kovrov-Mechanical-Plant': 'KMEZ'}
#2ой набор ссылок
names_2 = {'En-Group-71779': 'ENPG', 'Sovcomflot': 'FLOT', 'Segezha-Group': 'SGZH','Russneft': 'RNFT',
           'Pharmacy-Chain-36-6': 'APTK', 'Ashinsky-Metzavod': 'AMEZ', 'Multisistema': 'MSST', 'SMZ': 'MGNZ',
           'ASKO-STRAKHOVANIE': 'ACKO', 'Astrahanskaya-ESK': 'ASSB', 'Buryatzoloto': 'BRZL', 'Gaz-Service': 'GAZS',
           'Gazprom-Gasdistribution-Rostov-on-Don': 'RTGZ', 'FEEC': 'DVEC', 'FESCO': 'FESH', 'ZIL': 'ZILL',
           'Mordovskaya-ESK': 'MRSB', 'RPC-UWC': 'UWGN',  'United-Credit-Systems-3211': 'UCSS',
           'Pavlovskiy-avtobus': 'PAZA', 'RBC': 'RBCM', 'Rosinter-Restaurants-Holding': 'ROST', 'Rusolovo': 'ROLO',
           'Ryazanskaya-ESK': 'RZSB', 'Hals-Development': 'HALS', 'Svetofor-Group': 'SVET', 'TransFin-M': 'TRFM',
           'TZA': 'TUZA', 'Tuchkovskiy-complex-of-construction-materials': 'TUCH', 'Farmsintez': 'LIFE',
           'Profnastil': 'PRFN', 'Chelyabinsk-Forge-and-Press-Plant': 'CHKZ','Chelyabinsk-Metallurgical-Plant': 'CHMK',
           'Elektrotsink': 'ELTZ', 'Southern-Urals-Nickel-Plant': 'UNKL', 'Rosgosstrakh': 'RGSS',
           'Sakhalinenergo': 'SLEN', 'Samolet-Group-of-Companies': 'SMLT'}
#3ий набор ссылок
names_3 = {'Siberian-Gostinec': 'SIBG', 'GEOTECH-Seismorazvedka': 'GTSS', 'Dagestan-ESK': 'DASB',
           'Invest-Development': 'IDVP', 'Neftekamskiy-Avtozavod': 'NFAZ', 'RN-West-Siberia': 'CHGZ'}
names = []
tickers = []
links = []
cap = []
l_l = []
c_l = []
n_p = []
#аргументы: url страницы, с которой необходимо получить контент,
#params - опциональный аргумент, нужен чтобы мы могли передавать дополнительные параметры к адресу URL
#(когда переходим на страницу URL, то данных мб больше чем на 1 стр, поэтому к ссылке добавляются нове параметры)
def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

#парсим html
def get_content_1(html):
    l_l_1 = []  # Долгосрочные обязательства
    c_l_1 = []  # Краткосрочные обязательства
    n_p_1 = []  # Чистая прибыль
    cap_1 = []  # Капитал и резервы
    soup = BeautifulSoup(html, 'html.parser')  # создаем объект суп
    div = soup.find_all('div', class_='fixed_table js_fixed_block')[4]  # парсим название отчетности
    info_ = div.find_all('td', class_="fielt_msfo_first")
    cap_1.append(info_[2].text)
    l_l_1.append(info_[3].text)
    c_l_1.append(info_[4].text)
    n_p_1.append(info_[7].text)
    cap.append(cap_1)
    l_l.append(l_l_1)
    c_l.append(c_l_1)
    n_p.append(n_p_1)
    return 0

def get_content_2(html):
    l_l_2 = []  # Долгосрочные обязательства
    c_l_2 = []  # Краткосрочные обязательства
    n_p_2 = []  # Чистая прибыль
    cap_2 = []  # Капитал и резервы
    soup = BeautifulSoup(html, 'html.parser')  # создаем объект суп
    div = soup.find_all('div', class_='fixed_table js_fixed_block')[3]  # парсим название отчетности
    info_ = div.find_all('td', class_="fielt_msfo_first")
    cap_2.append(info_[2].text)
    l_l_2.append(info_[3].text)
    c_l_2.append(info_[4].text)
    n_p_2.append(info_[7].text)
    cap.append(cap_2)
    l_l.append(l_l_2)
    c_l.append(c_l_2)
    n_p.append(n_p_2)
    return 0

def get_content_3(html):
    l_l_3 = []  # Долгосрочные обязательства
    c_l_3 = []  # Краткосрочные обязательства
    n_p_3 = []  # Чистая прибыль
    cap_3 = []  # Капитал и резервы

    soup = BeautifulSoup(html, 'html.parser')  # создаем объект суп
    div = soup.find_all('div', class_='fixed_table js_fixed_block')[2]  # парсим название отчетности
    info_ = div.find_all('td', class_="fielt_msfo_first")
    cap_3.append(info_[2].text)
    l_l_3.append(info_[3].text)
    c_l_3.append(info_[4].text)
    n_p_3.append(info_[7].text)
    cap.append(cap_3)
    l_l.append(l_l_3)
    c_l.append(c_l_3)
    n_p.append(n_p_3)
    return 0
#показывает исходный код страницы URL
#здесь вызываются все остальные функции
def parse():
    U_1 = []
    U_2 = []
    U_3 = []
    lst_ticker_1 = []
    lst_ticker_2 = []
    lst_ticker_3 = []
    lst_name_1 = names_1.keys()
    lst_name_2 = names_2.keys()
    lst_name_3 = names_3.keys()
    names.append(lst_name_1)
    names.append(lst_name_2)
    names.append(lst_name_3)
    #Списки ключей
    for i_1 in names_1:
        lst_ticker_1.append(names_1[i_1])
    for i_2 in names_2:
        lst_ticker_2.append(names_2[i_2])
    for i_3 in names_3:
        lst_ticker_3.append(names_3[i_3])
    tickers.append(lst_ticker_1)
    tickers.append(lst_ticker_2)
    tickers.append(lst_ticker_3)
    #Составляем URL
    for l_1 in lst_name_1:
        url_1 = Balance_URL + l_1 + '/'
        U_1.append(url_1)
    for l_2 in lst_name_2:
        url_2 = Balance_URL + l_2 + '/'
        U_2.append(url_2)
    for l_3 in lst_name_3:
        url_3 = Balance_URL + l_3 + '/'
        U_3.append(url_3)
    links.append(U_1)
    links.append(U_2)
    links.append(U_3)
    for u_1 in U_1:
        html = get_html(u_1) #for 1 page
        if html.status_code == 200: #все ок
            get_content_1(html.text)
        else:
            print('Error')
    print('1 parser done')
    for u_2 in U_2:
        html = get_html(u_2) #for 1 page
        if html.status_code == 200: #все ок
            get_content_2(html.text)
        else:
            print('Error')
    print('2 parser done')
    for u_3 in U_3:
        html = get_html(u_3) #for 1 page
        if html.status_code == 200: #все ок
            get_content_3(html.text)
        else:
            print('Error')
    print('3 parser done')
    return 0

def save():
    t = []
    n = []
    l = []
    c = []
    la_l = []
    cu_l = []
    net_p = []
    for ticker in tickers:
        for i in ticker:
            t.append(i)
    for name in names:
        for j in name:
            n.append(j)
    for link in links:
        for k in link:
            l.append(k)
    for h in cap:
        for p in h:
            c.append(p)
    for x in l_l:
        for w in x:
            la_l.append(w)
    for y in c_l:
        for b in y:
            cu_l.append(b)
    for r in n_p:
        for z in r:
            net_p.append(z)
    df_new = pd.DataFrame({'NAME': n, 'TRADE_CODE': t, 'CAPITAL, млн RUB': c, 'LONG_TERM_LIABILITIES, млн RUB': la_l,
                           'CURRENT_LIABILITIES, млн RUB': cu_l, 'NET_PROFIT, млн RUB': net_p, 'LINKS': l})
    print('Check file: Капитал')
    df_new.to_excel("Капитал.xlsx", index=False)
    return 0

parse()
save()