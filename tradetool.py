import requests
import apimoex
import pandas as pd

def OFZ():
    Bonds_list = []

    request_url = ('https://iss.moex.com/iss/engines/stock/'
                 'markets/bonds/boards/TQOB/securities.json')

    arguments = {
        'securities.columns': ('SECID,'
                               'SHORTNAME,'
                               'COUPONVALUE,'
                               'COUPONPERIOD,'
                               'MATDATE,'
                               'SECTYPE,'
                               'YIELDATPREVWAPRICE,'
                               'FACEVALUE,'
                               'PREVWAPRICE'),
        'marketdata.columns': ('SECID,'
                               'BID,'
                               'OFFER')
    }
    with requests.Session() as session:
        iss = apimoex.ISSClient(session, request_url, arguments)
        responce = iss.get()

        for i in range(len(responce['securities'])):
            try:
                cupon = 365 // responce['securities'][i]['COUPONPERIOD']
            except:
                cupon = 0

            data = {
                # "№": number,
                'Наименование': responce['securities'][i]['SHORTNAME'],
                'Сумма купона': responce['securities'][i]['COUPONVALUE'],
                'Купонов в год': cupon,
                'Дата погашения': responce['securities'][i]['MATDATE'],
                # 'Тип ценной бумаги': responce['securities'][i]['SECTYPE'],
                # 'Future_lot': responce['securities'][i]['LOTVOLUME'],
                'Спрос': responce['marketdata'][i]['BID'],
                'Предложение': responce['marketdata'][i]['OFFER'],
                'Доходность по оценке пред. дня': responce['securities'][i]['YIELDATPREVWAPRICE'],
                'Средняя цена предыдущего дня': responce['securities'][i]['PREVWAPRICE']
            }
            Bonds_list.append(data)

    data = pd.DataFrame(Bonds_list)
    data.fillna(value=0, inplace=True)
    return data.loc[(data['Спрос'] > 0) & (data['Предложение'] > 0)]

def SUB():
    Bonds_list = []

    request_url = ('https://iss.moex.com/iss/engines/stock/'
                 'markets/bonds/boards/TQCB/securities.json')

    arguments = {
        'securities.columns': ('SECID,'
                               'SHORTNAME,'
                               'COUPONVALUE,'
                               'COUPONPERIOD,'
                               'MATDATE,'
                               'SECTYPE,'
                               'YIELDATPREVWAPRICE,'
                               'FACEVALUE,'
                               'PREVWAPRICE'),
        'marketdata.columns': ('SECID,'
                               'BID,'
                               'OFFER')
    }
    with requests.Session() as session:
        iss = apimoex.ISSClient(session, request_url, arguments)
        responce = iss.get()

        for i in range(len(responce['securities'])):
            try:
                cupon = 365 // responce['securities'][i]['COUPONPERIOD']
            except:
                cupon = 0
            if responce['securities'][i]['SECTYPE'] == "4":
                data = {
                    # "№": number,
                    'Наименование': responce['securities'][i]['SHORTNAME'],
                    'Сумма купона': responce['securities'][i]['COUPONVALUE'],
                    'Купонов в год': cupon,
                    'Дата погашения': responce['securities'][i]['MATDATE'],
                    # 'Тип ценной бумаги': responce['securities'][i]['SECTYPE'],
                    # 'Future_lot': responce['securities'][i]['LOTVOLUME'],
                    'Спрос': responce['marketdata'][i]['BID'],
                    'Предложение': responce['marketdata'][i]['OFFER'],
                    'Доходность по оценке пред. дня': responce['securities'][i]['YIELDATPREVWAPRICE'],
                    'Средняя цена предыдущего дня': responce['securities'][i]['PREVWAPRICE']
                }
                Bonds_list.append(data)

    data = pd.DataFrame(Bonds_list)
    data.fillna(value=0, inplace=True)
    return data.loc[(data['Спрос'] > 0) & (data['Предложение'] > 0)]