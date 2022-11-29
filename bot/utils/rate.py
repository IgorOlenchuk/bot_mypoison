import requests

def rate(valute):
    RATE_CNY = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    rate = RATE_CNY['Valute'][valute]['Value']/10
    return rate
