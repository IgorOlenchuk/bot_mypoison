from decimal import Decimal, getcontext
import requests
from utils.utils import get_data
from utils import config


DB_API_URL = config.DB_API_URL


async def rate(valute):
    RATE_CNY = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    rate = RATE_CNY['Valute'][valute]['Value']/10
    url = f'{DB_API_URL}settings/1/'
    s = await get_data(url)
    r = Decimal(rate * s['k_yuany'])
    return r


async def settings(valute, cost, count):
    r = await rate(valute)
    url = f'{DB_API_URL}settings/1/'
    s = await get_data(url)
    cost = int(cost)
    count = int(count)
    sum = Decimal((cost*r+s['k_comis_1'])*count)
    return sum


async def comission():
    url = f'{DB_API_URL}settings/1/'
    s = await get_data(url)
    c = s['k_comis_1']
    return c


