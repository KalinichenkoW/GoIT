import sys
from datetime import datetime, timedelta
import httpx
import asyncio
import platform
import json


class HttpError(Exception):
    pass


async def request(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            result = r.json()
            return result
        else:
            raise HttpError(f"Error status: {r.status_code} for {url}")



async def main(index_day):
    if int(index_day) > 10:
        return 'Specify no more than 10 days'
    
    d = datetime.now() - timedelta(days=int(index_day))
    shift = d.strftime("%d.%m.%Y")
    try:
        response = await request(f'https://api.privatbank.ua/p24api/exchange_rates?date={shift}')
        currency = {}
        for i in response['exchangeRate']:            
            if (i['currency']=='USD') or (i['currency']=='EUR'):                                              
                currency.update({
                    i['currency']:{
                        'sale':i['saleRate'],
                        'purchase': i['purchaseRate']
                        }
                    })
        
        return [{response['date']:currency}]
    except HttpError as err:
        print(err)
        return None
    

if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print(sys.argv)
    r = asyncio.run(main(sys.argv[1]))
    print(r)

