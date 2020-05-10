import aiohttp
import asyncio
import logging
from typing import Dict


logger = logging.getLogger(__name__)


async def get_response_content(response: aiohttp.ClientResponse):
    content_type = response.content_type
    if content_type == "application/json":
        return await response.json()
    else:
        return await response.text()


class Client:
    async def get(self, url: str):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    return await get_response_content(response)
            except aiohttp.ClientError as e:
                logger.error(e)
            except Exception as e:
                logger.error(e)
            return None

    async def post(self, url: str, data: Dict):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, data) as response:
                    return await get_response_content(response)
            except aiohttp.ClientError as e:
                logger.error(e)

    async def patch(self, url: str):
        pass

    async def put(self, url: str):
        pass

    async def delete(self, url: str):
        pass

    async def head(self, url: str):
        pass

    async def options(self, url: str):
        pass


if __name__ == "__main__":
    import csv
    import datetime
    import json
    import os
    import re
    import yfinance as yf
    
    async def main():
        tickers = ['AAPL', 'MSFT', 'SPY', 'IBM']
        data = yf.download(
            tickers=' '.join(tickers),
            period='ytd',
            group_by='ticker',
            auto_adjust=True,
            prepost=True,
        )
        json_path = os.path.join(os.getcwd(), "stockanalysis", "static", "stocks")
        for symbol in tickers:
            ticker = data[symbol]
            result = ticker.to_json(orient='index', indent=4, date_format='iso')
            with open(os.path.join(json_path, f'{symbol}.json'), "w", newline="") as jsonfile:
                jsonfile.write(result)
        print()
        # for k in r.keys():
        #     timestamp = datetime.datetime.fromtimestamp(int(k)/1000.0)
        #     print(timestamp.strftime('%Y-%m-%d'))
        print()
        
        # print(data['AAPL'])
        print()
        # print(data['SPY'])
        # with open(os.path.join(csv_path, "msft.csv"), "w", newline="") as csvfile:
        #     fieldnames = ['date', 'open', 'close', 'high', 'low', 'volume']

    # async def main():
    #     client = Client()
    #     symbol = 'AAPL'
    #     data = await client.get(
    #         "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=demo"
    #     )
    #     if data:
    #         csv_path = os.path.join(os.getcwd(), "stockanalysis", "static", "stocks")
    #         with open(os.path.join(csv_path, "IBM.csv"), "w", newline="") as csvfile:
    #             fieldnames = ['date', 'open', 'close', 'high', 'low', 'volume']
    #             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #             writer.writeheader()
    #             for k in data.keys():
    #                 if k.startswith("Time"):
    #                     for _k, _v in data[k].items():
    #                         content = {'date': _k}
    #                         for key, value in _v.items():
    #                             __k = re.sub(r'([0-9]+)\.', "", key).strip()
    #                             content[__k] = value
    #                         writer.writerow(content)
    #     # print(json.dumps(data, indent=4, sort_keys=True))

    asyncio.run(main())
    symbol = 'AAPL'
    # url = (
    #     "https://www.google.com/finance/getprices?q="
    #     + symbol
    #     + "&x="
    #     + "NASDAQ"
    #     + "&i=86400&p=40Y&f=d,c,h,l,o,v"
    # )
