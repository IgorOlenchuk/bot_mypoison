import requests

def rate(valute):
    RATE_CNY = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    rate = round(RATE_CNY['Valute'][valute]['Value']/10, 1)
    return rate
