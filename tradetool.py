import requests
import apimoex
import pandas as pd
import datetime as dt

import locale
locale.setlocale(locale.LC_TIME, 'ru')

def to_date(x):
  try:
    d = dt.datetime.strptime(x, "%Y-%m-%d")
    date = d.strftime("%d %B")
    return date
  except:
    return 0
def to_year(x):
  try:
    d = dt.datetime.strptime(x, "%Y-%m-%d")
    year = int(d.strftime("%Y"))
    return year
  except:
    return 0


class Bonds:
    Bonds_list = []

    request_url = ('https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQCB/securities.json',
                   'https://iss.moex.com/iss/engines/stock/markets/bonds/boards/TQOB/securities.json')
    arguments = {
        'securities.columns': (
            'SECID,'
            'SHORTNAME,'
            'COUPONVALUE,'
            'COUPONPERIOD,'
            'MATDATE,'
            'SECTYPE,'
            'YIELDATPREVWAPRICE,'
            'FACEVALUE,'
            'PREVWAPRICE,'
            'FACEUNIT,'
            'LOTVALUE,'
            'SECNAME,'
        ),
        'marketdata.columns': ('SECID,'
                               'BID,'
                               'OFFER')
    }
    for url in request_url:
        with requests.Session() as session:
            iss = apimoex.ISSClient(session, url, arguments)
            responce = iss.get()

            for i in range(len(responce['securities'])):
                data = {
                    # 'ID': responce['securities'][i]['SECID'],
                    'Наименование': responce['securities'][i]['SHORTNAME'],
                    'Дата погашения': to_date(responce['securities'][i]['MATDATE']),
                    'Год погашения': to_year(responce['securities'][i]['MATDATE']),
                    'Номинал': responce['securities'][i]['LOTVALUE'],
                    'Валюта': responce['securities'][i]['FACEUNIT'],
                    'Спрос': responce['marketdata'][i]['BID'],
                    'Предложение': responce['marketdata'][i]['OFFER'],
                    'Сумма купона': responce['securities'][i]['COUPONVALUE'],
                    'Купонов в год': responce['securities'][i]['COUPONPERIOD'],
                    'Доходность по оценке пред. дня': responce['securities'][i]['YIELDATPREVWAPRICE'],
                    'Средняя цена предыдущего дня': responce['securities'][i]['PREVWAPRICE'],
                    'Тип ценной бумаги': responce['securities'][i]['SECTYPE'],
                    # 'Номинант': responce['securities'][i]['SECNAME']
                }
                Bonds_list.append(data)

    df = pd.DataFrame(Bonds_list)
    df['Купонов в год'] = 365 // df['Купонов в год']
    df.loc[df["Валюта"] == "SUR", "Валюта"] = "RUB"
    df.fillna(value=0, inplace=True)

